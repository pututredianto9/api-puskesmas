from enum import unique
from django.db import models

# Create your models here.



class Provinsi(models.Model):
    KD_PROVINSI = models.CharField(max_length=2, unique=True)
    PROVINSI = models.CharField(max_length=100)

    def __str__(self):
        return self.PROVINSI

class Kabupaten(models.Model):
    KD_KABUPATEN = models.CharField(max_length=4, unique=True)
    KD_PROVINSI = models.ForeignKey(Provinsi, on_delete = models.CASCADE, null=True)
    KABUPATEN = models.CharField(max_length=100)
    def __str__(self):
        return self.KABUPATEN

class Kecamatan(models.Model):
    KD_KECAMATAN = models.CharField(max_length = 8, unique = True)
    KD_KABUPATEN = models.ForeignKey(Kabupaten, on_delete=models.CASCADE, null=True)
    KECAMATAN = models.CharField(max_length=100)

    def __str__(self):
        return self.KECAMATAN

class Puskesmas(models.Model):
    KD_PUSKESMAS = models.CharField(max_length=11, unique=True)
    KD_KECAMATAN = models.ForeignKey(Kecamatan,on_delete=models.CASCADE, null=True)
    PUSKESMAS = models.CharField(max_length=60)
    ALAMAT = models.CharField(max_length=100)

    def __str__(self):
        return self.PUSKESMAS