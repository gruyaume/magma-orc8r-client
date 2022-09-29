# Copyright 2022 Guillaume Belanger
# See LICENSE file for licensing details.

from typing import List

from endpoints.base_endpoint import BaseEndpoint
from schemas.network import Network


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

    def get(self, network_id: str) -> Network:
        response = super().base_get(network_id)
        return Network(**response.json())

    def create(self, network: Network) -> None:
        super().base_post(data=network.dict())
