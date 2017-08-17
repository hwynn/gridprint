#!/usr/bin/python
import copy
import sys

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

def proteinFromFile(filename):
	fo = open(filename, "r+", encoding='utf-8');
	header = fo.readline();
	line = fo.readline();
	full = "";
	while(line!=""): #kinda dangerous
		if(line[-1]=='\n'):
			line =  line[0:-1];
		full = full + line;
		line = fo.readline();
	fo.close();
	return full;
#s1 = proteinFromFile("mouse_hemoglobin_alpha.fasta.txt");
#s2 = proteinFromFile("human_hemoglobin_alpha.fasta.txt");

#----recursive traceback algorithms-------------

def bRecBacktrace(s, v, w, bs, bu, bl, x, y, mode, CPath=[]):
	V = [" "]+list(v);
	W = [" "]+list(w);
	pathList = copy.deepcopy(CPath); #we will append the current position to this
	pathList.append([x, y]);
	if(mode=="s"):
		if(x==0 and y==0):
			return pathList;
		elif(x==0):
			if(bs[y][x] == "|"):		#did we come from above?
				pathList = copy.deepcopy(bRecBacktrace(s, v, w, bs, bu, bl, x, y-1, "u", pathList));
			else:
				print("error: cannot traceback above");
			if(bs[y][x] == "\\"):	#did we come diagonally?
				pathList = copy.deepcopy(bRecBacktrace(s, v, w, bs, bu, bl, x-1, y-1, "s", pathList));
		elif(y==0):
			if(bs[y][x] == "-"):		#did we come from the left?
				pathList = copy.deepcopy(bRecBacktrace(s, v, w, bs, bu, bl, x-1, y, "l", pathList));
			else:
				print("error: cannot traceback left");
			if(bs[y][x] == "\\"):	#did we come diagonally?
				pathList = copy.deepcopy(bRecBacktrace(s, v, w, bs, bu, bl, x-1, y-1, "s", pathList));
		elif(y<1 or x<1):
			print("error: unidentified traceback error");
		else:
			if(bs[y][x] == "|"):		#did we come from above?
				pathList = copy.deepcopy(bRecBacktrace(s, v, w, bs, bu, bl, x, y-1, "u", pathList));
			if(bs[y][x] == "-"):		#did we come from the left?
				pathList = copy.deepcopy(bRecBacktrace(s, v, w, bs, bu, bl, x-1, y, "l", pathList));		
			if(bs[y][x] == "\\"):	#did we come diagonally?
				pathList = copy.deepcopy(bRecBacktrace(s, v, w, bs, bu, bl, x-1, y-1, "s", pathList));
			if(bs[y][x] == " "):
				print("error: blank cell in traceback");
	elif(mode=="l"):
		if(x==0 and y==0):
			return pathList;
		elif(x==0):
			if(bl[y][x] == "|"):		#did we come from above?
				print("error: this shouldn't happen");
				pathList = copy.deepcopy(bRecBacktrace(s, v, w, bs, bu, bl, x, y-1, "u", pathList));
			else:
				print("error: cannot traceback above");
			if(bl[y][x] == "\\"):	#did we come diagonally?
				pathList = copy.deepcopy(bRecBacktrace(s, v, w, bs, bu, bl, x-1, y-1, "s", pathList));
		elif(y==0):
			if(bl[y][x] == "-"):		#did we come from the left?
				pathList = copy.deepcopy(bRecBacktrace(s, v, w, bs, bu, bl, x-1, y, "l", pathList));
			else:
				print("error: cannot traceback left");
			if(bl[y][x] == "\\"):	#did we come diagonally?
				pathList = copy.deepcopy(bRecBacktrace(s, v, w, bs, bu, bl, x-1, y-1, "s", pathList));
		elif(y<1 or x<1):
			print("error: unidentified traceback error");
		else:
			if(bl[y][x] == "|"):		#did we come from above?
				print("error: this shouldn't happen");
				pathList = copy.deepcopy(bRecBacktrace(s, v, w, bs, bu, bl, x, y-1, "u", pathList));
			if(bl[y][x] == "-"):		#did we come from the left?
				pathList = copy.deepcopy(bRecBacktrace(s, v, w, bs, bu, bl, x-1, y, "l", pathList));		
			if(bl[y][x] == "\\"):	#did we come diagonally?
				pathList = copy.deepcopy(bRecBacktrace(s, v, w, bs, bu, bl, x-1, y-1, "s", pathList));
			if(bl[y][x] == " "):
				print("error: blank cell in traceback");
			
	elif(mode=="u"):
		if(x==0 and y==0):
			return pathList;
		elif(x==0):
			if(bu[y][x] == "|"):		#did we come from above?
				pathList = copy.deepcopy(bRecBacktrace(s, v, w, bs, bu, bl, x, y-1, "u", pathList));
			else:
				print("error: cannot traceback above");
			if(bu[y][x] == "\\"):	#did we come diagonally?
				pathList = copy.deepcopy(bRecBacktrace(s, v, w, bs, bu, bl, x-1, y-1, "s", pathList));
		elif(y==0):
			if(bu[y][x] == "-"):		#did we come from the left?
				print("error: this shouldn't happen");
				pathList = copy.deepcopy(bRecBacktrace(s, v, w, bs, bu, bl, x-1, y, "l", pathList));
			else:
				print("error: cannot traceback left");
			if(bu[y][x] == "\\"):	#did we come diagonally?
				pathList = copy.deepcopy(bRecBacktrace(s, v, w, bs, bu, bl, x-1, y-1, "s", pathList));
		elif(y<1 or x<1):
			print("error: unidentified traceback error");
		else:
			if(bu[y][x] == "|"):		#did we come from above?
				pathList = copy.deepcopy(bRecBacktrace(s, v, w, bs, bu, bl, x, y-1, "u", pathList));
			if(bu[y][x] == "-"):		#did we come from the left?
				print("error: this shouldn't happen");
				pathList = copy.deepcopy(bRecBacktrace(s, v, w, bs, bu, bl, x-1, y, "l", pathList));		
			if(bu[y][x] == "\\"):	#did we come diagonally?
				pathList = copy.deepcopy(bRecBacktrace(s, v, w, bs, bu, bl, x-1, y-1, "s", pathList));
			if(bu[y][x] == " "):
				print("error: blank cell in traceback");
				
	return copy.deepcopy(pathList);

#----grid navigating algorithms-----------------------	
	
def localAlignment(y, x):
	V = [" "]+list(y);
	W = [" "]+list(x);
	S = [];
	L = [];
	U = [];
	Bs = [];
	Bl = [];
	Bu = [];
	a = 1;
	p = 11;
	S.append(([None]*(len(W))));
	L.append(([None]*(len(W))));
	U.append(([None]*(len(W))));
	Bs.append(([None]*(len(W))));
	Bl.append(([None]*(len(W))));
	Bu.append(([None]*(len(W))));
	for i in range(len(V)-1):
		S.append([None]*(len(W)));
		L.append([None]*(len(W)));
		U.append([None]*(len(W)));
		Bs.append([None]*(len(W)));
		Bl.append(([None]*(len(W))));
		Bu.append(([None]*(len(W))));
	for i in range(len(V)): #horizontal
		#S[y,x];
		for j in range(len(W)): #vertical
			if(i==0 and j==0):
				L[i][j]=0;
				U[i][j]=0;
				S[i][j]=0;
				Bl[i][j]=" ";
				Bu[i][j]=" ";
				Bs[i][j]=" ";
			elif(i==0 or j==0):
				if(j==0):
					L[i][j]=0;
					Bl[i][j]=" ";
					if(i==1):
						U[i][j] = (S[i-1][j]-(p+a));
					else:
						U[i][j] = max((U[i-1][j] - a), (S[i-1][j]-(p+a)));
					Bu[i][j] = "|";
					S[i][j]=U[i][j];
					Bs[i][j] = "|";
				elif(i==0):
					U[i][j]=0;
					Bu[i][j]=" ";
					if(j==1):
						L[i][j] = (S[i][j-1]-(p+a));
					else:
						L[i][j] = max((L[i][j-1] - a), (S[i][j-1]-(p+a)));
					Bl[i][j]="-";
					S[i][j]=L[i][j];
					Bs[i][j] = "-";
						
			else: 
				#finding L
				if(Bl[i][j-1]==" "):
					L[i][j] = (S[i-1][j-1] + DeltaBLOSUM(V[i], W[j]));
					Bl[i][j] ="\\";
				elif(Bl[i][j-1]=="\\"):
					L[i][j] = (S[i][j-1]-(p+a));
					Bl[i][j] = "-";
				elif(Bl[i][j-1]=="-"):
					L[i][j] = max((L[i][j-1] - a), (S[i][j-1]-(p+a)));
					Bl[i][j] = "-";
				else:
					print("Error: no direction for l found");
				#check if diagonal is good enough to change our minds;
				if(((S[i-1][j-1] + DeltaBLOSUM(V[i], W[j]))-L[i][j])>=12):
					L[i][j] = (S[i-1][j-1] + DeltaBLOSUM(V[i], W[j]));
					Bl[i][j] = "\\";
				
				#finding U
				if(Bu[i-1][j]==" "):
					U[i][j] = (S[i-1][j-1] + DeltaBLOSUM(V[i], W[j]));
					Bu[i][j] = "\\";
				elif(Bu[i-1][j]=="\\"):
					U[i][j] = (S[i-1][j]-(p+a));
					Bu[i][j] = "|";
				elif(Bu[i-1][j]=="|"):
					U[i][j] = max((U[i-1][j] - a), (S[i-1][j]-(p+a)));
					Bu[i][j] = "|";
				else:
					print("Error: no direction for u found");
				#check if diagonal is good enough to change our minds;
				if(((S[i-1][j-1] + DeltaBLOSUM(V[i], W[j]))-U[i][j])>=12):
					U[i][j] = (S[i-1][j-1] + DeltaBLOSUM(V[i], W[j]));
					Bu[i][j] = "\\";
				
				if((i==(len(V)-1) and j!=(len(W)-1)) or (i!=(len(V)-1) and j==(len(W)-1))):
					if(i==(len(V)-1)):
						U[i][j] = (S[i-1][j-1] + DeltaBLOSUM(V[i], W[j]));
						Bu[i][j] = "\\";
					elif(j==(len(W)-1)):
						L[i][j] = (S[i-1][j-1] + DeltaBLOSUM(V[i], W[j]));
						Bl[i][j] ="\\";
					else:
						print("Error: no direction for endzone found");

				S[i][j] = max((S[i-1][j-1] + DeltaBLOSUM(V[i], W[j])), U[i][j], L[i][j]);
				if(S[i][j] == L[i][j]):
					Bs[i][j] = "-";
				if(S[i][j] == U[i][j]):
					Bs[i][j] = "|";
				if(S[i][j] == (S[i-1][j-1] + DeltaBLOSUM(V[i], W[j]))):
					Bs[i][j] = "\\";
	ourPaths = bRecBacktrace(S, y, x, Bs, Bu, Bl,len(x),len(y), "s");
	
	del ourPaths[-1];
	ourPaths.reverse();

	return (S, ourPaths);

def globalAlignment(word1, word2):
	V = [" "]+list(word1);
	W = [" "]+list(word2);
	S =[[ None for i in range(len(word2)+1)] for i in range(len(word1)+1) ];
	L =[[ None for i in range(len(word2)+1)] for i in range(len(word1)+1) ];
	U =[[ None for i in range(len(word2)+1)] for i in range(len(word1)+1) ];
	Bl =[[ None for i in range(len(word2)+1)] for i in range(len(word1)+1) ];
	Bu =[[ None for i in range(len(word2)+1)] for i in range(len(word1)+1) ];
	Bs =[[ None for i in range(len(word2)+1)] for i in range(len(word1)+1) ];
	a = 1;
	p = 11;
	#k is constant. we'll make it 3 for no particular reason.
	k = 3;
	if(len(word2) > len(word1)):
		k = k + (len(word2) - len(word1));
	elif(len(word2) < len(word1)):
		k = k + (len(word1) - len(word2));
	N = len(word1);
	M = len(word2);
	#for point [0][0]
	L[0][0] = 0;
	U[0][0] = 0;
	S[0][0] = 0;
	Bl[0][0] = " ";
	Bu[0][0] = " ";
	Bs[0][0] = " ";
	for i in range(1,k+1):
		L[i][0]=0;
		Bl[i][0]=" ";
		if(i==1):
			U[i][0] = (S[i-1][0]-(p+a));
		else:
			U[i][0] = max((U[i-1][0] - a), (S[i-1][0]-(p+a)));
		Bu[i][0] = "|";
		S[i][0]=U[i][0];
		Bs[i][0] = "|";
	for j in range(1,k+1):
		U[0][j]=0;
		Bu[0][j]=" ";
		if(j==1):
			L[0][j] = (S[0][j-1]-(p+a));
		else:
			L[0][j] = max((L[0][j-1] - a), (S[0][j-1]-(p+a)));
		Bl[0][j]="-";
		S[0][j]=L[0][j];
		Bs[0][j] = "-";
	for i in range(1,N+1):
		for j in range(max(1,i-k),min(M,i+k)+1):
			#...
			if((j-i)==k): #cannot use [i-1][j]
				U[i][j] = (S[i-1][j-1] + DeltaBLOSUM(V[i], W[j]));
				Bu[i][j] = "\\";
			else:
				#finding U
				if(Bu[i-1][j]==" "):
					U[i][j] = (S[i-1][j-1] + DeltaBLOSUM(V[i], W[j]));
					Bu[i][j] = "\\";
				elif(Bu[i-1][j]=="\\"):
					U[i][j] = (S[i-1][j]-(p+a));
					Bu[i][j] = "|";
				elif(Bu[i-1][j]=="|"):
					U[i][j] = max((U[i-1][j] - a), (S[i-1][j]-(p+a)));
					Bu[i][j] = "|";
				else:
					print("Error: no direction for u found");
				#check if diagonal is good enough to change our minds;
				if(((S[i-1][j-1] + DeltaBLOSUM(V[i], W[j]))-U[i][j])>=12):
					U[i][j] = (S[i-1][j-1] + DeltaBLOSUM(V[i], W[j]));
					Bu[i][j] = "\\";
			#...
			if((i-j)==k): #cannot use [i][j-1]
				L[i][j] = (S[i-1][j-1] + DeltaBLOSUM(V[i], W[j]));
				Bl[i][j] ="\\";
			else:
				#finding L
				if(Bl[i][j-1]==" "):
					L[i][j] = (S[i-1][j-1] + DeltaBLOSUM(V[i], W[j]));
					Bl[i][j] ="\\";
				elif(Bl[i][j-1]=="\\"):
					L[i][j] = (S[i][j-1]-(p+a));
					Bl[i][j] = "-";
				elif(Bl[i][j-1]=="-"):
					L[i][j] = max((L[i][j-1] - a), (S[i][j-1]-(p+a)));
					Bl[i][j] = "-";
				else:
					print("Error: no direction for l found");
				#check if diagonal is good enough to change our minds;
				if(((S[i-1][j-1] + DeltaBLOSUM(V[i], W[j]))-L[i][j])>=12):
					L[i][j] = (S[i-1][j-1] + DeltaBLOSUM(V[i], W[j]));
					Bl[i][j] = "\\";
			
			#are we on the edge of the grids?
			if((i==(len(V)-1) and j!=(len(W)-1)) or (i!=(len(V)-1) and j==(len(W)-1))):
				if(i==(len(V)-1)):
					U[i][j] = (S[i-1][j-1] + DeltaBLOSUM(V[i], W[j]));
					Bu[i][j] = "\\";
				elif(j==(len(W)-1)):
					L[i][j] = (S[i-1][j-1] + DeltaBLOSUM(V[i], W[j]));
					Bl[i][j] ="\\";
				else:
					print("Error: no direction for endzone found");

			S[i][j] = max((S[i-1][j-1] + DeltaBLOSUM(V[i], W[j])), U[i][j], L[i][j]);
			if(S[i][j] == L[i][j]):
				Bs[i][j] = "-";
			if(S[i][j] == U[i][j]):
				Bs[i][j] = "|";
			if(S[i][j] == (S[i-1][j-1] + DeltaBLOSUM(V[i], W[j]))):
				Bs[i][j] = "\\";
	ourPaths = bRecBacktrace(S, word1, word2, Bs, Bu, Bl,len(word2),len(word1), "s");
	del ourPaths[-1];
	ourPaths.reverse();
	return (S, ourPaths);
		
#---printing/displaying functions--------------------

def shortPrintAlignment(v, w, path):
	offset = 60;
	V = ["-"]+list(v);
	W = ["-"]+list(w);
	top = ""; #W
	middle = ""; #relationship
	bottom = ""; #V
	if(path[1] == [0,1]): #moved down. gap in W
		top = top + "-";
		middle = middle + " ";
		bottom = bottom + V[path[0][1]];
	elif(path[1] == [1,0]): #moved left, gap in V
		top = top + W[path[0][0]];
		middle = middle + " ";
		bottom = bottom + "-";
	else: #moved diagonal, match or mismatch
		top = top + W[path[0][0]];
		if(W[path[0][0]]==V[path[0][1]]):
			middle = middle + "|";
		else:
			middle = middle + "*";
		bottom = bottom + V[path[0][1]];
		
	for i in range(1,len(path)):
		if(i%offset == 0):
			print(top, middle, bottom, sep="\n");
			top = "";
			middle = "";
			bottom = "";
			print("");
		
		if(path[i][0]==path[i-1][0]): #we didn't move left.
			top = top + "-";
			middle = middle + " ";
			bottom = bottom + V[path[i][1]];
		elif(path[i][1]==path[i-1][1]): #we didn't move down
			top = top + W[path[i][0]];
			middle = middle + " ";
			bottom = bottom + "-";
		else: #we moved diagonally
			top = top + W[path[i][0]];
			if(W[path[i][0]]==V[path[i][1]]):
				middle = middle + "|";
			else:
				middle = middle + "*";
			bottom = bottom + V[path[i][1]];
		if(i == len(path)-1):
			print(top, middle, bottom, sep="\n");

	print("");
	print("");
	return 0;

def tinyprintGrid(v, w, s):
	#w has maximum size of 14
	if(len(w)>14):
		print("Sorry. I can't print a grid of this. It's too big.");
		return 0;
	V = [" "]+list(v);
	W = [" "]+list(w);
	print(" "*5, end="");
	for j in range(len(W)-1):
		#print W
		if(j==0):
			print("W", " "*4, sep="", end="");
		else:
			print(W[j], " "*4, sep="", end="");
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
			('[{n}]'.format(n=str(s[i][j]).center(3," ")));
			print("=", str(s[i][j]).center(3," "), "=", sep="", end="");
		print("=", str(s[i][-1]).center(3," "), "=",sep="");
		#print down
		print(" "*4," "*1, sep="", end="");
		for j in range(len(W)-1):
			if(W[j+1]==V[i+1]):
				print('|', " ","\\"," "*2, sep="", end="");
			else:
				print('|', " "*4, sep="", end="");
		print('|');
	#print last row
	print(V[-1], " "*2, sep="", end="");
	for j in range(len(W)-1):
		print("=", str(s[len(V)-1][j]).center(3," "), "=", sep="", end="");
	print("=", str(s[len(V)-1][-1]).center(3," "), "=",sep="");
	return 0;

def printSubGrid(v, w, s, v1, vL, w1, wL):
	#w has maximum size of 14
	
	if(wL>14):
		print("Sorry. I can't print a grid of this. It's too big.");
		return 0;
	V = [" "]+list(v);
	W = [" "]+list(w);
	if((v1+vL)>len(V) or (w1+wL)>len(w)):
		print("Error: this exceeds the bounds of the grid");
		return 0;
	print(" "*5, end="");
	for j in range(w1, w1+wL-1):
		#print W
		if(j==0):
			print("W", " "*4, sep="", end="");
		else:
			print(W[j], " "*4, sep="", end="");
	print(W[w1+wL]);
	print("");
	for i in range(v1, v1+vL):
		#print V
		if(i==0):
			print("V", " "*2, sep="", end="");
		else:
			print(V[i], " "*2, sep="", end="");
		#print row
		for j in range(w1, w1+wL):
			('[{n}]'.format(n=str(s[i][j]).center(3," ")));
			print("=", str(s[i][j]).center(3," "), "=", sep="", end="");
		print("");
		#print down
		print(" "*4," "*1, sep="", end="");
		for j in range(w1, w1+wL-1):
			if(W[j+1]==V[i+1]):
				print('|', " ","\\"," "*2, sep="", end="");
			else:
				print('|', " "*4, sep="", end="");
		print('|');
	#print last row
	
	return 0;

def pathCheck(word1, word2, path, grid=[[0]]):
	if (path[-1][0]!=len(word2) and path[-1][1]!=len(word1)):
		return 0;

	V = [" "]+list(word1);
	W = [" "]+list(word2);
	vGap = False; #flags to tell us if gaps have been started yet.
	wGap = False;
	a = 1;
	p = 11;
	score = 0;
	current = [0,0];
	next = [0,0];
	while(len(path)!=0):
		current = copy.deepcopy(next);
		next = copy.deepcopy(path[0]);
		del path[0];
		#diagonal
		if(next[0]==(current[0]+1) and next[1]==(current[1]+1)):
			score = score + DeltaBLOSUM(V[next[1]], W[next[0]]);
			#print(current, "->", next);
			vGap = False;
			wGap = False;
		#right
		elif(next[0]==(current[0]+1) and next[1]==(current[1])):
			if(wGap):
				#print("W gap extension", current, "->", next);
				score = score - (a);
				vGap = False;
			else:
				#print("W gap start", current, "->", next);
				score = score - (a+p);
				wGap = True;
				vGap = False;
		#down
		elif(next[0]==(current[0]) and next[1]==(current[1]+1)):
			if(vGap):
				#print("V gap extension", current, "->", next);
				score = score - (a);
				wGap = False;
			else:
				#print("V gap start", current, "->", next);
				score = score - (a+p);
				vGap = True;
				wGap = False;
		else:
			print("Error: next cell in path could not be located");
		#if(len(grid)!=1):
			#if(score!=grid[next[1]][next[0]]):
				#print("Incorrect score", next, grid[next[1]][next[0]], "should be:", score);
	return score;
#----operation running functions-----------

def alignmentProcess(word1, word2):
	print("Using Local Alignment:");
	gap = localAlignment(word1, word2);
	tinyprintGrid(word1, word2, gap[0]);
	#printSubGrid(word1, word2, gap[0], 2, 5, 2,5);
	#print(gap[1]);
	print(gap[0][len(word1)][len(word2)]);
	shortPrintAlignment(word1, word2, gap[1]);

	print("Using Banded Global Alignment:");
	glob1 = globalAlignment(word1, word2);
	tinyprintGrid(word1, word2, glob1[0]);
	#print(glob1[1]);
	#shortPrintAlignment(word1, word2, glob1[1]);
	print(glob1[0][len(word1)][len(word2)]);
	shortPrintAlignment(word1, word2, glob1[1]);
#-----high level function calls-------------

print(sys.argv, len(sys.argv));
if(len(sys.argv) > 2):
	s1 = proteinFromFile(sys.argv[1]);
	s2 = proteinFromFile(sys.argv[2]);
else:	
	#s1 = proteinFromFile("guitarfish1_cytochrome_c_oxidase_subunit1.fasta.txt"); #AHH54580.1
	#s2 = proteinFromFile("guitarfish2_cytochrome_c_oxidase_subunit1.fasta.txt"); #AHH54579.1
	#s1 = "LYFIFGAWAGLFGTGLSLLIRTELSQPGTLLGDDQIYNVVVTAHA";
	#s2 = "MVLSPADKTNVKAAWGKVGAHA";
	#s1 = "LYFI";
	#s2 = "MVLSGE";
	#s1 = "LYFIFGAWAGLFGTGLSLLIRTELSQPGTLLGDDQIYNVVV";
	#s2 = "MVLSPADKTNVKAAWGKVG";
	s1 = "LYFIFGAWAGLFGTGLSLLIRTELSQPGTLLGDDQIYNVVVTAHAFVMIFFMVMPIMIGG";
	s2 = "MVLSPADKTNVKAAWGKVGAHAGEYGAEALERMFLSFPTTKTYFPHFDLSHGSAQVKGHG";


alignmentProcess(s1, s2);