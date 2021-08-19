from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path ('', views.index, name='index'),
    path ('about', views.about),
]

urlpatterns += staticfiles_urlpatterns()