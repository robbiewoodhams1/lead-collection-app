from django.db import models

# Create your models here.

class Lead(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=50)
    website = models.URLField(blank=True)
    city = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    place_id = models.CharField(max_length=255, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    called = models.BooleanField(default=False)
    outcome = models.CharField(
        choices=[
            ('not_answered', 'Not Answered'),
            ('call_back_later', 'Call Back Later'),
            ('converted', 'Converted'),
            ('no_interest', 'No Interest'),
            ('not_called', 'Not Called')
        ],
        default='not_called'
    )
    type = models.CharField(
        choices=[
            ('lead', 'Lead'),
            ('client', 'Client'),
            ('lost', 'Lost')
        ],
        default='lead'
    )
    notes = models.TextField(blank=True)

    def __str__(self):
        return self.name
