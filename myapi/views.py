from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from .serializers import GestanteSerializer
from .models import Gestante


class GestanteViewSet(viewsets.ModelViewSet):
    queryset = Gestante.objects.all().order_by('name')
    serializer_class = GestanteSerializer
    