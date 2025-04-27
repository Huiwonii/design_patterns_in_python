from abc import ABCMeta, abstractmethod


class IComponent(metaclass=ABCMeta):
    "컴포넌트가 반드시 구현해야 하는 메소드 정의"

    @staticmethod
    @abstractmethod
    def method():
        "반드시 구현해야 하는 메소드"


class Component(IComponent):
    "기본 컴포넌트 (필요에 따라 데코레이터로 감쌀 수 있음)"

    def method(self):
        "기본 메소드 구현"
        return "Component Method"


class Decorator(IComponent):
    "Decorator 클래스도 IComponent를 구현함 (컴포넌트를 감싸는 역할)"

    def __init__(self, obj):
        "감쌀 대상 객체를 저장"
        self.object = obj

    def method(self):
        "감싼 객체의 메소드를 확장하거나 변경"
        return f"Decorator Method({self.object.method()})"


COMPONENT = Component()
print(COMPONENT.method())  # 기본 컴포넌트 메소드 호출

DECORATED_COMPONENT = Decorator(COMPONENT)
print(DECORATED_COMPONENT.method())  # 데코레이터를 적용한 메소드 호출
