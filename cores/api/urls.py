

from django.urls import path
from django.contrib import admin
from cores import views
from ..views import ArticlesViewSet
from rest_framework import routers


urlpatterns = []
router = routers.SimpleRouter()
router.register('articles', ArticlesViewSet, basename='articles')
urlpatterns += router.urls