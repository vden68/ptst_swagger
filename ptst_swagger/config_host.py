__author__ = 'v.denisov'

import allure
from ptst_swagger.reguest import RegustsHelper as rh


class ConfigHost():

    def __init__(self):
        self._paths_sw = None
        self._url_host = None
        self._cookies = None

    @property
    def paths_sw(self):
        return self._paths_sw

    @paths_sw.setter
    def set_paths_sw(self, value):
        self._paths_sw = value

    @property
    def url_host(self):
        return self._url_host

    @url_host.setter
    def set_url_host(self, value):
        self._url_host = value

    @classmethod
    @allure.step("get swagger json")
    def get_swagger_json(self, url):
        swagger_response = rh.get(url=url)
        self.paths_sw = swagger_response.json()['paths']
        return swagger_response