__author__ = 'v.denisov'

from ptst_swagger.reguest import RegustsHelper as rh

class SwaggerClient():

    def __init__(self):
        pass

    @classmethod
    def get_swagger_json(self, url):
        swagger_json = rh.get(url=url,data=None, params=None, headers=None, cookies=None)
        return swagger_json
