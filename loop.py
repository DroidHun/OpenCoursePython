# -*- encoding: utf-8 -*-

hello_world = ['hello', 'world'];

hello_world_string = 'hello_world_string'

letter_count = 0;

#한글 주석 달면 터미널에서는 되나?
for letter in hello_world_string :
	print 'Letter number', letter_count, 'is', letter
	letter_count = letter_count + 1;

#0부터 9까지
print 'loop1'
for num in range(10) : 
	print 'num : ', num ;
print 'loop2'
#3부터 9까지
for num in range (7, 10) :
	print 'num : ', num ;

print 'loop3'
# 2부터 10까지 2씩 건너서. 
for num in range(2, 12, 2) : 
	print 'num : ', num

count = 1;
print 'while'
while count < 100 : 
	count = count * 9 ;
	print 'now while count is : ', count
print 'the counter is : ', count


print 