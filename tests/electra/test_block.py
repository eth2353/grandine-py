import json
from pathlib import Path

import pytest

from grandine_py import (
    ElectraBeaconBlockContentsMainnet,
    ElectraBlindedBeaconBlockMinimal,
    ElectraSignedBeaconBlockGnosis,
    ElectraSignedBeaconBlockMainnet,
    ElectraSignedBuilderBidMainnet,
    ElectraSignedBuilderBidMinimal,
)


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
    ],
)
def test_ssz(
    block_cls: ElectraSignedBeaconBlockMainnet | ElectraSignedBeaconBlockGnosis,
    path_to_ssz: Path,
) -> None:
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
    ],
)
def test_json(
    block_cls: ElectraSignedBeaconBlockMainnet | ElectraSignedBeaconBlockGnosis,
    path_to_json: Path,
) -> None:
    with open(path_to_json, "rb") as f:
        encoded = f.read()
        decoded = block_cls.from_json(encoded)
        re_encoded = decoded.to_json()
        assert json.loads(encoded.decode())["data"] == json.loads(re_encoded.decode())


def test_replace_execution_payload_with_builder_bid_blinds_block_contents(
    builder_bid_json: dict[str, object],
) -> None:
    with open(Path(__file__).parent / "fixtures/mainnet-13689000.json", "rb") as f:
        signed_block = json.loads(f.read().decode())

    block_contents = ElectraBeaconBlockContentsMainnet.from_json(
        json.dumps(
            {
                "data": {
                    "block": signed_block["data"]["message"],
                    "kzg_proofs": [],
                    "blobs": [],
                }
            }
        ).encode()
    )

    builder_bid = ElectraSignedBuilderBidMainnet.from_json(
        json.dumps({"data": builder_bid_json}).encode()
    )
    blinded_block = block_contents.replace_execution_payload_with_builder_bid(
        builder_bid
    )
    blinded_json = json.loads(blinded_block.to_json().decode())

    assert "execution_payload" not in blinded_json["body"]
    assert (
        blinded_json["body"]["execution_payload_header"]
        == builder_bid_json["data"]["message"]["header"]
    )
    assert (
        blinded_json["body"]["blob_kzg_commitments"]
        == builder_bid_json["data"]["message"]["blob_kzg_commitments"]
    )
    assert (
        blinded_json["body"]["execution_requests"]
        == builder_bid_json["data"]["message"]["execution_requests"]
    )


def test_replace_execution_payload_with_builder_bid_updates_blinded_block(
    builder_bid_json: dict[str, object],
) -> None:
    with open(
        Path(__file__).parent / "fixtures/minimal-signed-blinded-block.json", "rb"
    ) as f:
        signed_blinded_block = json.loads(f.read().decode())

    block = ElectraBlindedBeaconBlockMinimal.from_json(
        json.dumps({"data": signed_blinded_block["data"]["message"]}).encode()
    )
    original_blinded_body = signed_blinded_block["data"]["message"]["body"]

    builder_bid = ElectraSignedBuilderBidMinimal.from_json(
        json.dumps({"data": builder_bid_json}).encode()
    )
    blinded_block = block.replace_execution_payload_with_builder_bid(builder_bid)
    blinded_json = json.loads(blinded_block.to_json().decode())

    assert (
        original_blinded_body["execution_payload_header"]
        != blinded_json["body"]["execution_payload_header"]
    )
    assert (
        blinded_json["body"]["execution_payload_header"]
        == builder_bid_json["data"]["message"]["header"]
    )
    assert (
        original_blinded_body["blob_kzg_commitments"]
        != blinded_json["body"]["blob_kzg_commitments"]
    )
    assert (
        blinded_json["body"]["blob_kzg_commitments"]
        == builder_bid_json["data"]["message"]["blob_kzg_commitments"]
    )
    assert (
        original_blinded_body["execution_requests"]
        != blinded_json["body"]["execution_requests"]
    )
    assert (
        blinded_json["body"]["execution_requests"]
        == builder_bid_json["data"]["message"]["execution_requests"]
    )


def test_replace_execution_payload_with_builder_bid_ssz_and_json_twins_match() -> None:
    with open(Path(__file__).parent / "fixtures/mainnet-13689000.json", "rb") as f:
        signed_block = json.loads(f.read())

    block_contents = ElectraBeaconBlockContentsMainnet.from_json(
        json.dumps(
            {
                "data": {
                    "block": signed_block["data"]["message"],
                    "kzg_proofs": [],
                    "blobs": [],
                }
            }
        ).encode()
    )

    with open(
        Path(__file__).parent / "fixtures/mainnet-signed-builder-bid-slot-14149070.ssz",
        "rb",
    ) as f:
        ssz_builder_bid = ElectraSignedBuilderBidMainnet.from_ssz(f.read())
    with open(
        Path(__file__).parent
        / "fixtures/mainnet-signed-builder-bid-slot-14149070.json",
        "rb",
    ) as f:
        json_builder_bid = ElectraSignedBuilderBidMainnet.from_json(f.read())

    blinded_from_ssz = block_contents.replace_execution_payload_with_builder_bid(
        ssz_builder_bid
    )
    blinded_from_json = block_contents.replace_execution_payload_with_builder_bid(
        json_builder_bid
    )

    assert json.loads(blinded_from_ssz.to_json()) == json.loads(
        blinded_from_json.to_json()
    )
