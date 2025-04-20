# pylint: disable=too-few-public-methods
"FactoryA 샘플 코드"
from abc import ABCMeta, abstractmethod


class IProduct(metaclass=ABCMeta):
    "상품(Product) 인터페이스"

    @staticmethod
    @abstractmethod
    def create_object():
        "객체를 생성하는 추상 메소드"


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


class FactoryA:
    "FactoryA 클래스 - 제품을 생성하는 역할"

    @staticmethod
    def create_object(some_property):
        "some_property 값에 따라 알맞은 제품 객체를 생성"
        try:
            if some_property == 'a':
                return ConcreteProductA()
            if some_property == 'b':
                return ConcreteProductB()
            if some_property == 'c':
                return ConcreteProductC()
            raise Exception('Class Not Found')  # 해당하는 제품이 없으면 예외 발생
        except Exception as _e:
            print(_e)
        return None
