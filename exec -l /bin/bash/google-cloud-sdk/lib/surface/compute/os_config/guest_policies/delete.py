# -*- coding: utf-8 -*- #
# Copyright 2019 Google LLC. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Implements command to delete a given guest policy."""

from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from googlecloudsdk.api_lib.compute.os_config import osconfig_utils
from googlecloudsdk.calliope import base
from googlecloudsdk.core import log
from googlecloudsdk.core import properties


@base.ReleaseTracks(base.ReleaseTrack.ALPHA)
class Delete(base.DeleteCommand):
  """Delete the given guest policy.

  ## EXAMPLES

    To delete the guest policy named 'policy1' in the current project, run:

          $ {command} policy1

    To delete the guest policy named 'policy1' in the organization '12345', run:

          $ {command} policy1 --organization=12345

  """

  @staticmethod
  def Args(parser):
    parser.add_argument(
        'POLICY_ID', type=str, help='ID of the guest policy to delete.')
    osconfig_utils.AddFolderAndOrgArgs(parser, 'guest policy', 'to delete')

  def Run(self, args):
    release_track = self.ReleaseTrack()
    client = osconfig_utils.GetClientInstance(release_track)
    messages = osconfig_utils.GetClientMessages(release_track)

    guest_policy_name = ''
    if args.organization:
      guest_policy_name = osconfig_utils.GetGuestPolicyUriPath(
          'organizations', args.organization, args.POLICY_ID)
      request = messages.OsconfigOrganizationsGuestPoliciesDeleteRequest(
          name=guest_policy_name)
      service = client.organizations_guestPolicies
    elif args.folder:
      guest_policy_name = osconfig_utils.GetGuestPolicyUriPath(
          'folders', args.folder, args.POLICY_ID)
      request = messages.OsconfigFoldersGuestPoliciesDeleteRequest(
          name=guest_policy_name)
      service = client.folders_guestPolicies
    else:
      project = properties.VALUES.core.project.GetOrFail()
      guest_policy_name = osconfig_utils.GetGuestPolicyUriPath(
          'projects', project, args.POLICY_ID)
      request = messages.OsconfigProjectsGuestPoliciesDeleteRequest(
          name=guest_policy_name)
      service = client.projects_guestPolicies

    response = service.Delete(request)
    log.DeletedResource(guest_policy_name)
    return response
