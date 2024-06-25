from django.urls import path,include
from csk.views import *
app_name='anything'
urlpatterns=[
    path('msdhoni/',msdhoni,name='msdhoni'),
]