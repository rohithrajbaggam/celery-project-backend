from django.urls import path 
from .views import UserDataModelAPIView, UserDataModelMultiThreadDataUploadAPIView, sendMailTaskCeleryFunctionAPIView, ReadJsonDataAPIView


urlpatterns = [
    path("user-data-upload/", UserDataModelAPIView.as_view(), name="sendEmailCeleryAPIView"),
    path("user-data-upload-multi-thread/", UserDataModelMultiThreadDataUploadAPIView.as_view(), name="UserDataModelMultiThreadDataUploadAPIView"),
    path("send-email-task-api/", sendMailTaskCeleryFunctionAPIView.as_view(), name="sendMailTaskCeleryFunctionAPIView"),
    path("json-file/", ReadJsonDataAPIView.as_view(), name="ReadJsonDataAPIView"),
]

