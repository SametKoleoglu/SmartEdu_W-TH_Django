from django.db import models
from teachers.models import Teacher
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=50,null=True,unique=True,verbose_name='Category Name',help_text='Write Category Name')
    slug = models.SlugField(max_length=50,unique=True,null=True)
    description = models.TextField(blank=True,null=True)
    date = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name



class Tag(models.Model):
    name = models.CharField(max_length=50,null=True,unique=True,verbose_name='Tag Name',help_text='Write Tag Name')
    slug = models.SlugField(max_length=50,unique=True,null=True)
    date = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name

class Course(models.Model):
    teacher = models.ForeignKey(Teacher,null=True,on_delete=models.CASCADE)
    name = models.CharField(max_length=100,unique=True,verbose_name='Course Name',help_text='Write Course Name')
    category = models.ForeignKey(Category,null=True,on_delete=models.DO_NOTHING)
    tag = models.ManyToManyField(Tag,blank=True,null=True)
    student = models.ManyToManyField(User,blank=True,related_name='courses_joined')
    description = models.TextField(blank=True,null=True)
    image = models.ImageField(upload_to='courses/%Y/%m/%d',default="courses/default_course.jpg")
    date = models.DateTimeField(auto_now=True)
    available = models.BooleanField(default=True)
    
    
    def __str__(self):
        return self.name
    
    


