# Copyright 2022 Guillaume Belanger
# See LICENSE file for licensing details.

from typing import Dict, Optional

from pydantic import BaseModel, Field


class EmailReceiver(BaseModel):
    """Warning: schemas shouldn't be instanciated using class attributes.

    Please use dict instead::
    elastic_hit = ElasticHit(
    **{
        "smarthost": "my smarthost name",
        "to": "Bbb",
        "from": "ccc"
    }
    )
    """

    auth_identity: Optional[str] = None
    auth_password: Optional[str] = None
    auth_secret: Optional[str] = None
    auth_username: Optional[str] = None
    from_: str = Field(default=..., alias="from")
    headers: Optional[Dict] = None
    hello: Optional[str] = None
    html: Optional[str] = None
    send_resolved: Optional[bool] = None
    smarthost: str
    text: Optional[str] = None
    to: str
