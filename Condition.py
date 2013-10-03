# -*- encoding: utf-8 -*-

#일반적 포맷의 contdition check

#if <consition is True> : 
#	<code to excute if condision is True>


#일반 조건
if 9 > 5 :
	print '그래 9가 5보다 크단다'

#not 조건
if 9!=5 :
	print '그래 9가 5랑 같지가 않지'

#else 문 사용
if 9 < 5 :
	print '?'
else :
	print '9가 5보다 작지가 않음'

#and, not 추가
#후술식이 참이 아니면. 
if not ( 10 == 4 ) and 9 > 5 :
	print '수학은 거짓말 ㄴㄴ해'
else :
	print ':('

light_color = raw_input("What color is the traffic light? ")
light_color = light_color.lower()
print light_color
if light_color == "red":
   print "You should stop"
elif light_color == "yellow":
   print "Slow down!"
elif light_color == "green":
   print "Go ahead!"
else:
   print "What country are you in??"





