from abc import (
    ABCMeta,
    abstractmethod,
)


class IProtoType(metaclass=ABCMeta):
    "복제(clone) 메소드를 가진 인터페이스"

    @staticmethod
    @abstractmethod
    def clone():
        """복제 메소드 (얕은 복사 또는 깊은 복사)
        구체 클래스에서 세부 구현은 자유롭게 결정
        """


class MyClass(IProtoType):
    "IProtoType 인터페이스를 구현한 구체 클래스"

    def __init__(self, field):
        self.field = field  # 어떤 타입이든 저장할 수 있는 필드

    def clone(self):
        "얕은 복사(shallow copy)를 이용한 복제 메소드"
        return type(self)(
            self.field
            # self.field.copy()를 쓰면 1단계 수준까지 shallow copy 가능
            # 리스트 안에 리스트처럼 복잡한 구조를 깊게 복사하려면
            # Python의 copy 모듈(deepcopy) 사용 필요
        )

    def __str__(self):
        return f"{id(self)}\tfield={self.field}\ttype={type(self.field)}"


OBJECT1 = MyClass([1, 2, 3, 4])  # 리스트를 담은 객체 생성
print(f"OBJECT1 {OBJECT1}")

OBJECT2 = OBJECT1.clone()  # 복제(clone) 실행

# 복제한 OBJECT2의 리스트 일부를 수정해 봄
# 만약 OBJECT1의 리스트도 같이 바뀌었다면,
# 이는 얕은 복사(shallow copy)였다는 증거
OBJECT2.field[1] = 101

# OBJECT1과 OBJECT2 비교 출력
print(f"OBJECT2 {OBJECT2}")
print(f"OBJECT1 {OBJECT1}")
