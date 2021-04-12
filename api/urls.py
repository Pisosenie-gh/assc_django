from rest_framework import routers
from .views import ArticlesView
from django.urls import path
urlpatterns = [
    path('articles/', ArticlesView.as_view())
]