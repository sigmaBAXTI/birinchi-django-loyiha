from django.db import models

# Create your models here.
class Yangilik(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()

    def __str__(self):
        return self.title