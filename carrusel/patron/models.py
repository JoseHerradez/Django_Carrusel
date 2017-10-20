from django.db import models

class Carousel(models.Model):
    count = models.IntegerField()
    title = models.CharField(max_length=50, blank=True)
    current_position = models.IntegerField(blank=True, default=0)
    timer = models.IntegerField(blank=True, default=3)
    auto = models.BooleanField(default=False)
    circular = models.BooleanField(default=True)
    elements = None

    def __str__(self):
        return self.title

class Content(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=256, blank=True)
    url = models.URLField(blank=True, null=True)
    image = models.ImageField(upload_to='content/')
    position = models.PositiveIntegerField(default=0)
    carousel = models.ForeignKey(Carousel, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
