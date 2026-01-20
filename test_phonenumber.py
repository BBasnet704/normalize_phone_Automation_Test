from phonenumber import normalize_phone
import pytest


def  test_number_with_10digits():
    assert normalize_phone("9861611666") == "+9779861611666"
    assert normalize_phone("9841380489") == "+9779841380489"

def test_number_start_with_977():
    assert normalize_phone("+9779861611666") == "+9779861611666"
    assert normalize_phone("+9779841380489") == "+9779841380489"

def test_number_starts_with_0():
    assert normalize_phone("09861611666") == "+9779861611666"

def test_numbers_start_with_98or97():
    assert normalize_phone("9861611666") == "+9779861611666"
    assert normalize_phone("9741380489") == "+9779741380489"

def test_remove_spaces_and_dashes():
    assert normalize_phone("98 61 611 666") == "+9779861611666"
    assert normalize_phone("98-61-611-666") == "+9779861611666"

def test_number_less_than_10(): 
    with pytest.raises(ValueError, match= "Invalid phone number"):
     normalize_phone("98746627")
     


def test_with_random_number():
    with pytest.raises(ValueError , match = "Invalid phone number"):
        normalize_phone("8765432123")

def test_with_specialcharacter():
    with pytest.raises(ValueError, match= "Invalid phone number"):
        normalize_phone("9867@123#")

def test_alphanumeric():
    with pytest.raises(ValueError, match= "Invalid phone number"):
        normalize_phone("barsha@123")

def test_blank_field():
    with pytest.raises(ValueError, match= "Invalid phone number"):
        normalize_phone("")

def test_characters():
    with pytest.raises(ValueError,match="Invalid phone number"):
        normalize_phone("abcd")