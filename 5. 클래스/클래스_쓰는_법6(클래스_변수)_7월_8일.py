class Family:
    lastname = "박"  # 클래스안에 변수 선언

a = Family()
b = Family()

print(a.lastname)
print(b.lastname)

print(id(Family.lastname))     # id == 객체의 주소을 리턴
print(id(a.lastname))       # 클래스 변수와 주소값이 같다 == 서로 주소값 공유 
print(id(b.lastname))
