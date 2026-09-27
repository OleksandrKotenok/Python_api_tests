import pytest
import requests

def test_get():
    response = requests.get("https://jsonplaceholder.typicode.com/posts/1/comments")
    print(response.json())
    assert response.status_code == 200

def test_post():
    payload = {
        "title": "My post",
        "body": "Hello",
        "userId": 1
    }
    response = requests.post("https://jsonplaceholder.typicode.com/posts", json=payload)
    print(response.json())

    assert response.status_code == 201

def test_get2():
    response = requests.get("https://jsonplaceholder.typicode.com/posts/101")
    print(response.json())

@pytest.fixture
def booking_id():
    payload = {
        "firstname": "QA A",
        "lastname": "Not_a_test",
        "totalprice": 100,
        "depositpaid": True,
        "bookingdates": {"checkin": "2026-10-01", "checkout": "2026-10-05"}
    }
    response = requests.post("https://restful-booker.herokuapp.com/booking", json=payload)
    return response.json()["bookingid"]

def test_get_booking(booking_id):
    response = requests.get(f"https://restful-booker.herokuapp.com/booking/{booking_id}")
    print(response.json())

    assert response.status_code == 200
    assert response.json()["firstname"] == "QA A"