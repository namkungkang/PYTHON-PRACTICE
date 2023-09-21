#딕셔너리

person = {'이름' : '남궁강', '나이' :23, '몸무게' : 65}
'이름'  in person
'남궁강' in person #키벨류는 들어있지않음
len(person)
person.pop('이름') #pop은 이름을 한번 출력하고 딕셔너리에서 삭제됨
person

fruit = {'apple': 6000, 'melon' : 3000, 'banana' : 5000, 'orange' : 4000}
fruit.keys()
fruit.values()
list1 = [6000,3000,5000,7000] # 딕셔너리의 모든 값을 리스트 형식으로 출력
print(list1)    
print('딕셔너리의 항목의 개수 : {}'.format(len(fruit)))
print('apple is in fruit : {}'.format('apple' in fruit)) #키와 키값이 있는지 검사
print('mango is in fruit : {}'.format('apple' not in fruit))

for key in fruit :

    print('{} : {}'. format(key,fruit[key])) #딕셔너리 항목을 하나하나 열거하는 것
    
    fruit.get('apple') #key의 벨류값을 반환
    fruit.pop('apple') # apple 키 값 삭제
    fruit.clear() #딕셔너리 모든 항목 삭제

#딕셔너리 주의점
# dic(1)은 리스트에선 두번째이지만 딕셔너리에선 첫번째 혼동 X

#튜플
#튜플 자체로는 변경이 안된다

# tup = (100,)  #뒤에 콤마 써주는게 올바름
# tup

t0 = (10,20,30)
t1 = t0 + t0 
t1

a = 100
b = 200
print('swap 이전: a',a,'b =',b)

#emp = a
#a = b
#b = temp
#위에 코드보다 더 간단한 방법
a , b = b , a
print('swap 이후: a',a,'b =',b)

#언패킹
c = (1, 2)
d, e =  c
d
e

#예제 
d=(10,20,30)
c,b,a = d
a
b
c

#예제
t_fruits=('apple','banana','peach')
print('변경 전 :',t_fruits)
list1 = list(t_fruits)
list1[1] = 'kiwi'
t_fruits = tuple(list1)
print('변경 후 :', t_fruits)

#집합
s1 = {100,200,300}
s2 = {600,700,800}
s1
s1.add(500)
s1
s1.discard(100)
s1 | s2
