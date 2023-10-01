from django.urls import path
from . import views

# empty string for homepage. will send index.html when this path is triggered
# for dynamic detail pages, need to add syntax for primary key
urlpatterns  = [
    path('', views.MenuList.as_view(), name='home'),
    path('detail/<int:pk>/', views.ItemDetail.as_view(), name='detail')
]