'''
This is an example of using python/request to test API

To run/execute:
   Open a terminal and execute this command:
   % pytest test_api.py -s

'''
import pytest
import requests

# VARIABLES
URL = "https://rickandmortyapi.com/api/"
CHARACTER = "character"
LOCATION = "location"
EPISODE = "episode"


@pytest.mark.parametrize("test_case_name, api, name", [
    ("Verify CHARACTER returns results", CHARACTER, "Rick Sanchez"),
    ("Verify LOCATION returns results", LOCATION, "Earth (C-137)"),
    ("Verify EPISODE returns results", EPISODE, "Pilot"),
])
def test_execute_test_case(test_case_name, api, name):
    print("\n*** TC: " + test_case_name)
    url = URL + api
    response = requests.get(url)
    assert response.status_code == 200, f"Status code is wrong: {response.status_code}"
    print(f"Number of records: {len(response.json())}")
    assert len(response.json()) == 2, f"Response has wrong number of records: {len(response.json())} "
    print(response.json()["info"])
    num_of_results = len(response.json()["results"])
    print("Number of results: {}".format(num_of_results))
    assert num_of_results == 20, f"Response has wrong number of results: {num_of_results}"
    assert response.json()["results"][0]["name"] == name, f"Response has wrong name: {response.json()['results'][0]['name']}"
