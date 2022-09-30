# Copyright 2022 Guillaume Belanger
# See LICENSE file for licensing details.

from pydantic import BaseModel


class PLMNConfig(BaseModel):
    mcc: str
    mnc: str
