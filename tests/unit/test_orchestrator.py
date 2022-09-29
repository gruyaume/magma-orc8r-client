# Copyright 2022 Guillaume Belanger
# See LICENSE file for licensing details.

from typing import List, Union
from unittest.mock import patch

from orchestrator import Orc8r
from pytest import fixture


class MockContextManager:
    def __enter__(self):
        return self

    def __exit__(self, *args):
        pass


class MockRequest:
    def __init__(self, return_json: Union[dict, List]):
        self.return_json = return_json

    def raise_for_status(self):
        pass

    def json(self):
        return self.return_json


class TestOrc8r:
    @fixture(scope="module")
    def orc8r_client(self):
        return Orc8r(
            url="https://api.magma.local",
            api_version="v1",
            admin_operator_pfx_path="tests/unit/admin_operator.pfx",
            admin_operator_pfx_password="banana",
        )

    @patch("requests.get")
    @patch("endpoints.base_endpoint.pfx_to_pem")
    def test_given_orc8r_has_networks_when_lte_list_then_list_of_lte_networks_is_returned(
        self, patch_pfx_to_pem, patch_requests_get, orc8r_client
    ):
        json_return = ["network 1", "network2"]
        patch_requests_get.return_value = MockRequest(return_json=json_return)
        patch_pfx_to_pem.return_value = MockContextManager()

        list_of_networks = orc8r_client.lte.list()

        assert list_of_networks == json_return
