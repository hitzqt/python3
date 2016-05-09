#!/usr/bin/python3
'''
def rmdup(alist):
	newset=set(alist)
	print(newset)
	newlist=list(newset)
	print(newlist)
	return newlist
'''

def dedup(x):
	return list(set(x))

if __name__ == '__main__':
	alist=[1,2,3,4,5,5,6,3,3,2,4,5,6,7,8,8,6,5,4]
	print(alist)
	newlist=dedup(alist)
	print(newlist)
