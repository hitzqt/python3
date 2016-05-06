#! /usr/bin/python3
flag=True
playRound=1
types={'rock','paper','scissors'}

while flag:
	decision1=input('player 1 please make a dicision within rock, paper or scissors:')
	while not decision1 in types:
		decision1=input('wrong input, only accept rock, paper or scissors:')
	decision2=input('player 2 please make a dicision within rock, paper or scissors:')
	while not decision2 in types:
		decision2=input('wrong input, only accept rock, paper or scissors:')

	if decision1==decision2:
		print('draw situation')
		continue
	elif decision1=='rock':
		if decision2=='paper':
			print('the winner is player 2')
		else:
			print('the winner is player 1')
	elif decision1=='paper':
		if decision2=='scissors':
			print('the winner is player 2')
		else:
			print('the winner is player 1')		
	elif decision1=='scissors':
		if decision2=='rock':
			print('the winner is player 2')
		else:
			print('the winner is player 1')	
	else:
		print('error')
		continue
	conn=input('Do you want to play again(y or n):')
	if conn=='y':
		playRound+=1
		print('play round {0}'.format(playRound))
		continue
	else:
		flag=0
