from django.db import models
from django.conf import settings
 
class Profile(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    language = models.CharField(max_length=200, choices=settings.LANGUAGES)
    preferences = models.JSONField('Article title', default=dict)
 
    def __str__(self):
        return self.title