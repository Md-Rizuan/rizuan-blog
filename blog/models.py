from django.db import models
from django.utils.text import slugify

from ckeditor.fields import RichTextField

# Create your models here.

from user_profile.models import User

class Category(models.Model):
    title = models.CharField(max_length=150, unique=True)
    slug = models.SlugField(null=True,blank=True)
    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)
    
class Tag(models.Model):

    title = models.CharField(max_length=150)
    slug = models.SlugField(null=True,blank=True)
    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)
class District(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
class Thana(models.Model):
    district = models.ForeignKey(District, on_delete=models.CASCADE, related_name='thanas')
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} ({self.district.name})"

class Blog(models.Model):
    user = models.ForeignKey(
        User,
        related_name='user_blogs',
        on_delete=models.CASCADE
    )
    category = models.ForeignKey(
        Category,
        related_name='category_blogs',
        on_delete=models.CASCADE
    )
    tags = models.ManyToManyField(
        Tag,
        related_name='tag_blogs',
        blank=True 
    )
    likes = models.ManyToManyField(
        Tag,
        related_name='user_likes',
        blank=True
    )
    title = models.CharField(
        max_length=250
    )
    slug = models.SlugField(null=True, blank=True)
    banner = models.ImageField(upload_to='blog_banners')
    description = RichTextField()
    created_date = models.DateField(auto_now_add=True)
    district = models.ForeignKey(District, on_delete=models.CASCADE, related_name='district_blogs', null=True, blank=True)
    thana = models.ForeignKey(Thana, on_delete=models.CASCADE, related_name='thana_blogs', null=True, blank=True)


    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    
class Comment(models.Model):
    user = models.ForeignKey(
        User,
        related_name='user_comments',
        on_delete=models.CASCADE
    )
    blog = models.ForeignKey(
        Blog,
        related_name='blog_comments',
        on_delete=models.CASCADE
    )
    text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text
    
class Reply(models.Model):
    user = models.ForeignKey(
        User,
        related_name='user_replies',
        on_delete=models.CASCADE
    )
    comment = models.ForeignKey(
        Comment,
        related_name='comment_replies',
        on_delete=models.CASCADE
    )
    text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text
    

class Todo(models.Model):
    title = models.CharField(max_length=100)
    deadline = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    

    def __str__(self):
        return self.title
    
     




    
