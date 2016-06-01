"""This bot will update the main server with new stats"""
import requests
import json

LOCAL_ENDPOINT = "http://127.0.0.1:8000/api/v1/"

class Flourine(object):

    def __init__(self, local_endpoint):
        self.local_endpoint = local_endpoint

    def _hit_endpoint(self, target, verb="get", **kwargs):
        return getattr(requests, verb)(target, **kwargs).json()

    def upload_data(self, name, value):
        response = self._hit_endpoint(self.local_endpoint, verb="post", data={name: name, value: json.dumps(value)})
        assert response.ok


if __name__ == "__main__":
    FBot = Flourine(LOCAL_ENDPOINT)
    FBot.upload_data("test", {"foo": "bar"})
