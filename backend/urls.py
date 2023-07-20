from django.contrib import admin
from django.urls import path

from chatapp.views import index
from chatapp.views import process_json
from chatapp.prompt import process_json2

from chatapp.views import companyinfo


urlpatterns = [
    path('', index, name='index'),
    path('admin/', admin.site.urls),

    path('process_json/', process_json, name='process_json'),
    path('process_json2/', process_json2, name='process_json2'),

    path('companyinfo/', companyinfo, name='companyinfo'),

]