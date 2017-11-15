from django.db import models

# Create your models here.


class BreadcrumbsLevels(models.Model):
    niveles = models.IntegerField()

class BreadcrumbsContent(models.Model):
    title = models.CharField(max_length=30)
    url = models.URLField()
    position = models.IntegerField(blank=True, null=True)
    breadcrumb = models.ForeignKey(BreadcrumbsLevels, on_delete=models.CASCADE)