import unittest
from .kiwi import *

def test():
	with open('data.txt', 'r') as myfile:
		output=Search_flights(myfile).compute()
		assert "PV511,PV967,PV731" in output
		assert "PV511,PV967" in output
		assert "PV967,PV731" in output
		assert "PV719,PV493" not in output
