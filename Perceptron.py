import random
import numpy as np
from matplotlib import pyplot as plt

class Perceptron:

	def __init__(self, n):
		#creates a linearly separable plane with x =y

		self.X = self.gen_random_points(n)

		#plt.show()

	def plot(self):

		for i in self.X:
			if i[1] == 1:
				plt.scatter(i[0][1],i[0][2],color = 'red')
			else:
				plt.scatter(i[0][1],i[0][2],color = 'blue')	

		l = np.linspace(-1,1)
		a, b = -self.w[1]/self.w[2], -self.w[0]/self.w[2]
		plt.plot(l, a*l+b, 'k-')
		plt.show()



	def gen_random_points(self,n):
		X  = []
		for i in range(n):
			x1,y1 = [random.uniform(-1,1) for i in range(2)]
			if(x1 > y1):
				X.append((np.array([1,x1,y1]),-1))
			else:
				X.append((np.array([1,x1,y1]),1))

		return X

	def check_valid(self,w):
		#this checks yw'x >= 0 for all data points
		temp = []
		for i in self.X:
			print i[1]*(w.T.dot(i[0])) 
			if i[1]*(w.T.dot(i[0])) < 0:
				return i;
		return temp

	def fit(self):
		w = np.array([1,1,1])
		while 1:
			c = self.check_valid(w)
			print c

			if(len(c) == 0):
				break
			w = w+c[1]*c[0]
		self.w = w;

p = Perceptron(50)
p.fit()
print p.w
print p.plot()