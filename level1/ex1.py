# Hello World 파스칼표기법
# hello World 낙타표기법
# hello_world 언더스코어(파이썬)

# 타입추론
# 모든것이 오브젝트
# 인터프리터
# alt+shift+아래화살표 줄복사
# ctlr+/ 주석처리

# 1. 숫자
a = 1
b = 1.2
c = 4e5

# print(a)
# print(b)
# print(c)

print(type(a))
print(type(b))
print(type(c))

# 연산자 +, -, *, /, %
e = 3
f = 4

print(e**f)  # 3**4 3의 4제곱
print(e//f)  # // 몫
print(e%f)   # % 나머지

# 2. 문자열
# "", '', ''' ''' 구분안함
s1 = "안녕하세요"
s2 = '안녕하세요'
s3 = '''
안녕하세요
'''

s4 = s1 + s2
print(s4)

s5 = "홍길동"
print(s5+"님 안녕하세요")
print(f"{s5}님 안녕하세요")
print("="*30)  #문자열 여러번 반복

# 3.슬라이싱 연산자:
str1 = "가나다라마"

print(str1[0:3]) #슬라이스 연산자는 마지막 인덱스 번호 직전까지 가져옴. 0,1,2
print(str1[-1])  #뒤에서부터 가져옴
print(str1[1:])  #마지막 인덱스 번호가 없으면 끝까지 가져옴


