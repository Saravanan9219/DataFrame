# coding: utf-8


"""
Wrapper around Stock Frame for
mathematical calculations
"""


from api.frame import StockFrame


class StockData(StockFrame):
    """
    Stock Frame provides pandas data frame for the provided
    ticker for specific period intervals
    params: ticker: ticker symbol
            period: [daily, monthly, weekly]
            start_date(optional): YYY-mm-dd
            api_key: api_key to user for api call(quandl)

    Usage:
        std = StockFrame('ICICIBANK', 'monthly').get_std_values('High')
   """

    def get_std_values(self, attr='High'):
        """get standard deviation values"""
        return self.data_frame[attr].std()
