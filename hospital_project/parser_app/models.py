from django.db import models


class Category(models.Model):
    name_category = models.CharField(max_length=100)
    link = models.CharField(max_length=300)
    status = models.CharField(max_length=100)


class City(models.Model):
    category = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    link = models.CharField(max_length=300)
    status = models.CharField(max_length=100)


class ClinicLink(models.Model):
    category = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    link = models.CharField(max_length=300)
    status = models.CharField(max_length=100)


class ClinicInfo(models.Model):
    name = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    practicing_physicians_count = models.PositiveIntegerField()
    address = models.CharField(max_length=100)
    number_phone = models.CharField(max_length=100)
    overview = models.TextField()
