# Copyright 2022 Guillaume Belanger
# See LICENSE file for licensing details.

from typing import List, Optional

from pydantic import BaseModel
from schemas.disk_partition import DiskPartition


class SystemStatus(BaseModel):
    cpu_idle: Optional[int] = None
    cpu_system: Optional[int] = None
    cpu_user: Optional[int] = None
    disk_partitions: Optional[List[DiskPartition]] = None
    mem_available: Optional[int] = None
    mem_free: Optional[int] = None
    mem_total: Optional[int] = None
    mem_used: Optional[int] = None
    swap_free: Optional[int] = None
    swap_total: Optional[int] = None
    swap_used: Optional[int] = None
    time: Optional[int] = None
    uptime_secs: Optional[int] = None
