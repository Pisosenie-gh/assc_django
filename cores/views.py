from django.shortcuts import render
from rest_framework import viewsets
from .models import Articles
from django.views.generic import ListView,DetailView
from django.views.generic.edit import FormMixin
from hitcount.views import HitCountDetailView
from .serializers import ArticlesSerializers
class HomeListView(ListView):
    model = Articles
    template_name = 'projects.html'
    context_object_name = 'list_articles'


class HomeDetailView(HitCountDetailView):
    model = Articles
    template_name = 'detail.html'
    context_object_name = 'get_article'
    count_hit = True


class ArticlesViewSet(viewsets.ViewSet):
    queryset = Articles.objects.all()
    serializers_class = ArticlesSerializers




