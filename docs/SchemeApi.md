# swagger_client.SchemeApi

All URIs are relative to *https://virtserver.swaggerhub.com/suryaharshan1/Tortoise/1.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_scheme**](SchemeApi.md#add_scheme) | **POST** /schemes | Add a new scheme
[**edit_scheme**](SchemeApi.md#edit_scheme) | **PUT** /schemes/{schemeId} | Edit scheme details
[**fetch_all_schemes**](SchemeApi.md#fetch_all_schemes) | **GET** /schemes | Fetch all schemes
[**get_scheme**](SchemeApi.md#get_scheme) | **GET** /schemes/{schemeId} | Get scheme by ID


# **add_scheme**
> add_scheme(body)

Add a new scheme

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
api_instance = swagger_client.SchemeApi(swagger_client.ApiClient(configuration))
body = swagger_client.Scheme() # Scheme | Scheme object that needs to be added

try:
    # Add a new scheme
    api_instance.add_scheme(body)
except ApiException as e:
    print("Exception when calling SchemeApi->add_scheme: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Scheme**](Scheme.md)| Scheme object that needs to be added | 

### Return type

void (empty response body)

### Authorization

[tortoise_merchant_apiKey](../README.md#tortoise_merchant_apiKey), [tortoise_merchant_appId](../README.md#tortoise_merchant_appId)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_scheme**
> edit_scheme(scheme_id, body)

Edit scheme details

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
api_instance = swagger_client.SchemeApi(swagger_client.ApiClient(configuration))
scheme_id = 'scheme_id_example' # str | ID of the scheme to edit
body = swagger_client.Scheme() # Scheme | Scheme object that needs to be edited

try:
    # Edit scheme details
    api_instance.edit_scheme(scheme_id, body)
except ApiException as e:
    print("Exception when calling SchemeApi->edit_scheme: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scheme_id** | **str**| ID of the scheme to edit | 
 **body** | [**Scheme**](Scheme.md)| Scheme object that needs to be edited | 

### Return type

void (empty response body)

### Authorization

[tortoise_merchant_apiKey](../README.md#tortoise_merchant_apiKey), [tortoise_merchant_appId](../README.md#tortoise_merchant_appId)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fetch_all_schemes**
> list[Scheme] fetch_all_schemes()

Fetch all schemes

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
api_instance = swagger_client.SchemeApi(swagger_client.ApiClient(configuration))

try:
    # Fetch all schemes
    api_response = api_instance.fetch_all_schemes()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SchemeApi->fetch_all_schemes: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Scheme]**](Scheme.md)

### Authorization

[tortoise_merchant_apiKey](../README.md#tortoise_merchant_apiKey), [tortoise_merchant_appId](../README.md#tortoise_merchant_appId)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_scheme**
> Scheme get_scheme(scheme_id)

Get scheme by ID

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
api_instance = swagger_client.SchemeApi(swagger_client.ApiClient(configuration))
scheme_id = 'scheme_id_example' # str | ID of the scheme to fetch

try:
    # Get scheme by ID
    api_response = api_instance.get_scheme(scheme_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SchemeApi->get_scheme: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scheme_id** | **str**| ID of the scheme to fetch | 

### Return type

[**Scheme**](Scheme.md)

### Authorization

[tortoise_merchant_apiKey](../README.md#tortoise_merchant_apiKey), [tortoise_merchant_appId](../README.md#tortoise_merchant_appId)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

