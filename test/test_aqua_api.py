import unittest
import openapi_client
from openapi_client import ApiException
from openapi_client import Logger


class AquaApi(unittest.TestCase):

    def setUp(self):
        self.log = Logger.getLoggerObj()
        self.log.info("")
        self.log.info("Setting up the host/api url for test execution")
        configuration = openapi_client.Configuration(host= "http://localhost:5000")
        api_client = openapi_client.ApiClient(configuration)
        self.api = openapi_client.AquaApiApi(api_client)

    def tearDown(self):
        self.log.info("tear down resources")
        pass

    def test_positive(self):
        """create task"""
        task_detail = openapi_client.TaskDetail(task="test for first positive test case", completed=False)
        resp = self.api.create_task(task_detail)
        assert resp.task_id != "" and resp.task_id != None
        task_id = resp.task_id
        self.log.info("Task {} is created with id {}".format(task_detail.to_str(), task_id))

        """get task api"""
        resp = self.api.get_task(task_id)
        assert resp.task == 'test for first positive test case' and resp.completed == False
        self.log.info("Details retrieved for task_id {} are {}".format(resp, task_id))

        """get the list of stacks"""
        task_list = self.api.list_tasks()
        self.log.info("list of stacks returned successfully and number of tasks are {}".format(len(task_list)))
        for task in task_list:
            if task['id'] == task_id:
                assert task['task'] == 'test for first positive test case' and task['completed'] == False
                self.log.info("task created for this test with id: {} is found in list".format(task_id))


        """get task details using task_id"""
        resp = self.api.get_task(task_id)
        assert resp.task == 'test for first positive test case' and resp.completed == False
        self.log.info("Details for stack_id: {} returned successfully {}".format(task_id, resp))

        """" mark the task as completed and check if the 'completed' has actually been changed to True"""
        resp = self.api.mark_task_completed(task_id)
        assert resp == {} and self.api.get_task(task_id).completed == True
        self.log.info("task with task_id: {} is marked as completed".format(task_id))

        """ mark the task as incomplete and check if the 'completed' has actually been changed to False"""
        resp = self.api.mark_task_incomplete(task_id)
        assert resp == {} and self.api.get_task(task_id).completed == False
        self.log.info("task with task_id: {} is marked as incomplete".format(task_id))

        """ modify the task """
        modified_task = "modified: test for first positive test case"
        task_detail = openapi_client.TaskDetail(task= modified_task, completed= False)
        resp = self.api.modify_task(task_id, task_detail)
        assert resp.task_id == task_id and self.api.get_task(task_id).task == modified_task
        self.log.info("task with task_id: {} is modified and updated details are {}".format(task_id, resp))

        """delete task"""
        resp = self.api.delete_task(task_id)
        assert resp.task_id == task_id
        self.log.info("Task with id: {} is deleted successfully".format(task_id))

    def test_negative_createTask(self):
        self.log.info("To Test: response when incomplete TaskDetails are passed in body while creating a task")
        try:
            task_details = openapi_client.TaskDetail(task="Incomplete body")
            self.api.create_task(task_details)
        except ApiException as e:
            assert e.status == 400
            self.log.info("Passed: if incomplete request body is passed then 400 status code is returned as expected")

    def test_negative_getTask(self):
        self.log.info("To Test: response when non-existent task_id is passed to getTask api")
        try:
            self.api.get_task(task_id="AAA")
        except ApiException as e:
            assert e.status == 404
            self.log.info("Passed: if non-existent task_id is passed then 404:NotFound status code is returned as expected")

    def test_negative_markTaskComplete(self):
        self.log.info("To Test: response when non-existent task_id is passed to markTaskComplete api")
        try:
            self.api.mark_task_completed("AAA")
        except ApiException as e:
            assert e.status == 404
            self.log.info("Passed: if non-existent task_id is passed then 404:NotFound status code is returned as expected")

    def test_negative_markTaskIncomplete(self):
        self.log.info("To Test: response when non-existent task_id is passed to markTaskIncomplete api")
        try:
            self.api.mark_task_incomplete("AAA")
        except ApiException as e:
            assert e.status == 404
            self.log.info("Passed: if non-existent task_id is passed then 404:NotFound status code is returned as expected")

    def test_negative_deleteTask(self):
        self.log.info("To Test: response when non-existent task_id is passed to deleteTask api")
        try:
            self.api.delete_task("AAA")
        except ApiException as e:
            assert e.status == 404
            self.log.info("Passed: if non-existent task_id is passed then 404:NotFound status code is returned as expected")

    def test_negative_modifyTask1(self):
        self.log.info("To Test: if non-existent task_id is passed to modifyTask api")
        try:
            task_detail = openapi_client.TaskDetail(task="just for sake of validation", completed=False)
            self.api.modify_task(task_id="AAA", task_detail=task_detail)
        except ApiException as e:
            assert e.status == 404
            self.log.info("Passed: if non-existent task_id is passed then 404:NotFound status code is returned as expected")

    def test_negative_modifyTask2(self):
        self.log.info("To Test: if incomplete task_details are passed to modify task api")
        try:
            """ firstly get any existing task_id from task list"""
            task_list = self.api.list_tasks()
            task_id = task_list[0]['id']
            task_detail = openapi_client.TaskDetail(task="incompleted body: not passing completed status")
            self.api.modify_task(task_id=task_id, task_detail=task_detail)
        except ApiException as e:
            assert e.status == 400
            self.log.info("Passed: if incomplete task_details are passed then 400 status code is returned as expected")


if __name__ == '__main__':
    unittest.main()