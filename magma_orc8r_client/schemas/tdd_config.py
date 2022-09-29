# Copyright 2022 Guillaume Belanger
# See LICENSE file for licensing details.

from pydantic import BaseModel


class TDDConfig(BaseModel):
    earfcndl: int
    earfcnul: int
    special_subframe_pattern: int
    subframe_assignment: int
