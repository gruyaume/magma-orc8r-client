# Copyright 2022 Guillaume Belanger
# See LICENSE file for licensing details.

from pydantic import BaseModel
from schemas.gateway_pool_id import GatewayPoolID


class CellularGatewayPoolRecord(BaseModel):
    gateway_pool_id: GatewayPoolID
    mme_code: int = 1
    mme_relative_capacity: int = 10
