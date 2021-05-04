# 1. 문자열 함수
#find, rfind, join

str1 = "가나-다-라"
r1 = str1.find("-")
print(r1)
r2 = str1.find("-",3)
print(r2)

r3 = str1.rfind("-")
print(r3)

tel1 = "02-2222-7874"
tel2 = "051-777-8373"

r4 = tel1.find("-")
r5 = tel1.rfind("-")
print(r4)
print(r5)
print(tel1[r4+1:r5])

r6 = tel2.find("-")
r7 = tel2.rfind("-")
print(tel2[r6+1:r7])

# 가,나,다,라,마
str2 = "가나다라마"
r8 = ",".join(str2)
print(r8)

