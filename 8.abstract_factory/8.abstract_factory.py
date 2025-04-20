from abc import (
    ABCMeta,
    abstractmethod,
)
from factory_a import FactoryA
from factory_b import FactoryB


class IAbstractFactory(metaclass=ABCMeta):
    "추상 팩토리 인터페이스"

    @staticmethod
    @abstractmethod
    def create_object(factory):
        "정적 메소드 - 추상 팩토리 인터페이스 메소드"


class AbstractFactory(IAbstractFactory):
    "구체 추상 팩토리 클래스 (IAbstractFactory를 구현)"

    @staticmethod
    def create_object(factory):
        "정적 메소드 - 알맞은 팩토리를 선택해서 객체를 생성"
        try:
            if factory in ['aa', 'ab', 'ac']:
                return FactoryA.create_object(factory[1])  # FactoryA 사용
            if factory in ['ba', 'bb', 'bc']:
                return FactoryB.create_object(factory[1])  # FactoryB 사용
            raise Exception('No Factory Found')  # 알맞은 팩토리가 없을 때 예외 발생
        except Exception as _e:
            print(_e)
        return None


# 클라이언트 코드 (사용 예시)
PRODUCT = AbstractFactory.create_object('ab')
print(f"{PRODUCT.__class__}")

PRODUCT = AbstractFactory.create_object('bc')
print(f"{PRODUCT.__class__}")
