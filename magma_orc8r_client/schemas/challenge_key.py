# Copyright 2022 Guillaume Belanger
# See LICENSE file for licensing details.


from typing import Optional

from pydantic import BaseModel


class ChallengeKey(BaseModel):
    key: Optional[str] = None
    key_type: str
