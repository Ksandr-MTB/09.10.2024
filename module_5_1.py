class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        if new_floor > self.number_of_floors or new_floor < 1:
            print('Такого этажа не сущестрвует')
        else:
            for i in range(1, new_floor + 1):
                print(i)

    def __len__(self):
        print(self.number_of_floors)

    def __str__(self):
        print(f'Название: {self.name}, кол-во этажей: {self.number_of_floors}')



h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)
h1.go_to(5)
h2.go_to(10)
h1.__str__()
h2.__str__()
h1.__len__()
h2.__len__()

# print(h1.name, h1.number_of_floors)
# print(h2.name, h2.number_of_floors)

# def exponentiation(n):
#     print(n ** 2, n ** 3)
#
#
# exponentiation(5)
