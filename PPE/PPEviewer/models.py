from django.db import models

# Create your models here.

class feedback(models.Model):
    Name=(models.CharField(max_length=50))
    Department=(models.CharField(max_length=50))
    Suggestion=(models.CharField(max_length=50))
    Rating=(models.IntegerField(default=5))

    # def __str__(self):
    #     self.Name
class ppeviwer(models.Model):
    name=(models.CharField(max_length=50))
    missed_ppe=(models.CharField(max_length=50))
    time=(models.CharField(max_length=50))
    date=(models.IntegerField(default=50))





