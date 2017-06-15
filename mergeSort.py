#!/usr/bin/python


def divide(pList):
	if(len(pList)<2):
		return(pList, []);
	elif((len(pList)%2)!=0):
		return( pList[0:int((len(pList)+1)/2)], pList[int((len(pList)+1)/2):int(len(pList))]);
	else:
		return((pList[0:int(len(pList)/2)]), (pList[int(len(pList)/2):int(len(pList))]));

"""l= [0, 1, 2, 3, 4, 5, 6];
len(l) = 7;
(len(l)+1)/2 = 4;

la = [0, 1, 2, 3];
la = l[0:5]
lb = [4, 5, 6];

l = [0, 1, 2];
len(l) = 3;
((len(l)+1)/2) = 2;
la = [0, 1];
la = l[0:2];
la = l[0:((len(l)+1)/2)];
lb = l[2:3];
lb = l[((len(l)+1)/2):len(l)];

l= [0, 1, 2, 3, 4, 5];
la = [0, 1, 2];
la = l[0:(len(l)/2)];

lb = [3, 4, 5];"""

myList = [0, 1, 2, 3, 4];
print(myList);
print(divide(myList)[0]);
print(divide(myList)[1]);