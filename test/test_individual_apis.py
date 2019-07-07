# coding: utf-8

"""
    Aqua Security Test Api Definition Document Authered By - Shaharuk Shaikh

    This document is the api def document api's given to test by Aqua Security  

    The version of the OpenAPI document: 0.1
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import openapi_client
from openapi_client.api.aqua_api_api import AquaApiApi  
from openapi_client.rest import ApiException


class TestAquaApiApi(unittest.TestCase):
    """AquaApiApi unit test stubs"""

    def setUp(self):
        self.api = openapi_client.api.aqua_api_api.AquaApiApi()


    def tearDown(self):
        pass

    def test_create_task(self):
        """Test case for create_task

        create task  
        """
        task_detail = openapi_client.TaskDetail(task="CheckAPI", completed=False)
        resp = self.api.create_task(task_detail)
        print(resp)
        pass

    def test_delete_task(self):
        """Test case for delete_task

        delete task  
        """
        resp = self.api.delete_task('VtSbPpQ4')
        print(resp)
        pass

    def test_get_task(self):
        """Test case for get_task

        get the task details  
        """
        resp = self.api.get_task('FuWRtoV0')
        print(resp)
        pass

    def test_list_tasks(self):
        """Test case for list_tasks

        listing taks  
        """
        resp = self.api.list_tasks()
        print(resp)
        pass

    def test_mark_task_completed(self):
        """Test case for mark_task_completed

        Mark existing task as completed  
        """
        resp = self.api.mark_task_completed('FuWRtoV0')
        print(resp)
        pass

    def test_mark_task_incomplete(self):
        """Test case for mark_task_incomplete

        mark task incomplete  
        """
        resp = self.api.mark_task_incomplete('FuWRtoV0')
        print(resp)
        pass

    def test_modify_task(self):
        """Test case for modify_task

        modify tasks  
        """
        task_detail = openapi_client.TaskDetail(task="modified task", completed=False)
        resp = self.api.modify_task('FuWRtoV0', task_detail)
        print(resp)
        pass


if __name__ == '__main__':
    unittest.main()