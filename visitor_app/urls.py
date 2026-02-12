from django.urls import path 
from django.contrib import admin
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.menu, name='menu'),
    path('entry/', views.visitor_entry, name='entry'),
    path('list/', views.visitor_list, name='list'),
    path('summary/', views.summary, name='summary'),
]
