#!/usr/bin/python3

num=int(input('please input a number:'))

divisor=2
while divisor<=(num/2):
	residue=num%divisor
	if residue==0:
		print('it is not a prime number')
		break
	divisor+=1

if divisor>num/2:
	print('it is a prime number')
