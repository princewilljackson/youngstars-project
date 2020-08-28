from django.urls import path

from youngstars_app import views

app_name = 'youngstars_app'

urlpatterns = [
    path('', views.home, name='home'),
    path('test-page/', views.test, name='test-page'),
]