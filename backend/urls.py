from django.contrib import admin
from django.urls import path

from chatapp.views import index

from chatapp.views import process_json
from promptapp.views import process_json2



urlpatterns = [
    path('', index, name='index'),
    path('admin/', admin.site.urls),
    path('process_json/', process_json, name='process_json'),
    path('process_json2/', process_json2, name='process_json2'),

]