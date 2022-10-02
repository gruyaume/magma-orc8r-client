# Copyright 2022 Guillaume Belanger
# See LICENSE file for licensing details.

from pydantic import BaseModel
from schemas.challenge_key import ChallengeKey


class GatewayDevice(BaseModel):
    hardware_id: str
    key: ChallengeKey
