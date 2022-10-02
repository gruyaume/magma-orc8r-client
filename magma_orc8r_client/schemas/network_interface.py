# Copyright 2022 Guillaume Belanger
# See LICENSE file for licensing details.


from enum import Enum
from typing import List, Optional

from pydantic import BaseModel


class Status(Enum):
    up = "UP"
    down = "DOWN"
    unknown = "UNKNOWN"


class NetworkInterface(BaseModel):
    ip_addresses: Optional[List[str]] = None
    ipv6_addresses: Optional[List[str]] = None
    mac_address: Optional[str] = None
    network_interface_id: Optional[str] = None
    status: Optional[Status] = None
