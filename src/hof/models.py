from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

from onedayhof.utils import random_name_upload_to


class Store(models.Model):

    name = models.CharField(max_length=80)
    owner = models.CharField(max_length=20)
    contract_condition = models.TextField()
    tel = models.CharField(max_length=20)
    address = models.CharField(max_length=120)
    lnglat = models.CharField(max_length=80, default='')
    max_guest = models.CharField(max_length=20)

    menu = models.TextField(blank=True, default='')
    rating = models.PositiveSmallIntegerField(blank=True, default=0)
    description = models.TextField(blank=True, default='')


    def __str__(self):
        return self.name


class StoreImage(models.Model):
    store = models.ForeignKey(Store, default=None)
    image = models.ImageField(upload_to=random_name_upload_to)



class Review(models.Model):
    store = models.ForeignKey(Store)
    rating = models.PositiveSmallIntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(5)])
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __str__(self):
        return self.content


class ReviewImage(models.Model):
    review = models.ForeignKey(Review, default=None)
    image = models.ImageField(blank=True, null=True, upload_to=random_name_upload_to)