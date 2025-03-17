import pytest
from unitconvert.length import inches_to_cm, cm_to_inches

def test_inches_to_cm():
    assert inches_to_cm(1) == 2.54
    assert inches_to_cm(10) == 25.4

def test_cm_to_inches():
    assert cm_to_inches(2.54) == 1
    assert cm_to_inches(25.4) == 10
