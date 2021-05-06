from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('thread/', views.thread, name='thread'),
    path('about/', views.about, name='about'),
]