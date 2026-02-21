"""Integration tests for grandine-py Mainnet preset types."""

import json
import pytest

from grandine_py import (
    ElectraSignedBeaconBlockMainnet,
)


class TestElectraSignedBeaconBlockMainnet:
    """Tests for ElectraSignedBeaconBlockMainnet SSZ and JSON serialization."""

    def test_from_ssz_decodes_correctly(self, mainnet_block_ssz: bytes) -> None:
        """Test that SSZ bytes can be decoded into a block object."""
        block = ElectraSignedBeaconBlockMainnet.from_ssz(mainnet_block_ssz)
        assert block is not None

    def test_from_ssz_roundtrip(self, mainnet_block_ssz: bytes) -> None:
        """Test SSZ decoding and re-encoding produces identical bytes."""
        block = ElectraSignedBeaconBlockMainnet.from_ssz(mainnet_block_ssz)
        re_encoded = block.to_ssz()
        assert re_encoded == mainnet_block_ssz

    def test_to_ssz_returns_bytes(self, mainnet_block_ssz: bytes) -> None:
        """Test that to_ssz returns bytes."""
        block = ElectraSignedBeaconBlockMainnet.from_ssz(mainnet_block_ssz)
        result = block.to_ssz()
        assert isinstance(result, bytes)
        assert len(result) > 0


class TestElectraSignedBeaconBlockMainnetJSON:
    """Tests for ElectraSignedBeaconBlockMainnet JSON serialization."""

    def test_from_json_decodes_correctly(
        self,
        mainnet_block_json: bytes,
        mainnet_block_json_dict: dict,
    ) -> None:
        """Test that JSON with 'data' wrapper can be decoded."""
        # The JSON fixture has format: {"version": ..., "data": {"message": ..., "signature": ...}}
        # Extract just the data portion and wrap it for from_json
        data_only = {"data": mainnet_block_json_dict["data"]}
        json_bytes = json.dumps(data_only).encode()
        
        block = ElectraSignedBeaconBlockMainnet.from_json(json_bytes)
        assert block is not None

    def test_from_json_roundtrip_preserves_data(
        self,
        mainnet_block_json: bytes,
        mainnet_block_json_dict: dict,
    ) -> None:
        """Test JSON decoding and re-encoding preserves the block data."""
        data_only = {"data": mainnet_block_json_dict["data"]}
        json_bytes = json.dumps(data_only).encode()

        block = ElectraSignedBeaconBlockMainnet.from_json(json_bytes)
        re_encoded = block.to_json()

        # Parse and compare the actual block data
        # Note: from_json expects {"data": ...} wrapper, but to_json returns
        # just the block data without the wrapper
        original_data = data_only["data"]
        re_decoded = json.loads(re_encoded)
        assert re_decoded["message"]["slot"] == original_data["message"]["slot"]
        assert re_decoded["message"]["proposer_index"] == original_data["message"]["proposer_index"]

    def test_to_json_returns_bytes(
        self,
        mainnet_block_json: bytes,
        mainnet_block_json_dict: dict,
    ) -> None:
        """Test that to_json returns bytes."""
        data_only = {"data": mainnet_block_json_dict["data"]}
        json_bytes = json.dumps(data_only).encode()
        
        block = ElectraSignedBeaconBlockMainnet.from_json(json_bytes)
        result = block.to_json()
        assert isinstance(result, bytes)
        assert len(result) > 0


class TestErrorHandling:
    """Tests for error handling in grandine-py Mainnet types."""

    def test_from_ssz_with_invalid_bytes_raises_value_error(self) -> None:
        """Test that from_ssz raises ValueError with invalid SSZ bytes."""
        invalid_ssz = b"invalid data that is not valid SSZ"
        with pytest.raises(ValueError):
            ElectraSignedBeaconBlockMainnet.from_ssz(invalid_ssz)

    def test_from_ssz_with_empty_bytes_raises_value_error(self) -> None:
        """Test that from_ssz raises ValueError with empty bytes."""
        with pytest.raises(ValueError):
            ElectraSignedBeaconBlockMainnet.from_ssz(b"")

    def test_from_json_with_invalid_json_raises_value_error(self) -> None:
        """Test that from_json raises ValueError with invalid JSON."""
        invalid_json = b"not valid json"
        with pytest.raises(ValueError):
            ElectraSignedBeaconBlockMainnet.from_json(invalid_json)

    def test_from_json_with_missing_data_key_raises_value_error(self) -> None:
        """Test that from_json raises ValueError with JSON missing 'data' key."""
        wrong_format = b'{"message": {}, "signature": "0x00"}'
        with pytest.raises(ValueError):
            ElectraSignedBeaconBlockMainnet.from_json(wrong_format)

    def test_from_json_with_empty_object_raises_value_error(self) -> None:
        """Test that from_json raises ValueError with empty JSON object."""
        with pytest.raises(ValueError):
            ElectraSignedBeaconBlockMainnet.from_json(b"{}")
