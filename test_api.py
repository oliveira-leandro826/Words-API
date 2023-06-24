from app import app
from flask import json

def test_vowel_count_error_content_type():
    response = app.test_client().post(
        '/vowel_count',
        data=json.dumps({"words": ["batman", "robin", "coringa"]}),
        content_type='text/plain',
    )

    assert response.status_code == 415

def test_vowel_count_error_bad_request():        
    response = app.test_client().post(
        '/vowel_count',
        data=json.dumps(["batman", "robin", "coringa"]),
        content_type='application/json',
    )

    assert response.status_code == 400

def test_vowel_count_success():        
    response = app.test_client().post(
        '/vowel_count',
        data=json.dumps({"words": ["batman", "robin", "coringa"]}),
        content_type='application/json',
    )

    data = json.loads(response.get_data(as_text=True))

    assert response.status_code == 200
    assert data == {"batman": 2, "robin": 2, "coringa": 3}

def test_sort_success_error_bad_request():        
    response = app.test_client().post(
        '/sort',
        data=json.dumps({"words": ["batman", "robin", "coringa"]}),
        content_type='application/json',
    )

    assert response.status_code == 400

def test_sort_success_asc():        
    response = app.test_client().post(
        '/sort',
        data=json.dumps({"words": ["batman", "robin", "coringa"], "order": "asc"}),
        content_type='application/json',
    )

    data = json.loads(response.get_data(as_text=True))

    assert response.status_code == 200
    assert data == ["batman", "coringa", "robin"]

def test_sort_success_desc():        
    response = app.test_client().post(
        '/sort',
        data=json.dumps({"words": ["batman", "robin", "coringa"], "order": "desc"}),
        content_type='application/json',
    )

    data = json.loads(response.get_data(as_text=True))
    print(data)

    assert response.status_code == 200
    assert data == ["robin", "coringa", "batman"]