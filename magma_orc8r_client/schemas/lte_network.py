# Copyright 2022 Guillaume Belanger
# See LICENSE file for licensing details.

from typing import Optional

from pydantic import BaseModel
from schemas.network_cellular_configs import NetworkCellularConfigs
from schemas.network_dns_config import NetworkDNSConfig
from schemas.network_features import NetworkFeatures
from schemas.network_subscriber_config import NetworkSubscriberConfig


class LTENetwork(BaseModel):
    cellular: NetworkCellularConfigs
    description: str
    dns: NetworkDNSConfig
    id: str
    name: str
    features: Optional[NetworkFeatures] = None
    type: Optional[str] = None
    subscriber_config: Optional[NetworkSubscriberConfig] = None
