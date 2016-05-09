#!/usr/bin/python3
import random

def checker(a,b):
	cntCows=0
	cntBulls=0

	alist=list(a)
	print(alist)
	blist=list(b)
	print(blist)

	for x in range(len(blist)):
		for y in range(len(alist)):
			if alist[y]==blist[x]:
				if x==y:
					cntCows+=1
				else:
					cntBulls+=1
	if cntCows==len(alist):
		print('exactly right!!!')
		return 1
	else:
		print('{0} cows, {1} bulls'.format(cntCows,cntBulls))
		return 0

if __name__ == '__main__':
	numbank=list(range(ord('0'),ord('9')))
	numbank=[chr(x) for x in numbank]

#    number = str(random.randint(0,9999)) 

	destnum=[]
	for x in range(4):
		destnum.append(random.choice(numbank))
	destnum=''.join(destnum)
	print('destnum: '+ destnum)
	guessnum=input('please input a 4-digit number:')
	guessnum=guessnum[:4]
	while not checker(destnum,guessnum):
		guessnum=input('try again:')
		guessnum=guessnum[:4]



