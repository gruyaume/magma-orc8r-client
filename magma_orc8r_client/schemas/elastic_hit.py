# Copyright 2022 Guillaume Belanger
# See LICENSE file for licensing details.

from typing import Dict, List, Optional

from pydantic import BaseModel


class ElasticHit(BaseModel):
    _id: str
    _index: str
    _primary_term: Optional[str] = None
    _score: Optional[int] = None
    _seq_no: Optional[int] = None
    _sort: Optional[List[int]] = None
    _source: Dict
    _type: str
