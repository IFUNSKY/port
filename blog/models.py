from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=200, default='DEFAULT VALUE')
    pub_date = models.DateTimeField(auto_now=False, auto_now_add=False,)
    image = models.ImageField(upload_to='images/')
    summary = models.CharField(max_length=200, default='DEFAULT VALUE')
