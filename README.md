# grandine-py

Python bindings for [Grandine](https://github.com/grandinetech/grandine) SSZ (Simple Serialize) types.

## Overview

This package provides Python bindings for SSZ serialization/deserialization of Ethereum consensus layer types using the Grandine consensus client library. It uses [PyO3](https://github.com/PyO3/pyo3) to expose Rust SSZ functionality to Python.

## Supported Presets

- **Mainnet** - Ethereum mainnet configuration
- **Minimal** - Minimal preset for testing
- **Gnosis** - Gnosis Chain configuration

## Installation

Requires Python 3.12+ and Rust toolchain.

```bash
pip install maturin
maturin develop
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
