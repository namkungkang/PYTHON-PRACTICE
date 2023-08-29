print(abs(-5))
print(pow(4,2))
print(max(4,3))
print(min(4,5))
print(round(3.14))
print(round(4.99))

#퀴즈
from random import *
date = randint(4, 28)
print('오프라인 스터디 모임 날짜는 매월' ,date, '일로 선정되었습니다')

#문자열
sentence = '나는 소년입니다'
print(sentence)
sentence2 = '파이선은 쉬워요'
print(sentence2)

#슬라이싱
jumin = '020131-3222411'
print('성별 :' + jumin[7])
print('연 :' +jumin[0:2])
print('월 :' +jumin[2:4])
print('일 : ' +jumin[4:6])

print('생년월일 :' +jumin[:6])
print('뒤 7자리 :' +jumin[7:])

#문자열처리함수
python = 'Python is Amazing'
print(python.lower())
print(python.upper())
print(python[0].isupper())
print(len(python))
print(python.replace('Python', 'Java'))

index = python.index('n')
print(index)
index = python.index('n', index+1)
print(index)
print(python.find("Java"))
print('hi')

print(python.count('n'))








