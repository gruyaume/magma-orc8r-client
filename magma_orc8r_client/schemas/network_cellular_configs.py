# Copyright 2022 Guillaume Belanger
# See LICENSE file for licensing details.

from typing import Optional

from pydantic import BaseModel
from schemas.feg_network_id import FEGNetworkID
from schemas.network_epc_configs import NetworkEPCConfigs
from schemas.network_ran_configs import NetworkRANConfigs


class NetworkCellularConfigs(BaseModel):
    epc: NetworkEPCConfigs
    feg_network_id: Optional[FEGNetworkID] = None
    ran: NetworkRANConfigs
