pip install -r deps.txt

python manage.py migrate

pip install django
pip install gunicorn
pip install django-cors-headers