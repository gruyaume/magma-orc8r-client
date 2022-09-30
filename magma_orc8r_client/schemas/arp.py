# Copyright 2022 Guillaume Belanger
# See LICENSE file for licensing details.

from pydantic import BaseModel


class ARP(BaseModel):
    preemption_capability: bool = True
    preemption_vulnerability: bool = False
    priority_level: int = 15
