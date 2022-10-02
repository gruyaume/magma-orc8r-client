# Copyright 2022 Guillaume Belanger
# See LICENSE file for licensing details.

from enum import Enum
from typing import Optional

from pydantic import BaseModel


class IPv6PrefixAllocationMode(Enum):
    random = "RANDOM"
    hash = "HASH"


class GatewayEPCConfigs(BaseModel):
    congestion_control_enabled: bool = True
    dns_primary: Optional[str] = None
    dns_secondary: Optional[str] = None
    ip_block: str
    ipv4_p_cscf_addr: Optional[str] = None
    ipv4_sgw_s1u_addr: Optional[str] = None
    ipv6_block: Optional[str] = None
    ipv6_dns_addr: Optional[str] = None
    ipv6_p_cscf_addr: Optional[str] = None
    ipv6_prefix_allocation_mode: Optional[IPv6PrefixAllocationMode] = None
    nat_enabled: bool
    sgi_management_iface_gw: Optional[str] = None
    sgi_management_iface_static_ip: Optional[str] = None
    sgi_management_iface_vlan: Optional[str] = None
