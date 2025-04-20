from abc import (
    ABCMeta,
    abstractmethod,
)


class IProduct(metaclass=ABCMeta):
    "상품(Product) 역할을 하는 인터페이스(추상 클래스)"

    @staticmethod
    @abstractmethod
    def create_object():
        "객체를 생성하는 추상 메소드 (구현 필수)"


class ConcreteProductA(IProduct):
    "IProduct 인터페이스를 구현한 구체 클래스 A"

    def __init__(self):
        self.name = "ConcreteProductA"

    def create_object(self):
        return self


class ConcreteProductB(IProduct):
    "IProduct 인터페이스를 구현한 구체 클래스 B"

    def __init__(self):
        self.name = "ConcreteProductB"

    def create_object(self):
        return self


class ConcreteProductC(IProduct):
    "IProduct 인터페이스를 구현한 구체 클래스 C"

    def __init__(self):
        self.name = "ConcreteProductC"

    def create_object(self):
        return self


class Creator:
    "팩토리 역할을 하는 클래스 (객체를 생성해주는 책임)"

    @staticmethod
    def create_object(some_property):
        "입력값에 따라 알맞은 구체 Product 객체를 생성하는 정적 메소드"
        if some_property == 'a':
            return ConcreteProductA()
        if some_property == 'b':
            return ConcreteProductB()
        if some_property == 'c':
            return ConcreteProductC()
        return None


PRODUCT = Creator.create_object('b')
print(PRODUCT.name)
