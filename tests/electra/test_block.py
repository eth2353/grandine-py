import json
from pathlib import Path
from typing import TYPE_CHECKING

import pytest

from grandine_py import ElectraSignedBeaconBlockMainnet
from grandine_py.grandine_py import ElectraSignedBeaconBlockGnosis


@pytest.mark.parametrize(
    ("block_cls", "path_to_ssz"),
    [
        pytest.param(
            ElectraSignedBeaconBlockMainnet,
            Path(__file__).parent / "fixtures/mainnet-13689000.ssz",
        ),
        pytest.param(
            ElectraSignedBeaconBlockGnosis,
            Path(__file__).parent / "fixtures/gnosis-26539000.ssz",
        ),
    ]
)
def test_ssz(block_cls: ElectraSignedBeaconBlockMainnet | ElectraSignedBeaconBlockGnosis, path_to_ssz: Path) -> None:
    with open(path_to_ssz, "rb") as f:
        encoded = f.read()
        decoded = block_cls.from_ssz(encoded)
        assert decoded.to_ssz() == encoded


@pytest.mark.parametrize(
    ("block_cls", "path_to_json"),
    [
        pytest.param(
            ElectraSignedBeaconBlockMainnet,
            Path(__file__).parent / "fixtures/mainnet-13689000.json",
        ),
        pytest.param(
            ElectraSignedBeaconBlockGnosis,
            Path(__file__).parent / "fixtures/gnosis-26539000.json",
        ),
    ]
)
def test_json(block_cls: ElectraSignedBeaconBlockMainnet | ElectraSignedBeaconBlockGnosis, path_to_json: Path) -> None:
    with open(path_to_json, "rb") as f:
        encoded = f.read()
        decoded = block_cls.from_json(encoded)
        re_encoded = decoded.to_json()
        assert json.loads(encoded.decode())["data"] == json.loads(re_encoded.decode())
