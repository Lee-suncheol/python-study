# for문으로 리스트, 튜플, 딕셔너리 다루기

# 1. list안에 Tuple을 뽑아보기

list1 = [
    (1,"leesunchul81","1234"),
    (2,"cos","5678")
]

for a,b,c in list1:
    print(f"{a},{b},{c}")

# 2. 가장 기본 for문

for i in range(3,10):  # 0 ~ 9까지
    print(i)

# 리스트안에 딕셔너리 뽑아내기
# 리스트에 id값만 담기
list2 = []

dic1 = [
    {"id":1,"name":"leesunchul81"},
    {"id":2,"name":"ssar"}
]
#print(dic1)
print("="*50)
for list2 in dic1:
    print(list2)
print("="*50)

list3 =[]
for a in list2.items():
    list3.append(a)

print(list3)

print("="*50)
list4 = [d["id"] for d in dic1]
print(list4)

