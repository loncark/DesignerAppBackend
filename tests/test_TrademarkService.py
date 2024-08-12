import pytest
import json, requests
import os
from unittest.mock import patch
from service.TrademarkService import fetchAndFilterResponse, fetchResponse, filterJson

current_dir = os.path.dirname(os.path.abspath(__file__))
mock_data_path = os.path.join(current_dir, '', 'mockdata', 'TrademarkMock.json')
with open(mock_data_path, 'r') as f:
    MOCK_API_RESPONSE = json.load(f)

@pytest.fixture
def mock_api_response(mocker):
    mock_response = mocker.Mock()
    mock_response.json.return_value = MOCK_API_RESPONSE
    return mock_response

def test_fetchResponse(mock_api_response, mocker):
    mocker.patch('requests.get', return_value=mock_api_response)
    
    result = fetchResponse("test prompt")
    
    assert result == MOCK_API_RESPONSE
    requests.get.assert_called_once()

def test_filterJson():
    filtered_data = filterJson(MOCK_API_RESPONSE)
    
    assert "count" in filtered_data
    assert "items" in filtered_data
    assert len(filtered_data["items"]) == len(MOCK_API_RESPONSE["items"])
    
    for item in filtered_data["items"]:
        assert "description" in item
        assert "keyword" in item
        assert "owners" in item
        assert "status_label" in item
        
        for owner in item["owners"]:
            assert "address1" in owner
            assert "city" in owner
            assert "country" in owner
            assert "name" in owner

@patch('service.TrademarkService.fetchResponse')
def test_fetchAndFilterResponse(mock_fetch):
    mock_fetch.return_value = MOCK_API_RESPONSE
    
    result = fetchAndFilterResponse("test prompt")
    
    assert "count" in result
    assert "items" in result
    mock_fetch.assert_called_once_with("test prompt")

def test_fetchResponse_error_handling(mocker):
    mock_response = mocker.Mock()
    mock_response.raise_for_status.side_effect = requests.exceptions.HTTPError("404 Client Error")
    mocker.patch('requests.get', return_value=mock_response)
    
    with pytest.raises(requests.exceptions.HTTPError):
        fetchResponse("test prompt")

def test_filterJson_empty_input():
    empty_input = {"count": 0, "items": []}
    result = filterJson(empty_input)
    
    assert result["count"] == 0
    assert result["items"] == []

def test_fetchAndFilterResponse_integration(mock_api_response, mocker):
    mocker.patch('requests.get', return_value=mock_api_response)
    
    result = fetchAndFilterResponse("test prompt")
    
    assert "count" in result
    assert "items" in result
    assert len(result["items"]) == len(MOCK_API_RESPONSE["items"])
    requests.get.assert_called_once()