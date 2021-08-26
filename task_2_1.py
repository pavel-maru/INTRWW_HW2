# 1. Проверить механизм наследования в Python. Для этого создать два класса. Первый — родительский (ItemDiscount),
# должен содержать статическую информацию о товаре: название и цену. Второй — дочерний (ItemDiscountReport),
# должен содержать функцию (get_parent_data), отвечающую за отображение информации о товаре в одной строке.
# Проверить работу программы, создав экземпляр (объект) родительского класса.


class ItemDiscount:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class ItemDiscountReport(ItemDiscount):
    def get_parent_data(self):
        print(f'name: {self.name}, price: {self.price}')


child = ItemDiscountReport('soap', 34)
child.get_parent_data()