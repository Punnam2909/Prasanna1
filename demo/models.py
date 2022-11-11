from django.db import models
from PIL import Image

# Create your models here.


class Post(models.Model):
    img=models.ImageField(upload_to="Photos/",null=True,default=True)
    Name= models.CharField(max_length=120)
    Job= models.CharField(max_length=120)
    Company= models.CharField(max_length=120)
    DOJ= models.DateField()
    salary= models.IntegerField()
    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"
    def __str__(self):
        return self.Name

    def save(self,*args,**kwargs):
        super().save(*args,**kwargs)
        pic=Image.open(self.img.path)

        if pic.height >300 or pic.width >300:
            output_size=(300,300)
            pic.thumbnail(output_size)
            pic.save(self.img.path)



class Poll(models.Model):
    Name=models.CharField(default="None",max_length=120)
    DOB=models.DateField()
    class Meta:
        verbose_name = "Poll"
        verbose_name_plural = "Polls"

    def __str__(self):
        return self.Name



class Roll(models.Model):
    Name=models.CharField(max_length=120)
    DOB=models.DateField()
    class Meta:
        verbose_name = "Roll"
        verbose_name_plural = "Rolls"

    def __str__(self):
        return self.Name



class Category(models.Model):
    Family=models.CharField(default=None,max_length=120)
    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.Family

class Intial(models.Model):
    category=models.ForeignKey(Category,on_delete=models.CASCADE,related_name="Categories")
    Surname=models.CharField(max_length=120)
    class Meta:
        verbose_name = "Intial"
        verbose_name_plural = "Intials"

    def __str__(self):
        return self.Surname
