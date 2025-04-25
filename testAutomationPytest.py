# testAutomationPytest.py
import pytest
import requests

testcases = [
    ("http://localhost:8000/add/2/2", 4),
    ("http://localhost:8000/subtract/2/2", 0),
    ("http://localhost:8000/multiply/2/2", 4),
    ("http://localhost:8000/add/-1/1", 0),
    ("http://localhost:8000/multiply/0/5", 0),
]

@pytest.mark.parametrize("url, expected", testcases)
def test_api(url, expected):
    response = requests.get(url)
    result = response.json()["result"]
    assert result == expected
