from django.db import models

class Customer(models.Model):
    tc_no = models.CharField(max_length = 11, unique = True)
    name = models.CharField(max_length = 50)
    surname = models.CharField(max_length = 50)
    phone = models.CharField(max_length = 11)
    city = models.CharField(max_length = 50)
    state = models.CharField(max_length = 50)

    def __str__(self):
        return '%s, %s' %(self.name, self.surname)
