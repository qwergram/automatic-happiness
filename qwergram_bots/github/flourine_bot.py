"""This bot will update the main server with new stats"""
import requests
import json
import os

LOCAL_ENDPOINT = "http://127.0.0.1:8000/api/v1/stats/"


class Flourine(object):

    def __init__(self, local_endpoint, admin, admin_pass):
        self.local_endpoint = local_endpoint
        self.admin = admin
        self.admin_pass = admin_pass

    def _hit_endpoint(self, target, verb="get", **kwargs):
        response = getattr(requests, verb)(target, **kwargs)
        assert response.ok, response.reason
        return response.json()

    def get_url_from_name(self, name):
        results = self._hit_endpoint(self.local_endpoint)['results']
        for result in results:
            if result['name'] == name:
                return result['url']


    def upload_data(self, name, value):
        data = {"name": name, "value": json.dumps(value)}
        try:
            response = self._hit_endpoint(self.local_endpoint, verb="post", data=data, auth=(self.admin, self.admin_pass))
        except AssertionError:
            url = self.get_url_from_name(name)
            response = self._hit_endpoint(url, verb="put", data=data, auth=(self.admin, self.admin_pass))
        return response

if __name__ == "__main__":
    admin = os.environ['ADMIN_USER']
    admin_pass = os.environ['ADMIN_PASS']
    FBot = Flourine(LOCAL_ENDPOINT, admin, admin_pass)
    print(FBot.upload_data("test2", {"fizz": "bar"}))
