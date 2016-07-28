import unittest
from .kiwi import *

def test():
	with open('data.txt', 'r') as myfile:
		output=SearchFlight(data).compute()
		assert "PV511,PV967,PV731" in output
		assert "PV511,PV967" in output
		assert "PV967,PV731" in output
