# Copyright 2022 Guillaume Belanger
# See LICENSE file for licensing details.


from typing import List, Optional

from pydantic import BaseModel
from schemas.network_interface import NetworkInterface
from schemas.route import Route


class CPUInfo(BaseModel):
    architecture: Optional[str] = None
    core_count: Optional[int] = None
    model_name: Optional[int] = None


class NetworkInfo(BaseModel):
    network_interfaces: List[NetworkInterface]
    routing_table: List[Route]


class MachineInfo(BaseModel):
    cpu_info: CPUInfo
    network_info: NetworkInfo
