"""Generated client library for stream version v1."""
# NOTE: This file is autogenerated and should not be edited by hand.

from __future__ import absolute_import

from apitools.base.py import base_api
from googlecloudsdk.generated_clients.apis.stream.v1 import stream_v1_messages as messages


class StreamV1(base_api.BaseApiClient):
  """Generated client library for service stream version v1."""

  MESSAGES_MODULE = messages
  BASE_URL = 'https://stream.googleapis.com/'
  MTLS_BASE_URL = 'https://stream.mtls.googleapis.com/'

  _PACKAGE = 'stream'
  _SCOPES = ['https://www.googleapis.com/auth/cloud-platform']
  _VERSION = 'v1'
  _CLIENT_ID = 'CLIENT_ID'
  _CLIENT_SECRET = 'CLIENT_SECRET'
  _USER_AGENT = 'google-cloud-sdk'
  _CLIENT_CLASS_NAME = 'StreamV1'
  _URL_VERSION = 'v1'
  _API_KEY = None

  def __init__(self, url='', credentials=None,
               get_credentials=True, http=None, model=None,
               log_request=False, log_response=False,
               credentials_args=None, default_global_params=None,
               additional_http_headers=None, response_encoding=None):
    """Create a new stream handle."""
    url = url or self.BASE_URL
    super(StreamV1, self).__init__(
        url, credentials=credentials,
        get_credentials=get_credentials, http=http, model=model,
        log_request=log_request, log_response=log_response,
        credentials_args=credentials_args,
        default_global_params=default_global_params,
        additional_http_headers=additional_http_headers,
        response_encoding=response_encoding)
    self.projects_locations_operations = self.ProjectsLocationsOperationsService(self)
    self.projects_locations_streamContents = self.ProjectsLocationsStreamContentsService(self)
    self.projects_locations_streamInstances = self.ProjectsLocationsStreamInstancesService(self)
    self.projects_locations = self.ProjectsLocationsService(self)
    self.projects = self.ProjectsService(self)

  class ProjectsLocationsOperationsService(base_api.BaseApiService):
    """Service class for the projects_locations_operations resource."""

    _NAME = 'projects_locations_operations'

    def __init__(self, client):
      super(StreamV1.ProjectsLocationsOperationsService, self).__init__(client)
      self._upload_configs = {
          }

    def Cancel(self, request, global_params=None):
      r"""Starts asynchronous cancellation on a long-running operation. The server makes a best effort to cancel the operation, but success is not guaranteed. If the server doesn't support this method, it returns `google.rpc.Code.UNIMPLEMENTED`. Clients can use Operations.GetOperation or other methods to check whether the cancellation succeeded or whether the operation completed despite cancellation. On successful cancellation, the operation is not deleted; instead, it becomes an operation with an Operation.error value with a google.rpc.Status.code of `1`, corresponding to `Code.CANCELLED`.

      Args:
        request: (StreamProjectsLocationsOperationsCancelRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Empty) The response message.
      """
      config = self.GetMethodConfig('Cancel')
      return self._RunMethod(
          config, request, global_params=global_params)

    Cancel.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/projects/{projectsId}/locations/{locationsId}/operations/{operationsId}:cancel',
        http_method='POST',
        method_id='stream.projects.locations.operations.cancel',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1/{+name}:cancel',
        request_field='cancelOperationRequest',
        request_type_name='StreamProjectsLocationsOperationsCancelRequest',
        response_type_name='Empty',
        supports_download=False,
    )

    def Delete(self, request, global_params=None):
      r"""Deletes a long-running operation. This method indicates that the client is no longer interested in the operation result. It does not cancel the operation. If the server doesn't support this method, it returns `google.rpc.Code.UNIMPLEMENTED`.

      Args:
        request: (StreamProjectsLocationsOperationsDeleteRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Empty) The response message.
      """
      config = self.GetMethodConfig('Delete')
      return self._RunMethod(
          config, request, global_params=global_params)

    Delete.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/projects/{projectsId}/locations/{locationsId}/operations/{operationsId}',
        http_method='DELETE',
        method_id='stream.projects.locations.operations.delete',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1/{+name}',
        request_field='',
        request_type_name='StreamProjectsLocationsOperationsDeleteRequest',
        response_type_name='Empty',
        supports_download=False,
    )

    def Get(self, request, global_params=None):
      r"""Gets the latest state of a long-running operation. Clients can use this method to poll the operation result at intervals as recommended by the API service.

      Args:
        request: (StreamProjectsLocationsOperationsGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/projects/{projectsId}/locations/{locationsId}/operations/{operationsId}',
        http_method='GET',
        method_id='stream.projects.locations.operations.get',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1/{+name}',
        request_field='',
        request_type_name='StreamProjectsLocationsOperationsGetRequest',
        response_type_name='Operation',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      r"""Lists operations that match the specified filter in the request. If the server doesn't support this method, it returns `UNIMPLEMENTED`.

      Args:
        request: (StreamProjectsLocationsOperationsListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListOperationsResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/projects/{projectsId}/locations/{locationsId}/operations',
        http_method='GET',
        method_id='stream.projects.locations.operations.list',
        ordered_params=['name'],
        path_params=['name'],
        query_params=['filter', 'pageSize', 'pageToken'],
        relative_path='v1/{+name}/operations',
        request_field='',
        request_type_name='StreamProjectsLocationsOperationsListRequest',
        response_type_name='ListOperationsResponse',
        supports_download=False,
    )

  class ProjectsLocationsStreamContentsService(base_api.BaseApiService):
    """Service class for the projects_locations_streamContents resource."""

    _NAME = 'projects_locations_streamContents'

    def __init__(self, client):
      super(StreamV1.ProjectsLocationsStreamContentsService, self).__init__(client)
      self._upload_configs = {
          }

    def Build(self, request, global_params=None):
      r"""Builds the content to a Stream compatible format using the associated sources in a consumer cloud storage bucket. A new content version is created with the user-specified tag if the build succeeds. The returned Operation can be used to track the build status by polling operations.get. The Operation will complete when the build is done. Returns [StreamContent] in the Operation.response field on successful completion.

      Args:
        request: (StreamProjectsLocationsStreamContentsBuildRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Build')
      return self._RunMethod(
          config, request, global_params=global_params)

    Build.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/projects/{projectsId}/locations/{locationsId}/streamContents/{streamContentsId}:build',
        http_method='POST',
        method_id='stream.projects.locations.streamContents.build',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1/{+name}:build',
        request_field='buildStreamContentRequest',
        request_type_name='StreamProjectsLocationsStreamContentsBuildRequest',
        response_type_name='Operation',
        supports_download=False,
    )

    def Create(self, request, global_params=None):
      r"""Creates a new StreamContent that manages the metadata and builds of user-provided Stream compatible content sources in a consumer cloud storage bucket. The returned Operation can be used to track the creation status by polling operations.get. The Operation will complete when the creation is done. Returns [StreamContent] in the Operation.response field on successful completion.

      Args:
        request: (StreamProjectsLocationsStreamContentsCreateRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Create')
      return self._RunMethod(
          config, request, global_params=global_params)

    Create.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/projects/{projectsId}/locations/{locationsId}/streamContents',
        http_method='POST',
        method_id='stream.projects.locations.streamContents.create',
        ordered_params=['parent'],
        path_params=['parent'],
        query_params=['requestId', 'streamContentId'],
        relative_path='v1/{+parent}/streamContents',
        request_field='streamContent',
        request_type_name='StreamProjectsLocationsStreamContentsCreateRequest',
        response_type_name='Operation',
        supports_download=False,
    )

    def Delete(self, request, global_params=None):
      r"""Deletes a single StreamContent. This method removes the version history of content builds but does not delete any content source in the consumer cloud storage bucket. The returned Operation can be used to track the deletion status by polling operations.get. The Operation will complete when the deletion is done. Returns Empty in the Operation.response field on successful completion.

      Args:
        request: (StreamProjectsLocationsStreamContentsDeleteRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Delete')
      return self._RunMethod(
          config, request, global_params=global_params)

    Delete.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/projects/{projectsId}/locations/{locationsId}/streamContents/{streamContentsId}',
        http_method='DELETE',
        method_id='stream.projects.locations.streamContents.delete',
        ordered_params=['name'],
        path_params=['name'],
        query_params=['requestId'],
        relative_path='v1/{+name}',
        request_field='',
        request_type_name='StreamProjectsLocationsStreamContentsDeleteRequest',
        response_type_name='Operation',
        supports_download=False,
    )

    def Get(self, request, global_params=None):
      r"""Gets details of a single StreamContent.

      Args:
        request: (StreamProjectsLocationsStreamContentsGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (StreamContent) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/projects/{projectsId}/locations/{locationsId}/streamContents/{streamContentsId}',
        http_method='GET',
        method_id='stream.projects.locations.streamContents.get',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1/{+name}',
        request_field='',
        request_type_name='StreamProjectsLocationsStreamContentsGetRequest',
        response_type_name='StreamContent',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      r"""Lists StreamContents in a given project and location.

      Args:
        request: (StreamProjectsLocationsStreamContentsListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListStreamContentsResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/projects/{projectsId}/locations/{locationsId}/streamContents',
        http_method='GET',
        method_id='stream.projects.locations.streamContents.list',
        ordered_params=['parent'],
        path_params=['parent'],
        query_params=['filter', 'orderBy', 'pageSize', 'pageToken'],
        relative_path='v1/{+parent}/streamContents',
        request_field='',
        request_type_name='StreamProjectsLocationsStreamContentsListRequest',
        response_type_name='ListStreamContentsResponse',
        supports_download=False,
    )

    def Patch(self, request, global_params=None):
      r"""Updates the parameters of a single StreamContent.

      Args:
        request: (StreamProjectsLocationsStreamContentsPatchRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Patch')
      return self._RunMethod(
          config, request, global_params=global_params)

    Patch.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/projects/{projectsId}/locations/{locationsId}/streamContents/{streamContentsId}',
        http_method='PATCH',
        method_id='stream.projects.locations.streamContents.patch',
        ordered_params=['name'],
        path_params=['name'],
        query_params=['requestId', 'updateMask'],
        relative_path='v1/{+name}',
        request_field='streamContent',
        request_type_name='StreamProjectsLocationsStreamContentsPatchRequest',
        response_type_name='Operation',
        supports_download=False,
    )

  class ProjectsLocationsStreamInstancesService(base_api.BaseApiService):
    """Service class for the projects_locations_streamInstances resource."""

    _NAME = 'projects_locations_streamInstances'

    def __init__(self, client):
      super(StreamV1.ProjectsLocationsStreamInstancesService, self).__init__(client)
      self._upload_configs = {
          }

    def Create(self, request, global_params=None):
      r"""Creates a new StreamInstance that manages the turnup and rollout of the streaming service for a given StreamContent. The returned Operation can be used to track the creation status by polling operations.get. The Operation will complete when the creation is done. Returns [StreamInstance] in the Operation.response field on successful completion.

      Args:
        request: (StreamProjectsLocationsStreamInstancesCreateRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Create')
      return self._RunMethod(
          config, request, global_params=global_params)

    Create.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/projects/{projectsId}/locations/{locationsId}/streamInstances',
        http_method='POST',
        method_id='stream.projects.locations.streamInstances.create',
        ordered_params=['parent'],
        path_params=['parent'],
        query_params=['requestId', 'streamInstanceId'],
        relative_path='v1/{+parent}/streamInstances',
        request_field='streamInstance',
        request_type_name='StreamProjectsLocationsStreamInstancesCreateRequest',
        response_type_name='Operation',
        supports_download=False,
    )

    def Delete(self, request, global_params=None):
      r"""Deletes a single StreamInstance. This method tears down the streaming service of the associated StreamContent. The returned Operation can be used to track the deletion status by polling operations.get. The Operation will complete when the deletion is done. Returns Empty in the Operation.response field on successful completion.

      Args:
        request: (StreamProjectsLocationsStreamInstancesDeleteRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Delete')
      return self._RunMethod(
          config, request, global_params=global_params)

    Delete.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/projects/{projectsId}/locations/{locationsId}/streamInstances/{streamInstancesId}',
        http_method='DELETE',
        method_id='stream.projects.locations.streamInstances.delete',
        ordered_params=['name'],
        path_params=['name'],
        query_params=['requestId'],
        relative_path='v1/{+name}',
        request_field='',
        request_type_name='StreamProjectsLocationsStreamInstancesDeleteRequest',
        response_type_name='Operation',
        supports_download=False,
    )

    def Get(self, request, global_params=None):
      r"""Gets details of a single StreamInstance.

      Args:
        request: (StreamProjectsLocationsStreamInstancesGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (StreamInstance) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/projects/{projectsId}/locations/{locationsId}/streamInstances/{streamInstancesId}',
        http_method='GET',
        method_id='stream.projects.locations.streamInstances.get',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1/{+name}',
        request_field='',
        request_type_name='StreamProjectsLocationsStreamInstancesGetRequest',
        response_type_name='StreamInstance',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      r"""Lists StreamInstances in a given project and location.

      Args:
        request: (StreamProjectsLocationsStreamInstancesListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListStreamInstancesResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/projects/{projectsId}/locations/{locationsId}/streamInstances',
        http_method='GET',
        method_id='stream.projects.locations.streamInstances.list',
        ordered_params=['parent'],
        path_params=['parent'],
        query_params=['filter', 'orderBy', 'pageSize', 'pageToken'],
        relative_path='v1/{+parent}/streamInstances',
        request_field='',
        request_type_name='StreamProjectsLocationsStreamInstancesListRequest',
        response_type_name='ListStreamInstancesResponse',
        supports_download=False,
    )

    def Patch(self, request, global_params=None):
      r"""Updates the parameters of a single StreamInstance.

      Args:
        request: (StreamProjectsLocationsStreamInstancesPatchRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Patch')
      return self._RunMethod(
          config, request, global_params=global_params)

    Patch.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/projects/{projectsId}/locations/{locationsId}/streamInstances/{streamInstancesId}',
        http_method='PATCH',
        method_id='stream.projects.locations.streamInstances.patch',
        ordered_params=['name'],
        path_params=['name'],
        query_params=['requestId', 'updateMask'],
        relative_path='v1/{+name}',
        request_field='streamInstance',
        request_type_name='StreamProjectsLocationsStreamInstancesPatchRequest',
        response_type_name='Operation',
        supports_download=False,
    )

  class ProjectsLocationsService(base_api.BaseApiService):
    """Service class for the projects_locations resource."""

    _NAME = 'projects_locations'

    def __init__(self, client):
      super(StreamV1.ProjectsLocationsService, self).__init__(client)
      self._upload_configs = {
          }

    def Get(self, request, global_params=None):
      r"""Gets information about a location.

      Args:
        request: (StreamProjectsLocationsGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Location) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/projects/{projectsId}/locations/{locationsId}',
        http_method='GET',
        method_id='stream.projects.locations.get',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1/{+name}',
        request_field='',
        request_type_name='StreamProjectsLocationsGetRequest',
        response_type_name='Location',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      r"""Lists information about the supported locations for this service.

      Args:
        request: (StreamProjectsLocationsListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListLocationsResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/projects/{projectsId}/locations',
        http_method='GET',
        method_id='stream.projects.locations.list',
        ordered_params=['name'],
        path_params=['name'],
        query_params=['extraLocationTypes', 'filter', 'pageSize', 'pageToken'],
        relative_path='v1/{+name}/locations',
        request_field='',
        request_type_name='StreamProjectsLocationsListRequest',
        response_type_name='ListLocationsResponse',
        supports_download=False,
    )

  class ProjectsService(base_api.BaseApiService):
    """Service class for the projects resource."""

    _NAME = 'projects'

    def __init__(self, client):
      super(StreamV1.ProjectsService, self).__init__(client)
      self._upload_configs = {
          }
