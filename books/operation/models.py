from django.db import models
from datetime import datetime
from users.models import UserProfile
from courses.models import Course
# Create your models here.

class UserAsk(models.Model):
    name = models.CharField(max_length=50, verbose_name='姓名')
    mobile = models.CharField(max_length=11, verbose_name='手机号')
    course_name = models.CharField(max_length=50, verbose_name='课程名称')
    add_time = models.DateField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = '用户咨询'
        verbose_name_plural = verbose_name


class CourseComments(models.Model):
    "课程评论"
    user = models.ForeignKey(UserProfile, verbose_name='用户')
    course = models.ForeignKey(Course, verbose_name='课程')
    comments = models.CharField(max_length=200, verbose_name='评论')
    add_time = models.DateField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = '课程评论'
        verbose_name_plural = verbose_name


class UserFavorite(models.Model):
    user = models.ForeignKey(UserProfile, verbose_name='用户')
    fav_id = models.IntegerField(default=0, verbose_name='数据id')
    fav_type = models.IntegerField(choices=((1,"课程"),(2,"课程机构"),(3,"讲师")), default=1, verbose_name='数据类型')
    add_time = models.DateField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = '用户收藏'
        verbose_name_plural = verbose_name


class UserMessage(models.Model):
    user = models.IntegerField(default=0,verbose_name='接收用户')
    message = models.CharField(max_length=500, verbose_name='消息')
    has_read = models.BooleanField(default=False, verbose_name='是否已读')
    add_time = models.DateField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = '用户消息'
        verbose_name_plural = verbose_name

class UserCourse(models.Model):
    user = models.ForeignKey(UserProfile, verbose_name='用户')
    course = models.ForeignKey(Course, verbose_name='课程')
    add_time = models.DateField(default=datetime.now, verbose_name='学习时间')

    class Meta:
        verbose_name = '用户课程'
        verbose_name_plural = verbose_name
