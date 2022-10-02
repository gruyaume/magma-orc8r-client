# Copyright 2022 Guillaume Belanger
# See LICENSE file for licensing details.


from pydantic import BaseModel


class GatewayRANConfigs(BaseModel):
    pci: int
    transmit_enabled: bool
