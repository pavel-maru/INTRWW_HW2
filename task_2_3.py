# 3. Усовершенствовать родительский класс таким образом, чтобы получить доступ к защищенным переменным.
# Результат выполнения заданий 1 и 2 должен быть идентичным.


class ItemDiscount:
    def __init__(self, name, price):
        self.__name = name
        self.__price = price


class ItemDiscountReport(ItemDiscount):
    def __init__(self, name, price):
        super().__init__(name, price)
        self.__name = name
        self.__price = price

    def get_parent_data(self):
        print(f'name: {self.__name}, price: {self.__price}')


child = ItemDiscountReport('soap', 34)
child.get_parent_data()