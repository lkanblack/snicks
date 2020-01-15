from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    image = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=200)
    text = models.TextField()
    #created_date = models.DateTimeField(default=timezone.now)
    #published_date = models.DateTimeField(blank=True, null=True)
    price = models.IntegerField()

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title