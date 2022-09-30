# Copyright 2022 Guillaume Belanger
# See LICENSE file for licensing details.

from pydantic import BaseModel
from schemas.enodeb_configuration import eNodeBConfiguration


class eNodeBConfig(BaseModel):  # noqa: N801
    config_type: str
    managed_config: eNodeBConfiguration
    unmanaged_config: eNodeBConfiguration
