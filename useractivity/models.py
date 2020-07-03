from django.db import models
class User(models.Model):
    id = models.CharField(max_length=30)
    real_name = models.CharField(max_length=30)
    tz = models.CharField(max_length=30)
class ActivityPeriod(models.Model):
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()



