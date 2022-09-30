# Copyright 2022 Guillaume Belanger
# See LICENSE file for licensing details.

from typing import Optional

from pydantic import BaseModel


class IMEI(BaseModel):
    snr: Optional[str] = None
    tac: str
