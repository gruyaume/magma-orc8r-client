# Copyright 2022 Guillaume Belanger
# See LICENSE file for licensing details.

from typing import List, Optional

from pydantic import BaseModel


class DNSConfigRecord(BaseModel):
    a_record: Optional[List[str]] = None
    aaaa_record: Optional[List[str]] = None
    cname_record: Optional[List[str]] = None
    domain: str
