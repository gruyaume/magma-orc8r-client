# Copyright 2022 Guillaume Belanger
# See LICENSE file for licensing details.

from pydantic import BaseModel


class eNodeBState(BaseModel):  # noqa: N801
    enodeb_configured: bool
    enodeb_connected: bool
    fsm_state: str
    gps_connected: bool
    gps_latitude: str
    gps_longitude: str
    ip_address: str
    mme_connected: bool
    opstate_enabled: bool
    ptp_connected: bool
    reporting_gateway_id: str
    rf_tx_desired: bool
    rf_tx_on: bool
    time_reported: int
    ues_connected: int
