from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

from onedayhof.utils import random_name_upload_to


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
    ('건대/강변', '건대/강변'),
    ('교대/강남', '교대/강남'),
    ('구로/영등포', '구로/영등포'),
    ('사당/이수', '사당/이수'),
    ('서울대', '서울대'),
    ('신림', '신림'),
    ('신사', '신사/논현'),
    ('압구정', '압구정'),
    ('이태원/용산', '이태원/용산'),
    ('종로/명동', '종로/명동'),
    ('잠실/송파', '잠실/송파'),
    ('홍대/신촌', '홍대/신촌'),
    ('회기/강북', '회기/강북'),
    ('혜화/대학로', '혜화/대학로'),
    ('기타지역','기타지역'),
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

    #태그용. 1개씩밖에 선택 못함.
    max_guest = models.CharField(max_length=10, choices=MAX_GUEST_CHOICES, default='', verbose_name='수용가능 인원수')
    gu = models.CharField(max_length=5, choices=GU_CHOICES, default='', verbose_name='업체위치 1')
    region = models.CharField(max_length=8, choices=REGION_CHOICES, default='', verbose_name='업체위치 2')
    atmosphere = models.CharField(max_length=15, choices=ATMOSPHERE_CHOICES, default='', verbose_name='매장 분위기')


    def __str__(self):
        return self.name


class StoreImage(models.Model):
    store = models.ForeignKey(Store, default=None)
    image = models.ImageField(upload_to=random_name_upload_to, verbose_name='사진 업로드')



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