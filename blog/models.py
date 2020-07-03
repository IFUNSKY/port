from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=200, default='DEFAULT VALUE')
    pub_date = models.DateTimeField(auto_now=False, auto_now_add=False,)
    image = models.ImageField(upload_to='images/')
    summary = models.TextField(max_length=200, default='DEFAULT VALUE')

    def __str__(self):
        return self.title

    def sum(self):
        return self.summary[:10]

    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e %Y')
