# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-23 05:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hof', '0018_auto_20160223_0335'),
    ]

    operations = [
        migrations.AlterField(
            model_name='store',
            name='gu',
            field=models.CharField(choices=[('강남구', '강남구'), ('강동구', '강동구'), ('강북구', '강북구'), ('강서구', '강서구'), ('관악구', '관악구'), ('광진구', '광진구'), ('구로구', '구로구'), ('금천구', '금천구'), ('노원구', '노원구'), ('도봉구', '도봉구'), ('동대문구', '동대문구'), ('동작구', '동작구'), ('마포구', '마포구'), ('서대문구', '서대문구'), ('서초구', '서초구'), ('성동구', '성동구'), ('성북구', '성북구'), ('송파구', '송파구'), ('양천구', '양천구'), ('영등포구', '영등포구'), ('용산구', '용산구'), ('은평구', '은평구'), ('종로구', '종로구'), ('중구', '중구'), ('중랑구', '중랑구'), ('그 외 지역', '그 외 지역')], default='', max_length=7, verbose_name='업체위치 1'),
        ),
        migrations.AlterField(
            model_name='store',
            name='region',
            field=models.CharField(choices=[('건대/강변', '건대/강변'), ('교대/강남', '교대/강남'), ('구로/영등포', '구로/영등포'), ('사당/이수', '사당/이수'), ('서울대', '서울대'), ('신림', '신림'), ('신사', '신사/논현'), ('압구정', '압구정'), ('이태원/용산', '이태원/용산'), ('종로/명동', '종로/명동'), ('잠실/송파', '잠실/송파'), ('홍대/신촌', '홍대/신촌'), ('회기/강북', '회기/강북'), ('혜화/대학로', '혜화/대학로'), ('기타지역', '기타지역')], default='', max_length=7, verbose_name='업체위치 2'),
        ),
    ]
