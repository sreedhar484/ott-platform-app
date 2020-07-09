from django.db import models
from django.contrib.auth.models import User
from multiselectfield import MultiSelectField

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='pics',default='default.png')
    MY_CHOICES = (('horror', 'horror'),
              ('comedy', 'comedy'),
              ('thriller', 'thriller'),
              ('suspense', 'suspense'),
              ('romance', 'romance'),
              ('sci-fi','sci-fi'),
              ('drama','drama'),
              ('action','action'))
    m_type = MultiSelectField(choices=MY_CHOICES)
    favorate_hero = models.CharField(max_length=1000)
    favorate_heroin = models.CharField(max_length=1000)
    favorate_director = models.CharField(max_length=1000)

    def __str__(self):
        return self.user.username

class Movies(models.Model):
    name = models.CharField(max_length=1000)
    movie_poster = models.ImageField(upload_to='poster')
    movie_long = models.ImageField(upload_to='long poster')
    discription = models.TextField(default=None)
    language = models.CharField(max_length=1000)
    MY_CHOICES = (('horror', 'horror'),
              ('comedy', 'comedy'),
              ('thriller', 'thriller'),
              ('suspense', 'suspense'),
              ('romance', 'romance'),
              ('sci-fi','sci-fi'),
              ('drama','drama'),
              ('action','action'))
    select_movie_types_liked = MultiSelectField(choices=MY_CHOICES)
    triler = models.FileField(default=None,upload_to='trailer')
    movie = models.FileField(default=None,upload_to='movie')
    hero_name = models.CharField(max_length=1000)
    actor = models.ImageField(upload_to='hero')
    heroin_name = models.CharField(max_length=1000)
    actress = models.ImageField(upload_to='heroin')
    director = models.ImageField(upload_to='director')
    director_name = models.CharField(max_length=1000)
    def __str__(self):
        return self.name

class Slide(models.Model):
    question = models.ForeignKey(Movies,default=None,on_delete=models.CASCADE)
    slide_poster = models.ImageField(upload_to='slide')
    

class App(models.Model):
    app = models.FileField(default=None,upload_to='app')

