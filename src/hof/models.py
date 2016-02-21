from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

from onedayhof.utils import random_name_upload_to


# this is important # CHOICES 향후 추가 필요함!

MAX_GUEST_CHOICES = (
    ('sizeA', '80명 미만'),
    ('sizeB', '80 ~ 140명'),
    ('sizeC', '140 ~ 200명'),
    ('sizeD', '200명 이상'),
)

GU_CHOICES = (
    ('gangdong', '강동구'),
    ('gangbuk', '강북구'),
    ('gangseo', '강서구'),
    ('gwangjin', '광진구'),
    ('guro', '구로구'),
    ('nowon', '노원구'),
    ('dobong', '도봉구'),
    ('dongdaemun', '동대문구'),
    ('dongjak', '동작구'),
    ('mapo','마포구'),
    ('seodaemun','서대문구'),
    ('seongdong','성동구'),
    ('seongbuk','성북구'),
    ('songpa','송파구'),
    ('yangcheon','양천구'),
    ('yeongdeungpo','영등포구'),
    ('yongsan','용산구'),
    ('eunpyeong','은평구'),
    ('jongno','종로구'),
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
    max_guest = models.CharField(max_length=5, choices=MAX_GUEST_CHOICES, default='', verbose_name='수용가능 인원수')
    gu = models.CharField(max_length=15, choices=GU_CHOICES, default='', verbose_name='업체위치 1')
    region = models.CharField(max_length=15, choices=REGION_CHOICES, default='', verbose_name='업체위치 2')
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