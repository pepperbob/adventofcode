import re
class Rule(object):
	def __init__(self, sor):
		self.sor = sor
		self.k1 = None
		self.k2 = None
		self.k3 = None
		self.k4 = None
		self.e0 = None
		self.e1 = None
		
	def set_button(self, name, koord):
		erg=re.search("X.(\\d+), Y.(\\d+)", koord)
		x,y = int(erg.group(1)), int(erg.group(2))
		if "A" in name:
			self.k1, self.k3 = (x,y)
		elif "B" in name:
			self.k2, self.k4 = (x,y)
		else:
			self.e0, self.e1 = (x,y)
			self.e0 += 10000000000000
			self.e1 += 10000000000000
	
	def solve(self):
		s = self
		A = (s.e1-s.e0*s.k4/s.k2)/(s.k3 - s.k1*s.k4/s.k2)
		B = s.e0/s.k2 - A*s.k1/s.k2
		A=round(A,3)
		B=round(B,3)
		if int(A) != A or int(B) != B:
			#print(s.sor)
			#print(A,B)
			# input()
			return (0,0)
		return (A, B)
		
data = open("input.txt").read().split("\n\n")
print(data[0])
input()
print(data[-1])
input()

tokens = []
for set_of_rows in data:
	rule = Rule(set_of_rows)
	for c in set_of_rows.splitlines():
		name, koord = c.split(":")
		rule.set_button(name, koord)
	a,b = rule.solve()
	# print(a, b)
	tokens.append(3*a+b)
	# input("..")

print("Solition 1", sum(tokens))
