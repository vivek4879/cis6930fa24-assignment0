# import pytest
# from unittest.mock import patch, MagicMock
# from main import get_data_from_url
# from main import output_print
# from io import StringIO
# import sys

# Mock_Response = { "items": [{"title": "Test Title", "subjects":["Subject1", "Subject2"], "field_offices":["Office1", 'Office2']}]}


# @patch('main.requests.get')
# def test_NonEmpty_data(mock_get):
#     mock_response = MagicMock()
#     mock_response.status_code = 200
#     mock_response.json.return_value = Mock_Response
#     mock_get.return_value = mock_response
#     response = get_data_from_url('https://api.fbi.gov/wanted/v1/list', page=1)

#     assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"
#     data = response.json()
#     assert 'items' in data, "'items' key found in response data"
#     assert len(data['items']) > 0, "Expected non-empty items list"

# @patch('main.requests.get')
# def test_extract_title(mock_get):
#     mock_response = MagicMock()
#     mock_response.status_code = 200
#     mock_response.json.return_value = Mock_Response
#     mock_get.return_value = mock_response
#     response = get_data_from_url('https://api.fbi.gov/wanted/v1/list', page=1)

#     data = response.json()
#     for record in data['items']:
#         title = record.get('title', None)
#         assert title is not None, "Expected 'title' field in record, but not found"
#         assert isinstance(title, str), f"Expected 'title' to be a string, got {type(title)}"

# @patch('main.requests.get')
# def test_extract_subjects(mock_get):
#     mock_response = MagicMock()
#     mock_response.status_code = 200
#     mock_response.json.return_value = Mock_Response
#     mock_get.return_value = mock_response
#     response = get_data_from_url('https://api.fbi.gov/wanted/v1/list', page=1)

#     data = response.json()
#     for record in data['items']:
#         subjects = record.get('subjects', None)
#         assert subjects is not None, "Expected 'subjects' field in record, but not found"
#         assert isinstance(subjects, list), f"Expected 'subjects' to be a list, got {type(subjects)}"

# @patch('main.requests.get')
# def field_offices(mock_get):
#     mock_response = MagicMock()
#     mock_response.status_code = 200
#     mock_response.json.return_value = Mock_Response
#     mock_get.return_value = mock_response
#     response = get_data_from_url('https://api.fbi.gov/wanted/v1/list', page=1)

#     data = response.json()
#     for record in data['items']:
#         field_offices = record.get('field_offices', None)
#         if field_offices is not None:
#             assert isinstance(field_offices, list), f"Expected 'field_offices' to be a list, got {type(field_offices)}"

# @patch('main.requests.get')
# def test_print_thorn(mock_get):
#     mock_response = MagicMock()
#     mock_response.status_code = 200
#     mock_response.json.return_value = Mock_Response
#     mock_get.return_value = mock_response 

#     with patch('sys.stdout', new_callable = StringIO) as mock_output:
#         response = get_data_from_url('https://api.fbi.gov/wanted/v1/list', page=1)
#         output_print(response)

#         printed_output = mock_output.getvalue().strip()

#     expected_output = 'Test TitleþSubject1,Subject2þOffice1,Office2'

#     assert printed_output == expected_output, f"Expected '{expected_output}', but got '{printed_output}'"


# def test_test():
#     assert True


import pytest
from unittest.mock import patch, MagicMock
from io import StringIO
import json
from main import get_data_from_url, output_print, get_data_from_json

# Mock response data from FBI API
Mock_Response = {
    "items": [
        {
            "title": "Test Title",
            "subjects": ["Subject1", "Subject2"],
            "field_offices": ["Office1", "Office2"]
        }
    ]
}

# Test for downloading non-empty data from a URL
@patch('main.requests.get')  # Mock the requests.get method in main module
def test_download_non_empty_data(mock_get):
    # Mocking the API response
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.json.return_value = Mock_Response
    mock_get.return_value = mock_response

    # Call function
    response = get_data_from_url('https://api.fbi.gov/wanted/v1/list', page=1)

    # Ensure non-empty data
    assert response is not None
    assert len(response['items']) > 0

# Test for extracting the title field from the FBI API
@patch('main.requests.get')
def test_extract_title(mock_get):
    # Mocking the API response
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.json.return_value = Mock_Response
    mock_get.return_value = mock_response

    response = get_data_from_url('https://api.fbi.gov/wanted/v1/list', page=1)

    # Extracting and verifying title
    for record in response['items']:
        title = record.get('title', None)
        assert title is not None
        assert isinstance(title, str)

# Test for extracting the subjects field from the FBI API
@patch('main.requests.get')
def test_extract_subjects(mock_get):
    # Mocking the API response
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.json.return_value = Mock_Response
    mock_get.return_value = mock_response

    response = get_data_from_url('https://api.fbi.gov/wanted/v1/list', page=1)

    # Extracting and verifying subjects
    for record in response['items']:
        subjects = record.get('subjects', None)
        assert subjects is not None
        assert isinstance(subjects, list)
        assert ','.join(subjects) == 'Subject1,Subject2'

# Test for extracting the field_offices field from the FBI API
@patch('main.requests.get')
def test_extract_field_offices(mock_get):
    # Mocking the API response
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.json.return_value = Mock_Response
    mock_get.return_value = mock_response

    response = get_data_from_url('https://api.fbi.gov/wanted/v1/list', page=1)

    # Extracting and verifying field_offices
    for record in response['items']:
        field_offices = record.get('field_offices', None)
        assert field_offices is not None
        assert isinstance(field_offices, list)
        assert ','.join(field_offices) == 'Office1,Office2'

# Test for printing the full thorn-separated file
@patch('main.requests.get')
def test_print_thorn_separated(mock_get):
    # Mocking the API response
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.json.return_value = Mock_Response
    mock_get.return_value = mock_response

    with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
        response = get_data_from_url('https://api.fbi.gov/wanted/v1/list', page=1)
        output_print(response)

        # Verifying thorn-separated output
        printed_output = mock_stdout.getvalue().strip()
        expected_output = 'Test TitleþSubject1,Subject2þOffice1,Office2'
        assert printed_output == expected_output
