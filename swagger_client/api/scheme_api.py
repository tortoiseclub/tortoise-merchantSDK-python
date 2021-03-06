# coding: utf-8

"""
    Tortoise Merchant API

    Tortoise API for merchant to integrate with their existing systems   # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: developer@tortoise.pro
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class SchemeApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def add_scheme(self, body, **kwargs):  # noqa: E501
        """Add a new scheme  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.add_scheme(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Scheme body: Scheme object that needs to be added (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.add_scheme_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.add_scheme_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def add_scheme_with_http_info(self, body, **kwargs):  # noqa: E501
        """Add a new scheme  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.add_scheme_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Scheme body: Scheme object that needs to be added (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method add_scheme" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `add_scheme`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['tortoise_merchant_apiKey', 'tortoise_merchant_appId']  # noqa: E501

        return self.api_client.call_api(
            '/schemes', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def edit_scheme(self, scheme_id, body, **kwargs):  # noqa: E501
        """Edit scheme details  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.edit_scheme(scheme_id, body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str scheme_id: ID of the scheme to edit (required)
        :param Scheme body: Scheme object that needs to be edited (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.edit_scheme_with_http_info(scheme_id, body, **kwargs)  # noqa: E501
        else:
            (data) = self.edit_scheme_with_http_info(scheme_id, body, **kwargs)  # noqa: E501
            return data

    def edit_scheme_with_http_info(self, scheme_id, body, **kwargs):  # noqa: E501
        """Edit scheme details  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.edit_scheme_with_http_info(scheme_id, body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str scheme_id: ID of the scheme to edit (required)
        :param Scheme body: Scheme object that needs to be edited (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['scheme_id', 'body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method edit_scheme" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'scheme_id' is set
        if ('scheme_id' not in params or
                params['scheme_id'] is None):
            raise ValueError("Missing the required parameter `scheme_id` when calling `edit_scheme`")  # noqa: E501
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `edit_scheme`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'scheme_id' in params:
            path_params['schemeId'] = params['scheme_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['tortoise_merchant_apiKey', 'tortoise_merchant_appId']  # noqa: E501

        return self.api_client.call_api(
            '/schemes/{schemeId}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def fetch_all_schemes(self, **kwargs):  # noqa: E501
        """Fetch all schemes  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_all_schemes(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: list[Scheme]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_all_schemes_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.fetch_all_schemes_with_http_info(**kwargs)  # noqa: E501
            return data

    def fetch_all_schemes_with_http_info(self, **kwargs):  # noqa: E501
        """Fetch all schemes  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_all_schemes_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: list[Scheme]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_all_schemes" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['tortoise_merchant_apiKey', 'tortoise_merchant_appId']  # noqa: E501

        return self.api_client.call_api(
            '/schemes', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[Scheme]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_scheme(self, scheme_id, **kwargs):  # noqa: E501
        """Get scheme by ID  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_scheme(scheme_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str scheme_id: ID of the scheme to fetch (required)
        :return: Scheme
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_scheme_with_http_info(scheme_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_scheme_with_http_info(scheme_id, **kwargs)  # noqa: E501
            return data

    def get_scheme_with_http_info(self, scheme_id, **kwargs):  # noqa: E501
        """Get scheme by ID  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_scheme_with_http_info(scheme_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str scheme_id: ID of the scheme to fetch (required)
        :return: Scheme
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['scheme_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_scheme" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'scheme_id' is set
        if ('scheme_id' not in params or
                params['scheme_id'] is None):
            raise ValueError("Missing the required parameter `scheme_id` when calling `get_scheme`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'scheme_id' in params:
            path_params['schemeId'] = params['scheme_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['tortoise_merchant_apiKey', 'tortoise_merchant_appId']  # noqa: E501

        return self.api_client.call_api(
            '/schemes/{schemeId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Scheme',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
