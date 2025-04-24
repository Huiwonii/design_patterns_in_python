from abc import ABCMeta, abstractmethod


class IAbstraction(metaclass=ABCMeta):
    @staticmethod
    @abstractmethod
    def method(*args):
        "클라이언트가 호출할 추상 메소드"


class RefinedAbstractionA(IAbstraction):
    "구체 추상화 A (다리 역할, 실제 구현을 위임)"

    def __init__(self, implementer):
        self.implementer = implementer()  # 구현체 주입

    def method(self, *args):
        self.implementer.method(*args)


class RefinedAbstractionB(IAbstraction):
    "구체 추상화 B (다리 역할, 실제 구현을 위임)"

    def __init__(self, implementer):
        self.implementer = implementer()  # 구현체 주입

    def method(self, *args):
        self.implementer.method(*args)


class IImplementer(metaclass=ABCMeta):
    "구현체 인터페이스 (추상화에서 호출될 메소드 정의)"

    @staticmethod
    @abstractmethod
    def method(*args: tuple) -> None:
        "구체적으로 실행될 메소드"


class ConcreteImplementerA(IImplementer):
    "구현체 A - 튜플 전체를 한 번에 출력"

    @staticmethod
    def method(*args: tuple) -> None:
        print(args)


class ConcreteImplementerB(IImplementer):
    "구현체 B - 각각의 인자를 따로 출력"

    @staticmethod
    def method(*args: tuple) -> None:
        for arg in args:
            print(arg)


REFINED_ABSTRACTION_A = RefinedAbstractionA(ConcreteImplementerA)
REFINED_ABSTRACTION_A.method('a', 'b', 'c')

print('---')

REFINED_ABSTRACTION_B = RefinedAbstractionB(ConcreteImplementerB)
REFINED_ABSTRACTION_B.method('a', 'b', 'c')
