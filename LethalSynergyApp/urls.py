from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path ('', views.index, name='index'),
    path ('about', views.about),
    path ('ffxiv', views.ffxiv),
    path ('lost_ark', views.lost_ark),
    path ('eso', views.eso),
    path ('elyon', views.elyon)
]

urlpatterns += staticfiles_urlpatterns()