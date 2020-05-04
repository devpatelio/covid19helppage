
from django.contrib import admin
from django.urls import path, include
from . import views as account_views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('signup', account_views.signup, name='signup'),
    # path('form_request', views.new_topic, name='form_request')
    path('logout', auth_views.LogoutView.as_view(), name='logout')
]
