import csv,sys
from pprint import pprint

class Node(object):
		"""Node for BFS, time and place"""
		def __init__(self, code, time):
			self.code = code
			self.time = time
				
class Search_flights(object):
	"""Time and place of traveler"""
	def __init__(self,csv_data):
		reader = csv.reader(csv_data)
		headers = reader.next()
		column = {h:[] for h in headers}
		for row in reader:
			for h, v in zip(headers, row):
				column[h].append(v)
		pprint(column)    # Pretty printer
		
	def compute():
		pass

	def bfs( start, history):
		"""recursive BFS with checking for time and duplicates"""
		for nxt in next_node(start):
			break

with open('data.txt', 'r') as myfile:
	s = Search_flights(myfile)
#	s.compute()


#Search_flights(sys.stdin.read()).compute()

