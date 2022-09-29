# Copyright 2022 Guillaume Belanger
# See LICENSE file for licensing details.

from pydantic import BaseModel
from schemas.epc import EPC
from schemas.ran import RAN


class Cellular(BaseModel):
    epc: EPC
    ran: RAN
