#!/usr/bin/python3
import random

seed=random.randint(0,99)

guesses=[]

flag=True

while flag:
	aGuess=int(input('please guess the number:'))
	if aGuess==seed:
		print('exactly right')
		guesses.append(aGuess)
		flag=0
	elif aGuess>seed:
		print('too high')
		guesses.append(aGuess)
		continue
	elif aGuess<seed:
		print('too low')
		guesses.append(aGuess)
		continue
print(*guesses, sep='\t')