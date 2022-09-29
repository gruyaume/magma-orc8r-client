# Copyright 2022 Guillaume Belanger
# See LICENSE file for licensing details.


from endpoints.lte import LteApi


class Orc8r:
    """Class that represents a Magma Orchestrator Instance"""

    def __init__(
        self,
        url: str,
        admin_operator_pfx_path: str,
        admin_operator_pfx_password: str,
        api_version: str = "v1",
    ):
        self.url = f"{url}/magma/{api_version}/"
        self.api_version = api_version
        self.admin_operator_pfx_path = admin_operator_pfx_path
        self.admin_operator_pfx_password = admin_operator_pfx_password

        # Endpoints
        self.lte = LteApi(
            base_url=self.url,
            admin_operator_pfx_path=admin_operator_pfx_path,
            admin_operator_pfx_password=admin_operator_pfx_password,
        )
