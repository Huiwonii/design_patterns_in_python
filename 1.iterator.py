from abc import (
    ABCMeta,
    abstractmethod,
)


class IIterator(metaclass=ABCMeta):
    "이터레이터 인터페이스"

    @staticmethod
    @abstractmethod
    def has_next():
        "끝에 도달했는지 여부를 반환하는 메소드 (True/False)"

    @staticmethod
    @abstractmethod
    def next():
        "다음 객체를 반환하는 메소드"


class Iterable(IIterator):
    "구체적인 이터레이터 클래스 (컬렉션을 순회 가능하게 함)"

    def __init__(self, aggregates):
        self.index = 0
        self.aggregates = aggregates

    def next(self):
        if self.index < len(self.aggregates):
            aggregate = self.aggregates[self.index]
            self.index += 1
            return aggregate
        raise Exception("AtEndOfIteratorException", "이터레이터 끝에 도달함")

    def has_next(self):
        return self.index < len(self.aggregates)


class IAggregate(metaclass=ABCMeta):
    "컬렉션 아이템들이 구현해야 하는 인터페이스"

    @staticmethod
    @abstractmethod
    def method():
        "아이템이 가져야 할 메소드"


class Aggregate(IAggregate):
    "구체적인 아이템 클래스"

    @staticmethod
    def method():
        print("이 메소드가 호출되었습니다.")


# 클라이언트 코드 (사용 예시)

# Aggregate 객체들을 담은 리스트를 생성
AGGREGATES = [Aggregate(), Aggregate(), Aggregate(), Aggregate()]

# 사실 파이썬 리스트는 이미 기본적으로 이터러블이지만,
# 여기서는 직접 만든 Iterable 클래스를 사용해서 순회하는 예제
ITERABLE = Iterable(AGGREGATES)

while ITERABLE.has_next():
    ITERABLE.next().method()
