#!/usr/bin/python
import copy

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
				self.HEdges[i].append(None);
		
		#2d array of vertical edges
		self.VEdges = [];				#self.VEdges[y,x]
		for i in range(self.height-1):
			#add array of random int
			self.VEdges.append([]);
			for j in range(self.width):
				self.VEdges[i].append(None);
		
		#2d array of diagonal edges
		self.DEdges = [];				#self.DEdges[y,x]
		for i in range(self.height-1):
			self.DEdges.append([]);
			for j in range(self.width-1):
				self.DEdges[i].append(None);
		
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

	def oldTinyprintGrid(self):
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
		
	def DynGridB(self):
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
					y = S[A-1][B]+0; #deletions
				if(B!=0): #check the path that led right to current node
					x = S[A][B-1]+0;	#insertions
				if(B!=0 and A!=0 and self.word1[B]==self.word2[A]):
					d = S[A-1][B-1] + 1; #matches
				S[A].append(max(x, y, d)); #adding to the local storage for the function's uses
				self.nodes[A][B] = (max(x, y, d)); #adding to the Grid object instance

		return S[self.height-1][self.width-1];

	def oldRecBackTrigger(self):
		myList = self.oldRecBacktrace(self.width-1,self.height-1);
		for x in myList:
			x.reverse();
			#print(x);
		return myList;
		
	def oldRecBacktrace(self, x, y, CPath=[[]]):
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
				nextPaths = copy.deepcopy(nextPaths) + copy.deepcopy(self.oldRecBacktrace(x,y-1, pathList));
		#did we come from the left?
		if(x!=0):
			if(self.nodes[y][x] == self.nodes[y][x-1]):
				nextPaths = copy.deepcopy(nextPaths) + copy.deepcopy(self.oldRecBacktrace(x-1,y, pathList));		
		#did we come diagonally?
		if(x!=0 and y!=0):
			if(self.word1[x]==self.word2[y]):
				nextPaths = copy.deepcopy(nextPaths) + copy.deepcopy(self.oldRecBacktrace(x-1,y-1, pathList));
		return copy.deepcopy(nextPaths);
	
	def localAlign(self, y, x):
		#v and w in local alignment are substrings of the self.word1 and self.word2 strings. 
		#alignments will have to be adjusted to reflect their positions in the global edit graph. 
		#so some other function should be in charge of calling and adjusting the results of this
		V=[" "]+list(y);
		W=[" "]+list(x);
		S = [];
		S.append([0]*(len(W)));
		for i in range(len(V)-1):
			S.append(([0]+[None]*(len(W)-1))); #fill in for free rides
			
		
		for i in range(1,len(V)): #i is y, uses vertical
			S.append([]);				#S[y,x];
			for j in range(1,len(W)): #j is x, uses horizontal
				print(i-1, len(S), j, len(S[i]));
				next = max((S[i-1][j]+0), (S[i][j-1]+0), (S[i-1][j-1] + 1)); #deletions, insertions, matche or mismatch
				S[i][j] = next; 
				self.nodes[i][j] = (next); #adding to the Grid object instance
		return S[len(V)-1][len(W)-1];

	def oldPrintAlignment(self, path):
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
		
	def GridShowLCSprocess(self):
		self.DynGridB();
		print("-"*20);
		print("Edit Graph:");
		print("");
		self.oldTinyprintGrid();
		print("");

		print("-"*20);
		print("Possible Alignments:");
		print("");
		myPaths = self.oldRecBackTrigger();
		for x in myPaths:
			self.oldPrintAlignment(x);
			print("");
		print("");

		return 0;

ourGrid = Grid("ATCGTAC","ATGTTAT");
ourGrid.GridShowLCSprocess();
	
#BLOSUM stuff
vx = ['A', 'R', 'N', 'D', 'C', 'Q', 'E', 'G', 'H', 'I', 'L', 'K', 'M', 'F', 'P', 'S', 'T', 'W', 'Y', 'V', 'B', 'Z', 'X', '-'];
wx = ['A', 'R', 'N', 'D', 'C', 'Q', 'E', 'G', 'H', 'I', 'L', 'K', 'M', 'F', 'P', 'S', 'T', 'W', 'Y', 'V', 'B', 'Z', 'X', '-'];
Bindex = [[4, -1, -2, -2, 0, -1, -1, 0, -2, -1, -1, -1, -1, -2, -1, 1, 0, -3, -2, 0, -2, -1, 0, -4],
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
	
def DeltaBLOSUM(vi, wj):
	return Bindex[vx.index(vi)][vx.index(wj)];
	#this could use some error checking

def recBackTrigger(v, w, s):
	myList = recBacktrace(v, w, s,len(w),len(v));
	for x in myList:
		x.reverse();
	return myList;

def recBacktrace(v, w, s, x, y, CPath=[[]]):
	V = [" "]+list(v);
	W = [" "]+list(w);
	#make new list to put our old list into (copies if needed)
	pathList = copy.deepcopy(CPath); #we will append the current position to all paths in this
	#print("list of paths: ");
	for path in pathList:
		path.append([x, y]);		
	nextPaths = []; #we will append entire paths to this
	if(x==0 and y==0):
		return pathList;
	#s[y,x]
	#did we come from above?
	if(y!=0):
		if(s[y][x] == s[y-1][x]):
			nextPaths = copy.deepcopy(nextPaths) + copy.deepcopy(recBacktrace(v, w, s, x, y-1, pathList));
	#did we come from the left?
	if(x!=0):
		if(s[y][x] == s[y][x-1]):
			nextPaths = copy.deepcopy(nextPaths) + copy.deepcopy(recBacktrace(v, w, s, x-1, y, pathList));		
	#did we come diagonally?
	if(x!=0 and y!=0):
		if(V[y]==W[x]):
			nextPaths = copy.deepcopy(nextPaths) + copy.deepcopy(recBacktrace(v, w, s, x-1, y-1, pathList));
	return copy.deepcopy(nextPaths);
	
def printAlignment(v, w, path):
	V = [" "]+list(v);
	W = [" "]+list(w);
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
				print(V[path[i][1]], " "*2, sep="", end="");
	
	print("");
	print("W:", " "*5, sep="", end="");

	for i in range(len(path)):
		if(i!=0):	#This is flawed if skips can happen at the first character
			#print(path[i][0], path[i-1][0], end="");
			if(path[i][0]==path[i-1][0]): #this indicates a skip. 
				print("-", " "*2, sep="", end="");
			else:
				print(W[path[i][0]], " "*2, sep="", end="");	

	print("");
	print(" "*4, end="");

	for i in range(len(path)):
		print(path[i][0], end="  ");
	print("");

def tinyprintGrid(v, w, s):
	V = [" "]+list(v);
	W = [" "]+list(w);
	print(" "*4, end="");
	for j in range(len(W)-1):
		#print W
		if(j==0):
			print("W", " "*5, sep="", end="");
		else:
			print(W[j], " "*5, sep="", end="");
	print(W[-1]);
	print("");
	for i in range(len(V)-1):
		#print V
		if(i==0):
			print("V", " "*2, sep="", end="");
		else:
			print(V[i], " "*2, sep="", end="");
		#print row
		for j in range(len(W)-1):
			print("[", str(s[i][j]), "]", "---", sep="", end="");
		print("[", s[i][-1], "]",sep="");
		#print down
		print(" "*3," "*1, sep="", end="");
		for j in range(len(W)-1):
			if(W[j+1]==V[i+1]):
				print('|', " "*2,"\\"," "*2, sep="", end="");
			else:
				print('|', " "*5, sep="", end="");
		print('|');
	#print last row
	print(V[-1], " "*2, sep="", end="");
	for j in range(len(W)-1):
		print("[", str(s[len(V)-1][j]), "]", "---", sep="", end="");
	print("[", s[len(V)-1][-1], "]",sep="");

def quickGrid(y, x):
	V=[" "]+list(y);
	W=[" "]+list(x);
	S = [];
	B = [];
	S.append([0]*(len(W)));
	B.append([" "]*(len(W)));
	for i in range(len(V)-1):
		S.append(([0]+[None]*(len(W)-1)));
		B.append(([" "]+[None]*(len(W)-1)));
	for i in range(1,len(V)): #horizontal
		for j in range(1,len(W)): #vertical
			if(V[i]==W[j]):
				S[i][j] = max(0, (S[i-1][j]+0), (S[i][j-1]+0), (S[i-1][j-1] + 1)); #matches
			else:
				S[i][j] = max(0, (S[i-1][j]+0), (S[i][j-1]+0)); #deletions, insertions
			if(S[i][j] == S[i-1][j]):
				B[i][j] = "|";
			elif(S[i][j] == S[i][j-1]):
				B[i][j] = "-";
			elif(S[i][j] == S[i-1][j-1]+1):
				B[i][j] = ('\\');
			else:
				print("error: cannot determine backtracing direction");
	return (S[len(y)][len(x)], B);

def dynGrid(y, x):
	V = [" "]+list(y);
	W = [" "]+list(x);
	S = [];
	B = [];
	S.append([0]*(len(W)));
	B.append([" "]*(len(W)));
	for i in range(len(V)-1):
		S.append(([0]+[None]*(len(W)-1)));
		B.append(([" "]+[None]*(len(W)-1)));
	for i in range(1,len(V)): #horizontal
		#S[y,x];
		for j in range(1,len(W)): #vertical
			if(V[i]==W[j]):
				S[i][j] = max(0, (S[i-1][j]+0), (S[i][j-1]+0), (S[i-1][j-1] + 1)); #matches
			else:
				S[i][j] = max(0, (S[i-1][j]+0), (S[i][j-1]+0)); #deletions, insertions
			if(S[i][j] == S[i-1][j]):
				B[i][j] = "|";
			elif(S[i][j] == S[i][j-1]):
				B[i][j] = "-";
			elif(S[i][j] == S[i-1][j-1]+1):
				B[i][j] = ('\\');
			else:
				print("error: cannot determine backtracing direction");
	return (S, B);

def printLCS(b, V, i, j):
	if(i==0 or j==0):
		return;
	if(b[i][j]=='\\'):
		printLCS(b, V, i-1, j-1);
		print(V[i], end=" ");
	elif(b[i][j]=="|"):
		printLCS(b, V, i-1, j);
	else:
		printLCS(b, V, i, j-1);

def showLCSprocess(word1, word2):
	print("-"*20);
	print("Edit Graph:");
	print("");
	tinyprintGrid(word1, word2, dynGrid(word1, word2)[0]);
	print("");
	
	#print("-"*20);
	#print("Operation Graph:");
	#print("");
	#print(dynGrid(word1, word2)[1]);
	#print("");
	
	print("-"*20);
	print("Possible Alignments:");
	print("");
	myPaths = recBackTrigger(word1, word2, dynGrid(word1, word2)[0]);
	for x in myPaths:
		printAlignment(word1, word2, x);
		print("");
	print("");

	print("-"*20);
	print("Longest Common String:");
	print("");
	printLCS(dynGrid(word1, word2)[1], " "+word1, len(word1), len(word2)); #Note the extra space for the V arguement
	print("");

	return 0;

def fastLCS(word1, word2):
	printLCS(dynGrid(word1, word2)[1], " "+word1, len(word1), len(word2));

tinyprintGrid("ATCGTAC", "ATGTTAT", dynGrid("ATCGTAC", "ATGTTAT")[0]);

print(DeltaBLOSUM("W", "W"));