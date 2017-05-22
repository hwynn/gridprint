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
	def __init__(self, str1, str2):
		self.word2 = [" "]+list(str2);
		self.word1 = [" "]+list(str1);
		self.height = len(self.word2); #one grid line per element in list
		self.width = len(self.word1); #is there a way to make these const?

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
				self.HEdges[i].append(0);
		
		#2d array of vertical edges
		self.VEdges = [];				#self.VEdges[y,x]
		for i in range(self.height-1):
			#add array of random int
			self.VEdges.append([]);
			for j in range(self.width):
				self.VEdges[i].append(0);
		
		#2d array of diagonal edges
		self.DEdges = [];				#self.DEdges[y,x]
		for i in range(self.height-1):
			self.DEdges.append([]);
			for j in range(self.width-1):
				self.DEdges[i].append(1);

	def printRow(self, i):
		for j in range(self.width-1):
			print('[{n}]{e}'.format(n=str(self.nodes[i][j]).center(3," "), e=str(self.HEdges[i][j]).center(5,"-")), end="");
		print('[{n}]'.format(n=str(self.nodes[i][-1]).center(3," ")));
	
	def printDown(self, i):
		print(" "*2, end="");
		for j in range(self.width-1):
			print('|', end="");
			print(" "*2, end="");
			print("\\", end="")
			print(" "*6, end="");
		print('|');
		
		print("  ", end="");
		for j in range(self.width-1):
			print(self.VEdges[i][j], end="");
			print(" "*4, end="");
			print(self.DEdges[i][j], end="");
			print(" "*4, end="");
		print(self.VEdges[i][-1]);
		
		print(" "*2, end="");
		for j in range(self.width-1):
			print('|', end="");
			print(" "*6, end="");
			print("\\", end="")
			print(" "*2, end="");
		print('|');
	
	def printGrid(self):
		for x in range(self.height-1):
			self.printRow(x);
			self.printDown(x);
		self.printRow(self.height-1);

	def tinyprintGrid(self):
		print(" "*4, end="");
		for j in range(self.width-1):
			#print word1
			if(j==0):
				print("W", " "*5, sep="", end="");
			else:
				print(self.word1[j], " "*5, sep="", end="");
		print(self.word1[-1]);
		print("");
		for i in range(self.height-1):
			#print word2
			if(i==0):
				print("V", " "*2, sep="", end="");
			else:
				print(self.word2[i], " "*2, sep="", end="");
			#print row
			for j in range(self.width-1):
				print("[", str(self.nodes[i][j]), "]", "---", sep="", end="");
			print("[", self.nodes[i][-1], "]",sep="");
			#print down
			print(" "*3," "*1, sep="", end="");
			for j in range(self.width-1):
				if(self.word1[j+1]==self.word2[i+1]):
					print('|', " "*2,"\\"," "*2, sep="", end="");
				else:
					print('|', " "*5, sep="", end="");
			print('|');
		#print last row
		print(self.word2[-1], " "*2, sep="", end="");
		for j in range(self.width-1):
			print("[", str(self.nodes[self.height-1][j]), "]", "---", sep="", end="");
		print("[", self.nodes[self.height-1][-1], "]",sep="");
		
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
	#self.nodes[y,x] [self.word2,self.word1]
	#self.HEdges[y,x]
	#self.VEdges[y,x]
	def dynGridA(self):
		S = [];
		for i in range(self.width): #i is x, uses horizontal
			S.append([]);				#S[x,y];	#S[i,j];	[word1, word2]
			for j in range(self.height): #j is y, uses vertical
				x = 0;
				y = 0;
				d = 0;
				if(i==0 and j==0):
					S[0].append(0);
					continue
				if(j!=0): #check the path that led down to current node
					y= S[i][j-1];
				if(i!=0): #check the path that led right to current node
					x= S[i-1][j];
				if(i!=0 and j!=0 and self.word1[i]==self.word2[j]): #check the path that led diagonally down-right
					#self.DEdges[y,x]
					d = S[i-1][j-1] + 1;
				S[i].append(max(x, y, d)); #adding to the local storage for the function's uses
				self.nodes[j][i] = (max(x, y, d)); #adding to the Grid object instance
		return S[self.width-1][self.height-1];
	
	def dynGridB(self):
		S = [];
		for A in range(self.height): #A is y, uses vertical
			S.append([]);				#S[y,x];
			for B in range(self.width): #B is x, uses horizontal
				x = 0;
				y = 0;
				d = 0;
				if(A==0 and B==0):
					S[0].append(0);
					continue
				if(A!=0): #check the path that led down to current node
					y = S[A-1][B];
				if(B!=0): #check the path that led right to current node
					x = S[A][B-1];	
				if(B!=0 and A!=0 and self.word1[i]==self.word2[j]):
					d = S[A-1][B-1] + 1;
				S[A].append(max(x, y, d)); #adding to the local storage for the function's uses
				self.nodes[A][B] = (max(x, y, d)); #adding to the Grid object instance
		return S[self.height-1][self.width-1];
	
	def recBackTrigger(self):
		myList = self.recBacktrace(self.width-1,self.height-1);
		for x in myList:
			x.reverse();
			#print(x);
		return myList;
		
	def recBacktrace(self, x, y, CPath=[[]]):
		#make new list to put our old list into (copies if needed)
		pathList = copy.deepcopy(CPath); #we will append the current position to all paths in this
		#print("list of paths: ");
		for path in pathList:
			path.append([x,y]);		
		nextPaths = []; #we will append entire paths to this
		if(x==0 and y==0):
			return pathList;
		#self.nodes[y,x]
		#did we come from above?
		if(y!=0):
			if(self.nodes[y][x] == self.nodes[y-1][x]):
				nextPaths = copy.deepcopy(nextPaths) + copy.deepcopy(self.recBacktrace(x,y-1, pathList));
		#did we come from the left?
		if(x!=0):
			if(self.nodes[y][x] == self.nodes[y][x-1]):
				nextPaths = copy.deepcopy(nextPaths) + copy.deepcopy(self.recBacktrace(x-1,y, pathList));		
		#did we come diagonally?
		if(x!=0 and y!=0):
			if(self.word1[x]==self.word2[y]):
				nextPaths = copy.deepcopy(nextPaths) + copy.deepcopy(self.recBacktrace(x-1,y-1, pathList));
		return copy.deepcopy(nextPaths);
	
	def printAlignment(self, path):
		print(" "*4, end="");
		for i in range(len(path)):
			print(path[i][1], end=" "*2);
					
		print("");
		print("V:", " "*5, sep="", end="");

		for i in range(len(path)):
			if(i!=0):	#This is flawed if skips can happen at the first character
				if(path[i][1]==path[i-1][1]): #this indicates a skip. 
					print("-", " "*2, sep="", end="");					
				else:
					print(self.word2[path[i][1]], " "*2, sep="", end="");
		
		print("");
		print("W:", " "*5, sep="", end="");

		for i in range(len(path)):
			if(i!=0):	#This is flawed if skips can happen at the first character
				#print(path[i][0], path[i-1][0], end="");
				if(path[i][0]==path[i-1][0]): #this indicates a skip. 
					print("-", " "*2, sep="", end="");
				else:
					print(self.word1[path[i][0]], " "*2, sep="", end="");	

		print("");
		print(" "*4, end="");
					
		for i in range(len(path)):
			print(path[i][0], end="  ");
		print("");

butt = Grid("ATCGTAC","ATGTTAT"); #Grid(W,V)
butt.dynGridA();
butt.tinyprintGrid();
myPaths = butt.recBackTrigger();
for x in myPaths:
	butt.printAlignment(x);
	print("");