# Copyright 2022 Guillaume Belanger
# See LICENSE file for licensing details.

from typing import Optional

from pydantic import BaseModel


class DiskPartition(BaseModel):
    device: Optional[str] = None
    free: Optional[str] = None
    mount_point: Optional[str] = None
    total: Optional[int] = None
    used: Optional[int] = None
