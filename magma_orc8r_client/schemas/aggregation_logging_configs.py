# Copyright 2022 Guillaume Belanger
# See LICENSE file for licensing details.

from typing import Dict, Optional

from pydantic import BaseModel


class AggregationLoggingConfigs(BaseModel):
    target_cfiles_by_tag: Optional[Dict] = None
    throttle_interval: Optional[str] = None
    throttle_rate: Optional[int] = None
    throttle_window: Optional[int] = None
