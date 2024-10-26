class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'


class Shop:
    __file_name = 'products.txt'

    def get_products(self):

        self.file = open(self.__file_name, 'r')
        qq = self.file.read()
        self.file.close()
        return qq

    def add(self, *products):
        self.file = open(self.__file_name, 'r')
        qq = self.file.read()
        self.file.close()
        self.file = open(self.__file_name, 'a')
        for i in range(len(products)):
            if str(products[i]) in qq:
                print(f'Продукт {products[i]} уже есть в магазине')
            else:
                self.file.write(f'{str(products[i])} \n')
        self.file.close()


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')
print(p2)
s1.add(p1, p2, p3)
print(s1.get_products())
