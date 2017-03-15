# graph_mapping

- Requirement
<pre>pip install virtualenv</pre>


- 建立virtual env
<pre>
virtualenv djangoVirtualENV
</pre>


- 進入virtual env
<pre>
cd djangoVirtualENV
source djangoVirtualENV/bin/activate
</pre>


- 安裝以下套件
<pre>
	pip install django psycopg2 requests pillow
</pre>


- 確認是否有資料庫異動
<pre>
python manage.py makemigrations
</pre>


- 若資料庫(model)有異動，執行資料庫migrate
<pre>
python manage.py migrate
</pre>


- 啟動server
<pre>
python manage.py runserver
</pre>


- 刪光資料庫
<pre>
python manage.py flush
</pre>


- 離開virtualenv
<pre>
deactivate
</pre>


