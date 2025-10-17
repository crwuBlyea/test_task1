import math
class Figure:
    def __init__(self, name: str):
        self.__name = name
    def get_name(self) -> str:
        return self.__name
    def calculate_area(self):
        pass
class Circle(Figure):
    def __init__(self, radius: float = 1):
        super().__init__("Circle")
        self.radius = radius
    @property
    def radius(self):
        return self.__radius
    @radius.setter
    def radius(self, value):
        if value >= 0:
            self.__radius = value
        else:
            raise ValueError("Radius can't be negative or zero")
    def calculate_area(self) -> float:
        return math.pi*self.radius**2

class Triangle(Figure):
    def __init__(self, side1: float = 1, side2: float = 1, side3: float = 1):
        super().__init__("Triangle")
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
    @property
    def side1(self):
        return self.__side1
    @side1.setter
    def side1(self, value: float):
        if value <= 0:
            raise ValueError("Side1 cannot be negative or zero")
        self.__side1 = value
    @property
    def side2(self):
        return self.__side2
    @side2.setter
    def side2(self, value: float):
        if value <= 0:
            raise ValueError("Side2 cannot be negative or zero")
        self.__side2 = value
    @property
    def side3(self):
        return self.__side3
    @side3.setter
    def side3(self, value: float):
        if value <= 0:
            raise ValueError("Side3 cannot be negative or zero")
        self.__side3 = value
    def calculate_area(self) -> float:
        if not self.__is_triangle_exist():
            raise ValueError("Triangle with these sides does not exist")
        semi_perimeter = (self.side1+self.side2+self.side3)/2
        return math.sqrt(semi_perimeter*(semi_perimeter - self.side1)*(semi_perimeter - self.side2)*(semi_perimeter - self.side3))
    def is_right_angled(self) -> bool:
        if not self.__is_triangle_exist():
            raise ValueError("Triangle with these sides does not exist")
        sorted_sides = sorted([self.side1,self.side2, self.side3])
        return True if sorted_sides[0]**2 + sorted_sides[1]**2 == round(sorted_sides[2]**2, 6) else False
    def __is_triangle_exist(self) -> bool:
        sorted_sides = sorted([self.side1, self.side2, self.side3])
        return True if sorted_sides[0] + sorted_sides[1] > sorted_sides[2] else False


