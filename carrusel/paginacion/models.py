from django.db import models

class List(models.Model):
    ident = models.IntegerField()

class ListElem(models.Model):
    ident = models.ForeignKey(List)
    elem = models.CharField(max_length=200)

    def __str__(self):
        return str(self.elem)
