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

    def update_local_database(self):
        for stock in self.stocks:
            target = self.yahoo_endpoint.format(SYMB=stock)
            response = self._hit_endpoint(target)
            assert response.ok, response.reason
            for line in response.split('\n'):
                line = line.split(',')
                print(line)


if __name__ == "__main__":
    stocks = "SPX NDX DJIA VOO VB CORP VNQ VWO SHY".split()
    NBot = Neon(stocks, YAHOO_CSV_TARGET, LOCAL_ENDPOINT)
    NBot.update_local_database()
