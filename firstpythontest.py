from fuel import convert
from fuel import gauge
import pytest

def test_convert_mid():
    assert convert("30/40") == 75
    assert convert("1/5") == 20
    assert convert("5/7") == 71

def test_convert_ext():
    assert convert("99/100") == 99
    assert convert("0/100") == 0


def test_gauge_lett():
    assert gauge(99) == "F"
    assert gauge(1) == "E"

def test_gaug_numb():
    assert gauge(25) == "25%"
    assert gauge(50) == "50%"

def test_convert_exp():
    with pytest.raises(ValueError):
        convert("Eggs/Bacon")
    with pytest.raises(ZeroDivisionError):
        convert("1/0")
    