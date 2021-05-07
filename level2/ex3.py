
t1 = ("username","password","gender")
t2 = ("leesunchul81","1234","남")

for i in t1:
    print(i)

d1 = {}

#튜플을 딕셔너리로 변환
for i,k in enumerate(t1):  #enumerate인덱스 리턴
    d1[k] = t2[i]
    
print(d1) 