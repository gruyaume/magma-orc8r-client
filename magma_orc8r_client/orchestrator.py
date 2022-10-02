# Copyright 2022 Guillaume Belanger
# See LICENSE file for licensing details.

import logging

from endpoints.base_endpoint import BaseEndpoint
from endpoints.lte import LteApi

logger = logging.getLogger(__name__)


class Orc8r(BaseEndpoint):
    """Class that represents a Magma Orchestrator Instance"""

    def __init__(
        self,
        url: str,
        admin_operator_pfx_path: str,
        admin_operator_pfx_password: str,
        api_version: str = "v1",
    ):
        self.url = f"{url}/magma/{api_version}/"
        super().__init__(
            base_url=self.url,
            admin_operator_pfx_path=admin_operator_pfx_path,
            admin_operator_pfx_password=admin_operator_pfx_password,
        )

        self.api_version = api_version
        self.admin_operator_pfx_path = admin_operator_pfx_path
        self.admin_operator_pfx_password = admin_operator_pfx_password

        # Endpoints
        self.lte = LteApi(
            base_url=self.url,
            admin_operator_pfx_path=admin_operator_pfx_path,
            admin_operator_pfx_password=admin_operator_pfx_password,
        )
