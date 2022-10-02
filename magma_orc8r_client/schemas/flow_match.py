# Copyright 2022 Guillaume Belanger
# See LICENSE file for licensing details.

from enum import Enum
from typing import Optional

from pydantic import BaseModel
from schemas.ip_address import IPAddress


class Direction(Enum):
    uplink = "UPLINK"
    downlink = "DOWNLINK"


class IPProto(Enum):
    ip_proto_ip = "IPPROTO_IP"
    ip_proto_tcp = "IPPROTO_TCP"
    ip_proto_udp = "IPPROTO_UDP"
    ip_proto_icmp = "IPPROTO_UDP"


class FlowMatch(BaseModel):
    direction: Direction
    ip_dst: Optional[IPAddress] = None
    ip_proto: IPProto
    ip_src: Optional[IPAddress] = None
    ipv4_dst: Optional[str] = None
    ipv4_src: Optional[str] = None
    tcp_dst: Optional[int] = None
    tcp_src: Optional[int] = None
    udp_dst: Optional[int] = None
    udp_scr: Optional[int] = None
