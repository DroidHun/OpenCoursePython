# -*- encoding: utf-8 -*-

base = 10
exp = 4

#String 리턴 함수
def hello_world() :
	base = 20
	print 'hello_world 함수  실행!'
	return "hello_world!"

print hello_world()
print "헬로 월드 밖임 ㅋ"

#int 리턴 함수
def ret_5():
	print 5
	return 5

#Parameter 추가 
def compute_ext(base, exp) :
	poweredBase = base;
	print 'compute_ext', 'base is : ', base , 'exp is : ', exp 
	for num in range(exp) :
		poweredBase = poweredBase * base
	return poweredBase;
#사실 이렇게 안하고 이렇게 해도 됨
#	return base**exp;


print compute_ext(base, exp);
print 'base**exp = ', base**exp;

