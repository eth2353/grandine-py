# grandine-py

Python bindings for [Grandine](https://github.com/grandinetech/grandine) SSZ (Simple Serialize) types.

## Overview

This package provides Python bindings for SSZ serialization/deserialization of Ethereum consensus layer types using the Grandine consensus client library. It uses [PyO3](https://github.com/PyO3/pyo3) to expose Rust SSZ functionality to Python.

## Supported Presets

- [Mainnet](https://github.com/ethereum/consensus-specs/tree/master/presets/mainnet) - Ethereum mainnet, Hoodi testnet
- [Gnosis](https://github.com/gnosischain/specs/tree/master/consensus/preset/gnosis) - Gnosis Chain, Chiado testnet
- [Minimal](https://github.com/ethereum/consensus-specs/tree/master/presets/minimal) - devnets

## Installation

### Development

```bash
uvx maturin develop
```

### Other projects

```bash
uv add git+https://github.com/eth2353/grandine-py --rev v0.1.0
```

## Usage

```python
from grandine_py import (
    ElectraBeaconBlockContentsMainnet,
    ElectraSignedBeaconBlockMainnet,
)

# Decode from SSZ bytes
block = ElectraSignedBeaconBlockMainnet.from_ssz(ssz_bytes)

# Encode to SSZ bytes
ssz_bytes = block.to_ssz()

# Sign a block
signed_block = block.sign(signature_hex)
```

## Testing

Run the test suite using `uv`:

```bash
uv run pytest
```

For verbose output with test names:

```bash
uv run pytest -v
```
