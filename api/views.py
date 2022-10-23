from django.shortcuts import render
from api import serializers

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import get_user_model
from .serializers import UserSerializer, ProvinsiSerializer, KabupatenSerializer, KecamatanSerializer, PuskesmasSerializer
from .models import Puskesmas, Provinsi, Kabupaten, Kecamatan
# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = UserSerializer
    queryset = get_user_model().objects.all()

class ProvinsiList(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = ProvinsiSerializer
    queryset = Provinsi.objects.all()

class KecamatanList(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = KecamatanSerializer
    queryset = Kecamatan.objects.all()

class KabupatenList(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = KabupatenSerializer
    queryset = Kabupaten.objects.all()

class PuskesmasList(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = PuskesmasSerializer
    queryset = Puskesmas.objects.all()

