import requests

API_URL_GET = 'https://postman-echo.com/get'
API_URL_POST = 'https://postman-echo.com/post'



def test_get_without_params():
    get_response = requests.get(f'{API_URL_GET}')
    expected_json = {'args': {}, 'headers': {'host': 'postman-echo.com', 'x-forwarded-proto': 'https', 'user-agent': 'python-requests/2.33.1', 'accept': '*/*', 'accept-encoding': 'gzip, br'}, 'url': 'https://postman-echo.com/get'}
    actual_json = get_response.json()
    assert get_response.status_code == 200 and actual_json == expected_json


def test_get_with_params():
    params={'test':'123'}
    get_response = requests.get(f'{API_URL_GET}', params=params)
    actual_json = get_response.json()
    assert get_response.status_code == 200 and actual_json['args'] == {'test': '123'}

def test_get_with_headers():
    headers = {
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
        "sec-ch-ua-platform": '\"Windows\"'
    }
    get_response = requests.get(f'{API_URL_GET}', headers=headers)
    actual_json = get_response.json()
    assert get_response.status_code == 200 and actual_json['headers'] == {'host': 'postman-echo.com', 'x-forwarded-proto': 'https', 'user-agent': 'python-requests/2.33.1', 'accept-encoding': 'gzip, br', 'sec-ch-ua-platform': '"Windows"', 'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7', 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7'}

def test_post_without_params():
    post_response = requests.post(f'{API_URL_POST}')
    expected_json = {'args': {}, 'data': {}, 'files': {}, 'form': {}, 'headers': {'host': 'postman-echo.com', 'x-forwarded-proto': 'https', 'user-agent': 'python-requests/2.33.1', 'content-length': '0', 'accept': '*/*', 'accept-encoding': 'gzip, br'}, 'json': None, 'url': 'https://postman-echo.com/post'}
    actual_json = post_response.json()
    assert post_response.status_code==200 and actual_json == expected_json

def test_post_with_params():
    params={'test':'123'}
    post_response = requests.post(f'{API_URL_POST}', params=params)
    actual_json = post_response.json()
    assert post_response.status_code==200 and actual_json['args'] == {'test': '123'}

def test_post_with_body_files():
    data={'result':'https://skrinshoter.ru/sbJonFlEaFA'}
    post_response = requests.post(f'{API_URL_POST}', json=data)
    actual_json = post_response.json()
    assert post_response.status_code==200 and  actual_json['data'] =={'result': 'https://skrinshoter.ru/sbJonFlEaFA'}

def test_post_with_body_form():
    data={'id':'test001'}
    post_response = requests.post(f'{API_URL_POST}', json=data)
    actual_json = post_response.json()
    assert post_response.status_code==200 and  actual_json['data'] == {'id': 'test0010'}

