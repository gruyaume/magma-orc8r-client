# Copyright 2022 Guillaume Belanger
# See LICENSE file for licensing details.

from typing import Optional

from pydantic import BaseModel
from schemas.network_dns_records import NetworkDNSRecords


class NetworkDNSConfig(BaseModel):
    dhcp_server_enabled: Optional[bool] = None
    enable_caching: bool
    local_ttl: int
    records: Optional[NetworkDNSRecords] = None
