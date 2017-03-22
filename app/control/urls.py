from django.conf.urls import url,include
from . import views

app_name = 'control'

urlpatterns = [
    url(r'^' ,views.controller ,name="controller"),
    url(r'^ajaxStatusHandler/$' ,views.statusHandler ,name="statusHandler"),
]
