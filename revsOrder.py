#!/usr/bin/python3

def reverser():
	teststring=input('please input a scentence:')
	strList=teststring.split()
	print(strList)

	newlist=[]
	for x in range(1,len(strList)+1):
		newlist.append(strList[len(strList)-x])
	print(newlist)

	newstr=' '.join(newlist)
	print(newstr)
	return None
'''
def reverse_v1(x):
  y = x.split()
  result = []
  for word in y:
    result.insert(0,word)
  return " ".join(result)


'''


'''
def reverse_v2(x):
  y = x.split()
  return " ".join(y[::-1])

'''




'''
# method 3
def reverse_v3(x):
  y = x.split()
  return " ".join(reversed(y))
'''
reverser()

