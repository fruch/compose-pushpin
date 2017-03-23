from locust import HttpLocust, TaskSet

def index(l):
    with l.client.get("/hello/test", catch_response=True) as response:
        if response.status_code == 200:
            response.success()
        else:
            response.failure("%d, %s" % (response.status_code, response.content))


class UserBehavior(TaskSet):
    tasks = {index: 1}

class LongPollUser(HttpLocust):
    task_set = UserBehavior
    min_wait = 100
    max_wait = 300
