# Copyright 2022 Guillaume Belanger
# See LICENSE file for licensing details.

from enum import Enum
from typing import Optional

from pydantic import BaseModel


class HEEncodingType(Enum):
    base64 = "BASE64"
    hex2bin = "HEX2BIN"


class HEHashFunction(Enum):
    md5 = "MD5"
    hex = "HEX"
    sha256 = "SHA256"


class GatewayHEConfig(BaseModel):
    enable_encryption: bool
    enable_header_enrichment: bool
    encryption_key: Optional[str] = None
    he_encoding_type: HEEncodingType
    he_hash_function: HEHashFunction
    hmac_key: Optional[str] = None
