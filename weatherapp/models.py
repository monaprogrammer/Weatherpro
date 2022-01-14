from django.db import models

class Weatherapi(models.Model):
    descriptions = models.TextField(max_length=1000)
    city = models.CharField(max_length=100)
    city_weather = models.IntegerField()
    created_on = models.DateTimeField(auto_now_add=True)


    def __str__(self):
       return self.city


class Weatherapp():
    pass

class Weatherapptest():
    pass