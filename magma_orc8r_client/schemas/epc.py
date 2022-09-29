# Copyright 2022 Guillaume Belanger
# See LICENSE file for licensing details.

from pydantic import BaseModel


class EPC(BaseModel):
    gx_gy_relay_enabled: bool
    hss_relay_enabled: bool
    lte_auth_amf: str
    lte_auth_op: str
    mcc: str
    mnc: str
    tac: int
