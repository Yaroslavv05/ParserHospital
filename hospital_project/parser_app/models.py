from django.db import models


class Category(models.Model):
    name_category = models.CharField(max_length=100)
    cities = models.TextField()
    links_on_cities = models.TextField()


class Links(models.Model):
    links_on_hospital = models.CharField(max_length=300)


# class Info(models.Model):
#     name_hospital = models.CharField(max_length=100)
#     number_phone = models.CharField(max_length=100)
#     overview = models.CharField(max_length=300)
#     ratings = models.CharField(max_length=100)
#     col_vo_reviews = models.TextField()

class Info(models.Model):
    name = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    practicing_physicians_count = models.PositiveIntegerField()
    reviews_count = models.PositiveIntegerField()
    address = models.CharField(max_length=100)
    number_phone = models.CharField(max_length=100)
    overview = models.TextField()