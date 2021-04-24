from django.db import models


class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=250)
    birth_date = models.DateField()

    def __str__(self):
        return self.first_name + " " + self.last_name
