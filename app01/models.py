from django.db import models
from django.db.models import Q
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser, Group, PermissionsMixin,
)
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType
from django.utils.safestring import mark_safe
import hashlib


# Create your models here.

class Accont(models.Model):
    """课程大类, e.g 前端  后端..."""
    name = models.CharField(max_length=64, unique=True)
    password = models.CharField('password', max_length=128,)
    is_staff = models.BooleanField(verbose_name='staff status', default=False, help_text='决定着用户是否可登录管理后台')

    def __str__(self):
        return "%s" % self.name

    class Meta:
        verbose_name = "用户表"
        verbose_name_plural = "用户表"


class Article(models.Model):
    """文章资讯"""
    title = models.CharField(max_length=255, unique=True, db_index=True, verbose_name="标题")
    source = models.CharField(max_length=255, verbose_name="来源")
    head_img = models.CharField(max_length=255)
    head_img2 = models.CharField(max_length=255)
    head_img3 = models.CharField(max_length=255)
    url = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now_add=True, verbose_name="创建日期")

    class Meta:
        verbose_name = "文章表"
        verbose_name_plural = "文章表"

