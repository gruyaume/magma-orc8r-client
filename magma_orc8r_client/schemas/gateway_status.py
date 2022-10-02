# Copyright 2022 Guillaume Belanger
# See LICENSE file for licensing details.

from enum import Enum
from typing import Dict, List, Optional

from pydantic import BaseModel
from schemas.machine_info import MachineInfo
from schemas.platform_info import PlatformInfo
from schemas.system_status import SystemStatus


class LogLevel(Enum):
    debug = "DEBUG"
    info = "INFO"
    warning = "WARNING"
    error = "ERROR"
    fatal = "FATAL"


class GatewayStatus(BaseModel):
    cert_expiration_time: Optional[int] = None
    checkin_time: Optional[int] = None
    hardware_id: Optional[str] = None
    kernel_version: Optional[str] = None
    kernel_versions_installed: Optional[List[str]] = None
    machine_info: Optional[MachineInfo] = None
    meta: Optional[Dict] = None
    platform_info: Optional[PlatformInfo] = None
    system_status: Optional[SystemStatus] = None
    version: Optional[str] = None
    vpn_ip: Optional[str] = None
