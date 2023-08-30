
# 문자열포맷
#정수
print('나는 %d살입니다' %20) 
#문자열
print('나는 %s을 좋아해요' %'파이선')
#문자
print('apple은 %c로 시작해요' %'A')
print('나는 %s살입니다' %20)
print('나는 %s와 %s를 좋아해요' %('파란','빨강'))

print('나는 {}살입니다' .format(20))
print('나는 {}색과 {}색을 좋아합니다' .format('빨강','파랑'))
print('나는 {0}색과 {1}색을 좋아합니다' .format('빨강','파랑'))
print('나는 {1}색과 {0}색을 좋아합니다' .format('빨강','파랑'))

print('나는 {age}살이며,{color}색을좋아해요' .format(age=20,color='빨간'))

age=20 
color='빨강'
print(f'나는{age}살이며 {color}색을 좋아해요')

#탈출문자
print('백문이 불여일견\n백견이 불여일타')

print('저는 "남궁강"입니다')
print("저는 '남궁강'입니다")
print('저는 \"남궁강\"입니다')

# \r
print('C:\\Users\\user\\Desktop\\python workspace>')
print('Red Apple\rPine')
'''
# \b
print('Redd\bApple')
# \t :탭
print('Red\tApple')
'''
#퀴즈
a = 'http://youtube.com'
a = a.replace('http://','')
print(a)
a = a[:a.index('.')]
print(a)
password = a[:3] + str(len(a)) + str(a.count('e')) +'!'
print(password)
print(f"{a}의 비밀번호는 {password} 입니다")

#리스트
# subway1=10
# subway2=20
# subway3=30

subway = ["유재석","조세호","박명수"]
print(subway)

print(subway.index("조세호"))

subway.append("하하")
print(subway)
print(subway.index("하하"))

subway.insert(1,"정형돈")
print(subway)

print(subway.pop())
print(subway)

print(subway.pop())
print(subway)

print(subway.pop())
print(subway)

subway.insert(2,"노홍철")
print(subway)

print(subway.count("유재석"))

#분류
num = [5,3,2,4,1]
num.sort()
print(num)

num.reverse()
print(num)

num.clear()
print(num)

#확장
num = [5,3,2,4,1]
mix_list = ["조세호",20,True]
#print(mix_list)
num.extend(mix_list)
print(num)


