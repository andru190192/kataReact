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
"""Implements command to describe a given guest policy."""

from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from googlecloudsdk.api_lib.compute.os_config import osconfig_utils
from googlecloudsdk.calliope import base
from googlecloudsdk.core import properties


@base.ReleaseTracks(base.ReleaseTrack.ALPHA)
class Describe(base.DescribeCommand):
  """Describe the given guest policy.

  ## EXAMPLES

    To describe the guest policy 'policy1' in the current project, run:

          $ {command} policy1

    To describe the guest policy 'policy1' in the organization '12345', run:

          $ {command} policy1 --organization=12345

  """

  @staticmethod
  def Args(parser):
    parser.add_argument(
        'POLICY_ID', type=str, help='ID of the guest policy to describe.')
    osconfig_utils.AddFolderAndOrgArgs(parser, 'guest policy', 'to describe')

  def Run(self, args):
    release_track = self.ReleaseTrack()
    client = osconfig_utils.GetClientInstance(release_track)
    messages = osconfig_utils.GetClientMessages(release_track)

    if args.organization:
      request = messages.OsconfigOrganizationsGuestPoliciesGetRequest(
          name=osconfig_utils.GetGuestPolicyUriPath(
              'organizations', args.organization, args.POLICY_ID))
      service = client.organizations_guestPolicies
    elif args.folder:
      request = messages.OsconfigFoldersGuestPoliciesGetRequest(
          name=osconfig_utils.GetGuestPolicyUriPath('folders', args.folder,
                                                    args.POLICY_ID))
      service = client.folders_guestPolicies
    else:
      project = properties.VALUES.core.project.GetOrFail()
      request = messages.OsconfigProjectsGuestPoliciesGetRequest(
          name=osconfig_utils.GetGuestPolicyUriPath('projects', project,
                                                    args.POLICY_ID))
      service = client.projects_guestPolicies

    return service.Get(request)
