# Copyright 2022 Guillaume Belanger
# See LICENSE file for licensing details.

from pydantic import BaseModel


class DNS(BaseModel):
    dhcp_server_enabled: bool
    enable_caching: bool
    local_ttl: int
