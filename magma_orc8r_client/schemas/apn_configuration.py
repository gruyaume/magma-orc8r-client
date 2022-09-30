# Copyright 2022 Guillaume Belanger
# See LICENSE file for licensing details.

from pydantic import BaseModel
from schemas.aggregated_maximum_bitrate import AggregatedMaximumBitrate
from schemas.qos_profile import QOSProfile


class APNConfiguration(BaseModel):
    ambr: AggregatedMaximumBitrate
    qos_profile: QOSProfile
