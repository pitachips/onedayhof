# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-24 07:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hof', '0020_auto_20160224_1530'),
    ]

    operations = [
        migrations.AddField(
            model_name='store',
            name='is_sidebar_recommended_store',
            field=models.PositiveSmallIntegerField(blank=True, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='store',
            name='atmosphere',
            field=models.CharField(choices=[('일반호프집', '일반호프집'), ('클럽(오픈 플로어)', '클럽(오픈 플로어)'), ('바 형태', '바 형태'), ('감성주점 느낌', '감성주점 느낌'), ('전통주점 스타일', '전통주점 스타일'), ('기타', '기타')], default='', max_length=10, verbose_name='매장 분위기'),
        ),
        migrations.AlterField(
            model_name='store',
            name='gu',
            field=models.CharField(choices=[('강남구', '강남구'), ('강동구', '강동구'), ('강북구', '강북구'), ('강서구', '강서구'), ('관악구', '관악구'), ('광진구', '광진구'), ('구로구', '구로구'), ('금천구', '금천구'), ('노원구', '노원구'), ('도봉구', '도봉구'), ('동대문구', '동대문구'), ('동작구', '동작구'), ('마포구', '마포구'), ('서대문구', '서대문구'), ('서초구', '서초구'), ('성동구', '성동구'), ('성북구', '성북구'), ('송파구', '송파구'), ('양천구', '양천구'), ('영등포구', '영등포구'), ('용산구', '용산구'), ('은평구', '은평구'), ('종로구', '종로구'), ('중구', '중구'), ('중랑구', '중랑구'), ('그 외 지역', '그 외 지역')], default='', max_length=6, verbose_name='업체위치'),
        ),
        migrations.AlterField(
            model_name='store',
            name='region',
            field=models.CharField(choices=[('서울대', '서울대'), ('신촌(연대/이대/서강대/홍대)', '신촌(연대/이대/서강대/홍대)'), ('안암(고려대/성신여대)', '안암(고려대/성신여대)'), ('대학로(성균관대/가톨릭대)', '대학로(성균관대/가톨릭대)'), ('회기(경희대/시립대/외대)', '회기(경희대/시립대/외대)'), ('왕십리(한양대)', '왕십리(한양대)'), ('건대/세종대', '건대/세종대'), ('서울여대/서울과기대/광운대', '서울여대/서울과기대/광운대'), ('중앙대/숭실대/총신대', '중앙대/숭실대/총신대'), ('동국대', '동국대'), ('숙명여대', '숙명여대'), ('기타지역', '기타지역')], default='', max_length=16, verbose_name='대학가, 주변대학'),
        ),
    ]
