# Copyright 2022 Guillaume Belanger
# See LICENSE file for licensing details.

from typing import Optional

from pydantic import BaseModel


class ConfigInfo(BaseModel):
    mconfig_created_at: Optional[int] = None
