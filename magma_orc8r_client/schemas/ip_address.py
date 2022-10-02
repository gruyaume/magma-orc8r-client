# Copyright 2022 Guillaume Belanger
# See LICENSE file for licensing details.

from enum import Enum

from pydantic import BaseModel


class Version(Enum):
    ipv4 = "IPv4"
    ipv6 = "IPv6"


class IPAddress(BaseModel):
    address: str
    version: Version
