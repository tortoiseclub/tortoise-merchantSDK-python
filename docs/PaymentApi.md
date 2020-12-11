# swagger_client.PaymentApi

All URIs are relative to *https://virtserver.swaggerhub.com/suryaharshan1/Tortoise/1.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_payment**](PaymentApi.md#add_payment) | **POST** /payments | Add a new payment
[**fetch_all_payments**](PaymentApi.md#fetch_all_payments) | **GET** /payments | Fetch all payments
[**get_payment**](PaymentApi.md#get_payment) | **GET** /payments/{paymentId} | Get payment by ID


# **add_payment**
> add_payment(body)

Add a new payment

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
api_instance = swagger_client.PaymentApi(swagger_client.ApiClient(configuration))
body = swagger_client.Payment() # Payment | Payment object that needs to be added

try:
    # Add a new payment
    api_instance.add_payment(body)
except ApiException as e:
    print("Exception when calling PaymentApi->add_payment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Payment**](Payment.md)| Payment object that needs to be added | 

### Return type

void (empty response body)

### Authorization

[tortoise_merchant_apiKey](../README.md#tortoise_merchant_apiKey), [tortoise_merchant_appId](../README.md#tortoise_merchant_appId)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fetch_all_payments**
> list[Payment] fetch_all_payments()

Fetch all payments

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
api_instance = swagger_client.PaymentApi(swagger_client.ApiClient(configuration))

try:
    # Fetch all payments
    api_response = api_instance.fetch_all_payments()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentApi->fetch_all_payments: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Payment]**](Payment.md)

### Authorization

[tortoise_merchant_apiKey](../README.md#tortoise_merchant_apiKey), [tortoise_merchant_appId](../README.md#tortoise_merchant_appId)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_payment**
> Payment get_payment(payment_id)

Get payment by ID

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
api_instance = swagger_client.PaymentApi(swagger_client.ApiClient(configuration))
payment_id = 'payment_id_example' # str | ID of the payment to fetch

try:
    # Get payment by ID
    api_response = api_instance.get_payment(payment_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentApi->get_payment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payment_id** | **str**| ID of the payment to fetch | 

### Return type

[**Payment**](Payment.md)

### Authorization

[tortoise_merchant_apiKey](../README.md#tortoise_merchant_apiKey), [tortoise_merchant_appId](../README.md#tortoise_merchant_appId)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

