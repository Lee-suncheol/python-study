
# 오버로딩 없음

def add(a,b):
    return a+b

print(add(1,2))

def minus(a,b=5):  # default 값 지정가능
    return a-b
print("="*50)
print(minus(10,))
print("="*50)

def many(*data): # 데이터를 튜플로 받음
    print(data)

many(1,2,3,4,5)

def keyword(**data): #딕셔너리 데이터 받기
    print(data)

keyword(id=1,username="leesunchul81")

n1 = 1

def var_test():
    global n1  # 글로벌 변수로 선언
    n1 = 2

var_test()

print(n1)

