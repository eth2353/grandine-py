"""Tests for Minimal preset types."""

import pytest

from grandine_py import (
    ElectraSignedBeaconBlockMinimal,
    ElectraBeaconBlockContentsMinimal,
    ElectraSignedBeaconBlockContentsMinimal,
    ElectraBlindedBeaconBlockMinimal,
    ElectraSignedBlindedBeaconBlockMinimal,
)


class TestMinimalTypesExist:
    """Tests that Minimal preset types exist and have expected methods."""

    def test_signed_beacon_block_has_from_ssz(self) -> None:
        """Test ElectraSignedBeaconBlockMinimal has from_ssz method."""
        assert hasattr(ElectraSignedBeaconBlockMinimal, 'from_ssz')
        assert callable(ElectraSignedBeaconBlockMinimal.from_ssz)

    def test_signed_beacon_block_has_to_ssz(self) -> None:
        """Test ElectraSignedBeaconBlockMinimal instances have to_ssz method."""
        # We can't easily create an instance without valid SSZ data
        # but we can verify the class structure
        assert hasattr(ElectraSignedBeaconBlockMinimal, 'to_ssz')

    def test_signed_beacon_block_has_from_json(self) -> None:
        """Test ElectraSignedBeaconBlockMinimal has from_json method."""
        assert hasattr(ElectraSignedBeaconBlockMinimal, 'from_json')

    def test_signed_beacon_block_has_to_json(self) -> None:
        """Test ElectraSignedBeaconBlockMinimal instances have to_json method."""
        assert hasattr(ElectraSignedBeaconBlockMinimal, 'to_json')


class TestBeaconBlockContentsMinimal:
    """Tests for ElectraBeaconBlockContentsMinimal."""

    def test_has_header_dict_method(self) -> None:
        """Test that the type has header_dict method."""
        assert hasattr(ElectraBeaconBlockContentsMinimal, 'header_dict')

    def test_has_sign_method(self) -> None:
        """Test that the type has sign method."""
        assert hasattr(ElectraBeaconBlockContentsMinimal, 'sign')

    def test_has_block_hash_tree_root_method(self) -> None:
        """Test that the type has block_hash_tree_root method."""
        assert hasattr(ElectraBeaconBlockContentsMinimal, 'block_hash_tree_root')


class TestBlindedBeaconBlockMinimal:
    """Tests for ElectraBlindedBeaconBlockMinimal."""

    def test_has_header_dict_method(self) -> None:
        """Test that the type has header_dict method."""
        assert hasattr(ElectraBlindedBeaconBlockMinimal, 'header_dict')

    def test_has_sign_method(self) -> None:
        """Test that the type has sign method."""
        assert hasattr(ElectraBlindedBeaconBlockMinimal, 'sign')

    def test_has_block_hash_tree_root_method(self) -> None:
        """Test that the type has block_hash_tree_root method."""
        assert hasattr(ElectraBlindedBeaconBlockMinimal, 'block_hash_tree_root')
