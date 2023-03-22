#파이썬의 기본적인 내용(import할 library 없는 것)

#1.3.1 산술 연산
print("---------- 산술 연산 ---------- ")
print("1 - 2  =", 1-2)
print("4 * 5  =", 4*5)
print("7 / 5  =", 7/5)
print("3 ** 2 =", 3**2)
print()

#1.3.2 자료형
print("---------- 자 료 형 ---------- ")
print("type(10)    =", type(10))
print("type(2.718) =", type(2.718))
print("type(hello) =", type("hello"))
print()

#1.3.3 변수
print("----------  변 수  ---------- ")
x = 10
print("x         =", x)
x = 100
print("x         =", x)
y = 3.14
print("x * y     =", x*y)
print("type(x*y) =", type(x*y))
print()

#1.3.4 리스트
print("---------- 리 스 트 ---------- ")
a = [1, 2, 3, 4, 5]
print("a      =", a)
print("len(a) =", len(a))
print("a[0]   =", a[0])
print("a[4]   =", a[4])
a[4]=99
print("a      =", a)
print()

#슬라이싱
print("a[0:2] = ", a[0:2])
print("a[1:]  = ", a[1:])
print("a[:3]  = ", a[:3])
print("a[:-1] = ", a[:-1])
print("a[:-2] = ", a[:-2])
print()

#1.3.5 딕셔너리
print("---------- 딕셔너리 ---------- ")
me = {"height":180}
print("me[\"height\"] =", me["height"])
me["weight"] = 70
print("me = ", me)
print()

#1.3.6 bool
print("---------- bool ---------- ")
hungry = True
sleepy = False
print("type(hungry) =", type(hungry))
print("not hungry   =", not hungry)
print("hungry and sleepy =", hungry and sleepy)
print("hungry or sleepy  =", hungry or sleepy)
print()

#1.3.7 if문
print("---------- if 문 ---------- ")
hungry = True
if hungry:
    print("I'm hungry")

hungry = False
if hungry:
    print("I'm hungry")
else :
    print("I'm not hungry")
    print("I'm sleepy")
print()

#1.3.8 for문
print("---------- for 문 ---------- ")
for i in [1, 2, 3]:
    print(i)
print()

#1.3.9 함수
print("----------  함 수  ---------- ")
def hello():
    print("Hello World!")
hello()

def hello(object):
    print("Hello " + object + "!")
hello("cat")

print()

#1.4.2 클래스
print("---------- 클 래 스 ---------- ")
class Man:
    def __init__(self, name):
        self.name = name
        print("Initialized!")
    
    def hello(self):
        print("Hello " + self.name + "!")

    def goodbye(self):
        print("Good-bye " + self.name + "!")

m = Man("David")
m.hello()
m.goodbye()