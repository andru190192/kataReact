"""Generated client library for cloudasset version v1."""
# NOTE: This file is autogenerated and should not be edited by hand.
from apitools.base.py import base_api
from googlecloudsdk.third_party.apis.cloudasset.v1 import cloudasset_v1_messages as messages


class CloudassetV1(base_api.BaseApiClient):
  """Generated client library for service cloudasset version v1."""

  MESSAGES_MODULE = messages
  BASE_URL = u'https://cloudasset.googleapis.com/'

  _PACKAGE = u'cloudasset'
  _SCOPES = [u'https://www.googleapis.com/auth/cloud-platform']
  _VERSION = u'v1'
  _CLIENT_ID = '1042881264118.apps.googleusercontent.com'
  _CLIENT_SECRET = 'x_Tw5K8nnjoRAqULM9PFAC2b'
  _USER_AGENT = 'x_Tw5K8nnjoRAqULM9PFAC2b'
  _CLIENT_CLASS_NAME = u'CloudassetV1'
  _URL_VERSION = u'v1'
  _API_KEY = None

  def __init__(self, url='', credentials=None,
               get_credentials=True, http=None, model=None,
               log_request=False, log_response=False,
               credentials_args=None, default_global_params=None,
               additional_http_headers=None, response_encoding=None):
    """Create a new cloudasset handle."""
    url = url or self.BASE_URL
    super(CloudassetV1, self).__init__(
        url, credentials=credentials,
        get_credentials=get_credentials, http=http, model=model,
        log_request=log_request, log_response=log_response,
        credentials_args=credentials_args,
        default_global_params=default_global_params,
        additional_http_headers=additional_http_headers,
        response_encoding=response_encoding)
    self.operations = self.OperationsService(self)
    self.v1 = self.V1Service(self)

  class OperationsService(base_api.BaseApiService):
    """Service class for the operations resource."""

    _NAME = u'operations'

    def __init__(self, client):
      super(CloudassetV1.OperationsService, self).__init__(client)
      self._upload_configs = {
          }

    def Get(self, request, global_params=None):
      r"""Gets the latest state of a long-running operation.  Clients can use this.
method to poll the operation result at intervals as recommended by the API
service.

      Args:
        request: (CloudassetOperationsGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1/{v1Id}/{v1Id1}/operations/{operationsId}/{operationsId1}',
        http_method=u'GET',
        method_id=u'cloudasset.operations.get',
        ordered_params=[u'name'],
        path_params=[u'name'],
        query_params=[],
        relative_path=u'v1/{+name}',
        request_field='',
        request_type_name=u'CloudassetOperationsGetRequest',
        response_type_name=u'Operation',
        supports_download=False,
    )

  class V1Service(base_api.BaseApiService):
    """Service class for the v1 resource."""

    _NAME = u'v1'

    def __init__(self, client):
      super(CloudassetV1.V1Service, self).__init__(client)
      self._upload_configs = {
          }

    def BatchGetAssetsHistory(self, request, global_params=None):
      r"""Batch gets the update history of assets that overlap a time window.
For RESOURCE content, this API outputs history with asset in both
non-delete or deleted status.
For IAM_POLICY content, this API outputs history when the asset and its
attached IAM POLICY both exist. This can create gaps in the output history.
If a specified asset does not exist, this API returns an INVALID_ARGUMENT
error.

      Args:
        request: (CloudassetBatchGetAssetsHistoryRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (BatchGetAssetsHistoryResponse) The response message.
      """
      config = self.GetMethodConfig('BatchGetAssetsHistory')
      return self._RunMethod(
          config, request, global_params=global_params)

    BatchGetAssetsHistory.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1/{v1Id}/{v1Id1}:batchGetAssetsHistory',
        http_method=u'GET',
        method_id=u'cloudasset.batchGetAssetsHistory',
        ordered_params=[u'parent'],
        path_params=[u'parent'],
        query_params=[u'assetNames', u'contentType', u'readTimeWindow_endTime', u'readTimeWindow_startTime'],
        relative_path=u'v1/{+parent}:batchGetAssetsHistory',
        request_field='',
        request_type_name=u'CloudassetBatchGetAssetsHistoryRequest',
        response_type_name=u'BatchGetAssetsHistoryResponse',
        supports_download=False,
    )

    def ExportAssets(self, request, global_params=None):
      r"""Exports assets with time and resource types to a given Cloud Storage.
location. The output format is newline-delimited JSON.
This API implements the google.longrunning.Operation API allowing you
to keep track of the export.

      Args:
        request: (CloudassetExportAssetsRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('ExportAssets')
      return self._RunMethod(
          config, request, global_params=global_params)

    ExportAssets.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1/{v1Id}/{v1Id1}:exportAssets',
        http_method=u'POST',
        method_id=u'cloudasset.exportAssets',
        ordered_params=[u'parent'],
        path_params=[u'parent'],
        query_params=[],
        relative_path=u'v1/{+parent}:exportAssets',
        request_field=u'exportAssetsRequest',
        request_type_name=u'CloudassetExportAssetsRequest',
        response_type_name=u'Operation',
        supports_download=False,
    )
