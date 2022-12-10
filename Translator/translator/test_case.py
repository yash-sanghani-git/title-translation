import pytest
import requests

def test_singlelang_post_api():
    url = "http://127.0.0.1:8000/single-language/"
    print(url)
    payload =  {
            "title":"hii",
            "language":"hi"
        }
    response = requests.post(url,payload)

    print(response)
    assert response.status_code ==201

def test_alllang_post_api():
    url = "http://127.0.0.1:8000/all-language/"
    print(url)
    payload =  {
                   "title":"good"    
               }
    response = requests.post(url,payload)

    print(response)
    assert response.status_code ==201