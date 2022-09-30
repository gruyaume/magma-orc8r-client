# Copyright 2022 Guillaume Belanger
# See LICENSE file for licensing details.

from pydantic import BaseModel


class CellularGatewayPoolConfigs(BaseModel):
    mme_group_id: int = 1
