# Copyright 2022 Guillaume Belanger
# See LICENSE file for licensing details.

from pydantic import BaseModel
from schemas.apn_configuration import APNConfiguration
from schemas.apn_name import APNName


class APN(BaseModel):
    apn_configuration: APNConfiguration
    apn_name: APNName
