# Copyright 2022 Guillaume Belanger
# See LICENSE file for licensing details.

from enum import Enum
from typing import Optional

from pydantic import BaseModel
from schemas.aggregation_logging_configs import AggregationLoggingConfigs


class LogLevel(Enum):
    debug = "DEBUG"
    info = "INFO"
    warning = "WARNING"
    error = "ERROR"
    fatal = "FATAL"


class GatewayLoggingConfig(BaseModel):
    aggregation: Optional[AggregationLoggingConfigs] = None
    event_verbosity: Optional[int] = None
    log_level: LogLevel
