def affineGap(y,x):
	V = [" "]+list(y);
	W = [" "]+list(x);
	S = [];
	S.append(([None]*(len(W))));
	for i in range(len(V)-1):
		S.append([None]*(len(W)));
	return S;

def build2(word1, word2):
	F = ([([None]*(len(word1)+1))]*(len(word2)+1));
	return F;

def banding(word1, word2):
	#https://stackoverflow.com/questions/9459337/assign-value-to-an-individual-cell-in-a-two-dimensional-python-array
	F =[[ None for i in range(len(word1)+1)] for j in range(len(word2)+1) ];
	return F;
	
a = affineGap("catae", "build");
for i in a:
	print(i);

print ("");
c = banding("catae", "build");
c[0][0]=0;
for i in c:
	print(i);

#F = ([([1]*(len(word1)+1))]*(len(word2)+1));
# this caused a problem that was solved here: https://stackoverflow.com/questions/9459337/assign-value-to-an-individual-cell-in-a-two-dimensional-python-array
