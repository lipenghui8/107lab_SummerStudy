from django.db import models


# Create your models here.
class BookInfo(models.Model):
    title = models.CharField(max_length=20)
    date = models.DateField()

    def __str__(self):
        return self.title


class People(models.Model):
    name = models.CharField(max_length=10)
    PersonInfo = models.CharField(max_length=100)
    gender = models.BooleanField(default=True)
    book = models.ForeignKey('BookInfo', on_delete=models.CASCADE,)

    def __str__(self):
        return self.name.encode('utf-8')