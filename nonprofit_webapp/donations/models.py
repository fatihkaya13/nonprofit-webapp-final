from django.db import models
from djmoney.models.fields import MoneyField
from django.contrib.auth.models import User

# Create your models here.
class Donation(models.Model):
    name = models.CharField(max_length=100, default="Volunteer App Donation")
    #amount = models.DecimalField(max_digits=10, decimal_places=2)
    amount = MoneyField(max_digits=14, decimal_places=2, default_currency='USD')

    FREQUENCY_TYPE = [
        ('One-time', 'One-time'),
        ('Monthly', 'Monthly'),
        ('Annually', 'Annually'),
    ]
    frequency = models.CharField(choices=FREQUENCY_TYPE, default='One-time', max_length=20)
    created = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.name

    # show newest donation on top
    class Meta:
        ordering = ('-created',)