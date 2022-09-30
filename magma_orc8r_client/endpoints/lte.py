# Copyright 2022 Guillaume Belanger
# See LICENSE file for licensing details.

from typing import List

from endpoints.base_endpoint import BaseEndpoint
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
            endpoint="lte",
        )

    def list(self) -> List[str]:
        response = super().base_get()
        return response.json()

    def get(self, network_id: str) -> LTENetwork:
        response = super().base_get(network_id)
        print(response.json())
        return LTENetwork(**response.json())

    def create(self, lte_network: LTENetwork) -> None:
        super().base_post(data=lte_network.dict())

    def delete(self, network_id: str) -> None:
        super().base_delete(command=network_id)

    def get_cellular(self, network_id: str) -> NetworkCellularConfigs:
        response = super().base_get(f"{network_id}/cellular")
        return NetworkCellularConfigs(**response.json())
