from django.shortcuts import render
from rest_framework import views 
from rest_framework.response import Response
from .tasks import UserDataUploadTask, UserDataUploadMultiThreadingTask, sendMailTaskCeleryFunction
import pandas as pd
from .models import UserDataModel
from .data import JsonData
import requests
import json
from datetime import datetime 



# Create your views here.
#  User Upload Data regular iteration 
class UserDataModelAPIView(views.APIView):
    def get(self, request):        
        return Response({"message" : "Request POST Method for uploading data ",
                         "process" : "Regular Iterator"}) 

    def delete(self, request):
        UserDataModel.objects.all().delete()
        return Response({"message" : "All items deleted"})
    def post(self, request):
    #    sendEmailCeleryTask.delay("sendEmailCeleryAPIView Task Active")
        UserDataUploadTask.delay("Upload the data")
        return Response({"message" : f"Request was sent to the server",
                         "process" : "Regular Iterator"})

#
class UserDataModelMultiThreadDataUploadAPIView(views.APIView):
    def get(self, request):        
        return Response({"message" : "Request POST Method for uploading data ",
                         "process" : "Multi Threading"}) 

    def delete(self, request):
        UserDataModel.objects.all().delete()
        return Response({"message" : "All items deleted"})
    def post(self, request):
    #    sendEmailCeleryTask.delay("sendEmailCeleryAPIView Task Active")
        UserDataUploadMultiThreadingTask.delay("Upload the data")
        return Response({"message" : f"Request was sent to the server",
                         "process" : "Multi Threading"})


# sendMailTaskCeleryFunction
class sendMailTaskCeleryFunctionAPIView(views.APIView):
    def get(self, request):        
        return Response({"message" : "Request POST Method for Sending Bulk Mail"}) 

    def delete(self, request):
        UserDataModel.objects.all().delete()
        return Response({"message" : "All items deleted"})
    def post(self, request):
    #    sendEmailCeleryTask.delay("sendEmailCeleryAPIView Task Active")
        sendMailTaskCeleryFunction.delay("Bulk Email Sender Celery Tast Started.....")
        return Response({"message" : f"Request sent Sending Bulk Mail"})


class ReadJsonDataAPIView(views.APIView):
    def post(self, request):
        data = request.FILES["jsonfile"]
        print(data)
        try:
            Jsondata = json.load(data)
            print(Jsondata)
        except Exception as e:
            print(e)
        return Response("ok")