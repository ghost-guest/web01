from django.db import models
from datetime import datetime
# Create your models here.


class City(models.Model):
    name = models.CharField(max_length=50, verbose_name='城市名称')
    add_time = models.DateField(default=datetime.now, verbose_name='添加时间')
    desc = models.CharField(max_length=200, verbose_name='城市描述')
    
    class Meta:
        verbose_name = '课程机构'
        verbose_name_plural = verbose_name


class CourseOrg(models.Model):
    name = models.CharField(max_length=50, verbose_name='机构名称')
    desc = models.TextField(verbose_name='机构描述')
    click_num = models.IntegerField(default=0, verbose_name='点击数')
    fav_num = models.IntegerField(default=0, verbose_name='收藏数')
    image = models.ImageField(upload_to='courses/%Y/%m', verbose_name='封面图', max_length=100)
    address = models.CharField(max_length = 100, verbose_name='机构地址')
    city = models.ForeignKey(City, verbose_name='城市')
    add_time = models.DateField(default=datetime.now, verbose_name='添加时间')
    
    class Meta:
        verbose_name = '课程机构'
        verbose_name_plural = verbose_name


class Teacher(models.Model):
    org = models.ForeignKey(CourseOrg, verbose_name='所属机构')
    name = models.CharField(max_length=50, verbose_name='教师名称')
    work_years = models.IntegerField(default=0, verbose_name='工作年限')
    work_company = models.CharField(max_length = 100, verbose_name='就职公司')
    work_position = models.CharField(max_length = 100, verbose_name='公司职位')
    add_time = models.DateField(default=datetime.now, verbose_name='添加时间')
    points = models.CharField(max_length = 100, verbose_name='教学特点')
    click_num = models.IntegerField(default=0, verbose_name='点击数')
    fav_num = models.IntegerField(default=0, verbose_name='收藏数')
    
    class Meta:
        verbose_name = '教师'
        verbose_name_plural = verbose_name