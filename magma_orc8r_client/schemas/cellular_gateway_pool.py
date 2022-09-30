# Copyright 2022 Guillaume Belanger
# See LICENSE file for licensing details.

from typing import List, Optional

from pydantic import BaseModel
from schemas.cellular_gateway_pool_configs import CellularGatewayPoolConfigs
from schemas.gateway_id import GatewayID
from schemas.gateway_pool_id import GatewayPoolID


class CellularGatewayPool(BaseModel):
    config: CellularGatewayPoolConfigs
    gateway_ids: List[GatewayID]
    gateway_pool_id: GatewayPoolID
    gateway_pool_name: Optional[str] = None
