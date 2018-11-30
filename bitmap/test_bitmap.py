"""Tests for ensuring valid input and output."""

from .bitmap import Bitmap
import pytest


source = 'bmp.bmp'


def test_read_file_file_not_found():
    """Tests invalid file input."""
    actual = 'thklwlht'
    with pytest.raises(FileNotFoundError):
        assert Bitmap.read_file(actual)


def test_read_file():
    """Tests some things."""
    pass
    return


def test_write_file_type_error():
    """Tests for invalid argument(s)."""
    actual = 'jerk'
    with pytest.raises(TypeError):
        assert Bitmap.write_file(actual)


def test_write_file_value_error():
    """Tests for well-formed--but invalid--argument(s)."""
    actual = ''
    with pytest.raises(ValueError):
        assert Bitmap.write_file(source, actual)


def test_write_file_attribute_error():
    """Tests for invalid attribute(s) in input."""
    actual = source
    with pytest.raises(AttributeError):
        assert Bitmap.write_file(source, actual)


