# Copyright 2022 Guillaume Belanger
# See LICENSE file for licensing details.

from typing import List, Optional

from pydantic import BaseModel
from schemas.config_info import ConfigInfo
from schemas.package import Package


class PlatformInfo(BaseModel):
    config_info: Optional[ConfigInfo] = None
    kernel_version: Optional[str] = None
    kernel_versions_installed: Optional[List[str]] = None
    packages: Optional[List[Package]] = None
    vpn_ip: Optional[str] = None
