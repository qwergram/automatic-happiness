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
        assert response.ok, (response.reason, target)
        return response.text

    def update_local_database(self):
        for stock in self.stocks:
            target = self.yahoo_endpoint.format(SYMB=stock)
            try:
                response = self._hit_endpoint(target)
                for line in response.split('\n'):
                    line = line.split(',')
            except AssertionError:
                print("Error returning Stock:", stock)


if __name__ == "__main__":
    # SP500 is ^GSPC for some reason. I'm not financially savy enough
    # to know why or if that's even true to begin with...
    stocks = "^GSPC NDX DJIA VOO VB CORP VNQ VWO SHY".split()
    NBot = Neon(stocks, YAHOO_CSV_TARGET, LOCAL_ENDPOINT)
    NBot.update_local_database()
