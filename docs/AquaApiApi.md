# openapi_client.AquaApiApi

All URIs are relative to *http://localhost:5000*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_task**](AquaApiApi.md#create_task) | **POST** /tasks | create task
[**delete_task**](AquaApiApi.md#delete_task) | **DELETE** /tasks/{task_id} | delete task
[**get_task**](AquaApiApi.md#get_task) | **GET** /tasks/{task_id} | get the task details
[**list_tasks**](AquaApiApi.md#list_tasks) | **GET** /tasks | listing taks
[**mark_task_completed**](AquaApiApi.md#mark_task_completed) | **POST** /tasks/{task_id}/completed | Mark existing task as completed
[**mark_task_incomplete**](AquaApiApi.md#mark_task_incomplete) | **POST** /tasks/{task_id}/incomplete | mark task incomplete
[**modify_task**](AquaApiApi.md#modify_task) | **PUT** /tasks/{task_id} | modify tasks


# **create_task**
> TaskID create_task(task_detail=task_detail)

create task

This api is used to create a task

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openapi_client.AquaApiApi()
task_detail = {
  "task": "check the create task api",
  "completed": false
} # TaskDetail |  (optional)

try:
    # create task
    api_response = api_instance.create_task(task_detail=task_detail)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AquaApiApi->create_task: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_detail** | [**TaskDetail**](TaskDetail.md)|  | [optional] 

### Return type

[**TaskID**](TaskID.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | returns id of the task which is created |  -  |
**400** | return blank response if incomplete request body is passed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_task**
> TaskID delete_task(task_id)

delete task

This api is used to delete the task

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openapi_client.AquaApiApi()
task_id = 'task_id_example' # str | 

try:
    # delete task
    api_response = api_instance.delete_task(task_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AquaApiApi->delete_task: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_id** | **str**|  | 

### Return type

[**TaskID**](TaskID.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | returns task id which is deleted |  -  |
**404** | returns blank response if the given task id doesn&#39;t exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_task**
> TaskDetail get_task(task_id)

get the task details

This api is used to get the task details

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openapi_client.AquaApiApi()
task_id = 'task_id_example' # str | 

try:
    # get the task details
    api_response = api_instance.get_task(task_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AquaApiApi->get_task: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_id** | **str**|  | 

### Return type

[**TaskDetail**](TaskDetail.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | returns the details of the task |  -  |
**404** | returns blank response if the task with given id soesn&#39;t exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_tasks**
> list[object] list_tasks()

listing taks

This api is used to list al stacks

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openapi_client.AquaApiApi()

try:
    # listing taks
    api_response = api_instance.list_tasks()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AquaApiApi->list_tasks: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**list[object]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | returns the list of stacks |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **mark_task_completed**
> object mark_task_completed(task_id)

Mark existing task as completed

This api is used to mark existing task as completed

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openapi_client.AquaApiApi()
task_id = 'task_id_example' # str | 

try:
    # Mark existing task as completed
    api_response = api_instance.mark_task_completed(task_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AquaApiApi->mark_task_completed: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_id** | **str**|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | returns blank response |  -  |
**404** | returns blank response if the given task id doesn&#39;t exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **mark_task_incomplete**
> object mark_task_incomplete(task_id)

mark task incomplete

This api is used to mark an existing task as incomplete

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openapi_client.AquaApiApi()
task_id = 'task_id_example' # str | 

try:
    # mark task incomplete
    api_response = api_instance.mark_task_incomplete(task_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AquaApiApi->mark_task_incomplete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_id** | **str**|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | returns blank response |  -  |
**404** | returns blank if the task with given id doesn&#39;t exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **modify_task**
> TaskID modify_task(task_id, task_detail=task_detail)

modify tasks

This api is used to modify task

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openapi_client.AquaApiApi()
task_id = 'task_id_example' # str | 
task_detail = {
  "task": "add task",
  "completed": true
} # TaskDetail |  (optional)

try:
    # modify tasks
    api_response = api_instance.modify_task(task_id, task_detail=task_detail)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AquaApiApi->modify_task: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_id** | **str**|  | 
 **task_detail** | [**TaskDetail**](TaskDetail.md)|  | [optional] 

### Return type

[**TaskID**](TaskID.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | returns task id which is modified |  -  |
**404** | returns blank response if the task with given id doesn&#39;t exist |  -  |
**400** | returns blank response if the incomplete request body is passed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

