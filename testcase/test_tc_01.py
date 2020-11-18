import requests
import pytest
import allure

url = "https://reqres.in/api/users?page=2"
response = requests.get(url)


@pytest.mark.tryfirst()
def test_respsonse_statusCode():
    re_code = response.status_code
    code = 'xxxxxx_state_c'
    if code == re_code:
        print(re_code)
    else:
        print('invalid response')


@pytest.mark.Skip()
def test_response_head_eTag():
    re_head = response.headers.get('Etag')
    header_val = print(re_head)
    if header_val == re_head:
        assert header_val == re_head


@pytest.mark.smoke
def test_response_head_verifyCookie():
    cookie_head = response.headers.get('Set-Cookie')
    cookie_val = print(cookie_head)
    if cookie_head == cookie_val:
        assert cookie_head == cookie_val


@pytest.mark.smoke
def test_response_cf_requestID():
    cf_request = response.headers.get('cf-request-id')
    cf_request_val = print(cf_request)
    if cf_request == cf_request_val:
        assert cf_request == cf_request_val


@pytest.mark.smoke
def f():
    return 3

@pytest.mark.smoke
def test_function():
    assert f() == 4


# print(response.headers)


test_respsonse_statusCode()
test_response_head_eTag()
test_response_head_verifyCookie()
test_response_cf_requestID()
