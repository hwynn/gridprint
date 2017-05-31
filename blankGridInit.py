def build(y,x):
	V=[" "]+list(y);
	W=[" "]+list(x);
	S = [];
	S.append([0]*(len(W)));
	for i in range(len(V)-1):
		S.append(([0]+[None]*(len(W)-1)));
	return S;
a= build("catae", "build");
for i in a:
	print(i);