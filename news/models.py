from django.db import models
# from django.contrib.auth import models.Us

class Author(models.Model):
    # user = models.OneToOneField()
    user_rating = models.IntegerField(default=0)

class Category(models.Model):
    category_name = models.CharField(max_length=255, unique=True)

class Post(models.Model):
    author = models.ForeignKey(Author)
    choice = models.CharField(max_length=3)
    create_date = models.DateTimeField(auto_now_add=True)
    category = models.ManyToManyField(Category)
    post_title = models.CharField(max_length=255)
    post_text = models.TextField()
    post_rating = models.IntegerField(default=0)

class PostCategory(models.Model):
    post = models.ForeignKey(Post)
    category = models.ForeignKey(Category)
# Create your models here.
# sauto_now
# Если True, то автоматически устанавливает в это поле текущую дату каждый раз при сохранении объекта.
# auto_now_add
# Если True, то автоматически устанавливает в это поле дату создания объекта.
# default
# Значение по умолчанию.
