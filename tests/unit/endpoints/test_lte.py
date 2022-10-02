# Copyright 2022 Guillaume Belanger
# See LICENSE file for licensing details.

from unittest.mock import patch

from orchestrator import Orc8r
from pytest import fixture
from schemas.lte_network import LTENetwork
from schemas.network_cellular_configs import NetworkCellularConfigs
from schemas.network_dns_config import NetworkDNSConfig
from schemas.network_epc_configs import NetworkEPCConfigs

from magma_orc8r_client.schemas.network_ran_configs import NetworkRANConfigs, TDDConfig
from tests.unit.common import MockContextManager, MockRequest


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
        patch_pfx_to_pem.return_value = MockContextManager(cert_dir=self.CERTIFICATE_DIRECTORY)
        patch_requests_get.return_value = MockRequest()

        orc8r_client.lte.list()

        patch_requests_get.assert_called_with(
            url=f"{self.BASE_URL}/magma/v1/lte",
            cert=self.CERTIFICATE_DIRECTORY,
            verify=False,
        )

    @patch("requests.get")
    @patch("endpoints.base_endpoint.pfx_to_pem")
    def test_given_orc8r_has_networks_when_get_lte_cellular_then_http_get_api_call_is_made_to_lte_cellular_endpoint(  # noqa: E501
        self, patch_pfx_to_pem, patch_requests_get, orc8r_client
    ):

        network_id = "whatevernetwork"
        patch_pfx_to_pem.return_value = MockContextManager(cert_dir=self.CERTIFICATE_DIRECTORY)
        patch_requests_get.return_value = MockRequest(
            return_json=NetworkCellularConfigs(
                epc=NetworkEPCConfigs(
                    gx_gy_relay_enabled=True,
                    hss_relay_enabled=True,
                    lte_auth_amf="aaa",
                    lte_auth_op="bbb",
                    mcc="001",
                    mnc="002",
                    tac=1,
                ),
                ran=NetworkRANConfigs(
                    bandwidth_mhz="123",
                    tdd_config={
                        "earfcndl": 123,
                        "special_subframe_pattern": 123,
                        "subframe_assignment": 123,
                    },
                ),
            ).dict()
        )

        orc8r_client.lte.get_cellular(network_id=network_id)

        patch_requests_get.assert_called_with(
            url=f"{self.BASE_URL}/magma/v1/lte/{network_id}/cellular",
            cert=self.CERTIFICATE_DIRECTORY,
            verify=False,
        )

    @patch("requests.post")
    @patch("endpoints.base_endpoint.pfx_to_pem")
    def test_given_when_create_network_then(
        self, patch_pfx_to_pem, patch_requests_post, orc8r_client
    ):
        patch_pfx_to_pem.return_value = MockContextManager(cert_dir=self.CERTIFICATE_DIRECTORY)
        network_id = "my_new_networkid"
        new_network = LTENetwork(
            dns=NetworkDNSConfig(dhcp_server_enabled=True, enable_caching=True, local_ttl=0),
            cellular=NetworkCellularConfigs(
                epc=NetworkEPCConfigs(
                    gx_gy_relay_enabled=True,
                    hss_relay_enabled=False,
                    lte_auth_amf="gAA=",
                    lte_auth_op="EREREREREREREREREREREQ==",
                    mcc="001",
                    mnc="01",
                    tac=1,
                ),
                ran=NetworkRANConfigs(
                    bandwidth_mhz=20,
                    tdd_config=TDDConfig(
                        earfcndl=44590,
                        special_subframe_pattern=7,
                        subframe_assignment=2,
                    ),
                ),
            ),
            description=network_id,
            id=network_id,
            name=network_id,
        )

        orc8r_client.lte.create_network(lte_network=new_network)

        patch_requests_post.assert_called_with(
            url=f"{self.BASE_URL}/magma/v1/lte",
            json=new_network.dict(),
            cert=self.CERTIFICATE_DIRECTORY,
            verify=False,
        )
