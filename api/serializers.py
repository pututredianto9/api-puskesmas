from dataclasses import field
from statistics import mode
from rest_framework import serializers
from django.contrib.auth import get_user_model
from . models import Puskesmas, Kecamatan, Provinsi, Kabupaten

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = '__all__'

class ProvinsiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Provinsi
        fields = ('__all__')
class KabupatenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kabupaten
        fields = ('__all__')
class KecamatanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kecamatan
        fields = ('__all__')
class PuskesmasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Puskesmas
        fields = ('__all__')

