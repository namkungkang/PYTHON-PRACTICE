# 리스트란 순서가 있는 수정가능한 객체의 집합
# 대괄호로 작성되며, 리스트 내부의 값은 콤마로 구분
# 추가, 수정, 삭제 가능
# 인덱싱 = 무엇인가를 '가리킨다'는 의미
# 슬렉싱 = 무엇인가를 '잘라낸다'는 의미

list1 = [2,5,7,9,10]
print(list1[0])
print(list1[3])
print(list1[2] + list1[-1])
print(list1[2] + list1[-2])

list2 = [1,2,3,['a','b','c']]
print(list2)
temp = list2[3]
print(temp)
print(list2[3][1])
list3 = [0,1,2,3,4]
print(list3[1:3])
print(list3[:3])
print(list3[3:4])
list4 = [1,2,3]
list5 = [3,4,5,6]
print(list4 + list5)

#추가
list6=[1,2,3,4,5]
list6.append(6)
print(list6)
list6.insert(1,7)
print(list6)

#수정
print(list6[1])
list6[1] = 8
print(list6)
print(list6[2:4])
list6[2:4] = [7]
print(list6)

#삭제
list7 = [1,2,3,4,5,6,7]
del list7[1]
print(list7)
print(list7[1:6])
del list7[1:6]
print(list7)

#정렬
list8=[9,77,23,45,56,34]
list8.sort()
print(list8)
list8.reverse()
print(list8)

#값 반환
list9 =['a','b','c','d','e','f','g']
print(list9.index('c'))
list9.pop()
print(list9)

#개수 확인
list0 = [0,1,2,3]
print(len(list0))
 



