class Vehicle:
    __COLOR_VARIANTS = ['синий', 'красный', 'черный', 'белый']
    def __init__(self, owner, __model, __engine_power, __color):
        self.owner = owner
        self.__model = __model
        self.__engine_power = __engine_power
        self.__color = __color

    def get_model(self):
        return (f'Модель: {self.__model}')

    def get_horsepower(self):
        return (f'Мощность двигателя: {self.__engine_power}')

    def get_color(self):
        return (f'Цвет: {self.__color}')

    def print_info(self):
        print (f'{self.get_model()} \n{self.get_horsepower()} \n{self.get_color()} \nВладелец: {self.owner}')

    def set_color(self, new_color):
        q = 0
        for i in range(len(self.__COLOR_VARIANTS)):
            if new_color.lower() == self.__COLOR_VARIANTS[i]:
                q = q+1
            else:
                q = q+0

        if q > 0:
            self.__color = new_color
        else:
            print(f'Нельзя сменить цвет на {new_color}.')
        # if new_color.lower in self.__COLOR_VARIANTS:
        #     self.__color = new_color
        # else:
        #     print(f'Нельзя сменить цвет на {new_color}.')


class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5

vehicle1 = Sedan('Fedos', 'Toyota Mark II', 500, 'blue')

vehicle1.print_info()

vehicle1.set_color('Pink')
vehicle1.set_color('Черный')
vehicle1.owner = 'Vasyok'

# Проверяем что поменялось
vehicle1.print_info()