import pytest
from xtb_api.xtb_api import XTBClient
import json

@pytest.fixture
def default_xtb_client():
    """Returns XTBClient instance with user, password"""
    return XTBClient("user", "password")


@pytest.mark.parametrize("command,arguments,expected", [
    ("login",None,{"command":"login"}),
    (
            "getChartLastRequest",
            {"info":{"period":5,"symbol":"EURPLN","start":1646995035000}},
            {"command":"getChartLastRequest",
             "arguments":{"info":{"period":5, "symbol":"EURPLN", "start": 1646995035000}}}
    )
])
def test_prepare_message(default_xtb_client, command, arguments, expected):
    assert default_xtb_client.prepare_message(command, arguments) == json.dumps(expected).encode('utf-8')


@pytest.mark.parametrize("data", [
{'status': True, 'streamSessionId': '7ae806fffee1c7d9-000032ec-002cd20a-ca033947d7f18'},
{'status': True, 'streamSessionId': '7ae806fffee1c7d9-000032ec-002cd20a-ca033947d7f187ae806fffee1c7d9-000032ec-002cd20a-ca033947d7f187ae806fffee1c7d9-000032ec-002cd20a-ca033947d7f187ae806fffee1c7d9-000032ec-002cd20a-ca033947d7f187ae806fffee1c7d9-000032ec-002cd20a-ca033947d7f187ae806fffee1c7d9-000032ec-002cd20a-ca033947d7f187ae806fffee1c7d9-000032ec-002cd20a-ca033947d7f187ae806fffee1c7d9-000032ec-002cd20a-ca033947d7f187ae806fffee1c7d9-000032ec-002cd20a-ca033947d7f187ae806fffee1c7d9-000032ec-002cd20a-ca033947d7f187ae806fffee1c7d9-000032ec-002cd20a-ca033947d7f187ae806fffee1c7d9-000032ec-002cd20a-ca033947d7f187ae806fffee1c7d9-000032ec-002cd20a-ca033947d7f187ae806fffee1c7d9-000032ec-002cd20a-ca033947d7f187ae806fffee1c7d9-000032ec-002cd20a-ca033947d7f187ae806fffee1c7d9-000032ec-002cd20a-ca033947d7f187ae806fffee1c7d9-000032ec-002cd20a-ca033947d7f187ae806fffee1c7d9-000032ec-002cd20a-ca033947d7f187ae806fffee1c7d9-000032ec-002cd20a-ca033947d7f187ae806fffee1c7d9-000032ec-002cd20a-ca033947d7f187ae806fffee1c7d9-000032ec-002cd20a-ca033947d7f187ae806fffee1c7d9-000032ec-002cd20a-ca033947d7f187ae806fffee1c7d9-000032ec-002cd20a-ca033947d7f187ae806fffee1c7d9-000032ec-002cd20a-ca033947d7f187ae806fffee1c7d9-000032ec-002cd20a-ca033947d7f187ae806fffee1c7d9-000032ec-002cd20a-ca033947d7f187ae806fffee1c7d9-000032ec-002cd20a-ca033947d7f187ae806fffee1c7d9-000032ec-002cd20a-ca033947d7f187ae806fffee1c7d9-000032ec-002cd20a-ca033947d7f187ae806fffee1c7d9-000032ec-002cd20a-ca033947d7f187ae806fffee1c7d9-000032ec-002cd20a-ca033947d7f187ae806fffee1c7d9-000032ec-002cd20a-ca033947d7f187ae806fffee1c7d9-000032ec-002cd20a-ca033947d7f187ae806fffee1c7d9-000032ec-002cd20a-ca033947d7f187ae806fffee1c7d9-000032ec-002cd20a-ca033947d7f187ae806fffee1c7d9-000032ec-002cd20a-ca033947d7f187ae806fffee1c7d9-000032ec-002cd20a-ca033947d7f187ae806fffee1c7d9-000032ec-002cd20a-ca033947d7f187ae806fffee1c7d9-000032ec-002cd20a-ca033947d7f187ae806fffee1c7d9-000032ec-002cd20a-ca033947d7f187ae806fffee1c7d9-000032ec-002cd20a-ca033947d7f187ae806fffee1c7d9-000032ec-002cd20a-ca033947d7f187ae806fffee1c7d9-000032ec-002cd20a-ca033947d7f187ae806fffee1c7d9-000032ec-002cd20a-ca033947d7f187ae806fffee1c7d9-000032ec-002cd20a-ca033947d7f187ae806fffee1c7d9-000032ec-002cd20a-ca033947d7f187ae806fffee1c7d9-000032ec-002cd20a-ca033947d7f187ae806fffee1c7d9-000032ec-002cd20a-ca033947d7f187ae806fffee1c7d9-000032ec-002cd20a-ca033947d7f187ae806fffee1c7d9-000032ec-002cd20a-ca033947d7f187ae806fffee1c7d9-000032ec-002cd20a-ca033947d7f187ae806fffee1c7d9-000032ec-002cd20a-ca033947d7f187ae806fffee1c7d9-000032ec-002cd20a-ca033947d7f187ae806fffee1c7d9-000032ec-002cd20a-ca033947d7f187ae806fffee1c7d9-000032ec-002cd20a-ca033947d7f187ae806fffee1c7d9-000032ec-002cd20a-ca033947d7f187ae806fffee1c7d9-000032ec-002cd20a-ca033947d7f187ae806fffee1c7d9-000032ec-002cd20a-ca033947d7f187ae806fffee1c7d9-000032ec-002cd20a-ca033947d7f187ae806fffee1c7d9-000032ec-002cd20a-ca033947d7f187ae806fffee1c7d9-000032ec-002cd20a-ca033947d7f187ae806fffee1c7d9-000032ec-002cd20a-ca033947d7f187ae806fffee1c7d9-000032ec-002cd20a-ca033947d7f187ae806fffee1c7d9-000032ec-002cd20a-ca033947d7f187ae806fffee1c7d9-000032ec-002cd20a-ca033947d7f187ae806fffee1c7d9-000032ec-002cd20a-ca033947d7f187ae806fffee1c7d9-000032ec-002cd20a-ca033947d7f187ae806fffee1c7d9-000032ec-002cd20a-ca033947d7f187ae806fffee1c7d9-000032ec-002cd20a-ca033947d7f187ae806fffee1c7d9-000032ec-002cd20a-ca033947d7f187ae806fffee1c7d9-000032ec-002cd20a-ca033947d7f187ae806fffee1c7d9-000032ec-002cd20a-ca033947d7f187ae806fffee1c7d9-000032ec-002cd20a-ca033947d7f187ae806fffee1c7d9-000032ec-002cd20a-ca033947d7f187ae806fffee1c7d9-000032ec-002cd20a-ca033947d7f187ae806fffee1c7d9-000032ec-002cd20a-ca033947d7f187ae806fffee1c7d9-000032ec-002cd20a-ca033947d7f187ae806fffee1c7d9-000032ec-002cd20a-ca033947d7f187ae806fffee1c7d9-000032ec-002cd20a-ca033947d7f187ae806fffee1c7d9-000032ec-002cd20a-ca033947d7f187ae806fffee1c7d9-000032ec-002cd20a-ca033947d7f187ae806fffee1c7d9-000032ec-002cd20a-ca033947d7f187ae806fffee1c7d9-000032ec-002cd20a-ca033947d7f187ae806fffee1c7d9-000032ec-002cd20a-ca033947d7f187ae806fffee1c7d9-000032ec-002cd20a-ca033947d7f187ae806fffee1c7d9-000032ec-002cd20a-ca033947d7f187ae806fffee1c7d9-000032ec-002cd20a-ca033947d7f187ae806fffee1c7d9-000032ec-002cd20a-ca033947d7f187ae806fffee1c7d9-000032ec-002cd20a-ca033947d7f187ae806fffee1c7d9-000032ec-002cd20a-ca033947d7f187ae806fffee1c7d9-000032ec-002cd20a-ca033947d7f187ae806fffee1c7d9-000032ec-002cd20a-ca033947d7f187ae806fffee1c7d9-000032ec-002cd20a-ca033947d7f187ae806fffee1c7d9-000032ec-002cd20a-ca033947d7f187ae806fffee1c7d9-000032ec-002cd20a-ca033947d7f187ae806fffee1c7d9-000032ec-002cd20a-ca033947d7f187ae806fffee1c7d9-000032ec-002cd20a-ca033947d7f187ae806fffee1c7d9-000032ec-002cd20a-ca033947d7f187ae806fffee1c7d9-000032ec-002cd20a-ca033947d7f187ae806fffee1c7d9-000032ec-002cd20a-ca033947d7f187ae806fffee1c7d9-000032ec-002cd20a-ca033947d7f187ae806fffee1c7d9-000032ec-002cd20a-ca033947d7f187ae806fffee1c7d9-000032ec-002cd20a-ca033947d7f187ae806fffee1c7d9-000032ec-002cd20a-ca033947d7f187ae806fffee1c7d9-000032ec-002cd20a-ca033947d7f187ae806fffee1c7d9-000032ec-002cd20a-ca033947d7f187ae806fffee1c7d9-000032ec-002cd20a-ca033947d7f187ae806fffee1c7d9-000032ec-002cd20a-ca033947d7f18'}
])
def test_read_response(monkeypatch, default_xtb_client, data):
    def mock_recv(b):
        return json.dumps(data).encode('utf-8')

    monkeypatch.setattr(default_xtb_client.s, 'recv', mock_recv)
    assert default_xtb_client.read_response() == data


@pytest.mark.parametrize("data", [
{'status': True, 'streamSessionId': '7ae806fffee1c7d9-000032ec-002cd20a-ca033947d7f18'}])
def test_read_response_fail(monkeypatch, default_xtb_client, data):
    def mock_recv(b):
        return json.dumps(data).encode('utf-8')

    monkeypatch.setattr(default_xtb_client.s, 'recv', mock_recv)
    assert default_xtb_client.read_response() != data.update({'streamSessionId':'7ae806fffe'})
