"""This bot will read the Yahoo CSVs and upload new data to the server"""
import requests
import os

LOCAL_ENDPOINT = "http://127.0.0.1:8000/api/v1/stocks/"
YAHOO_CSV_TARGET = "http://real-chart.finance.yahoo.com/table.csv?s={SYMB}"


class Neon(object):

    def __init__(self, stocks, yahoo_endpoint, local_endpoint, admin, admin_pass):
        self.stocks = stocks
        self.yahoo_endpoint = yahoo_endpoint
        self.local_endpoint = local_endpoint
        self.admin = admin
        self.admin_pass = admin_pass

    def _hit_endpoint(self, target, verb="get", **kwargs):
        response = getattr(requests, verb)(target, **kwargs)
        assert response.ok, (response.reason, target)
        return response.text

    def update_local_database(self):
        for stock in self.stocks:
            target = self.yahoo_endpoint.format(SYMB=stock)
            try:
                response = self._hit_endpoint(target)
                for line in response.split('\n')[1:-1]:
                    self.push_data_to_server(stock, *line.split(','))
            except AssertionError:
                print("Error returning Stock:", stock)

    def push_data_to_server(self, symbol, date, open, high, low, close, volume, adj_close):
        data = {
            "symbol": symbol,
            "date": date,
            "high": high,
            "low": low,
            "open": open,
            "close": close,
            "volume": volume,
            "adj_close": adj_close,
        }
        self._hit_endpoint(self.local_endpoint, verb="post", data=data, auth=(self.admin, self.admin_pass))


if __name__ == "__main__":
    stocks = "VOO VB CORP VNQ VWO SHY".split()
    admin = os.environ['ADMIN_USER']
    admin_pass = os.environ['ADMIN_PASS']
    NBot = Neon(stocks, YAHOO_CSV_TARGET, LOCAL_ENDPOINT, admin, admin_pass)
    NBot.update_local_database()
