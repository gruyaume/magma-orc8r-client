# Copyright 2022 Guillaume Belanger
# See LICENSE file for licensing details.

from typing import Dict

from pydantic import BaseModel


class NetworkFeatures(BaseModel):
    features: Dict[str, str]
