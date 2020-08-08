from django.shortcuts import render, HttpResponse
from .models import User, ActivityPeriod
from datetime import datetime
from django.http import HttpResponse, JsonResponse

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser

from .serializer import UserSerialiser, ActivityPeriodSerialiser

# Create your views here.


def index(request):
    return HttpResponse("Welcome")


def addUser(request):
    id = "101"
    real_name = "Heath Ledger"
    tz = "America/Los_Angeles"

    try:
        user, created = User.objects.get_or_create(
            id=id, real_name=real_name, tz=tz)
        if created:
            user.save()
            print("\n User {} created".format(user))
            msg = "User {} created".format(user)
        else:
            print("\n User {} already exist".format(user))
            msg = "User {} already exist".format(user)

    except Exception as ex:
        print(str(ex))
        print("User {} and {} not created".format(id, real_name))
        msg = str(ex) + "User {} and {} not created".format(id, real_name)
    return HttpResponse(msg)


def addActivityPeroid(request):
    id = "101"
    stime = datetime.now()
    etime = datetime.now()

    try:
        # getting parent id
        eid = User.objects.get(id=id)

        ap, created = ActivityPeriod.objects.get_or_create(
            eid=eid, start_time=stime, end_time=etime)

        if created:
            ap.save()
            print("\n Activity Peroid {} created".format(ap))
            msg = "Activity Peroid {} created".format(ap)
        else:
            print("\n Activity Peroid {} already exist".format(ap))
            msg = "Activity Peroid {} already exist".format(ap)

    except Exception as ex:
        print(str(ex))
        print("Activity Peroid {} not created".format(id))
        msg = str(ex) + "Activity Peroid {} not created".format(id)

    return HttpResponse(msg)


@api_view(['GET', 'POST'])
def api(request):
    if request.method == "GET":
        usersData = User.objects.all()
        serializer = UserSerialiser(usersData, many=True)
        data = {"ok": True, "members": serializer.data}
        return Response(data)

    elif request.method == "POST":
        serializer = UserSerialiser(data=request.data)
        print("\n\n\nserializer")
        print(serializer)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    else:
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
