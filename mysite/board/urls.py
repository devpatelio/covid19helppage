
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('<int:pk>/preview', views.preview, name='preview'),
    path('new_request', views.new_request, name='new_request'),
    # path('form_request', views.new_topic, name='form_request')
]

