from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

from onedayhof.utils import random_name_upload_to


# this is important # CHOICES 향후 추가 필요함!

GU_CHOICES = (
    ('gwanak', '관악구'),
    ('seocho', '서초구'),
    ('joongrang', '중랑구'),
    ('gumcheon', '금천구'),
    ('gangnam', '강남구'),
    ('joong', '중구'),
    ('etc_gu','그외 지역'),
)

REGION_CHOICES = (
    ('hongdae', '홍대/신촌'),
    ('hoegi', '회기/강북'),
    ('gyodae', '교대/강남'),
    ('sinlim', '신림'),
    ('sadang', '사당이수'),
    ('itaewon', '이태원용산'),
    ('guro', '구로/영등포'),
    ('jongro', '종로/명동'),
    ('jamsil', '잠실/송파'),
    ('gundae', '건대/강변'),
    ('etc_region','기타지역'),
)

ATMOSPHERE_CHOICES = (
    ('ordinary', '일반호프집'),
    ('club ', '클럽(오픈 플로어)'),
    ('bar', '바 형태'),
    ('gamsung', '감성주점 느낌'),
    ('traditional', '전통주점 스타일'),
    ('etc_atmosphere','기타'),
)

class Store(models.Model):

    name = models.CharField(max_length=80)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, default='1')
    contract_condition = models.TextField()
    tel = models.CharField(max_length=20)
    address = models.CharField(max_length=120)
    lnglat = models.CharField(max_length=80, default='')

    menu = models.TextField(blank=True, default='')
    rating = models.PositiveSmallIntegerField(blank=True, default=0)
    n_review = models.PositiveSmallIntegerField(default=0, blank=True)
    description = models.TextField(blank=True, default='')

    #태그용. 1개씩밖에 선택 못함.
    max_guest = models.PositiveSmallIntegerField()
    gu = models.CharField(max_length=15, choices=GU_CHOICES, default='')
    region = models.CharField(max_length=15, choices=REGION_CHOICES, default='')
    atmosphere = models.CharField(max_length=15, choices=ATMOSPHERE_CHOICES, default='')


    def __str__(self):
        return self.name


class StoreImage(models.Model):
    store = models.ForeignKey(Store, default=None)
    image = models.ImageField(upload_to=random_name_upload_to)



class Review(models.Model):
    store = models.ForeignKey(Store)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, default='1')
    rating = models.PositiveSmallIntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(5)])
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __str__(self):
        return self.content


class ReviewImage(models.Model):
    review = models.ForeignKey(Review, default=None)
    image = models.ImageField(blank=True, null=True, upload_to=random_name_upload_to)