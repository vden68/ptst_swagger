
from ptst_swagger.client import SwaggerClient

def test_t1():
    r = SwaggerClient.get_swagger_json(url='http://test.rais.d-net.pro:8080/bin/swagger/openapi.json')
    print('r=', r.json())

def test_t2():
    r = SwaggerClient.get_swagger_json(url='https://petstore.swagger.io/v2/swagger.json')
    print('r=', r.json())