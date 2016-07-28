import unittest
from .kiwi import *

def test():
    assert "PV511,PV967,PV731" in SearchFlight("data.txt")
    assert "PV511,PV967" in SearchFlight("data.txt")
    assert "PV967,PV731" in SearchFlight("data.txt")
