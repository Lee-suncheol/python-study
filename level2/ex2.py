# 클래스

class User:
    username = "leesunchul81"
    password = "1234"

u = User()

print(u.username)
print("="*50)

class Person:
    def __init__(self,username,password):
        self.username = username
        self.password = password

p = Person("leesunchul81","1234")

print(p.username)