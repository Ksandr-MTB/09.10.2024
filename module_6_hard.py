class Figure:
    sides_count = 0

    def __init__(self, __color, *__sides, filled=bool):
        self.__sides = __sides
        self.__color = __color
        if len(self.__sides) == 1:
            self.__sides = list(self.__sides)
            for i in range(self.sides_count - 1):
                self.__sides.append(self.__sides[0])
        elif len(self.__sides) != self.sides_count:
            self.__sides = []
            for i in range(self.sides_count):
                self.__sides.append(1)
        elif len(self.__sides) == self.sides_count and len(self.__sides) != 3:
            self.__sides = list(self.__sides)
            if sum(self.__sides) / len(self.__sides) == self.__sides[1]:
                pass
            else:
                for i in range(self.sides_count):
                    self.__sides.append(1)

    def get_color(self):
        return list(self.__color)

    def __is_valid_color(self, r, g, b):  # нужно использовать конструкцию _Figure__is_valid_color

        if -1 < r < 256 and -1 < g < 256 and -1 < b < 256 and type(r) == int and type(g) == int and type(b) == int:
            return True
        else:
            return False

    def set_color(self, r, g, b):
        valid_color = False
        if -1 < r < 256 and -1 < g < 256 and -1 < b < 256 and type(r) == int and type(g) == int and type(b) == int:
            valid_color = True
        if valid_color == True:
            self.__color = list(self.__color)
            self.__color[0] = r
            self.__color[1] = g
            self.__color[2] = b
            return self.__color  # нужно поставить return чтобы выводилось как в примере задания
        else:
            return list(self.__color)

    def __is_valid_sides(self, *args):
        if len(args) == len(self.__sides):
            qz = 0
            for i in range(len(args)):
                if type(args[i]) == int:
                    qz += 0
                else:
                    qz += 1
            if qz > 0:
                return False
            else:
                return True
        else:
            return False

    def get_sides(self):
        return (list(self.__sides))

    def set_sides(self, *new_sides):
        self.new_sides = new_sides
        if len(self.new_sides) == self.sides_count:
            self.__sides = self.new_sides

    def __len__(self):
        return sum(self.__sides)


class Circle(Figure):
    sides_count = 1

    def get_square(self):
        S = (3.14 * ((self._Figure__sides[0]) ** 2)) / 4
        return S


class Triangle(Figure):
    sides_count = 3

    def get_square(self):
        P = 0.5 * (sum(self._Figure__sides))
        S = (P * (P - self._Figure__sides[0]) * (P - self._Figure__sides[1]) * (P - self._Figure__sides[2])) ** (1 / 2)
        return S


class Cube(Figure):
    sides_count = 12

    def get_volume(self):
        V = self._Figure__sides[0] ** 3
        return V

circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())
