# Copyright 2022 Guillaume Belanger
# See LICENSE file for licensing details.

from pydantic import BaseModel


class FlowQOS(BaseModel):
    max_req_bw_dl: int
    max_req_bw_ul: int
