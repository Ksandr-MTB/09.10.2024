class House:
    houses_history = []

    def __new__(cls, *args, **kwargs):
        # print(*args, **kwargs)
        cls.houses_history.append(args[0])
        # print(cls.houses_history)
        return super().__new__(cls)

    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        if new_floor > self.number_of_floors or new_floor < 1:
            print('Такого этажа не сущестрвует')
        else:
            for i in range(1, new_floor + 1):
                print(i)

    def __del__(self):
        print(f'{self.name} снесён, но он останется в истории')

    def __len__(self):
        print(self.number_of_floors)

    def __str__(self):
        print(f'Название: {self.name}, кол-во этажей: {self.number_of_floors}')

    def __eq__(self, other):
        return self.number_of_floors == other.number_of_floors

    def __add__(self, value):
        self.number_of_floors += value
        # print(f'Высота {self.name} увеличилось на {value} этажей')

    def __lt__(self, other):
        return self.number_of_floors < other.number_of_floors

    def __le__(self, other):
        return self.number_of_floors <= other.number_of_floors

    def __gt__(self, other):
        return self.number_of_floors > other.number_of_floors

    def __ge__(self, other):
        return self.number_of_floors >= other.number_of_floors

    def __ne__(self, other):
        return self.number_of_floors != other.number_of_floors


h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)
del h2
del h3
print(House.houses_history)
# h1.go_to(5)
# h2.go_to(10)
# h1.__str__()
# h2.__str__()
# h1.__len__()
# h2.__len__()


# print(h1 == h2)
# h1.__add__(10)
# h1.__str__()
# print(h1 == h2)
# h1.__add__(10)
# h1.__str__()
# h2.__add__(10)
# h2.__str__()
#
# print(h1 > h2)
# print(h1 >= h2)
# print(h1 < h2)
# print(h1 <= h2)
# print(h1 != h2)
# h1.__del__()


