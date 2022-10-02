# Copyright 2022 Guillaume Belanger
# See LICENSE file for licensing details.

from typing import Optional

from pydantic import BaseModel


class Package(BaseModel):
    name: Optional[str] = None
    version: Optional[str] = None
