''' class Parent:
    print("hai")

class P1(Parent):
    print("Darshan")

print(P1)


class Animal:
    def add(self,a,b):
        a=int(input("a:"))
        b=int(input("b:"))
        print(a+b)

class An1(Animal):
    def sub(self,a,b):
        print(a-b)

class An2(An1):
    def mul(self):
        print(a*b)

a=An2()

a.add(8,8)

a.sub(2,3)
a.mul()
'''

class Mp:
    def name(self):
        print("name1")

class C1(Mp):
    def name1(self):
        print("name2")

class C2(Mp):
    def name2(self):
        print("name3")

n=C2()
m=C1()
n.name2()
m.name1()
n.name()

