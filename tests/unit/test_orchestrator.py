# Copyright 2022 Guillaume Belanger
# See LICENSE file for licensing details.

from unittest.mock import patch

from orchestrator import Orc8r
from pytest import fixture

from tests.unit.common import MockContextManager


class TestOrc8r:
    BASE_URL = "https://api.magma.local"
    CERTIFICATE_DIRECTORY = "whatever directory"

    @fixture(scope="module")
    def orc8r_client(self):
        return Orc8r(
            url=self.BASE_URL,
            api_version="v1",
            admin_operator_pfx_path="whatever_file_path.pfx",
            admin_operator_pfx_password="whateverpassword",
        )

    @patch("requests.get")
    @patch("endpoints.base_endpoint.pfx_to_pem")
    def test_given_orc8r_custom_endpoint_when_get_then_http_get_api_call_is_made_to_correct_endpoint(  # noqa: E501
        self, patch_pfx_to_pem, patch_requests_get, orc8r_client
    ):
        network_id = "whatevernetwork"
        patch_pfx_to_pem.return_value = MockContextManager(cert_dir=self.CERTIFICATE_DIRECTORY)

        orc8r_client.get(endpoint=f"lte/{network_id}/apns")

        patch_requests_get.assert_called_with(
            url=f"{self.BASE_URL}/magma/v1/lte/{network_id}/apns",
            cert=self.CERTIFICATE_DIRECTORY,
            verify=False,
        )
