from django.urls import path
from . import views

app_name = 'members'

urlpatterns = [
    path('<slug:club_slug>/', views.member_list, name='list'),
    path('update/<int:pk>/', views.member_update, name='update'),
]
