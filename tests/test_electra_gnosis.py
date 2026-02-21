"""Tests for Gnosis preset types."""

import pytest

from grandine_py import (
    ElectraSignedBeaconBlockGnosis,
    ElectraBeaconBlockContentsGnosis,
    ElectraSignedBeaconBlockContentsGnosis,
    ElectraBlindedBeaconBlockGnosis,
    ElectraSignedBlindedBeaconBlockGnosis,
)


class TestGnosisTypesExist:
    """Tests that Gnosis preset types exist and have expected methods."""

    def test_signed_beacon_block_has_from_ssz(self) -> None:
        """Test ElectraSignedBeaconBlockGnosis has from_ssz method."""
        assert hasattr(ElectraSignedBeaconBlockGnosis, 'from_ssz')
        assert callable(ElectraSignedBeaconBlockGnosis.from_ssz)

    def test_signed_beacon_block_has_to_ssz(self) -> None:
        """Test ElectraSignedBeaconBlockGnosis instances have to_ssz method."""
        assert hasattr(ElectraSignedBeaconBlockGnosis, 'to_ssz')

    def test_signed_beacon_block_has_from_json(self) -> None:
        """Test ElectraSignedBeaconBlockGnosis has from_json method."""
        assert hasattr(ElectraSignedBeaconBlockGnosis, 'from_json')

    def test_signed_beacon_block_has_to_json(self) -> None:
        """Test ElectraSignedBeaconBlockGnosis instances have to_json method."""
        assert hasattr(ElectraSignedBeaconBlockGnosis, 'to_json')


class TestBeaconBlockContentsGnosis:
    """Tests for ElectraBeaconBlockContentsGnosis."""

    def test_has_header_dict_method(self) -> None:
        """Test that the type has header_dict method."""
        assert hasattr(ElectraBeaconBlockContentsGnosis, 'header_dict')

    def test_has_sign_method(self) -> None:
        """Test that the type has sign method."""
        assert hasattr(ElectraBeaconBlockContentsGnosis, 'sign')

    def test_has_block_hash_tree_root_method(self) -> None:
        """Test that the type has block_hash_tree_root method."""
        assert hasattr(ElectraBeaconBlockContentsGnosis, 'block_hash_tree_root')


class TestBlindedBeaconBlockGnosis:
    """Tests for ElectraBlindedBeaconBlockGnosis."""

    def test_has_header_dict_method(self) -> None:
        """Test that the type has header_dict method."""
        assert hasattr(ElectraBlindedBeaconBlockGnosis, 'header_dict')

    def test_has_sign_method(self) -> None:
        """Test that the type has sign method."""
        assert hasattr(ElectraBlindedBeaconBlockGnosis, 'sign')

    def test_has_block_hash_tree_root_method(self) -> None:
        """Test that the type has block_hash_tree_root method."""
        assert hasattr(ElectraBlindedBeaconBlockGnosis, 'block_hash_tree_root')
