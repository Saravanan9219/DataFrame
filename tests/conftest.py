import json
import os
import pytest


FIXTURES_DIR = os.path.dirname(os.path.realpath(__file__))


class FakeResponse(object):
    def __init__(self, data):
        self.data = data

    @property
    def response(self):
        return self.data

    def json(self):
        return json.loads(self.response)



class RequestMock(object):
    def __init__(self, data=None):
        self.data = data
        self.args = None
        self.kwargs = None

    def __call__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs
        file_path = os.path.join(
            FIXTURES_DIR, 'fixtures/monthly_api_response.json')
        with open(file_path) as data_file:
            response_data = json.loads(data_file.read())
        if self.data:
            response_data['dataset_data']['data'] = self.data
        return FakeResponse(json.dumps(response_data))



@pytest.fixture
def api_mock():
    def mock_func(data=None):
        return RequestMock(data)
    return mock_func
