#Richard Janssen <richardnjanssen@gmail.com>
#22/07/2023
#CS50 Introduction to Programming with Python
#Unit tests
#This is a unit test for fuel.py program
#Make sure to have pytest framework installed (pip install pytest)
#-------------------------------------------------

from fuel import convert
from fuel import gauge
import pytest

def test_convert():
    assert convert("2/3") == 67
    assert convert("1/4") == 25
    with pytest.raises(ZeroDivisionError):
        convert("1/0")
    with pytest.raises(ValueError):
        convert("2/1")
    with pytest.raises(ValueError):
        convert("2.5/3.5")
    with pytest.raises(ValueError):
        convert("2.5/3")

def test_gauge():
    assert gauge(1) == "E"
    assert gauge(99) == "F"
    assert gauge(100) == "F"
    assert gauge(0) == "E"
    assert gauge(67) == "67%"