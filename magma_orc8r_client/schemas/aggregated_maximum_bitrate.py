# Copyright 2022 Guillaume Belanger
# See LICENSE file for licensing details.

from pydantic import BaseModel


class AggregatedMaximumBitrate(BaseModel):
    max_bandwidth_dl: int
    max_bandwidth_ul: int
