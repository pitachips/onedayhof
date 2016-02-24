from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.files import File
from django.db import models
from django.db.models.signals import pre_save

from onedayhof.utils import random_name_upload_to, thumbnail


# this is important # CHOICES 향후 추가 필요함!

MAX_GUEST_CHOICES = (
    ('80명 미만', '80명 미만'),
    ('80 ~ 140명', '80 ~ 140명'),
    ('140 ~ 200명', '140 ~ 200명'),
    ('200명 이상', '200명 이상'),
)

GU_CHOICES = (
    ('강남구', '강남구'),
    ('강동구', '강동구'),
    ('강북구', '강북구'),
    ('강서구', '강서구'),
    ('관악구', '관악구'),
    ('광진구', '광진구'),
    ('구로구', '구로구'),
    ('금천구', '금천구'),
    ('노원구', '노원구'),
    ('도봉구', '도봉구'),
    ('동대문구', '동대문구'),
    ('동작구', '동작구'),
    ('마포구','마포구'),
    ('서대문구','서대문구'),
    ('서초구', '서초구'),
    ('성동구','성동구'),
    ('성북구','성북구'),
    ('송파구','송파구'),
    ('양천구','양천구'),
    ('영등포구','영등포구'),
    ('용산구','용산구'),
    ('은평구','은평구'),
    ('종로구','종로구'),
    ('중구', '중구'),
    ('중랑구', '중랑구'),
    ('그 외 지역','그 외 지역'),
)

REGION_CHOICES = (
    ('서울대', '서울대'),
    ('신촌(연대/이대/서강대/홍대)', '신촌(연대/이대/서강대/홍대)'),
    ('안암(고려대/성신여대)', '안암(고려대/성신여대)'),
    ('대학로(성균관대/가톨릭대)', '대학로(성균관대/가톨릭대)'),
    ('회기(경희대/시립대/외대)', '회기(경희대/시립대/외대)'),
    ('왕십리(한양대)', '왕십리(한양대)'),
    ('건대/세종대', '건대/세종대'),
    ('서울여대/서울과기대/광운대', '서울여대/서울과기대/광운대'),
    ('중앙대/숭실대/총신대', '중앙대/숭실대/총신대'),
    ('동국대', '동국대'),
    ('숙명여대', '숙명여대'),
    ('기타지역', '기타지역'),
)

ATMOSPHERE_CHOICES = (
    ('일반호프집', '일반호프집'),
    ('클럽(오픈 플로어)', '클럽(오픈 플로어)'),
    ('바 형태', '바 형태'),
    ('감성주점 느낌', '감성주점 느낌'),
    ('전통주점 스타일', '전통주점 스타일'),
    ('기타','기타'),
)

class Store(models.Model):

    name = models.CharField(max_length=80, verbose_name='업체이름')
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, default='1')
    contract_condition = models.TextField(verbose_name='계약조건/분배조건')
    tel = models.CharField(max_length=20, verbose_name='업체 전화번호')
    address = models.CharField(max_length=120, verbose_name='주소')
    latitude = models.FloatField(null=True)
    longitude = models.FloatField(null=True)

    menu = models.TextField(blank=True, default='', verbose_name='주요 메뉴와 가격')
    rating = models.PositiveSmallIntegerField(blank=True, default=0)
    n_review = models.PositiveSmallIntegerField(default=0, blank=True)
    description = models.TextField(blank=True, default='', verbose_name='상세조건 및 기타')
    is_active = models.BooleanField(default=False)
    is_index_page_recommended_store = models.PositiveSmallIntegerField(unique=True, validators=[MinValueValidator(0), MaxValueValidator(9)], blank=True, null=True)
    is_sidebar_recommended_store = models.PositiveSmallIntegerField(unique=True, blank=True, null=True)

    #태그용. 1개씩밖에 선택 못함.
    max_guest = models.CharField(max_length=10, choices=MAX_GUEST_CHOICES, default='', verbose_name='수용가능 인원수')
    gu = models.CharField(max_length=6, choices=GU_CHOICES, default='', verbose_name='업체위치')
    region = models.CharField(max_length=16, choices=REGION_CHOICES, default='', verbose_name='대학가, 주변대학')
    atmosphere = models.CharField(max_length=10, choices=ATMOSPHERE_CHOICES, default='', verbose_name='매장 분위기')


    def __str__(self):
        return self.name


class StoreImage(models.Model):
    store = models.ForeignKey(Store, default=None)
    image = models.ImageField(upload_to=random_name_upload_to, verbose_name='사진 업로드')


def pre_on_storeimage_save(sender, **kwargs):
    store_image = kwargs['instance']
    if store_image.image:
        max_width = 800
        if store_image.image.width > max_width or store_image.image.height > max_width:
            processed_file = thumbnail(store_image.image.file, max_width, max_width)
            store_image.image.save(store_image.image.name, File(processed_file))

pre_save.connect(pre_on_storeimage_save, sender=StoreImage)



class Review(models.Model):
    store = models.ForeignKey(Store)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, default='1')
    rating = models.PositiveSmallIntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(5)], verbose_name='평점주기')
    content = models.TextField(verbose_name='댓글달기')
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __str__(self):
        return self.content


class ReviewImage(models.Model):
    review = models.ForeignKey(Review, default=None)
    image = models.ImageField(blank=True, null=True, upload_to=random_name_upload_to, verbose_name='사진 업로드')