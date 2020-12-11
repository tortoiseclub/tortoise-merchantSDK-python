# swagger_client.PlanApi

All URIs are relative to *https://virtserver.swaggerhub.com/suryaharshan1/Tortoise/1.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_plan**](PlanApi.md#add_plan) | **POST** /plans | Add a new plan
[**edit_plan**](PlanApi.md#edit_plan) | **PUT** /plans/{planId} | Edit a plan&#39;s details
[**fetch_all_plans**](PlanApi.md#fetch_all_plans) | **GET** /plans | Fetch all plans
[**get_plan**](PlanApi.md#get_plan) | **GET** /plans/{planId} | Get a plan by ID


# **add_plan**
> add_plan(body)

Add a new plan

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: tortoise_merchant_apiKey
configuration = swagger_client.Configuration()
configuration.api_key['X-TORTOISE-KEY'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-TORTOISE-KEY'] = 'Bearer'
# Configure API key authorization: tortoise_merchant_appId
configuration = swagger_client.Configuration()
configuration.api_key['X-TORTOISE-ID'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-TORTOISE-ID'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.PlanApi(swagger_client.ApiClient(configuration))
body = swagger_client.Plan() # Plan | Plan object that needs to be added

try:
    # Add a new plan
    api_instance.add_plan(body)
except ApiException as e:
    print("Exception when calling PlanApi->add_plan: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Plan**](Plan.md)| Plan object that needs to be added | 

### Return type

void (empty response body)

### Authorization

[tortoise_merchant_apiKey](../README.md#tortoise_merchant_apiKey), [tortoise_merchant_appId](../README.md#tortoise_merchant_appId)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_plan**
> edit_plan(plan_id, body)

Edit a plan's details

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: tortoise_merchant_apiKey
configuration = swagger_client.Configuration()
configuration.api_key['X-TORTOISE-KEY'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-TORTOISE-KEY'] = 'Bearer'
# Configure API key authorization: tortoise_merchant_appId
configuration = swagger_client.Configuration()
configuration.api_key['X-TORTOISE-ID'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-TORTOISE-ID'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.PlanApi(swagger_client.ApiClient(configuration))
plan_id = 'plan_id_example' # str | ID of the plan to edit
body = swagger_client.Plan() # Plan | Plan object that needs to be edited

try:
    # Edit a plan's details
    api_instance.edit_plan(plan_id, body)
except ApiException as e:
    print("Exception when calling PlanApi->edit_plan: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **plan_id** | **str**| ID of the plan to edit | 
 **body** | [**Plan**](Plan.md)| Plan object that needs to be edited | 

### Return type

void (empty response body)

### Authorization

[tortoise_merchant_apiKey](../README.md#tortoise_merchant_apiKey), [tortoise_merchant_appId](../README.md#tortoise_merchant_appId)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fetch_all_plans**
> list[Plan] fetch_all_plans()

Fetch all plans

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: tortoise_merchant_apiKey
configuration = swagger_client.Configuration()
configuration.api_key['X-TORTOISE-KEY'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-TORTOISE-KEY'] = 'Bearer'
# Configure API key authorization: tortoise_merchant_appId
configuration = swagger_client.Configuration()
configuration.api_key['X-TORTOISE-ID'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-TORTOISE-ID'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.PlanApi(swagger_client.ApiClient(configuration))

try:
    # Fetch all plans
    api_response = api_instance.fetch_all_plans()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PlanApi->fetch_all_plans: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Plan]**](Plan.md)

### Authorization

[tortoise_merchant_apiKey](../README.md#tortoise_merchant_apiKey), [tortoise_merchant_appId](../README.md#tortoise_merchant_appId)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_plan**
> Plan get_plan(plan_id)

Get a plan by ID

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: tortoise_merchant_apiKey
configuration = swagger_client.Configuration()
configuration.api_key['X-TORTOISE-KEY'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-TORTOISE-KEY'] = 'Bearer'
# Configure API key authorization: tortoise_merchant_appId
configuration = swagger_client.Configuration()
configuration.api_key['X-TORTOISE-ID'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-TORTOISE-ID'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.PlanApi(swagger_client.ApiClient(configuration))
plan_id = 'plan_id_example' # str | ID of the plan to fetch

try:
    # Get a plan by ID
    api_response = api_instance.get_plan(plan_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PlanApi->get_plan: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **plan_id** | **str**| ID of the plan to fetch | 

### Return type

[**Plan**](Plan.md)

### Authorization

[tortoise_merchant_apiKey](../README.md#tortoise_merchant_apiKey), [tortoise_merchant_appId](../README.md#tortoise_merchant_appId)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

