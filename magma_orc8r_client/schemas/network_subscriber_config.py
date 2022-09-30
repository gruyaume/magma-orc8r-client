# Copyright 2022 Guillaume Belanger
# See LICENSE file for licensing details.

from typing import Optional

from pydantic import BaseModel
from schemas.base_names import BaseNames
from schemas.rule_names import RuleNames


class NetworkSubscriberConfig(BaseModel):
    network_wide_base_names: Optional[BaseNames] = None
    network_wide_rule_names: Optional[RuleNames] = None
