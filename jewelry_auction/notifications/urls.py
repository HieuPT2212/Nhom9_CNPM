from django.urls import path
from . import views

app_name = 'notifications'

urlpatterns = [
    path('', views.notification_list, name='notification-list'),
    path('<int:pk>/', views.notification_detail, name='notification-detail'),
]