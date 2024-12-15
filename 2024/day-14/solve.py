data = open("input.txt").read().splitlines()
X,Y = 101-1,103-1
#X,Y=11-1,7-1

q1 = ((0,0), (X//2-1, Y//2-1))
q2 = ((X//2+1,0), (X, Y//2-1))
q3 = ((0, Y//2+1), (X//2-1, Y))
q4 = ((X//2+1, Y//2+1), (X, Y))

class Robot:
	def __init__(self, pos, vel):
		self.orig = pos
		self.pos = pos
		self.vel = vel
	
	def move(self, i):
		x,y=self.pos
		vx,vy=self.vel
		x = (x+vx*i)%(X+1)
		y = (y+vy*i)%(Y+1)
		self.pos = (x,y)
	
	def in_reg(self, reg):
		x,y = self.pos
		rfrom, rto= reg
		return x>=rfrom[0] and x<=rto[0] and y>=rfrom[1] and y<=rto[1]
	
	def reset(self):
		self.pos=self.orig
		
	def mark(self, canvas):
		canvas[self.pos[0]][self.pos[1]] = "*"

robots =[]
for d in data:
	robot, veloc = d.split(" ")
	x,y = robot.split("=")[1].split(",")
	vx, vy = veloc.split("=")[1].split(",")
	r = Robot((int(x), int(y)), (int(vx), int(vy)))
	robots.append(r)
	r.move(100)

rq1 = [r for r in robots if r.in_reg(q1)]
rq2 = [r for r in robots if r.in_reg(q2)]
rq3 = [r for r in robots if r.in_reg(q3)]
rq4 = [r for r in robots if r.in_reg(q4)]

# print(len(rq1))
# print(q2, len(rq2))
# print(q3, len(rq3))
# print(q4, len(rq4))

sol1 = len(rq1)*len(rq2)*len(rq3)*len(rq4)
print("sol1", sol1)

for r in robots:
	r.reset()

canvas = [["." for i in range(Y+1)] for k in range(X+1)]

## 4695
for kk in range(100000):
	for r in robots:
		r.move(kk)
		r.mark(canvas)

	for x in canvas:
		line = "".join(x)
		if "******" in line:
			for l in canvas:
				print("".join(l))
			print("--- ", kk)
			input("..")
	
	canvas = [["." for i in range(Y+1)] for k in range(X+1)]
