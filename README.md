# magma-orc8r-client

## Installation

```bash
pip3 install magma-orc8r-client
```

## Usage

### Leveraging built-in methods

```python
from magma_orc8r_client.orchestrator import Orc8r
from magma_orc8r_client.schemas.network_dns_config import NetworkDNSConfig
from magma_orc8r_client.schemas.network_epc_configs import NetworkEPCConfigs
from magma_orc8r_client.schemas.network_cellular_configs import NetworkCellularConfigs
from magma_orc8r_client.schemas.lte_network import LTENetwork
from magma_orc8r_client.schemas.network_ran_configs import NetworkRANConfigs, TDDConfig

orc8r_client = Orc8r(
    url="https://api.magma.com",
    admin_operator_pfx_path="/path/to/admin_operator.pfx",
    admin_operator_pfx_password="my_pfx_password",
)
network_id = "my_new_networkid"
new_network = LTENetwork(
    dns=NetworkDNSConfig(dhcp_server_enabled=True, enable_caching=True, local_ttl=0),
    cellular=NetworkCellularConfigs(
        epc=NetworkEPCConfigs(
            gx_gy_relay_enabled=True,
            hss_relay_enabled=False,
            lte_auth_amf="gAA=",
            lte_auth_op="EREREREREREREREREREREQ==",
            mcc="001",
            mnc="01",
            tac=1,
        ),
        ran=NetworkRANConfigs(
            bandwidth_mhz=20,
            tdd_config=TDDConfig(
                earfcndl=44590,
                special_subframe_pattern=7,
                subframe_assignment=2,
            ),
        ),
    ),
    description=network_id,
    id=network_id,
    name=network_id,
)

orc8r_client.lte.create_network(lte_network=new_network)

list_of_networks = orc8r_client.lte.list()
```

### Custom calls

```python
from magma_orc8r_client.orchestrator import Orc8r

orc8r_client = Orc8r(
    url="https://api.magma.com",
    admin_operator_pfx_path="/path/to/admin_operator.pfx",
    admin_operator_pfx_password="my_pfx_password",
)
network_id = "pizza"
apn_list = orc8r_client.get(endpoint=f"lte/{network_id}/apns")
```
