from abc import (
    ABCMeta,
    abstractmethod,
)


class IA(metaclass=ABCMeta):
    "IA 인터페이스 (method_a를 요구)"

    @staticmethod
    @abstractmethod
    def method_a():
        "추상 메소드 A"


class ClassA(IA):
    "IA 인터페이스를 구현한 클래스 A"

    def method_a(self):
        print("method A")


class IB(metaclass=ABCMeta):
    "IB 인터페이스 (method_b를 요구)"

    @staticmethod
    @abstractmethod
    def method_b():
        "추상 메소드 B"


class ClassB(IB):
    "IB 인터페이스를 구현한 클래스 B"

    def method_b(self):
        print("method B")


class ClassBAdapter(IA):
    "ClassB를 IA 인터페이스에 맞게 변환해주는 어댑터 클래스"

    def __init__(self):
        self.class_b = ClassB()

    def method_a(self):
        "method_a 호출 시 내부적으로 class_b의 method_b를 호출"
        self.class_b.method_b()



# 어댑터 만들기 전에는 객체 타입을 검사해서 각각 다른 메소드를 호출해야 했음
ITEMS = [ClassA(), ClassB()]
for item in ITEMS:
    if isinstance(item, ClassB):
        item.method_b()
    else:
        item.method_a()

# 어댑터를 만든 이후에는
# 모든 객체가 같은 인터페이스(method_a)를 사용하므로 일관된 코드 작성 가능
ITEMS = [ClassA(), ClassBAdapter()]
for item in ITEMS:
    item.method_a()
