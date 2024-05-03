import time
from locust import HttpUser, task, between
from locust.contrib.fasthttp import FastHttpUser


class QuickstartUser(FastHttpUser):
    wait_time = between(0.1, 1.1)

    @task
    def get_root(self):
        self.client.get("/")
