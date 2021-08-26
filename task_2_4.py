# 4. Реализовать возможность переустановки значения цены товара.
# Необходимо, чтобы и родительский, и дочерний классы получили новое значение цены.
# Следует проверить это, вызвав соответствующий метод родительского класса и функцию дочернего (функция,
# отвечающая за отображение информации о товаре в одной строке).


class ItemDiscount:
    def __init__(self, name, price):
        self.__name = name
        self.__price = price


class ItemDiscountReport(ItemDiscount):
    def __init__(self, name, price):
        super().__init__(name, price)
        self.__name = name
        self.__price = price

    def set_price(self, price):
        self.__price = price

    def get_parent_data(self):
        print(f'name: {self.__name}, price: {self.__price}')


child = ItemDiscountReport('soap', 34)
child.get_parent_data()
child.set_price(30)
child.get_parent_data()