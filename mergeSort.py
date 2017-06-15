#!/usr/bin/python

def complexDivide(pList):
	if(len(pList)<2):
		return(pList, []);
	elif((len(pList)%2)!=0):
		return(pList[0:int((len(pList)+1)/2)], pList[int((len(pList)+1)/2):int(len(pList))]);
	else:
		return((pList[0:int(len(pList)/2)]), (pList[int(len(pList)/2):int(len(pList))]));

def combine(sListA, sListB):
	newList = [];
	A = sListA.copy();
	B = sListB.copy();
	while(len(A)!=0 and len(B)!=0):
		#print("A:", A);
		#print("B: ", B);
		#print(newList);
		if(A[0] < B[0]):
			newList.append(A.pop(0));
		else:
			newList.append(B.pop(0));
	newList = newList + A;
	newList = newList + B;
	return newList;

def mergeSort(c):
	n = len(c);
	if(n==1):
		return c;
	left, right = complexDivide(c);
	sortedLeft = mergeSort(left);
	sortedRight = mergeSort(right);
	sortedList = combine(sortedLeft ,sortedRight);
	return sortedList;

#print(combine([2,4,5,7],[1,2,3,6]));
#print(combine([5],[2]));
print(mergeSort([2,4,5,7,1,2,3,6]));