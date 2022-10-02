# Copyright 2022 Guillaume Belanger
# See LICENSE file for licensing details.

from pydantic import BaseModel
from schemas.flow_match import FlowMatch


class FlowDescription(BaseModel):
    action: str
    match: FlowMatch
