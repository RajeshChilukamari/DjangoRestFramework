from faker import Factory
import factory
from rest_framework import serializers
from .models import User, ActivityPeriod


# child model
class ActivityPeriodSerialiser(serializers.ModelSerializer):
    class Meta:
        model = ActivityPeriod
        fields = ['start_time', 'end_time']


# parent model
class UserSerialiser(serializers.ModelSerializer):
    activity_periods = ActivityPeriodSerialiser(many=True, read_only=True)

    class Meta:
        model = User
        fields = ['id', 'real_name', 'tz', 'activity_periods']


# For populating the data
faker = Factory.create()


class RandomUserFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = User

    #id = User.objects.last().id + 1
    real_name = faker.name()
    tz = faker.timezone()


class RandomActivityPeriodFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = ActivityPeriod

    eid = factory.SubFactory(RandomUserFactory)
    start_time = faker.date_time()
    end_time = faker.date_time()
