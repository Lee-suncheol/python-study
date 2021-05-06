# 1. 리스트
list1 = [1,2,3,4]
list2 = [5,6,7,8]
print(list1[2])
print("="*50)

#더하기(중요)
list3 = list1 + list2
print(list3)

# 3 스칼라(자연수)
# [1,3,4] 벡터(방향성이 있음)
# 2차원 matrix, 3차원 tensor
#2차원배열(중요)
list4 = [
    list1,
    list2
]
print(list4)

list1.append(10)
print(list1)

list5 = [list1,11]
print(list5)

del(list1[0])
print(list1)

list1.remove(2) # 리스트에서 2라는 값을 삭제
print(list1)

list6 = list(range(10))
print(list6)
list7 = list(range(0,12)) #마지막 인덱스 직전까지
print(list7)

# 2. 튜플 - 리스트와 같음, 데이터 변경이 불가능
tuple1 = (1,2,3)  # 괄호()는 튜플 대괄호[]는 리스트
print(tuple1)

tuple2 = (4,5,6)

tuple3 = tuple1 + tuple2

print(tuple3)

tuple4 = (
    tuple1,
    tuple2
)
print(tuple4)

list10 = list(tuple1)
print(list10)

money = 10000000.01234

print(f"{money:,}")

# 3. 딕셔너리


