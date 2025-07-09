'''
This is an example of using python/request to test API

To run/execute:
   Open a terminal and execute this command:
   % pytest api_tests.py -s

'''

import requests

# VARIABLES
URL = "https://rickandmortyapi.com/api/"
CHARACTER = "character"
LOCATION = "location"
EPISODE = "episode"

# TESTS
def test_get_response_character():
    print("\n*** TC: Verify GET/character returns records")
    execute_test_case(CHARACTER, "Rick Sanchez")

def test_get_response_location():
    print("\n*** TC: Verify GET/location returns records")
    execute_test_case(LOCATION, "Earth (C-137)")

def test_get_response_episode():
    print("\n*** TC: Verify GET/episode returns records")
    execute_test_case(EPISODE, "Pilot")

def execute_test_case(api, name):
    url = URL + api
    response = requests.get(url)
    assert response.status_code == 200
    print(f"Number of records: {len(response.json())}")
    assert len(response.json()) == 2
    print(response.json()["info"])
    print("Number of results: {}".format(len(response.json()["results"])))
    assert len(response.json()["results"]) == 20
    assert response.json()["results"][0]["name"] == name
