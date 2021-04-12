from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework import generics

from cores.models import Articles
from rest_framework.response import Response

from cores.serializers import ArticlesSerializers
"""
class ArticlesViewSet(viewsets.ViewSet):
    
    queryset = Articles.objects.all()
    serializers_class = ArticlesSerializers



"""
class ArticlesView(generics.ListAPIView):
    queryset = Articles.objects.all()
    serializer_class = ArticlesSerializers