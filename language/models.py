from django.db import models

# Create your models here.
class Quiz(models.Model):
    quize_text_english = models.CharField(max_length=500, null=True)
    quize_text_portuguese = models.CharField(max_length=500, null=True)
    quize_text_chinese = models.CharField(max_length=500, null=True)
    pub_date = models.DateTimeField('date published', null=True)


class Video(models.Model):
    video_url = models.CharField(max_length=300)
    pub_date = models.DateTimeField('date published')

# test
