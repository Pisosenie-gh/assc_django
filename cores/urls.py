from django.urls import path
from django.contrib import admin
from cores import views
from .views import ArticlesViewSet
from rest_framework import routers

urlpatterns = [
    path('', views.HomeListView.as_view(), name='projects'),
    path('detail/<int:pk>',views.HomeDetailView.as_view(), name='detail_page'),




]
