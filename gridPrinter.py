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
		
		#BLOSUM stuff
		self.vx = ['A', 'R', 'N', 'D', 'C', 'Q', 'E', 'G', 'H', 'I', 'L', 'K', 'M', 'F', 'P', 'S', 'T', 'W', 'Y', 'V', 'B', 'Z', 'X', '-'];
		self.wx = ['A', 'R', 'N', 'D', 'C', 'Q', 'E', 'G', 'H', 'I', 'L', 'K', 'M', 'F', 'P', 'S', 'T', 'W', 'Y', 'V', 'B', 'Z', 'X', '-'];
		self.Bindex = [[4, -1, -2, -2, 0, -1, -1, 0, -2, -1, -1, -1, -1, -2, -1, 1, 0, -3, -2, 0, -2, -1, 0, -4],
[-1, 5, 0, -2, -3, 1, 0, -2, 0, -3, -2, 2, -1, -3, -2, -1, -1, -3, -2, -3, -1, 0, -1, -4],
[-2, 0, 6, 1, -3, 0, 0, 0, 1, -3, -3, 0, -2, -3, -2, 1, 0, -4, -2, -3, 3, 0, -1, -4],
[-2, -2, 1, 6, -3, 0, 2, -1, -1, -3, -4, -1, -3, -3, -1, 0, -1, -4, -3, -3, 4, 1, -1, -4],
[0, -3, -3, -3, 9, -3, -4, -3, -3, -1, -1, -3, -1, -2, -3, -1, -1, -2, -2, -1, -3, -3, -2, -4],
[-1, 1, 0, 0, -3, 5, 2, -2, 0, -3, -2, 1, 0, -3, -1, 0, -1, -2, -1, -2, 0, 3, -1, -4],
[-1, 0, 0, 2, -4, 2, 5, -2, 0, -3, -3, 1, -2, -3, -1, 0, -1, -3, -2, -2, 1, 4, -1, -4],
[0, -2, 0, -1, -3, -2, -2, 6, -2, -4, -4, -2, -3, -3, -2, 0, -2, -2, -3, -3, -1, -2, -1, -4], 
[-2, 0, 1, -1, -3, 0, 0, -2, 8, -3, -3, -1, -2, -1, -2, -1, -2, -2, 2, -3, 0, 0, -1, -4],
[-1, -3, -3, -3, -1, -3, -3, -4, -3, 4, 2, -3, 1, 0, -3, -2, -1, -3, -1, 3, -3, -3, -1, -4],
[-1, -2, -3, -4, -1, -2, -3, -4, -3, 2, 4, -2, 2, 0, -3, -2, -1, -2, -1, 1, -4, -3, -1, -4], 
[-1, 2, 0, -1, -3, 1, 1, -2, -1, -3, -2, 5, -1, -3, -1, 0, -1, -3, -2, -2, 0, 1, -1, -4],
[-1, -1, -2, -3, -1, 0, -2, -3, -2, 1, 2, -1, 5, 0, -2, -1, -1, -1, -1, 1, -3, -1, -1, -4],
[-2, -3, -3, -3, -2, -3, -3, -3, -1, 0, 0, -3, 0, 6, -4, -2, -2, 1, 3, -1, -3, -3, -1, -4],
[-1, -2, -2, -1, -3, -1, -1, -2, -2, -3, -3, -1, -2, -4, 7, -1, -1, -4, -3, -2, -2, -1, -2, -4],
[1, -1, 1, 0, -1, 0, 0, 0, -1, -2, -2, 0, -1, -2, -1, 4, 1, -3, -2, -2, 0, 0, 0, -4],
[0, -1, 0, -1, -1, -1, -1, -2, -2, -1, -1, -1, -1, -2, -1, 1, 5, -2, -2, 0, -1, -1, 0, -4],
[-3, -3, -4, -4, -2, -2, -3, -2, -2, -3, -2, -3, -1, 1, -4, -3, -2, 11, 2, -3, -4, -3, -2, -4],
[-2, -2, -2, -3, -2, -1, -2, -3, 2, -1, -1, -2, -1, 3, -3, -2, -2, 2, 7, -1, -3, -2, -1, -4], 
[0, -3, -3, -3, -1, -2, -2, -3, -3, 3, 1, -2, 1, -1, -2, -2, 0, -3, -1, 4, -3, -2, -1, -4], 
[-2, -1, 3, 4, -3, 0, 1, -1, 0, -3, -4, 0, -3, -3, -2, 0, -1, -4, -3, -3, 4, 1, -1, -4],
[-1, 0, 0, 1, -3, 3, 4, -2, 0, -3, -3, 1, -1, -3, -1, 0, -1, -3, -2, -2, 1, 4, -1, -4],
[0, -1, -1, -1, -2, -1, -1, -1, -1, -1, -1, -1, -1, -1, -2, 0, 0, -2, -1, -1, -1, -1, -1, -4],
[-4, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4, 1]];
	
	def DeltaBLOSUM(self, vi, wj):
		return self.Bindex[self.vx.index(vi)][self.vx.index(wj)];
		#this could use some error checking

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
		
	def dynGridA(self):
		S = [];
		for i in range(self.width): #i is x, uses horizontal
			S.append([]);				#S[x,y];	#S[i,j];	[word1, word2]
			for j in range(self.height): #j is y, uses vertical
				next=0;			
				if(i==0 and j==0):
					S[0].append(0);
					continue
				if(j!=0): #check the path that led down to current node
					next= max(next, (S[i][j-1]+0));
				if(i!=0): #check the path that led right to current node
					next= max(next, (S[i-1][j]+0));
				if(i!=0 and j!=0 and self.word1[i]==self.word2[j]): #check the path that led diagonally down-right
					#self.DEdges[y,x]
					next= max(next, (S[i-1][j-1] + 1));
				S[i].append(next); #adding to the local storage for the function's uses
				self.nodes[j][i] = (next); #adding to the Grid object instance
		return S[self.width-1][self.height-1];
	
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

	def localAlign(self, v, w):
		#v and w in local alignment are substrings of the self.word1 and self.word2 strings. 
		#alignments will have to be adjusted to reflect their positions in the global edit graph. 
		#so some other function should be in charge of calling and adjusting the results of this
		S = [];
		for i in range(self.width): #i is x, uses horizontal
			S.append([]);				#S[x,y];	#S[i,j];	[word1, word2]
			for j in range(self.height): #j is y, uses vertical
				next=0;			
				if(i==0 and j==0):
					S[0].append(0);
					continue
				if(j!=0): #check the path that led down to current node
					next= max(next, (S[i][j-1]+0));
				if(i!=0): #check the path that led right to current node
					next= max(next, (S[i-1][j]+0));
				if(i!=0 and j!=0 and self.word1[i]==self.word2[j]): #check the path that led diagonally down-right
					#self.DEdges[y,x]
					next= max(next, (S[i-1][j-1] + 1));
				S[i].append(next); #adding to the local storage for the function's uses
				self.nodes[j][i] = (next); #adding to the Grid object instance
		return S[self.width-1][self.height-1];
		
		
#butt = Grid("ATCTGATC","TGCATAC"); #Grid(W,V) (top, side)
#butt = Grid("ATCG","ATGT");
butt = Grid("ATCGTAC","ATGTTAT");
butt.localAlign("ATCGTAC","ATGTTAT");
butt.tinyprintGrid();
myPaths = butt.recBackTrigger();
for x in myPaths:
	butt.printAlignment(x);
	print("");

print(butt.DeltaBLOSUM("W", "W"));