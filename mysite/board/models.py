from django.db import models
from django.contrib.auth.models import User
import datetime
from django.utils import timezone

TYPE_OF_EVENT = [

    ('DELIVERY', 'Delivery'),
    ('FUNDRAISER', 'Fundraiser'),
    ('CAMPAIGN', 'Campaign'),
    ('OTHER', 'Other')

]

class Request(models.Model):
    title = models.CharField(max_length=400, unique=True)
    description = models.CharField(max_length=900, unique=True, default='No Description Given')
    published_date = models.DateTimeField(auto_now_add=True)
    event_date = models.DateTimeField('Event Date')
    event_address = models.CharField(max_length=400)
    city = models.CharField(max_length=200)
    requester = models.ForeignKey(User, on_delete=models.CASCADE, related_name='requester')
    coordinator = models.ForeignKey(User, null=True, on_delete=models.CASCADE, related_name='coordinator')
    volunteers = models.ManyToManyField(User, related_name='volunteer', default=User.objects.first())
    contact = models.CharField(max_length=254)
    number_of_volunteers = models.IntegerField(default=0)
    type = models.CharField(max_length=15, default='Other')

    def __str__(self):
        return self.title


# Create your models here.
