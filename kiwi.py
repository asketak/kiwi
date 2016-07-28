import csv,sys
from pprint import pprint

def diffdates(d1, d2):
    #Date format: %Y-%m-%d %H:%M:%S
    return (time.mktime(time.strptime(d2,"%Y-%m-%d %H:%M:%S")) -
               time.mktime(time.strptime(d1, "%Y-%m-%d %H:%M:%S")))

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
		pprint(self.column)
		print "====================="

	def next_node(self,previous_flight,hist):
		""" Returns all flights, that can be attented"""
		ret = []

		if len(hist) > 5:
			return ret
		for x in xrange(0,len(self.column["source"])):
			if (self.column["destination"][previous_flight] == self.column["source"][x]):

	 #and self.column["arrival"][previous_flight] <= self.column["departure"][x]) :
				ret.append(x);
		print "ret-next node"
		pprint(ret)
		return ret

		
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
			self.bfs(x,[])

with open('data.txt', 'r') as myfile:
	s = Search_flights(myfile)
	s.compute()


#Search_flights(sys.stdin.read()).compute()

