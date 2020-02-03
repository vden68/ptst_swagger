__author__ = 'v.denisov'

import json
from ptst_swagger.model.tests_to_swagger import TestsToSwagger


class SwaggerModel:

    def __init__(self):
        _record_test = None
        _record_test_list = None

    @property
    def record_test(self):
        return self._record_test

    @record_test.setter
    def set_record_test(self, value):
        self._record_test = value

    @property
    def record_test_list(self):
        return self._record_test_list

    @record_test_list.setter
    def set_record_test_list(self, r_list):
        self._record_test_list = r_list

    @classmethod
    def record_test_to_list(self, method, path, text):
        if not type(self.record_test_list) == list:
            self.record_test_list=[]
        r_list = self.record_test_list
        r_list.append(TestsToSwagger(method=method, path=path, text=text))
        self.record_test_list = r_list
        print('_record_test_list=', self.record_test_list)
        r_test_dict = []
        for r_test in self.record_test_list:
            r_test_dict.append({"method":r_test.method, "path":r_test.path, "text":r_test.text})
        print('_record_test_list.jsson=', json.dumps(r_test_dict))

        # test_list.append(TestsToSwagger(method=method, path=path, text=text))
        # print('test_list=', test_list)



