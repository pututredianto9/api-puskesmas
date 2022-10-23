from django.urls import path
from .views import PuskesmasList, KabupatenList, KecamatanList, ProvinsiList

urlpatterns = [
   path('puskesmas/', PuskesmasList.as_view({'get': 'list'}),name='puskesmas'),
   path('provinsi/', ProvinsiList.as_view({'get': 'list'}),name='provinsi'),
   path('kabupaten/', KabupatenList.as_view({'get': 'list'}),name='kabupaten'),
   path('kecamatan/', KecamatanList.as_view({'get': 'list'}),name='kecamatan'),
]
