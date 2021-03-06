# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-19 03:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hof', '0006_auto_20160219_0025'),
    ]

    operations = [
        migrations.AlterField(
            model_name='store',
            name='atmosphere',
            field=models.CharField(choices=[('ordinary', '일반호프집'), ('club ', '클럽(오픈 플로어)'), ('bar', '바 형태'), ('gamsung', '감성주점 느낌'), ('traditional', '전통주점 스타일'), ('etc_atmosphere', '기타')], default='', max_length=15),
        ),
        migrations.AlterField(
            model_name='store',
            name='gu',
            field=models.CharField(choices=[('gwanak', '관악구'), ('seocho', '서초구'), ('joongrang', '중랑구'), ('gumcheon', '금천구'), ('gangnam', '강남구'), ('joong', '중구'), ('etc_gu', '그외 지역')], default='', max_length=15),
        ),
        migrations.AlterField(
            model_name='store',
            name='region',
            field=models.CharField(choices=[('hongdae', '홍대/신촌'), ('hoegi', '회기/강북'), ('gyodae', '교대/강남'), ('sinlim', '신림'), ('sadang', '사당이수'), ('itaewon', '이태원용산'), ('guro', '구로/영등포'), ('jongro', '종로/명동'), ('jamsil', '잠실/송파'), ('gundae', '건대/강변'), ('etc_region', '기타지역')], default='', max_length=15),
        ),
    ]
