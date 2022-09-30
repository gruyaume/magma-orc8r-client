# Copyright 2022 Guillaume Belanger
# See LICENSE file for licensing details.

from typing import List, Optional

from pydantic import BaseModel
from schemas.base_name import BaseName
from schemas.rule_names import RuleNames
from schemas.subscriber_id import SubscriberID


class BaseNameRecord(BaseModel):
    assigned_subscribers: Optional[List[SubscriberID]] = None
    name: BaseName
    rule_names: RuleNames
