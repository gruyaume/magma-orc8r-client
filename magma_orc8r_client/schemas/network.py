# Copyright 2022 Guillaume Belanger
# See LICENSE file for licensing details.

from pydantic import BaseModel
from schemas.cellular import Cellular
from schemas.dns import DNS


class Network(BaseModel):
    cellular: Cellular
    description: str
    dns: DNS
    id: str
    name: str
