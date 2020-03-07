from django.db import models

# Create your models here.

class InductionData (models.Model):
    No = models.PositiveIntegerField()
    Date = models.DateField()
    Hour = models.PositiveIntegerField(choices=((str(x), x) for x in range(0,23)))
    Temp = models.IntegerField()
    Demand = models.DecimalField(max_digits=5, decimal_places=2)
    DayType = models.CharField(max_length=254)