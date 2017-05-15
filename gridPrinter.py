#!/usr/bin/python
import random
import copy

height = 3;
width = 4;

def ourList(num):
	L=[]
	for i in range(num):
		L.append(random.randrange(0, 9, 10));
	return L;

class Grid(object):
	def __init__(self, X=5, Y=5):
		self.height = Y; #these should never change
		self.width = X; #is there a way to make these const?
		#2d array of blanks
		self.nodes=[];
		for i in range(self.height): #2d array of size [Y][X]
			#self.nodes.append(["+"]*self.width); #[["+", "+", "+", "+", "+"]] intended result
			self.nodes.append([0]*self.width);
		#2d array of horizontal edges
		self.HEdges = [];
		for i in range(self.height):
			#add array of random int
			self.HEdges.append([]);
			for j in range(self.width-1):
				self.HEdges[i].append(random.randrange(0, 10, 1));
		#2d array of vertical edges
		self.VEdges = [];
		for i in range(self.height-1):
			#add array of random int
			self.VEdges.append([]);
			for j in range(self.width):
				self.VEdges[i].append(random.randrange(0, 10, 1));
		#current position
		self.cP=[0,0];
		#current distance
		self.cD=0;
	
	def printRow(self, i):
		for j in range(self.width-1):
			print('[{n}]{e}'.format(n=str(self.nodes[i][j]).center(3," "), e=str(self.HEdges[i][j]).center(5,"-")), end="");
		print('[{n}]'.format(n=str(self.nodes[i][-1]).center(3," ")));
	
	def printDown(self, i):
		print(" "*2, end="");
		for j in range(self.width-1):
			print('|', end=" "*9);
		print('|');
		
		print("  ", end="");
		for j in range(self.width-1):
			print('{e}{space}'.format(e=self.VEdges[i][j], space=" "*9), end="");
		print('{e}'.format(e=self.VEdges[i][-1]));
		
		print(" "*2, end="");
		for j in range(self.width-1):
			print('|', end=" "*9);
		print('|');
	
	def printGrid(self):
		for x in range(self.height-1):
			self.printRow(x);
			self.printDown(x);
		self.printRow(self.height-1);
	def recGrid(self):
		return self.MT(self.width-1, self.height-1);
	def MT(self, n,m): #recursively finds heaviest path to given point
		if(n<0 or n>=self.width or m<0 or m>=self.height):
			print("error: given coordinates are outside of grid boundary");
			return 0;
		if(n==0 and m==0):
			return 0;
		x=0;
		y=0;
		if(m!=0):
			y = self.MT(n,m-1) + self.VEdges[m-1][n];
		if(n!=0):
			x = self.MT(n-1,m) + self.HEdges[m][n-1];
		self.nodes[m][n] = max(x, y); #we honestly don't need to do this. But it's proof the algorithm is recursing
		return max(x, y);
	#def dynGrid(self):
		


butt = Grid(4,4);
#butt.printGrid();
butt.recGrid();
butt.printGrid();