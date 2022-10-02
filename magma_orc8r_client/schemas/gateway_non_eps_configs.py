# Copyright 2022 Guillaume Belanger
# See LICENSE file for licensing details.


from enum import Enum
from typing import List

from pydantic import BaseModel


class NonEPSSrviceControl(Enum):
    zero = 0
    one = 1
    two = 2
    three = 3


class GatewayNonEPSConfigs(BaseModel):
    arfcn_2g: List[int]
    csfb_mcc: str
    csfb_mnc: str
    csfb_rat: int
    lac: int
    non_eps_service_control: NonEPSSrviceControl
