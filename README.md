
## Celery Project Backend
## Celery Task Bulk Request

- In Django, celery is a distributed task queue that allows you to run background processes or tasks asynchronously. It provides a way to offload time-consuming tasks from the main application flow.
- Celery tasks are known as asynchronous tasks because they allow your application to execute tasks in a non-blocking way. When you execute a task synchronously, your application waits for the task to complete before it continues with the next operation.

### Note

```
* Regular API's both Sync (HTTP) & Async (WSS) uses development server for performing
	operations. 
* While we wan to performing operation which deals with large amount of data and
	which high data processing & large amount of time, if we run on this process in development
	server it requires large amount time to perform and meanwhile we won't get response,
  due to high data processing server get crash.
* To handle this kind of situation, we run this process in celery server to reduce 
	load balance on the main development server.
```

### Asynchronous tasks

- Async tasks, are tasks that are executed independently and do not block the execution of other tasks or processes.

### Why Celery Task is Async ?

- Celery tasks are known as asynchronous tasks because they are executed in the background and don't block the main thread of your application, allowing it to continue processing other requests.

### Celery tasks are mostly used in

- Email Sending
- Image & Text Processing
- API calls and other web requests

### Technologies

```python
Python -> (Programming Language)
Django -> (Framework)
Celery-Django -> (Secondary server)
postgres -> (Database)
Redis ->  (Message Broker)
Docker -> (To run postgres & Redis container)
Git -> Version control
```

### Tools

```python
Vscode -> (Code Editor)
Docker -> ( Database Container ) 
Postman -> ( API Tester )
Chrome -> ( Browser the Admin Panel )
```

### Message Broker

- To receive tasks from your program and send results to a back end, Celery requires a message broker for communication.
- Redis and RabbitMQ are two message brokers that developers often use together with Celery.

## Database Configurations

**Docker Container**

**docker-compose.yaml**

```docker
version: "3.8"
services:
  celery_project_database:
    image: postgres
    restart: always

    environment:
      - POSTGRES_DB=celery_project
      - POSTGRES_USER=celery_project
      - POSTGRES_PASSWORD=celery_project@123
    ports:
      - 9050:5432
#volumes:
#     pgdata:
```

```python
# Database Integration 
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'celery_project',
        'USER': 'celery_project',
        'PASSWORD': 'celery_project@123',
        'HOST': 'localhost',
        'PORT': 9050,
    }
}
```