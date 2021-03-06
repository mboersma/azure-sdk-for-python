# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class EvaluatePoliciesResponse(Model):
    """Response body for evaluating a policy set.

    :param results: Results of evaluating a policy set.
    :type results: list[~azure.mgmt.devtestlabs.models.PolicySetResult]
    """

    _attribute_map = {
        'results': {'key': 'results', 'type': '[PolicySetResult]'},
    }

    def __init__(self, results=None):
        self.results = results
