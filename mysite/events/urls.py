from django.urls import path
from . import views

app_name = 'events'

urlpatterns = [
    path('', views.event_list, name='list'),
    path('create/', views.event_create, name='create'),
    path('feed/json/', views.events_json, name='json'),
    path('<slug:slug>/', views.event_detail, name='detail'),
]
