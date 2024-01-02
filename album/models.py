from django.db import models
from musician.models import musicians

lists = (('1','1'),('2','2'),('3','3'),('4','4'),('5','5'))

# Create your models here.
class albums(models.Model):
    Album_name = models.CharField(max_length=100)
    author = models.ForeignKey(musicians, on_delete=models.CASCADE)
    albums_release_date = models.DateField()
    album_rating = models.CharField(max_length = 5, choices=lists)

    def __str__(self):
        return self.Album_name