# swagger_client.ProductApi

All URIs are relative to *https://virtserver.swaggerhub.com/suryaharshan1/Tortoise/1.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_product**](ProductApi.md#add_product) | **POST** /products | Add a new product
[**edit_product**](ProductApi.md#edit_product) | **PUT** /products/{productId} | Edit product details
[**fetch_all_products**](ProductApi.md#fetch_all_products) | **GET** /products | Fetch all products
[**get_product**](ProductApi.md#get_product) | **GET** /products/{productId} | Get product by ID


# **add_product**
> Product add_product(body)

Add a new product

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
api_instance = swagger_client.ProductApi(swagger_client.ApiClient(configuration))
body = swagger_client.Product() # Product | Product object that needs to be added

try:
    # Add a new product
    api_response = api_instance.add_product(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductApi->add_product: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Product**](Product.md)| Product object that needs to be added | 

### Return type

[**Product**](Product.md)

### Authorization

[tortoise_merchant_apiKey](../README.md#tortoise_merchant_apiKey), [tortoise_merchant_appId](../README.md#tortoise_merchant_appId)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_product**
> edit_product(product_id, body)

Edit product details

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
api_instance = swagger_client.ProductApi(swagger_client.ApiClient(configuration))
product_id = 'product_id_example' # str | ID of the product to edit
body = swagger_client.Product() # Product | Product object that needs to be edited

try:
    # Edit product details
    api_instance.edit_product(product_id, body)
except ApiException as e:
    print("Exception when calling ProductApi->edit_product: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_id** | **str**| ID of the product to edit | 
 **body** | [**Product**](Product.md)| Product object that needs to be edited | 

### Return type

void (empty response body)

### Authorization

[tortoise_merchant_apiKey](../README.md#tortoise_merchant_apiKey), [tortoise_merchant_appId](../README.md#tortoise_merchant_appId)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fetch_all_products**
> list[Product] fetch_all_products()

Fetch all products

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
api_instance = swagger_client.ProductApi(swagger_client.ApiClient(configuration))

try:
    # Fetch all products
    api_response = api_instance.fetch_all_products()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductApi->fetch_all_products: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Product]**](Product.md)

### Authorization

[tortoise_merchant_apiKey](../README.md#tortoise_merchant_apiKey), [tortoise_merchant_appId](../README.md#tortoise_merchant_appId)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_product**
> Product get_product(product_id)

Get product by ID

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
api_instance = swagger_client.ProductApi(swagger_client.ApiClient(configuration))
product_id = 'product_id_example' # str | ID of the product to fetch

try:
    # Get product by ID
    api_response = api_instance.get_product(product_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductApi->get_product: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_id** | **str**| ID of the product to fetch | 

### Return type

[**Product**](Product.md)

### Authorization

[tortoise_merchant_apiKey](../README.md#tortoise_merchant_apiKey), [tortoise_merchant_appId](../README.md#tortoise_merchant_appId)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

