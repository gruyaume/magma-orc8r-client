# Copyright 2022 Guillaume Belanger
# See LICENSE file for licensing details.

from typing import List

from endpoints.base_endpoint import BaseEndpoint
from schemas.apn import APN
from schemas.lte_network import LTENetwork
from schemas.network_cellular_configs import NetworkCellularConfigs


class LteApi(BaseEndpoint):
    def __init__(
        self, base_url: str, admin_operator_pfx_path: str, admin_operator_pfx_password: str
    ):
        super().__init__(
            base_url=base_url,
            admin_operator_pfx_path=admin_operator_pfx_path,
            admin_operator_pfx_password=admin_operator_pfx_password,
            base_endpoint="lte",
        )

    def list(self) -> List[str]:
        response = super().get()
        return response.json()

    def get_network(self, network_id: str) -> LTENetwork:
        response = super().get(network_id)
        print(response.json())
        return LTENetwork(**response.json())

    def create_network(self, lte_network: LTENetwork) -> None:
        super().post(data=lte_network.dict())

    def delete_network(self, network_id: str) -> None:
        super().delete(endpoint=f"/{network_id}")

    def get_cellular(self, network_id: str) -> NetworkCellularConfigs:
        response = super().get(endpoint=f"/{network_id}/cellular")
        return NetworkCellularConfigs(**response.json())

    def list_network_apns(self, network_id: str) -> List[APN]:
        response = super().get(endpoint=f"/{network_id}/apns")
        response_content = response.json()
        return [APN(**response_content[i]) for i in response_content]

    def delete_network_apn(self, network_id: str, apn_name: str) -> None:
        super().delete(endpoint=f"/{network_id}/apns/{apn_name}")

    def create_network_apn(self, network_id: str, apn: APN) -> None:
        super().post(endpoint=f"/{network_id}/apns", data=apn.dict())
