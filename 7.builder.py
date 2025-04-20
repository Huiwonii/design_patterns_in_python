from abc import (
    ABCMeta,
    abstractmethod,
)


class IBuilder(metaclass=ABCMeta):
    "빌더 인터페이스"

    @staticmethod
    @abstractmethod
    def build_part_a():
        "Part A를 만드는 메소드"

    @staticmethod
    @abstractmethod
    def build_part_b():
        "Part B를 만드는 메소드"

    @staticmethod
    @abstractmethod
    def build_part_c():
        "Part C를 만드는 메소드"

    @staticmethod
    @abstractmethod
    def get_result():
        "최종 결과물을 반환하는 메소드"


class Builder(IBuilder):
    "구체적인 빌더 클래스"

    def __init__(self):
        self.product = Product()

    def build_part_a(self):
        self.product.parts.append('a')
        return self

    def build_part_b(self):
        self.product.parts.append('b')
        return self

    def build_part_c(self):
        self.product.parts.append('c')
        return self

    def get_result(self):
        return self.product


class Product():
    "최종 완성될 product 클래스"

    def __init__(self):
        self.parts = []  # product를 구성하는 부품 목록


class Director:
    "Director 클래스 - product 조립"

    @staticmethod
    def construct():
        "product를 조립하는 메소드"
        return Builder()\
            .build_part_a()\
            .build_part_b()\
            .build_part_c()\
            .get_result()

PRODUCT = Director.construct()
print(PRODUCT.parts)
