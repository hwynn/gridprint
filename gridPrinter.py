#!/usr/bin/python
import random

height = 3;
width = 4;

def ourList(num):
	L=[]
	for i in range(num):
		L.append(random.randrange(1, 9, 1));

def printRow(num):
	#Horizontal Edge lengths
	num=num;
	HELens=["-"]*(num-1);
	L1=["+"]*num;
	for j in range(num-1):
		print('[{n}] -{e}- '.format(n=L1[j], e=HELens[j]), end="");
	print('[{n}]'.format(n=L1[-1]));

def printDown(num):
	#Vertical Edge lengths
	num=num;
	VELens=["|"]*(num);
	print(" ", end="");
	for i in range(num-1):
		print('|', end=" "*7);
	print('|');
	
	print(" ", end="");
	for i in range(num-1):
		print('{e}{space}'.format(e=VELens[i], space=" "*7), end="");
	print('{e}'.format(e=VELens[-1]));
	
	print(" ", end="");
	for i in range(num-1):
		print('|', end=" "*7);
	print('|');
def printGrid(H, W):
	for i in range(H-1):
		printRow(W);
		printDown(W);
	printRow(W);

printGrid(5,4);
"""
[+] --- [+] --- [+] --- [+]
 |       |       |       |
 |       |       |       |
 |       |       |       |
[+] --- [+] --- [+] --- [+]
 |       |       |       |
 |       |       |       |
 |       |       |       |
[+] --- [+] --- [+] --- [+]
"""