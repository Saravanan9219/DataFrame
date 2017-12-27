import mock

from api.stock_info import StockData


class TestStockData(object):

    @mock.patch('api.frame.requests.get')
    def test_standard_deviation(self, requests_mock, api_mock):
        requests_mock.side_effect = api_mock()
        std_value = StockData('TICKER', 'monthly').get_std_values()
        assert round(std_value, 2) == 20.14
