"""This bot will read the Yahoo CSVs and upload new data to the server"""
import requests
from github.flourine_bot import LOCAL_ENDPOINT

YAHOO_CSV_TARGET = "http://real-chart.finance.yahoo.com/table.csv?s={SYMB}"


class Neon(object):

    def __init__(self, stocks, yahoo_endpoint, local_endpoint):
        self.stocks = stocks
        self.yahoo_endpoint = yahoo_endpoint
        self.local_endpoint = local_endpoint

    def _hit_endpoint(self, target, verb="get", **kwargs):
        response = getattr(requests, verb)(target, **kwargs)
        assert response.ok, response.reason
        return response.json()
