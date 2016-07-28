import csv,sys
from pprint import pprint

class Search_flights(object):
	"""Main class for searching in flights"""

	column = None
	output = None

	def __init__(self,csv_data):
		reader = csv.reader(csv_data)
		headers = reader.next()
		self.column = {h:[] for h in headers}
		for row in reader:
			for h, v in zip(headers, row):
				self.column[h].append(v)

	def next_node(self,previous_flight,hist):
		if len(hist) > 2:
			return []
		return [3,5,2]
#		for x in xrange(1,len(self.column)):

		
	def bfs(self, previous_flight, history):
		"""recursive BFS with checking for time and duplicates"""
		print("called with ", previous_flight , history)
		history.append(previous_flight)
		nodes = self.next_node(previous_flight,history)
		if len(nodes) > 0:
			for nxt in nodes:
				self.bfs(nxt,history[:])

	def compute(self):
		for x in xrange(1,len(self.column["source"])):
			print "incompute"
			history = []
			self.bfs(x,history)

with open('data.txt', 'r') as myfile:
	s = Search_flights(myfile)
	s.compute()


#Search_flights(sys.stdin.read()).compute()

