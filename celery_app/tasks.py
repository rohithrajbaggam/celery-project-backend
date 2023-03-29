from celery import shared_task
from django.conf import settings
from timeit import default_timer as timer
from .models import UserDataModel
from .utils import send_mail_function
from .emaildata import emailDataJson
import requests
from core.settings import SECONDARY_SERVER
from concurrent.futures import ThreadPoolExecutor

def uploadDataToDBFun(i, session):
    data = session.get(url=f"{SECONDARY_SERVER}dataapp/user-data-api/{i}/").json()
    
    instance = UserDataModel.objects.create(
                first_name = data["first_name"],
                last_name = data["last_name"],
                email = data["email"],
                city = data["city"],
                countrycode = data["country"],
                country = data["countrycode"],
                bio = data["bio"]
                        )

@shared_task
def UserDataUploadTask(message):
    start_time = timer()
    try:
        print("Uploading Data regular iterator....")
        size = int(requests.get(f"{SECONDARY_SERVER}dataapp/data-count/").json()["data"])
        
        for i in range(1,size+1):
            try:
                session = requests.Session()
                uploadDataToDBFun(i, session) 
            except Exception as e:
                print(f"Exception from upload task regular, {e} -> 1")
                
        
    except Exception as e:
        print(f"Exception from upload task regular, {e} -> 2") 
    end_time = timer()
    time_difference = end_time - start_time
    print(f"Data Uploaded Successfully in {time_difference}")


@shared_task
def UserDataUploadMultiThreadingTask(message):
    start_time = timer() 
    try:
        print("Uploading Data through multi-threading....")
        size = int(requests.get(f"{SECONDARY_SERVER}dataapp/data-count/").json()["data"])
        
        with ThreadPoolExecutor(max_workers=10) as executor: 
            with requests.Session() as session:
                [executor.map(uploadDataToDBFun, [i], [session]) for i in range(size)]
                executor.shutdown(wait=True)
                
        
    except Exception as e:
        print(f"Multi Thread Task Exception, {e}")
    end_time = timer()
    time_difference = end_time - start_time
    print(f"Data Uploaded Successfully in {time_difference}")


@shared_task
def sendMailTaskCeleryFunction(message):
    print(message)
    start_time = timer()
    for i in emailDataJson:
        try:
            send_mail_function(subject=i["subject"],
                           email=["rohithbaggam.github@gmail.com"],
                           message=i["message"],
                           sender=settings.EMAIL_HOST)
        except Exception as e:
            print(f"Bulk Email Exception, {e}")
    end_time = timer()

    print(f"Bulk Email Sender Celery Tast Completed....., {end_time-start_time}") 
    





