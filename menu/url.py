from django.urls import path
from . import views

# empty string for homepage. will send index.html when this path is triggered
urlpatterns  = [
    path('', views.MenuList.as_view(), name='home') 
]