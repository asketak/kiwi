import unittest

def test(capsys):
	from .kiwi import *
	output, err = capsys.readouterr()
	assert "PV511,PV967,PV731" in output
	assert "PV511,PV967" in output
	assert "PV967,PV731" in output
	assert "PV719,PV493" in output
	assert "PV980,PV493,PV476" in output
	assert "PV980,PV493,PV310" in output

