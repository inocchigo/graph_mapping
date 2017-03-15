"""graph_mapping URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from parsing_data import views as pdv

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', pdv.index, name='index'),
    url(r'^parsing/$', pdv.parsing_and_store_to_db, name='parsing'),
    url(r'^listall/$', pdv.parsing_listall, name='listall'),
    url(r'^storetest/$', pdv.storeimage_to_db, name='storetest'),
    url(r'^get_image_by_id/$', pdv.get_image_by_id, name='get_image_by_id'),
    
]
