from django.db import models

# Create your models here.
# 用户表
class Users(models.Model):
    u_name = models.CharField(max_length=20)
    u_password = models.CharField(max_length=50)
    u_icons = models.ImageField(upload_to='icons')
    u_email = models.CharField(max_length=50)

    class Meta:
        db_table = "Users"

# 电影表
class Movies(models.Model):
    postid = models.CharField(max_length=20)
    title = models.CharField(max_length=100)
    image = models.CharField(max_length=200)
    duration = models.CharField(max_length=20)
    app_fu_title = models.CharField(max_length=200)

    class Meta:
        db_table = "Movies"

# 收藏表
class MyCollects(models.Model):
    m_users = models.ForeignKey('Users')
    m_movies = models.ForeignKey('Movies')

    class Meta:
        db_table = "MyCollects"