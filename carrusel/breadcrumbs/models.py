from django.db import models

# Create your models here.


class BreadcrumbsContent(models.Model):
    title = models.CharField(max_length=30)
    url = models.URLField()
    position = models.IntegerField(blank=True, null=True)

class BreadcrumbsContent(models.Model):
    title = models.CharField(max_length=30)
    url = models.URLField()
    position = models.IntegerField(blank=True, null=True)