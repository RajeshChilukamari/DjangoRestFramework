from django.db import models
import pytz

# Create your models here.


class User(models.Model):
    # (actual value, human readable name)
    timezones = tuple(zip(pytz.all_timezones, pytz.all_timezones))

    id = models.AutoField(primary_key=True)
    real_name = models.CharField(max_length=50)
    tz = models.CharField(max_length=32, choices=timezones, default='UTC')


class ActivityPeriod(models.Model):
    eid = models.ForeignKey(User, related_name="activity_periods",
                            on_delete=models.CASCADE)
    start_time = models.DateTimeField(auto_now_add=True)
    end_time = models.DateTimeField(auto_now_add=True)
