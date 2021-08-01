from django.db import models
# Create your models here.
class Bookinfo(models.Model):
    title = models.CharField(max_length=20)
    pub_data = models.DateField()

    def __str__(self):
        return self.title
class Heroinfo(models.Model):
    name = models.CharField(max_length=10)
    content = models.CharField(max_length=100)
    gender = models.BooleanField(default=True)
    book = models.ForeignKey(Bookinfo,on_delete=models.CASCADE)