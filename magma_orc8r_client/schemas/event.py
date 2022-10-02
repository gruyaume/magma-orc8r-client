# Copyright 2022 Guillaume Belanger
# See LICENSE file for licensing details.

from typing import Dict

from pydantic import BaseModel


class Event(BaseModel):
    event_type: str
    hardware_id: str
    stream_name: str
    tag: str
    timestamp: str
    value: Dict
