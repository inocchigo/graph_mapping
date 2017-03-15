from django.shortcuts import render
from django.template.loader import get_template
from django.http import HttpResponse
from datetime import datetime
from models import TargetPlace
from models import TargetImage
from PIL import Image
import cStringIO

import requests
import json
import re

def index(request):
    template = get_template('index.html')
    html = template.render({'now': datetime.now})
    return HttpResponse(html)

def parsing_listall(request):
	template = get_template('listall.html')
	all = TargetPlace.objects.all()
	html = template.render(locals())
	return HttpResponse(html)

def parsing_and_store_to_db(request):
    res = requests.get("http://gportal.ncdr.nat.gov.tw/arcgis/sharing/content/items/8fb6414662484d52853236b0192bcc9f/data?f=json")
    data = json.loads(res.text)
    targetPlaces = []

    #print data
    featureSets = data['operationalLayers'][0].get('featureCollection').get('layers')[0].get('featureSet').get('features')
    
    for feature in featureSets:
        X = feature.get('geometry').get('x')
        Y = feature.get('geometry').get('y')
        
        #seperate time and name from attributes.name
        name = feature.get('attributes').get('name')
        chinese_char = re.findall(ur'[\u4e00-\u9fff]+', name)
        first_chinese_index = name.find(chinese_char[0])
        time = name[0:first_chinese_index]
        rname = name[first_chinese_index:len(name)]
        region = rname[0:2]

        des = feature.get('attributes').get('description')
        url = feature.get('attributes').get('thumb_url')

        tp = TargetPlace(pointX=X, pointY=Y, name=rname, description=des, time= time, region=region, url=url)
        targetPlaces.append(tp)
        tp.save()

    print len(targetPlaces)
    template = get_template('parsing.html')
    html = template.render({'resp': targetPlaces})
    return HttpResponse(html)

def get_image_by_id(request):
    id = request.GET.get('id')
    print id
    tp = TargetPlace.objects.get(id=id)
    tpimage = TargetImage.objects.get(targetplace = tp)
    
    #im = Image.open(cStringIO.StringIO(tpimage.image_data))
    #response = HttpResponse(content_type="image/jpg")
    #im.save(response,im.format)
    #return response
    
    #im = Image.open(cStringIO.StringIO(tpimage.image_data))
    #output = cStringIO.StringIO()
    #im.save(output,"JPEG")
    #contents = output.getvalue().encode("base64")
    #output.close()
    #return HttpResponse('<img src="data:image/jpeg;base64,' + contents + ' />')

    im = Image.open(cStringIO.StringIO(tpimage.image_data))
    im.save("/Users/akiralee/python/django/graph_mapping/static/images/"+str(tpimage.id)+".JPG", "JPEG")
    return HttpResponse(
        "<img src=/static/images/" + str(tpimage.id) +".JPG" +'/>'
        #"<img src="%s/%s /> % (MEDIA_URL, "/generated_images/"+tpimage.name)
    )

def storeimage_to_db(request):
    all_targetplace = TargetPlace.objects.all()
    for tp in all_targetplace:
        print tp.id
        if not TargetImage.objects.filter(targetplace = tp).exists():
            response = requests.get(tp.url, stream=True).content
            imageName = tp.url.split('/')[4]
            tpimg = TargetImage(name=imageName, image_data=response, targetplace=tp)
            tpimg.save()


    template = get_template('index.html')
    html = template.render({'now': "All image save done."})
    return HttpResponse(html)


