import copy


class Singleton():
    "싱글톤 클래스 (인스턴스가 하나만 존재해야 하는 클래스)"
    value = []

    def __new__(cls):
        "새 인스턴스를 생성할 때 호출되는 메소드"
        return cls

    # def __init__(self):
    #     print("생성자 호출됨 (init)")

    @staticmethod
    def static_method():
        "클래스 내부 변수에 접근할 필요가 없을 때 사용하는 정적 메소드"

    @classmethod
    def class_method(cls):
        "클래스 레벨 변수에 접근할 때 사용하는 클래스 메소드"
        print(cls.value)


# Singleton을 어떤 방식으로 써도 메모리 주소(id)는 모두 동일해야 한다
print(f"id(Singleton)\t= {id(Singleton)}")

OBJECT1 = Singleton()
print(f"id(OBJECT1)\t= {id(OBJECT1)}")

OBJECT2 = copy.deepcopy(OBJECT1)
print(f"id(OBJECT2)\t= {id(OBJECT2)}")

OBJECT3 = Singleton()
print(f"id(OBJECT3)\t= {id(OBJECT3)}")
