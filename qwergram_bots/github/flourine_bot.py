"""This bot will update the main server with new stats"""
import requests
import json
import os

LOCAL_ENDPOINT = "http://127.0.0.1:8000/api/v1/"


class Flourine(object):

    def __init__(self, local_endpoint, admin, admin_pass):
        self.local_endpoint = local_endpoint
        self.admin = admin
        self.admin_pass = admin_pass

    def _hit_endpoint(self, target, verb="get", **kwargs):
        return getattr(requests, verb)(target, **kwargs)#.json()

    def upload_data(self, name, value):
        data = {"name": name, "value": value}
        auth = requests.HTTPBasicAuth(self.admin, self.admin_pass)
        response = self._hit_endpoint(self.local_endpoint, verb="post", data=data, auth=auth)
        assert response.ok, response.json()


if __name__ == "__main__":
    admin = os.environ['ADMIN_USER']
    admin_pass = os.environ['ADMIN_PASS']
    FBot = Flourine(LOCAL_ENDPOINT, admin, admin_pass)
    FBot.upload_data("test", {"foo": "bar"})
