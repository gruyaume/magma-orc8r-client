# Copyright 2022 Guillaume Belanger
# See LICENSE file for licensing details.

from typing import Optional

from pydantic import BaseModel


class eNodeBConfiguration(BaseModel):  # noqa: N801
    bandwidth_mhz: Optional[int] = None
    cell_id: int
    device_class: str
    earfcndl: Optional[int] = None
    pci: Optional[int] = None
    special_subframe_pattern: Optional[int] = None
    subframe_assignment: Optional[int] = None
    tac: Optional[int] = None
    transmit_enabled: bool
