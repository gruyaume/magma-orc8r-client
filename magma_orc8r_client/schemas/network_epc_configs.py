# Copyright 2022 Guillaume Belanger
# See LICENSE file for licensing details.

from typing import Dict, List, Optional

from pydantic import BaseModel
from schemas.imei import IMEI
from schemas.plmn_config import PLMNConfig


class NetworkEPCConfigs(BaseModel):
    cloud_subscriberdb_enabled: Optional[bool] = None
    congestion_control_enabled: Optional[bool] = True
    default_rule_id: Optional[str] = None
    gx_gy_relay_enabled: bool
    hss_relay_enabled: bool
    lte_auth_amf: str
    lte_auth_op: str
    mcc: str
    mnc: str
    mobility: Optional[Dict] = None
    network_services: Optional[List[str]] = None
    restricted_imeis: Optional[List[IMEI]] = None
    restricted_plmns: Optional[List[PLMNConfig]] = None
    service_area_maps: Optional[Dict] = None
    sub_profiles: Optional[Dict] = None
    tac: int
