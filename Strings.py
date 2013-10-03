# -*- encoding: utf-8 -*-

new_STRING = "HI I`M STRING!";

for letter in new_STRING :
	print letter

s1 = 'HI'
s2 = 'I`M STRING!'

#s1, s2 사이에 공백 없음
print s1 + s2 
#s1, s2 사이에 공백 있음
print s1, s2
print s1, 6.189, s2 

#indexing
print 'new_STRING[0] is', new_STRING[0]

#slice it
print 'new_STRING[0:3] is', new_STRING[0:3]
