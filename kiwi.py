import csv,sys,time,collections
from pprint import pprint
from collections import defaultdict

def diffdates(d1, d2):
	return (time.mktime(time.strptime(d2,"%Y-%m-%dT%H:%M:%S")) -
			   time.mktime(time.strptime(d1, "%Y-%m-%dT%H:%M:%S")))

class Search_flights(object):
	"""Main class for searching in flights"""

	column = None
	output = None

	def __init__(self,csv_data):
		""" loads csv data """
		reader = csv.reader(csv_data)
		headers = reader.next()
		self.column = {h:[] for h in headers}
		for row in reader:
			for h, v in zip(headers, row):
				self.column[h].append(v)

	def no_cycles(self,history,nxt):
		""" Check if the flight would make cycle if visiting nxt node """
		history.append(nxt)
		cities = [ self.column["source"][x] for x in history]
		cities.append(self.column["destination"][nxt])
		routes = zip(cities,cities[1:])
		frequencies = defaultdict(int)

		for route in routes:
			frequencies[route] += 1

		result = max(frequencies.iteritems(), key=lambda x: x[1])

		if result[1] > 1: 
			return 0
		return 1

	def next_node(self,previous_flight,hist):
		""" Returns all flights, that can be attented"""
		ret = []

		for x in xrange(0,len(self.column["source"])):
			if (self.column["destination"][previous_flight] == self.column["source"][x]
			and diffdates(self.column["arrival"][previous_flight], self.column["departure"][x]) < 3600*4  
			and diffdates(self.column["arrival"][previous_flight], self.column["departure"][x]) > 3600
			and self.no_cycles(hist[:],x)):
				ret.append(x);
		return ret

		
	def dfs(self, previous_flight, history):
		"""recursive dfs with checking for time and duplicates"""
		history.append(previous_flight)
		nodes = self.next_node(previous_flight,history)
		if len(nodes) > 0:
			for nxt in nodes:
				self.dfs(nxt,history[:])
		if len(history)>1:
			print(",".join([ self.column["flight_number"][x] for x in history]))

	def compute(self):
		"""Find all possible routes in loaded data"""
		for x in xrange(0,len(self.column["source"])):
			self.dfs(x,[])

data=sys.stdin.readlines();
s = Search_flights(data)
s.compute()
