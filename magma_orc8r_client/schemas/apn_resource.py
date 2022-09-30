# Copyright 2022 Guillaume Belanger
# See LICENSE file for licensing details.

from typing import Optional

from pydantic import BaseModel
from schemas.apn_name import APNName


class APNResource(BaseModel):
    apn_name: APNName
    gateway_ip: Optional[str] = None
    gateway_mac: Optional[str] = None
    id: str
    vlan_id: Optional[int] = None
