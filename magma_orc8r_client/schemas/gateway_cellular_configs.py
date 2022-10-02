# Copyright 2022 Guillaume Belanger
# See LICENSE file for licensing details.

from typing import Optional

from pydantic import BaseModel
from schemas.cellular_gateway_pool_records import CellularGatewayPoolRecords
from schemas.gateway_dns_configs import GatewayDNSConfigs
from schemas.gateway_epc_configs import GatewayEPCConfigs
from schemas.gateway_he_config import GatewayHEConfig
from schemas.gateway_non_eps_configs import GatewayNonEPSConfigs
from schemas.gateway_ran_configs import GatewayRANConfigs


class GatewayCellularConfigs(BaseModel):
    dns: GatewayDNSConfigs
    epc: GatewayEPCConfigs
    he_config: Optional[GatewayHEConfig] = None
    non_eps_service: Optional[GatewayNonEPSConfigs] = None
    pooling: Optional[CellularGatewayPoolRecords] = None
    ran: GatewayRANConfigs
