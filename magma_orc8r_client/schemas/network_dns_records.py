# Copyright 2022 Guillaume Belanger
# See LICENSE file for licensing details.

from typing import List

from schemas.dns_config_record import DNSConfigRecord


class NetworkDNSRecords(List[DNSConfigRecord]):
    pass
