from abc import ABCMeta, abstractmethod


class IComponent(metaclass=ABCMeta):
    """
    Leaf와 Composite들이 공통으로 가지는 인터페이스.
    부모 참조와 공통 메소드 정의 포함.
    """

    reference_to_parent = None

    @staticmethod
    @abstractmethod
    def method():
        "Leaf나 Composite가 공통으로 구현해야 하는 메소드"

    @staticmethod
    @abstractmethod
    def detach():
        "자신이 속해 있던 부모(Composite)로부터 분리될 때 호출됨"


class Leaf(IComponent):
    "Leaf는 Composite에 포함될 수 있지만, 하위 항목을 가질 수는 없음"

    def method(self):
        parent_id = (id(self.reference_to_parent)
                     if self.reference_to_parent is not None else None)
        print(f"<Leaf>\t\tid:{id(self)}\tParent:\t{parent_id}")

    def detach(self):
        "자신이 속해 있던 부모 Composite로부터 분리됨"
        if self.reference_to_parent is not None:
            self.reference_to_parent.delete(self)


class Composite(IComponent):
    "Composite는 다른 Leaf나 Composite들을 포함할 수 있음"

    def __init__(self):
        self.components = []

    def method(self):
        parent_id = (id(self.reference_to_parent)
                     if self.reference_to_parent is not None else None)
        print(f"<Composite>\tid:{id(self)}\tParent:\t{parent_id}\t"
              f"Components:{len(self.components)}")

        # 하위 요소들도 재귀적으로 호출
        for component in self.components:
            component.method()

    def attach(self, component):
        """
        기존 부모로부터 분리(detach)한 후,
        현재 Composite(self)를 새로운 부모로 설정하고 추가
        """
        component.detach()
        component.reference_to_parent = self
        self.components.append(component)

    def delete(self, component):
        "현재 Composite에서 하위 요소 제거"
        self.components.remove(component)

    def detach(self):
        "현재 Composite를 상위 Composite에서 분리"
        if self.reference_to_parent is not None:
            self.reference_to_parent.delete(self)
            self.reference_to_parent = None


LEAF_A = Leaf()
LEAF_B = Leaf()
COMPOSITE_1 = Composite()
COMPOSITE_2 = Composite()

print(f"LEAF_A\t\tid:{id(LEAF_A)}")
print(f"LEAF_B\t\tid:{id(LEAF_B)}")
print(f"COMPOSITE_1\tid:{id(COMPOSITE_1)}")
print(f"COMPOSITE_2\tid:{id(COMPOSITE_2)}")

# LEAF_A를 COMPOSITE_1에 추가
COMPOSITE_1.attach(LEAF_A)

# LEAF_A를 COMPOSITE_2로 이동 (이전 부모에서 자동 detach)
COMPOSITE_2.attach(LEAF_A)

# COMPOSITE_1 자체를 COMPOSITE_2에 포함시킴
COMPOSITE_2.attach(COMPOSITE_1)

LEAF_B.method()  # 어떤 Composite에도 속하지 않은 Leaf
COMPOSITE_2.method()  # COMPOSITE_2 아래에 LEAF_A, COMPOSITE_1 포함
