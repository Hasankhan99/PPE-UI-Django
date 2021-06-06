from django.db import models

# Create your models here.

class feedback(models.Model):
    Name=(models.CharField(max_length=50))
    Department=(models.CharField(max_length=50))
    Suggestion=(models.CharField(max_length=50))
    Rating=(models.IntegerField(default=5))

    # def __str__(self):
    #     self.Name