test_data = '{"items": [{"title": "vivek a him", "subjects": ["ads", "dbms", "mis"], "field_offices": ["Pune", "Mumbai", "Nashik"]}, {"title": "vivek a him", "subjects": ["ads", "dbms", "mis"], "field_offices": ["Pune", "Mumbai", "Nashik"]}]}'
import json
from main import get_data_from_url, extract_title, extract_field_offices, extract_subjects
from unittest.mock import MagicMock

# Downloading non-empty data from a URL

def test_Downloading_non_empty_data(mocker):
    #response = json.loads(test_data)
    mock_response = mocker.MagicMock()
    mock_response.status_code = 200
    mock_response.json.return_value = test_data
    url = 'https://api.fbi.gov/wanted/v1/list'
    mocker.patch("requests.get", return_value = mock_response)
    result = get_data_from_url(url, 2)
    assert result == test_data


# Extrating title field from FBI API
def test_Extracting_title():
    response = json.loads(test_data)
    for i in range(len(response["items"])):
        title = extract_title(response["items"][i])
        assert title == 'vivek a him'
# Extrating subjects field from FBI API
def test_Extracting_field_offcies():
    response = json.loads(test_data)
    for i in range(len(response["items"])):
        field_offices = extract_field_offices(response["items"][i])
        assert field_offices == 'Pune,Mumbai,Nashik'

# Extrating field_offices field from FBI API
def test_Extracting_subjects():
    response = json.loads(test_data)
    for i in range(len(response["items"])):
        subjects = extract_subjects(response["items"][i])
        assert subjects == 'ads,dbms,mis'

# Printing the full thorn separated file.


