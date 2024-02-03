from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

AGE_CHOICES = (
    ('ALL', 'ALL'),
    ('kids', 'Kids'),
)
MOVIE_CHOICES = (
    ('seasonal', 'Seasonal'),
    ('single', 'Single'),
)

class Videos(models.Model):
    v_title = models.CharField(max_length=100)
    video = models.FileField(upload_to='static/video')
    
    def __str__(self):
        return self.v_title

class Movies_Series(models.Model):
    ms_title = models.CharField(max_length=1000)
    description = models.TextField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    ms_type = models.CharField(choices=MOVIE_CHOICES,max_length=10)
    video = models.ForeignKey('Videos', on_delete=models.CASCADE)
    flyer = models.ImageField(upload_to='static/images/assets/flyer')
    age_limit = models.CharField(choices=AGE_CHOICES,max_length=10)
    
    def __str__(self):
        return self.ms_title