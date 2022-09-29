# magma-orc8r-client

## Installation

```bash
pip3 install magma-orc8r-client
```

## Usage

```python
from magma_orc8r_client.orchestrator import Orc8r
from magma_orc8r_client.schemas.dns import DNS
from magma_orc8r_client.schemas.epc import EPC
from magma_orc8r_client.schemas.cellular import Cellular
from magma_orc8r_client.schemas.network import Network
from magma_orc8r_client.schemas.ran import RAN
from magma_orc8r_client.schemas.tdd_config import TDDConfig

orc8r_client = Orc8r(
    url="https://api.magma.com",
    admin_operator_pfx_path="/path/to/admin_operator.pfx",
    admin_operator_pfx_password="my_pfx_password",
)
network_id = "my_new_networkid"
new_network = Network(
    dns=DNS(dhcp_server_enabled=True, enable_caching=True, local_ttl=0),
    cellular=Cellular(
        epc=EPC(
            gx_gy_relay_enabled=True,
            hss_relay_enabled=False,
            lte_auth_amf="gAA=",
            lte_auth_op="EREREREREREREREREREREQ==",
            mcc="001",
            mnc="01",
            tac=1,
        ),
        ran=RAN(
            bandwidth_mhz=20,
            tdd_config=TDDConfig(
                earfcndl=44590,
                earfcnul=18000,
                special_subframe_pattern=7,
                subframe_assignment=2,
            ),
        ),
    ),
    description=network_id,
    id=network_id,
    name=network_id,
)

orc8r_client.lte.create(network=new_network)

list_of_networks = orc8r_client.lte.list()
```
