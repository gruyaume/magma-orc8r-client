# Copyright 2022 Guillaume Belanger
# See LICENSE file for licensing details.

import logging
from contextlib import contextmanager
from pathlib import Path
from tempfile import NamedTemporaryFile
from typing import Iterator

import requests  # type: ignore[import]
import urllib3  # type: ignore[import]
from cryptography.hazmat.primitives.serialization import (
    Encoding,
    NoEncryption,
    PrivateFormat,
)
from cryptography.hazmat.primitives.serialization.pkcs12 import (
    load_key_and_certificates,
)

urllib3.disable_warnings()

logger = logging.getLogger(__name__)


@contextmanager
def pfx_to_pem(pfx_path: str, pfx_password: str) -> Iterator[str]:
    """Decrypts the .pfx file to be used with requests.

    Args:
        pfx_path: PFX file path
        pfx_password: PFX file password

    Returns:
        str: Temporary pem file path
    """
    pfx_file = Path(pfx_path).read_bytes()
    private_key, certificate, _ = load_key_and_certificates(
        pfx_file, pfx_password.encode("utf-8"), None
    )
    if not private_key or not certificate:
        raise RuntimeError("Could not load pfx package")
    with NamedTemporaryFile(suffix=".pem") as t_pem:
        with open(t_pem.name, "wb") as pem_file:
            pem_file.write(
                private_key.private_bytes(Encoding.PEM, PrivateFormat.PKCS8, NoEncryption())
            )
            pem_file.write(certificate.public_bytes(Encoding.PEM))
        yield t_pem.name


class BaseEndpoint:
    def __init__(
        self,
        base_url: str,
        admin_operator_pfx_path: str,
        admin_operator_pfx_password: str,
        base_endpoint: str = "",
    ):
        self.base_url = base_url
        self.base_endpoint = base_endpoint
        self.admin_operator_pfx_path = admin_operator_pfx_path
        self.admin_operator_pfx_password = admin_operator_pfx_password

    def get(self, endpoint: str = None) -> requests.Response:
        if endpoint and endpoint != "":
            url = f"{self.base_url}{self.base_endpoint}{endpoint}"
        else:
            url = f"{self.base_url}{self.base_endpoint}"
        with pfx_to_pem(self.admin_operator_pfx_path, self.admin_operator_pfx_password) as cert:
            response = requests.get(url=url, cert=cert, verify=False)
            response.raise_for_status()
            return response

    def post(self, data: dict, endpoint: str = None) -> requests.Response:
        if endpoint:
            url = f"{self.base_url}{self.base_endpoint}/{endpoint}"
        else:
            url = f"{self.base_url}{self.base_endpoint}"
        with pfx_to_pem(self.admin_operator_pfx_path, self.admin_operator_pfx_password) as cert:
            response = requests.post(url=url, cert=cert, json=data, verify=False)
            response.raise_for_status()
            return response

    def delete(self, endpoint: str = None) -> requests.Response:
        if endpoint:
            url = f"{self.base_url}{self.base_endpoint}/{endpoint}"
        else:
            url = f"{self.base_url}{self.base_endpoint}"
        with pfx_to_pem(self.admin_operator_pfx_path, self.admin_operator_pfx_password) as cert:
            response = requests.delete(url=url, cert=cert, verify=False)
            try:
                response.raise_for_status()
            except Exception as e:
                logger.info(response.text)
                raise e
            return response
