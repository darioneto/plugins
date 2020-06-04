# coding: utf-8

"""
    Influx API Service

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    OpenAPI spec version: 0.1.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from influxdb_client.api_client import ApiClient


class OperationLogsService(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_buckets_id_logs(self, bucket_id, **kwargs):  # noqa: E501
        """Retrieve operation logs for a bucket  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_buckets_id_logs(bucket_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str bucket_id: The bucket ID. (required)
        :param str zap_trace_span: OpenTracing span context
        :param int offset:
        :param int limit:
        :return: OperationLogs
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_buckets_id_logs_with_http_info(bucket_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_buckets_id_logs_with_http_info(bucket_id, **kwargs)  # noqa: E501
            return data

    def get_buckets_id_logs_with_http_info(self, bucket_id, **kwargs):  # noqa: E501
        """Retrieve operation logs for a bucket  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_buckets_id_logs_with_http_info(bucket_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str bucket_id: The bucket ID. (required)
        :param str zap_trace_span: OpenTracing span context
        :param int offset:
        :param int limit:
        :return: OperationLogs
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['bucket_id', 'zap_trace_span', 'offset', 'limit']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_buckets_id_logs" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'bucket_id' is set
        if ('bucket_id' not in local_var_params or
                local_var_params['bucket_id'] is None):
            raise ValueError("Missing the required parameter `bucket_id` when calling `get_buckets_id_logs`")  # noqa: E501

        if 'offset' in local_var_params and local_var_params['offset'] < 0:  # noqa: E501
            raise ValueError("Invalid value for parameter `offset` when calling `get_buckets_id_logs`, must be a value greater than or equal to `0`")  # noqa: E501
        if 'limit' in local_var_params and local_var_params['limit'] > 100:  # noqa: E501
            raise ValueError("Invalid value for parameter `limit` when calling `get_buckets_id_logs`, must be a value less than or equal to `100`")  # noqa: E501
        if 'limit' in local_var_params and local_var_params['limit'] < 1:  # noqa: E501
            raise ValueError("Invalid value for parameter `limit` when calling `get_buckets_id_logs`, must be a value greater than or equal to `1`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'bucket_id' in local_var_params:
            path_params['bucketID'] = local_var_params['bucket_id']  # noqa: E501

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))  # noqa: E501
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))  # noqa: E501

        header_params = {}
        if 'zap_trace_span' in local_var_params:
            header_params['Zap-Trace-Span'] = local_var_params['zap_trace_span']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v2/buckets/{bucketID}/logs', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='OperationLogs',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_dashboards_id_logs(self, dashboard_id, **kwargs):  # noqa: E501
        """Retrieve operation logs for a dashboard  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_dashboards_id_logs(dashboard_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str dashboard_id: The dashboard ID. (required)
        :param str zap_trace_span: OpenTracing span context
        :param int offset:
        :param int limit:
        :return: OperationLogs
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_dashboards_id_logs_with_http_info(dashboard_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_dashboards_id_logs_with_http_info(dashboard_id, **kwargs)  # noqa: E501
            return data

    def get_dashboards_id_logs_with_http_info(self, dashboard_id, **kwargs):  # noqa: E501
        """Retrieve operation logs for a dashboard  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_dashboards_id_logs_with_http_info(dashboard_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str dashboard_id: The dashboard ID. (required)
        :param str zap_trace_span: OpenTracing span context
        :param int offset:
        :param int limit:
        :return: OperationLogs
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['dashboard_id', 'zap_trace_span', 'offset', 'limit']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_dashboards_id_logs" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'dashboard_id' is set
        if ('dashboard_id' not in local_var_params or
                local_var_params['dashboard_id'] is None):
            raise ValueError("Missing the required parameter `dashboard_id` when calling `get_dashboards_id_logs`")  # noqa: E501

        if 'offset' in local_var_params and local_var_params['offset'] < 0:  # noqa: E501
            raise ValueError("Invalid value for parameter `offset` when calling `get_dashboards_id_logs`, must be a value greater than or equal to `0`")  # noqa: E501
        if 'limit' in local_var_params and local_var_params['limit'] > 100:  # noqa: E501
            raise ValueError("Invalid value for parameter `limit` when calling `get_dashboards_id_logs`, must be a value less than or equal to `100`")  # noqa: E501
        if 'limit' in local_var_params and local_var_params['limit'] < 1:  # noqa: E501
            raise ValueError("Invalid value for parameter `limit` when calling `get_dashboards_id_logs`, must be a value greater than or equal to `1`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'dashboard_id' in local_var_params:
            path_params['dashboardID'] = local_var_params['dashboard_id']  # noqa: E501

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))  # noqa: E501
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))  # noqa: E501

        header_params = {}
        if 'zap_trace_span' in local_var_params:
            header_params['Zap-Trace-Span'] = local_var_params['zap_trace_span']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v2/dashboards/{dashboardID}/logs', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='OperationLogs',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_orgs_id_logs(self, org_id, **kwargs):  # noqa: E501
        """Retrieve operation logs for an organization  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_orgs_id_logs(org_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str org_id: The organization ID. (required)
        :param str zap_trace_span: OpenTracing span context
        :param int offset:
        :param int limit:
        :return: OperationLogs
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_orgs_id_logs_with_http_info(org_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_orgs_id_logs_with_http_info(org_id, **kwargs)  # noqa: E501
            return data

    def get_orgs_id_logs_with_http_info(self, org_id, **kwargs):  # noqa: E501
        """Retrieve operation logs for an organization  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_orgs_id_logs_with_http_info(org_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str org_id: The organization ID. (required)
        :param str zap_trace_span: OpenTracing span context
        :param int offset:
        :param int limit:
        :return: OperationLogs
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['org_id', 'zap_trace_span', 'offset', 'limit']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_orgs_id_logs" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'org_id' is set
        if ('org_id' not in local_var_params or
                local_var_params['org_id'] is None):
            raise ValueError("Missing the required parameter `org_id` when calling `get_orgs_id_logs`")  # noqa: E501

        if 'offset' in local_var_params and local_var_params['offset'] < 0:  # noqa: E501
            raise ValueError("Invalid value for parameter `offset` when calling `get_orgs_id_logs`, must be a value greater than or equal to `0`")  # noqa: E501
        if 'limit' in local_var_params and local_var_params['limit'] > 100:  # noqa: E501
            raise ValueError("Invalid value for parameter `limit` when calling `get_orgs_id_logs`, must be a value less than or equal to `100`")  # noqa: E501
        if 'limit' in local_var_params and local_var_params['limit'] < 1:  # noqa: E501
            raise ValueError("Invalid value for parameter `limit` when calling `get_orgs_id_logs`, must be a value greater than or equal to `1`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'org_id' in local_var_params:
            path_params['orgID'] = local_var_params['org_id']  # noqa: E501

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))  # noqa: E501
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))  # noqa: E501

        header_params = {}
        if 'zap_trace_span' in local_var_params:
            header_params['Zap-Trace-Span'] = local_var_params['zap_trace_span']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v2/orgs/{orgID}/logs', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='OperationLogs',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_users_id_logs(self, user_id, **kwargs):  # noqa: E501
        """Retrieve operation logs for a user  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_users_id_logs(user_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str user_id: The user ID. (required)
        :param str zap_trace_span: OpenTracing span context
        :param int offset:
        :param int limit:
        :return: OperationLogs
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_users_id_logs_with_http_info(user_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_users_id_logs_with_http_info(user_id, **kwargs)  # noqa: E501
            return data

    def get_users_id_logs_with_http_info(self, user_id, **kwargs):  # noqa: E501
        """Retrieve operation logs for a user  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_users_id_logs_with_http_info(user_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str user_id: The user ID. (required)
        :param str zap_trace_span: OpenTracing span context
        :param int offset:
        :param int limit:
        :return: OperationLogs
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['user_id', 'zap_trace_span', 'offset', 'limit']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_users_id_logs" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'user_id' is set
        if ('user_id' not in local_var_params or
                local_var_params['user_id'] is None):
            raise ValueError("Missing the required parameter `user_id` when calling `get_users_id_logs`")  # noqa: E501

        if 'offset' in local_var_params and local_var_params['offset'] < 0:  # noqa: E501
            raise ValueError("Invalid value for parameter `offset` when calling `get_users_id_logs`, must be a value greater than or equal to `0`")  # noqa: E501
        if 'limit' in local_var_params and local_var_params['limit'] > 100:  # noqa: E501
            raise ValueError("Invalid value for parameter `limit` when calling `get_users_id_logs`, must be a value less than or equal to `100`")  # noqa: E501
        if 'limit' in local_var_params and local_var_params['limit'] < 1:  # noqa: E501
            raise ValueError("Invalid value for parameter `limit` when calling `get_users_id_logs`, must be a value greater than or equal to `1`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'user_id' in local_var_params:
            path_params['userID'] = local_var_params['user_id']  # noqa: E501

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))  # noqa: E501
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))  # noqa: E501

        header_params = {}
        if 'zap_trace_span' in local_var_params:
            header_params['Zap-Trace-Span'] = local_var_params['zap_trace_span']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v2/users/{userID}/logs', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='OperationLogs',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)
