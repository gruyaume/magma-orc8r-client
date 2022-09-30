# Copyright 2022 Guillaume Belanger
# See LICENSE file for licensing details.

from typing import Optional

from pydantic import BaseModel
from schemas.enodeb_config import eNodeBConfig
from schemas.enodeb_configuration import eNodeBConfiguration


class eNodeB(BaseModel):  # noqa: N801
    attached_gateway_id: Optional[str] = None
    config: eNodeBConfiguration
    description: str
    enodeb_config: eNodeBConfig
    name: str
    serial: str
