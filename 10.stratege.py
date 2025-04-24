from abc import ABCMeta, abstractmethod


class Context():
    "행동(전략)을 외부에서 주입받아 동작을 바꾸는 컨텍스트 객체"

    @staticmethod
    def request(strategy):
        """전략 객체를 받아서 그에 따라 요청을 처리"""
        return strategy()


class IStrategy(metaclass=ABCMeta):
    "전략 인터페이스"

    @staticmethod
    @abstractmethod
    def __str__():
        "__str__ 메소드를 반드시 구현해야 함"


class ConcreteStrategyA(IStrategy):
    "구체적인 전략 A"

    def __str__(self):
        return "I am ConcreteStrategyA"


class ConcreteStrategyB(IStrategy):
    "구체적인 전략 B"

    def __str__(self):
        return "I am ConcreteStrategyB"


class ConcreteStrategyC(IStrategy):
    "구체적인 전략 C"

    def __str__(self):
        return "I am ConcreteStrategyC"


CONTEXT = Context()

print(CONTEXT.request(ConcreteStrategyA))
print(CONTEXT.request(ConcreteStrategyB))
print(CONTEXT.request(ConcreteStrategyC))
