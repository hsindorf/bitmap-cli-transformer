"""Tests for ensuring valid input and output."""

from .bitmap import Bitmap
import pytest
import os


@pytest.fixture
def input_image():
    input_image = Bitmap.read_file('bmp.bmp')
    return input_image


def test_read_file_file_not_found():
    """Tests invalid file input."""
    actual = 'thklwlht'
    with pytest.raises(FileNotFoundError):
        Bitmap.read_file(actual)


def test_read_file_no_filename():
    """Test for blank filename"""
    with pytest.raises(ValueError):
        Bitmap.read_file('')


def test_read_file(input_image):
    """Test that the file can be read."""
    assert Bitmap.read_file('bmp.bmp') is not None


def test_write_file_type_error(input_image):
    """Tests for invalid argument(s)."""
    with pytest.raises(TypeError):
        input_image.write_file([1, 2, 3])


def test_write_file_blank_filename(input_image):
    """Tests for no name"""
    with pytest.raises(ValueError):
        input_image.write_file('')


# tint color method


def test_tint_color_red_file_change(input_image):
    """Tests that the file changes when using the tint color method"""
    input_image.tint_color('red')
    input_image.write_file('test_red.bmp')
    output_image = Bitmap.read_file('test_red.bmp')
    input_image = Bitmap.read_file('bmp.bmp')
    assert output_image.source != input_image.source
    os.remove('test_red.bmp')


def test_tint_color_green_file_change(input_image):
    """Tests that the file changes when using the tint color method"""
    input_image.tint_color('green')
    input_image.write_file('test_green.bmp')
    output_image = Bitmap.read_file('test_green.bmp')
    input_image = Bitmap.read_file('bmp.bmp')
    assert output_image.source != input_image.source
    os.remove('test_green.bmp')


def test_tint_color_blue_file_change(input_image):
    """Tests that the file changes when using the tint color method"""
    input_image.tint_color('blue')
    input_image.write_file('test_blue.bmp')
    output_image = Bitmap.read_file('test_blue.bmp')
    input_image = Bitmap.read_file('bmp.bmp')
    assert output_image.source != input_image.source
    os.remove('test_blue.bmp')


# lighten_darken method


def test_lighten_darken_light_file_change(input_image):
    """Tests that the file changes when using the lighten/darken method"""
    input_image.lighten_darken('light')
    input_image.write_file('test_light.bmp')
    output_image = Bitmap.read_file('test_light.bmp')
    input_image = Bitmap.read_file('bmp.bmp')
    assert output_image.source != input_image.source
    os.remove('test_light.bmp')


def test_lighten_darken_dark_file_change(input_image):
    """Tests that the file changes when using the lighten/darken method"""
    input_image.lighten_darken('dark')
    input_image.write_file('test_dark.bmp')
    output_image = Bitmap.read_file('test_dark.bmp')
    input_image = Bitmap.read_file('bmp.bmp')
    assert output_image.source != input_image.source
    os.remove('test_dark.bmp')


# invert method


def test_invert_file_change(input_image):
    """Tests that the file changes when using the tint color method"""
    input_image.invert()
    input_image.write_file('test_invert.bmp')
    output_image = Bitmap.read_file('test_invert.bmp')
    input_image = Bitmap.read_file('bmp.bmp')
    assert output_image.source != input_image.source
    os.remove('test_invert.bmp')


# the cave method


def test_the_cave_change(input_image):
    """Tests that the file changes when using the cave method"""
    input_image.the_cave()
    input_image.write_file('test_the_cave.bmp')
    output_image = Bitmap.read_file('test_the_cave.bmp')
    input_image = Bitmap.read_file('bmp.bmp')
    assert output_image.source != input_image.source
    os.remove('test_the_cave.bmp')
