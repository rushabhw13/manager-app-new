from django.db import models

class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    opening_hours = models.CharField(max_length=100)
    cuisines = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    directions = models.TextField()

    def __str__(self):
        return self.name


class Menu(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    nutrition_data = models.TextField()
    allergic_data = models.TextField()
    image = models.ImageField(upload_to='menu_images/', null=True, blank=True)

    def __str__(self):
        return self.name


class Tables(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    tables_seats = models.IntegerField()
    description = models.TextField()

    def __str__(self):
        return self.name


class Staff(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    qualification = models.TextField()
    experience = models.IntegerField()

    def __str__(self):
        return self.name
    
class Todayspecial(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='todayspecial_images/')

    def __str__(self):
        return self.name
