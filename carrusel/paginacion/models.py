from django.db import models

class Elemento(models.Model):
   
    name = models.CharField(max_length=50, blank=True)
    

    def __str__(self):
        return self.title


