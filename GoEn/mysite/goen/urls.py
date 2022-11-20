from django.conf.urls.static import static
from django.urls import path

from goen.views import home

urlpatterns = [
    path('', home)]

