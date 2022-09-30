# Copyright 2022 Guillaume Belanger
# See LICENSE file for licensing details.

from pydantic import BaseModel


class QOSProfile(BaseModel):
    class_id: int = 9
    preemption_capability: bool = True
    preemption_vulnerability: bool = False
    priority_level: int = 15
