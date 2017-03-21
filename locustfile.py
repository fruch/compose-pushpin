from locust import HttpLocust, TaskSet

def index(l):
    l.client.get("/hello/test")

class UserBehavior(TaskSet):
    tasks = {index: 1}

class LongPollUser(HttpLocust):
    task_set = UserBehavior
    min_wait = 100
    max_wait = 300
