from django.db import models

# Create your models here.


class BookInfo(models.Model):
    title = models.CharField(max_length=30)
    pub_data = models.DateField()

    def __str__(self):
        return self.title


class HeroInfo(models.Model):
    name = models.CharField(max_length=30)
    content = models.CharField(max_length=50)
    gender = models.BooleanField(default=False)
    book = models.ForeignKey(BookInfo, on_delete=models.CASCADE,)

    def __str__(self):
        return self.name
