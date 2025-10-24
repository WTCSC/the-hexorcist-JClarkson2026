from main import to_decimal, from_decimal
import pytest

def test_to_decimal_binary_to_decimal():
    """Convert binary '1010' (base 2) to decimal 10."""
    assert to_decimal("1010", 2) == 10


def test_to_decimal_hexadecimal_to_decimal():
    """Convert hexadecimal 'A' (base 16) to decimal 10."""
    assert to_decimal("A", 16) == 10


def test_to_decimal_base36_to_decimal():
    """Convert base-36 'Z' to decimal 35."""
    assert to_decimal("Z", 36) == 35


def test_to_decimal_zero_in_base10():
    """Convert '0' (base 10) to decimal 0."""
    assert to_decimal("0", 10) == 0


def test_to_decimal_regular_number_in_base10():
    """Convert '123' (base 10) to decimal 123."""
    assert to_decimal("123", 10) == 123

def test_from_decimal_to_binary():
    """Convert decimal 10 to binary '1010'."""
    assert from_decimal(10, 2) == "1010"


def test_from_decimal_to_hexadecimal():
    """Convert decimal 10 to hexadecimal 'A'."""
    assert from_decimal(10, 16) == "A"


def test_from_decimal_to_base36():
    """Convert decimal 35 to base-36 'Z'."""
    assert from_decimal(35, 36) == "Z"


def test_from_decimal_zero_in_base10():
    """Convert decimal 0 to base-10 string '0'."""
    assert from_decimal(0, 10) == "0"


def test_from_decimal_regular_number_in_base10():
    """Convert decimal 123 to base-10 string '123'."""
    assert from_decimal(123, 10) == "123"