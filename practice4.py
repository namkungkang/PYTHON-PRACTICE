#사전
cabinet ={3:"유재석",100:"김태호"}
print(cabinet[3])
print(cabinet[100])

print(cabinet.get(3))
print(cabinet.get(5))
print(cabinet.get(5,"사용가능"))
print("hi")

print(3 in cabinet)
print(5 in cabinet)

print(cabinet)
cabinet["C-20"] = "조세호"
print(cabinet)

del cabinet['C-20']
print(cabinet)

print(cabinet.keys())

print(cabinet.values())

print(cabinet.items())

cabinet.clear()
print(cabinet)

#튜플
menu = ('돈까스','치즈까스')
print(menu[0])
print(menu[1])

name = '김종국'
age = 20
hobby = '코딩'
print(name,age,hobby)

(name,age,hobby) = ('김종국',20,'코딩')
print(name,age,hobby)

#집합(set)
my_set = {1,2,3,3,3}
print(my_set)

java = {'유재석','김태호','양세형'}
python = set(['유재석', '박명수'])

#교집합
print(java & python)
print(java.intersection(python))

#합집합
print(java | python)
print(java.union(python))

#차집합
print(java-python)
print(java.difference(python))
print(python-java)

python.add('김태호')
print(python)

java.remove('김태호')
print(java)

#자료구조의 변경
menu = {'커피','우유','주스'}
print(menu)
print(menu,type(menu))
menu = list(menu)
print(menu,type(menu))

menu=tuple(menu)
print(menu, type(menu))

menu = set(menu)
print(menu,type(menu))



#퀴즈
from random import *
users = range(1,21)
users=list(users)
print(type(users))

print(users)
shuffle(users)
print(users)

winners = sample(users,4)

print('--당첨자 발표--')
print('치킨 당첨자 : {0}'.format(winners[0]))
print('커피 당첨자 : {0}'.format(winners[1:]))
print('--축하합니다--')


