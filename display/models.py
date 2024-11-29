from django.db import models

# Create your models here.
class whole_city(models.Model):
    city_Names = models.TextField(max_length=100)

    def __str__(self):
        return self.city_Names
