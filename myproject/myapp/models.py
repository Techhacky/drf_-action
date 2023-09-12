from django.db import models

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=100)
    # completed = models.BooleanField(default=False)
    description=models.CharField(max_length=1000)
   
    name = models.CharField( max_length=255)
    priority = models.PositiveSmallIntegerField( unique=True,null=False)

    def __str__(self):
        return self.name
