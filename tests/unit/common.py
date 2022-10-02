# Copyright 2022 Guillaume Belanger
# See LICENSE file for licensing details.

from typing import List, Union


class MockContextManager:
    def __init__(self, cert_dir: str = "whatever"):
        self.cert_dir = cert_dir

    def __enter__(self):
        return self.cert_dir

    def __exit__(self, *args):
        pass


class MockRequest:
    def __init__(self, return_json: Union[dict, List] = None):
        self.return_json = return_json

    def raise_for_status(self):
        pass

    def json(self):
        return self.return_json
