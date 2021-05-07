# 1. 딕셔너리 {"key":"value"} {1 : "홍길동"}=>파이썬에서 몽고DB에 값 넣을 때 사용
# 자바스크립트 {key : value} {username : "홍길동"}=>몽고DB(자바스크립트 오브젝트를 넣어야함)
# JSON {"key":value}

dic1 = {"username":"leesunchul81"}

print(dic1)
print("="*50)

# 딕셔너리 값 찾기
print(dic1["username"])
print("="*50)

# 딕셔너리 값 추가

dic1["password"] = "12345"
print(dic1)
print("="*50)

# 딕셔너리 값 삭제 del

# Key값 추출하기
dic2 = {"username":"leesunchul81", "password":"12345"}

print(dic2.keys())
print("="*50)
print(dic2.values())
print("="*50)

# Key값과 Value값 동시에 추출하기
for i in dic2.items():
    print(i)
print("="*50)
list1 = []
for k,v in dic2.items():
    print(k,v)
    list1.append(v)

print(list1)

#for i in range[1,6]
#    print(i)
