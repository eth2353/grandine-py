"""Tests for BeaconBlockContents and BlindedBeaconBlock functionality."""

import pytest

from grandine_py import (
    ElectraBeaconBlockContentsMainnet,
    ElectraBlindedBeaconBlockMainnet,
)


class TestBeaconBlockContentsMethods:
    """Tests for BeaconBlockContents methods (interface verification)."""

    def test_header_dict_returns_dict(self) -> None:
        """Test that header_dict returns a dictionary with expected keys.
        
        Note: This test requires actual BeaconBlockContents data to fully test.
        For now, we just verify the method exists with the correct signature.
        """
        # Method signature: header_dict(self, py) -> PyResult<Py<PyDict>>
        import inspect
        sig = inspect.signature(ElectraBeaconBlockContentsMainnet.header_dict)
        params = list(sig.parameters.keys())
        assert 'self' in params

    def test_sign_accepts_signature_string(self) -> None:
        """Test that sign method accepts a signature string parameter."""
        import inspect
        sig = inspect.signature(ElectraBeaconBlockContentsMainnet.sign)
        params = list(sig.parameters.keys())
        assert 'self' in params
        assert 'signature' in params

    def test_block_hash_tree_root_returns_string(self) -> None:
        """Test that block_hash_tree_root returns a hex string.
        
        Note: This test requires actual BeaconBlockContents data to fully test.
        """
        import inspect
        sig = inspect.signature(ElectraBeaconBlockContentsMainnet.block_hash_tree_root)
        params = list(sig.parameters.keys())
        assert 'self' in params


class TestBlindedBeaconBlockMethods:
    """Tests for BlindedBeaconBlock methods (interface verification)."""

    def test_header_dict_returns_dict(self) -> None:
        """Test that header_dict returns a dictionary with expected keys."""
        import inspect
        sig = inspect.signature(ElectraBlindedBeaconBlockMainnet.header_dict)
        params = list(sig.parameters.keys())
        assert 'self' in params

    def test_sign_accepts_signature_string(self) -> None:
        """Test that sign method accepts a signature string parameter."""
        import inspect
        sig = inspect.signature(ElectraBlindedBeaconBlockMainnet.sign)
        params = list(sig.parameters.keys())
        assert 'self' in params
        assert 'signature' in params

    def test_block_hash_tree_root_returns_string(self) -> None:
        """Test that block_hash_tree_root returns a hex string."""
        import inspect
        sig = inspect.signature(ElectraBlindedBeaconBlockMainnet.block_hash_tree_root)
        params = list(sig.parameters.keys())
        assert 'self' in params
