#!/usr/bin/python3
import string
import random

def keygen(bits):
	signs=list(range(ord('!'),ord('&')+1))
	lowers=list(range(ord('a'),ord('z')+1))
	uppers=list(range(ord('A'),ord('Z')+1))
	numbers=list(range(ord('0'),ord('9')+1))

	keybank=signs+lowers+uppers+numbers
	keybank=''.join([chr(x) for x in keybank])

	key=[]
	key.append(chr(signs[random.randint(0,len(signs)-1)]))
	key.append(chr(lowers[random.randint(0,len(lowers)-1)]))
	key.append(chr(uppers[random.randint(0,len(uppers)-1)]))
	key.append(chr(numbers[random.randint(0,len(numbers)-1)]))			
	for x in range(bits-4):
		key.append(random.choice(keybank))
	
	print(key)
	random.shuffle(key)
	print(key)

	return key

if __name__ == '__main__':
	num=int(input('please input the length of the password:'))
	password=''.join(keygen(num))
	print(password)