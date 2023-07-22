#Richard Janssen <richardnjanssen@gmail.com>
#22/07/2023
#CS50 Introduction to Programming with Python
#Unit tests
#This is a unit test for twttr program
#Make sure to have pytest framework installed (pip install pytest)
#-------------------------------------------------
from twttr import shorten

def test_uppercase():
    assert shorten("GOOD MORNING") == "GD MRNNG"
    assert shorten("HELLO WORLD") == "HLL WRLD"
    assert shorten("THIS IS A TEST") == "THS S TST"

def test_lowercase():
    assert shorten("good afternoon") == "gd ftrnn"
    assert shorten("hello everybody") == "hll vrybdy"
    assert shorten("this is a test") == "ths s tst"

def test_num():
    assert shorten("TH1S 1S 4 C0D3") == "TH1S 1S 4 C0D3"
    assert shorten("L0V3") == "L0V3"
    assert shorten("1 4M R1CH4RD") == "1 4M R1CH4RD"

def test_puntuation():
    assert shorten("Hello, world") == "Hll, wrld"
    assert shorten("What's up?") == "Wht's p?"