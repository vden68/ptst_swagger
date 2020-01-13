__author__ = 'v.denisov'

import requests


class RegustsHelper:

    def __init__(self, app):
        self.app = app

    def get(self, url, data=None, params=None):
        response = None
        try:
            response = requests.request(
                "GET", url, data=data, headers=self.app.headers, params=params,
                cookies=self.app.cookies, timeout=20,  verify=False)
        except requests.exceptions.ConnectTimeout:
            print('Oops. Connection timeout occured!')
        except requests.exceptions.ReadTimeout:
            print('Oops. Read timeout occured')
        except requests.exceptions.ConnectionError:
            print('Seems like dns lookup failed..')
        except requests.exceptions.HTTPError as err:
            print('Oops. HTTP Error occured')
            print('Response is: {content}'.format(content=err.response.content))
        else:
            print('Success!')
        return response

    def post(self, url, data=None, params=None):
        response = None
        try:
            response = requests.request(
                "POST", url, data=data, headers=self.app.headers, params=params,
                cookies=self.app.cookies, timeout=20,  verify=False)
        except requests.exceptions.ConnectTimeout:
            print('Oops. Connection timeout occured!')
        except requests.exceptions.ReadTimeout:
            print('Oops. Read timeout occured')
        except requests.exceptions.ConnectionError:
            print('Seems like dns lookup failed..')
        except requests.exceptions.HTTPError as err:
            print('Oops. HTTP Error occured')
            print('Response is: {content}'.format(content=err.response.content))
        else:
            print('Success!')
        return response


