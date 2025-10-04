from django.urls import path
from . import views

app_name = 'clubs'

urlpatterns = [
    path('', views.club_list, name='list'),

    path('<slug:slug>/', views.club_detail, name='detail'),
]