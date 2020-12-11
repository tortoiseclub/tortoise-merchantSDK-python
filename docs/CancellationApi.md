# swagger_client.CancellationApi

All URIs are relative to *https://virtserver.swaggerhub.com/suryaharshan1/Tortoise/1.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_cancellation**](CancellationApi.md#add_cancellation) | **POST** /cancellations | Create a new cancellation request for a plan
[**edit_cancellation**](CancellationApi.md#edit_cancellation) | **PUT** /cancellations/{cancellationId} | Edit a cancellation request for a plan
[**fetch_all_cancellations**](CancellationApi.md#fetch_all_cancellations) | **GET** /cancellations | Fetch all cancellations
[**get_cancellation**](CancellationApi.md#get_cancellation) | **GET** /cancellations/{cancellationId} | Get cancellation by ID


# **add_cancellation**
> add_cancellation(body)

Create a new cancellation request for a plan

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
api_instance = swagger_client.CancellationApi(swagger_client.ApiClient(configuration))
body = swagger_client.Cancellation() # Cancellation | cancellation object that needs to be added

try:
    # Create a new cancellation request for a plan
    api_instance.add_cancellation(body)
except ApiException as e:
    print("Exception when calling CancellationApi->add_cancellation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Cancellation**](Cancellation.md)| cancellation object that needs to be added | 

### Return type

void (empty response body)

### Authorization

[tortoise_merchant_apiKey](../README.md#tortoise_merchant_apiKey), [tortoise_merchant_appId](../README.md#tortoise_merchant_appId)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_cancellation**
> edit_cancellation(cancellation_id, body)

Edit a cancellation request for a plan

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
api_instance = swagger_client.CancellationApi(swagger_client.ApiClient(configuration))
cancellation_id = 'cancellation_id_example' # str | ID of the cancellation to edit
body = swagger_client.Cancellation() # Cancellation | Cancellation object that needs to be edited

try:
    # Edit a cancellation request for a plan
    api_instance.edit_cancellation(cancellation_id, body)
except ApiException as e:
    print("Exception when calling CancellationApi->edit_cancellation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cancellation_id** | **str**| ID of the cancellation to edit | 
 **body** | [**Cancellation**](Cancellation.md)| Cancellation object that needs to be edited | 

### Return type

void (empty response body)

### Authorization

[tortoise_merchant_apiKey](../README.md#tortoise_merchant_apiKey), [tortoise_merchant_appId](../README.md#tortoise_merchant_appId)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fetch_all_cancellations**
> list[Cancellation] fetch_all_cancellations()

Fetch all cancellations

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
api_instance = swagger_client.CancellationApi(swagger_client.ApiClient(configuration))

try:
    # Fetch all cancellations
    api_response = api_instance.fetch_all_cancellations()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CancellationApi->fetch_all_cancellations: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Cancellation]**](Cancellation.md)

### Authorization

[tortoise_merchant_apiKey](../README.md#tortoise_merchant_apiKey), [tortoise_merchant_appId](../README.md#tortoise_merchant_appId)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cancellation**
> Cancellation get_cancellation(cancellation_id)

Get cancellation by ID

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
api_instance = swagger_client.CancellationApi(swagger_client.ApiClient(configuration))
cancellation_id = 'cancellation_id_example' # str | ID of the cancellation to fetch

try:
    # Get cancellation by ID
    api_response = api_instance.get_cancellation(cancellation_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CancellationApi->get_cancellation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cancellation_id** | **str**| ID of the cancellation to fetch | 

### Return type

[**Cancellation**](Cancellation.md)

### Authorization

[tortoise_merchant_apiKey](../README.md#tortoise_merchant_apiKey), [tortoise_merchant_appId](../README.md#tortoise_merchant_appId)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

