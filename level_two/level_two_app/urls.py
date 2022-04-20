from django.urls import path
from level_two_app import views

urlpatterns = [
    path('', views.index, name='index')
]
