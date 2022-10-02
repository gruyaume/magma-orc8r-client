# Copyright 2022 Guillaume Belanger
# See LICENSE file for licensing details.


from typing import Optional

from pydantic import BaseModel
from schemas.gateway_dns_records import GatewayDNSRecords


class GatewayDNSConfigs(BaseModel):
    dhcp_server_enabled: bool
    enable_caching: bool
    local_ttl: int
    records: Optional[GatewayDNSRecords] = None
