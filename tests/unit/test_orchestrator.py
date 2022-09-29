# Copyright 2022 Guillaume Belanger
# See LICENSE file for licensing details.

from typing import List, Union
from unittest.mock import patch

from orchestrator import Orc8r
from pytest import fixture


class MockContextManager:
    def __init__(self, cert_dir: str = "whatever"):
        self.cert_dir = cert_dir

    def __enter__(self):
        return self.cert_dir

    def __exit__(self, *args):
        pass


class MockRequest:
    def __init__(self, return_json: Union[dict, List] = None):
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
            admin_operator_pfx_path="whatever_file_path.pfx",
            admin_operator_pfx_password="whateverpassword",
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

    @patch("requests.get")
    @patch("endpoints.base_endpoint.pfx_to_pem")
    def test_given_orc8r_has_networks_when_lte_list_then_http_get_api_call_is_made_to_lte_endpoint(
        self, patch_pfx_to_pem, patch_requests_get, orc8r_client
    ):
        cert_dir = "whatever directory"
        patch_pfx_to_pem.return_value = MockContextManager(cert_dir=cert_dir)
        patch_requests_get.return_value = MockRequest()

        orc8r_client.lte.list()

        patch_requests_get.assert_called_with(
            url="https://api.magma.local/magma/v1/lte",
            cert=cert_dir,
            verify=False,
        )
