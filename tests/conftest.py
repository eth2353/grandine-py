"""Pytest fixtures for grandine-py tests."""

import json
import pytest
from pathlib import Path


@pytest.fixture(scope="session")
def fixtures_dir() -> Path:
    """Return the path to the test fixtures directory."""
    return Path(__file__).parent / "fixtures"


@pytest.fixture(scope="session")
def mainnet_block_ssz(fixtures_dir: Path) -> bytes:
    """Return the SSZ-encoded Mainnet block."""
    return (fixtures_dir / "13689000.ssz").read_bytes()


@pytest.fixture(scope="session")
def mainnet_block_json(fixtures_dir: Path) -> bytes:
    """Return the JSON-encoded Mainnet block."""
    return (fixtures_dir / "13689000.json").read_bytes()


@pytest.fixture(scope="session")
def mainnet_block_json_dict(fixtures_dir: Path) -> dict:
    """Return the JSON Mainnet block as a Python dict."""
    return json.loads((fixtures_dir / "13689000.json").read_text())


@pytest.fixture
def sample_bls_signature() -> str:
    """Return a sample BLS signature for testing."""
    return (
        "0xa1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4e5f6"
        "a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4e5f6"
        "a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4e5f6"
    )
