# #5-3
# list1 = [3,5,7]
# list2 = [2,3,4,5,6]
# for i in list1:
#     print(' ')
#     for j in list2 :
#         print(i ,'*', j, '=', i*j)
#5-5
# list1 = ['I like', 'I love']
# list2 = ['pancake', 'kiwi juice', 'espresso']
# for i in list1:
#     for j in list2 :
#         print(i,j)
#5-7
# list1 = [10,20,30,50,60]
# list1[0] + list1[1] + list1[2] + list1[3] + list1[4] 

#5-8
# list1 = [10,20,30,50,60]
# list1[0] * list1[1] * list1[2] * list1[3] * list1[4] 
#5-12
# n = int(input("n을 입력하세요: "))
# input_string = input(f"{n}개의 수를 공백으로 구분하여 입력하세요: ")
# num_list = [int(num_str) for num_str in input_string.split()]

# print("합:", sum(num_list))
# print("평균:", sum(num_list) / len(num_list))
# print("최댓값:", max(num_list))
# print("최솟값:", min(num_list))

# #5-15
# greet = 'Have a beautiful day.'
# greet[0:4]
# greet[7:16]
# greet[17:20]

# #5-17
# animals = ['dog', 'cat', 'tiger', 'lion']
# print('animals : {}'.format(animals))
# animals.append(animals.pop(0))
# print('animals : {}'.format(animals))

# animals = ['dog', 'cat', 'tiger', 'lion']
# print('animals : {}'.format(animals))
# for i in animals:
#     print('I love {}.'.format(i))

#6-6
# t1 = 'a' , 'b' ,'c'
# t2 = ('a', 'b', 'c')
# t3 = ('d', 'e')
# t1 == t2
# t2 + t3

# 6-9
# tup = (1,2,5,4,3,2,1,4,7,8,9,9,3,7,3)
# print('주어진 튜플:', tup)
# set1 = set(tup)
# print('중복 제거 튜플:',set1)

# #6-10
# TUP = (1,2,5,4,3,2,1,4,7,8,9,9,3,7,3)
# max_item = 0
# for i in TUP:
#     if TUP.count(i) > TUP.count(max_item):
#         max_item = i
#     elif TUP.count(i) == TUP.count(max_item):
#         max_item = max(i, max_item)
# print('가장 많이 나타나는 요소는: {}'.format(max_item))



#11
# score = []
# for i in range(5):
#     while True:
#         try:
#             num = int(input(f"두 자리 정수를 입력하세요 : "))
#             if 10 <= num <= 99: 
#                 score.append(num)
#                 break
#             else:
        
#                 print("두 자리 정수를 입력해야 합니다. 다시 입력하세요.")
#         except ValueError:
#             print("올바른 정수를 입력하세요.")
# average = sum(score) / len(score)
# print("입력한 두 자리 정수 리스트:", score)
# print("평균:", average)
# count_greater_than_average = 0
# print("평균보다 큰 수:")
# for num in score:
#     if num > average:
#         print(num)
#         count_greater_than_average += 1
# print("평균보다 큰 수의 개수:", count_greater_than_average)






#12
# menu = {
#     'Americano': '가격 : 3000원',
#     'Ice Americano': '가격 : 3500원',
#     'Capuccino 가격': '가격 : 4000원',
#     'Cafe Latte': '가격 : 4500원',
#     'Espresso': '가격 : 3600원',
# }

# for key in menu:
#     print('{} : {}'.format(key, menu[key]))

# x = input('위의 메뉴 중 하나를 선택하세요 : ')
# if x in menu:
#     y = menu[x]
#     print('{0}는 {1} 입니다. 결제를 부탁합니다'.format(x, y))
# else:
#     print('선택한 메뉴가 메뉴판에 없습니다.')

#13

population_A = (100, 150, 230, 120, 180, 100, 140, 95, 81, 21, 4)
population_B = (300, 420, 530, 420, 400, 300, 40 ,5, 1, 1, 1)
a = sum(population_A[2:])
b = sum(population_B[2:])
print('마을 A와 B에 보낼 투표용지의 개수는 각각 {0} 장과 {1}장입니다'.format(a,b))
totalA = sum(population_A)
totalB = sum(population_B)

seniorA = sum(population_A[7:])
seniorB = sum(population_B[7:])

averageA = (seniorA / totalA) 
averageB = (seniorB / totalB) 

print('마을 A와 B의 고령화 정도는 각각 {:.3f}%와 {:.3f}%입니다.'.format(averageA,averageB))
