# Copyright 2022 Guillaume Belanger
# See LICENSE file for licensing details.

from pydantic import BaseModel


class Route(BaseModel):
    destination_ip: str
    gateway_ip: str
    genmask: str
    network_interface_id: str
