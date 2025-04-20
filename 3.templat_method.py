from abc import (
    ABCMeta,
    abstractmethod,
)

class AbstractClass(metaclass=ABCMeta):
    "템플릿 메소드와 단계별 메소드를 가지는 추상 클래스"

    @staticmethod
    def step_one():
        """
        훅(hook) 메소드 - 기본은 빈 메소드.
        필요한 경우 자식 클래스에서 선택적으로 재정의(override) 가능.
        """

    @staticmethod
    @abstractmethod
    def step_two():
        """
        반드시 자식 클래스에서 구현해야 하는 추상 메소드.
        구현하지 않으면 오류 발생.
        """

    @staticmethod
    def step_three():
        """
        훅 메소드 - 기본 동작을 제공.
        자식 클래스에서 필요하면 재정의 가능.
        """
        print("기본: Step Three - 이 줄을 출력합니다.")

    @classmethod
    def template_method(cls):
        """
        템플릿 메소드 - 전체 실행 순서를 정의.
        자식 클래스는 이 메소드를 수정하지 않고,
        필요한 단계(step)만 선택적으로 재정의해서 동작을 변경함.
        """
        cls.step_one()
        cls.step_two()
        cls.step_three()


class ConcreteClassA(AbstractClass):
    "step_two만 재정의한 구체 클래스"

    @staticmethod
    def step_two():
        print("ConcreteClassA : Step Two (오버라이드됨)")


class ConcreteClassB(AbstractClass):
    "step_one, step_two, step_three를 모두 재정의한 구체 클래스"

    @staticmethod
    def step_one():
        print("ConcreteClassB : Step One (오버라이드됨)")

    @staticmethod
    def step_two():
        print("ConcreteClassB : Step Two (오버라이드됨)")

    @staticmethod
    def step_three():
        print("ConcreteClassB : Step Three (오버라이드됨)")



CLASS_A = ConcreteClassA()
CLASS_A.template_method()

CLASS_B = ConcreteClassB()
CLASS_B.template_method()
