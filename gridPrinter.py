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

#note: this grid has lots of 2d arrays. I have made notes to keep their alignments straight.
#these will look like #self.thing(x,y). This just indicates the axis of that thing and nothing else.

class Grid(object):
	def __init__(self, X=5, Y=5):
		self.height = Y; #these should never change
		self.width = X; #is there a way to make these const?
		
		#2d array of blanks
		self.nodes=[];					#self.nodes[y,x]
		for i in range(self.height): #2d array of size [Y][X]
			#self.nodes.append(["+"]*self.width); #[["+", "+", "+", "+", "+"]] intended result
			self.nodes.append([0]*self.width);
		
		#2d array of horizontal edges
		self.HEdges = [];				#self.HEdges[y,x]
		for i in range(self.height):
			#add array of random int
			self.HEdges.append([]);
			for j in range(self.width-1):
				self.HEdges[i].append(random.randrange(0, 10, 1));
		
		#2d array of vertical edges
		self.VEdges = [];				#self.VEdges[y,x]
		for i in range(self.height-1):
			#add array of random int
			self.VEdges.append([]);
			for j in range(self.width):
				self.VEdges[i].append(random.randrange(0, 10, 1));
		
		#2d array of diagonal edges
		self.DEdges = [];				#self.DEdges[y,x]
		for i in range(self.height-1):
			self.DEdges.append([]);
				for j in range(self.width-1):
				self.HEdges[i].append(random.randrange(0, 10, 1));

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
	#recursively finds heaviest path to given point
	def MT(self, n,m): 					#self.MT(x,y) 
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
	#self.nodes[y,x]
	#self.HEdges[y,x]
	#self.VEdges[y,x]
	def dynGridA(self):
		S = [];
		for i in range(self.width): #i is x, uses horizontal
			S.append([]);				#S[x,y];
			for j in range(self.height): #j is y, uses vertical
				x = 0;
				y = 0;
				if(i==0 and j==0):
					S[0].append(0);
					continue
				if(j!=0): #check the path that led down to current node
					y= S[i][j-1] + self.VEdges[j-1][i];
				if(i!=0): #check the path that led right to current node
					x= S[i-1][j] + self.HEdges[j][i-1];
				S[i].append(max(x, y)); #adding to the local storage for the function's uses
				self.nodes[j][i] = (max(x, y)); #adding to the Grid object instance
		print(S);
		print(self.nodes);
		return S[self.width-1][self.height-1];
	
	def dynGridB(self):
		S = [];
		for A in range(self.height): #A is y, uses vertical
			S.append([]);				#S[y,x];
			for B in range(self.width): #B is x, uses horizontal
				x = 0;
				y = 0;
				if(A==0 and B==0):
					S[0].append(0);
					continue
				if(A!=0): #check the path that led down to current node
					y = S[A-1][B] + self.VEdges[A-1][B];
				if(B!=0): #check the path that led right to current node
					x = S[A][B-1] + self.HEdges[A][B-1];	
				S[A].append(max(x, y)); #adding to the local storage for the function's uses
				self.nodes[A][B] = (max(x, y)); #adding to the Grid object instance
		print(S);
		print(self.nodes);
		return S[self.height-1][self.width-1];


butt = Grid(4,3);
butt.printGrid();
#butt.recGrid();
butt.dynGridA();
butt.printGrid();
butt.dynGridB();
butt.printGrid();