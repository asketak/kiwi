import csv,sys,time
from pprint import pprint

def diffdates(d1, d2):
    return (time.mktime(time.strptime(d2,"%Y-%m-%dT%H:%M:%S")) -
               time.mktime(time.strptime(d1, "%Y-%m-%dT%H:%M:%S")))

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
		""" Returns all flights, that can be attented"""
		ret = []

		for x in xrange(0,len(self.column["source"])):
			if (self.column["destination"][previous_flight] == self.column["source"][x]
			and diffdates(self.column["arrival"][previous_flight], self.column["departure"][x]) < 3600*4  
			and diffdates(self.column["arrival"][previous_flight], self.column["departure"][x]) > 3600)  :
				ret.append(x);
		return ret

		
	def bfs(self, previous_flight, history):
		"""recursive BFS with checking for time and duplicates"""
		history.append(previous_flight)
		nodes = self.next_node(previous_flight,history)
		if len(nodes) > 0:
			for nxt in nodes:
				self.bfs(nxt,history[:])
		if len(history)>1:
			print(",".join([ self.column["flight_number"][x] for x in history]))

	def compute(self):
		for x in xrange(0,len(self.column["source"])):
			self.bfs(x,[])

with open('data.txt', 'r') as myfile:
	s = Search_flights(myfile)
	s.compute()


#Search_flights(sys.stdin.read()).compute()

