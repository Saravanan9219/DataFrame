# coding: utf-8

"""
Stock Frame
"""


import requests
import os
import pandas


class StockFrame(object):
    """
    Stock Frame provides pandas data frame for the provided
    ticker for specific period intervals
    params: ticker: ticker symbol
            period: [daily, monthly, weekly]
            start_date(optional): YYY-mm-dd
            api_key: api_key to user for api call(quandl)

    Usage:
        data_frame = StockFrame('ICICIBANK', 'monthly').data_frame
    """

    start_date = '2016-01-01'
    api_key = os.environ['API_TOKEN']

    def __init__(self, ticker, period, start_date=None, api_key=None):
        if api_key is not None:
            self.api_key = api_key
        if start_date is not None:
            self.start_date = start_date
        self.ticker = ticker
        self.period = period
        self.__api_response = None
        self.__data_frame = None

    @property
    def api_response(self):
        """Api response property"""
        if self.__api_response is None:
            params = {
                'ticker': self.ticker,
                'api_key': self.api_key,
                'period': self.period,
                'start_date': self.start_date
            }
            url = 'https://quandl.com/api/v3/datasets/NSE/{ticker}/' + \
                          'data.json?api_key={api_key}&collapse={period}' + \
                          '&start_date={start_date}'
            self.__api_response = requests.get(url.format(**params))
        return self.__api_response

    @property
    def data_frame(self):
        """Data frame property"""
        if self.__data_frame is None:
            data = self.api_response.json()['dataset_data']
            self.__data_frame = pandas.DataFrame(data['data'],
                                                 columns=data['column_names'])
        return self.__data_frame
