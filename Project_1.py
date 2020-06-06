# Project1. Developed by Arkhipova Anastasia 19704


class Load:
    """Класс для загрузки и хранения данных"""
    barcode_dict = {}
    products_lst = []

    @classmethod
    def write_barcode(cls, fl_barcode):
        """Метод позволяет считывать данные из файлов"""
        with open(fl_barcode, encoding='utf-8') as inp_barcode:
            for code in inp_barcode:
                lst = code.split(': ')
                country = lst[0]
                value = lst[1][:-1]
                if value.count('-') == 0:
                    cls.barcode_dict[str(value)] = country
                else:
                    for number in range(int(value[:value.find('-')]),
                                        int(value[value.find('-') + 1:]) + 1):
                        if len(str(number)) == 1:
                            number = '0' + str(number)
                        cls.barcode_dict[number] = country

    @classmethod
    def write_products(cls, fl_products):
        """Метод позволяет считывать данные из файлов"""
        with open(fl_products, encoding='utf-8') as inp_products:
            for product in inp_products:
                lst = product.split(';')
                cls.products_lst.append(Products(*lst[:-1]))


class ShoppingCart:
    """Класс представляет корзину интернет-магазина"""
    all_products = []

    def __init__(self):
        """Метод инициализации"""
        ShoppingCart.all_products = []

    def __str__(self):
        """Метод строкового представления"""
        return str(ShoppingCart.all_products)

    def add_product(self, product):
        """Метод добавляет товар в корзину"""
        if product not in ShoppingCart.all_products:
            ShoppingCart.all_products.append(product)
        else:
            print('Вы уже добавили этот товар в корзину.')

    def delete_product(self, product):
        """Метод удаляет товар из корзины"""
        if product in ShoppingCart.all_products:
            ShoppingCart.all_products.pop(ShoppingCart.all_products.index(product))
        else:
            print('Такого товара нет в корзине.')

    def count_total_cost(self):
        """Метод подсчитывает общую стоимость товаров в корзине"""
        total_sum = 0
        for product in ShoppingCart.all_products:
            if product.price is None:
                return 'Невозможно посчитать сумму'
            else:
                total_sum += product.price * product.number
        return total_sum

    def count_total_number(self):
        """Метод подсчитывает количество товаров к корзине"""
        total_number = 0
        for product in ShoppingCart.all_products:
            if product.number is None:
                return 'Невозможно посчитать количество'
            else:
                total_number += product.number
        return total_number

    def count_total_cost_discount(self, discount):
        """Метод подсчитывает общую стоимость с учетом скидки"""
        if discount <= 0:
            return 'Невозможно посчитать сумму'
        total_sum = 0
        for product in ShoppingCart.all_products:
            if product.price is None:
                return 'Невозможно посчитать сумму'
            else:
                total_sum += product.price * product.number
        total_sum = total_sum - (total_sum * (discount / 100))
        return total_sum

    def output(self, fl_output):
        """Метод позволяет записать данные корзины в файл"""
        total = ''
        for product in ShoppingCart.all_products:
            total += product.name + ';'
            if product.price is None:
                total += ';'
            else:
                total += str(product.price) + ';'
            if product.number is None:
                total += ';'
            else:
                total += str(product.number) + ';'
            if product.barcode is None:
                total += ';'
            else:
                total += str(product.barcode) + ';'
            total += '\n'
        with open(fl_output, 'w', encoding='utf-8') as out:
            out.write(total)


class Products:
    """Класс представляет товар"""
    barcode_dict = Load.barcode_dict

    def __init__(self, name, price, number, barcode=None):
        """Метод инициализации"""
        self.name = name

        self.__price = price
        self.__price = self.price

        self.__number = number
        self.__number = self.number

        try:
            self.barcode = int(barcode)
            if self.barcode is None or self.barcode is '':
                self.check_digit = None
                self.product_code = None
                self.country = None
                self.manufacturer = None
            else:
                # check barcode
                if len(str(self.barcode)) != 13:
                    self.barcode = None
                    self.check_digit = None
                    self.product_code = None
                    self.country = None
                    self.manufacturer = None
                digits = '0123456789'
                for symbol in str(self.barcode):
                    if symbol not in digits:
                        self.barcode = None
                        self.check_digit = None
                        self.product_code = None
                        self.country = None
                        self.manufacturer = None
                        break
                else:
                    self.barcode = barcode
                    self.check_digit = str(self.barcode)[-1]
                    self.product_code = str(self.barcode)[7:12]
                    if str(self.barcode)[:2] in Products.barcode_dict:
                        self.country = str(self.barcode)[:2]
                        self.manufacturer = str(self.barcode)[2:7]
                    else:
                        self.country = str(self.barcode)[:3]
                        self.manufacturer = str(self.barcode)[3:7]
        except ValueError:
            self.barcode = None
            self.check_digit = None
            self.product_code = None
            self.country = None
            self.manufacturer = None
        except TypeError:
            self.barcode = None
            self.check_digit = None
            self.product_code = None
            self.country = None
            self.manufacturer = None

    def __str__(self):
        """Метод строкового представления"""
        total = ''
        total += 'Товар: ' + self.name + '\n'

        if self.__price is None:
            total += 'Цена не установлена'
        else:
            total += 'Цена: ' + str(self.__price) + '\n'

        if self.__number is None:
            total += 'Количество не установлено'
        else:
            total += 'Количество: ' + str(self.__number) + '\n'

        if self.barcode is not None:
            total += 'Производитель: ' + Products.barcode_dict[self.country] + '\n'
        return total

    def __repr__(self):
        """Метод - репорт"""
        total = 'name: ' + str(self.name)
        return total

    @property
    def price(self):
        """Цена - свойство"""
        return self.__price

    @price.getter
    def price(self):
        """Цена - геттер"""
        try:
            self.__price = float(self.__price)
            if self.__price <= 0.0:
                self.__price = None
                print('ошибка')
        except ValueError:
            self.__price = None
        if self.__price is None:
            return 'Цена не установлена.'
        else:
            return self.__price

    @price.setter
    def price(self, new_price):
        """Цена - сеттер"""
        try:
            new_price = float(new_price)
            if new_price <= 0.0:
                print('ошибка')
            else:
                self.__price = new_price
        except ValueError:
            print('ошибка')

    @property
    def number(self):
        """Количество - свойство"""
        return self.__number

    @number.getter
    def number(self):
        """Количетсво - геттер"""
        try:
            self.__number = int(self.__number)
            if self.__number <= 0:
                self.__number = None
                print('ошибка')
        except ValueError:
            self.__number = None
        if self.__number is None:
            return 'Количество не установлено.'
        else:
            return self.__number

    @number.setter
    def number(self, new_number):
        """Количество - сеттер"""
        try:
            new_number = int(new_number)
            if new_number <= 0.0:
                print('ошибка')
            else:
                self.__number = new_number
        except ValueError:
            print('ошибка')

    @staticmethod
    def calculate_discount(product, discount):
        """Статик-метод для подсчета цены со скидкой за 1 единицу"""
        if discount <= 0:
            print('ошибка')
            return product.price
        else:
            price_discount = product.price - product.price * (discount / 100)
            print('Цена со скидкой: ', end='')
            return price_discount

    def product_authenticity(self):
        """Метод определяет подлинность товара"""
        if self.barcode is None:
            return 'Значение штрих-кода не задано.'
        else:
            sum1 = 0
            sum2 = 0
            for i in range(1, len(str(self.barcode)), 2):
                sum1 += int(str(self.barcode)[i])
            sum1 = sum1 * 3
            for i in range(0, len(str(self.barcode)) - 1, 2):
                sum2 += int(str(self.barcode)[i])
            sum = 10 - ((sum1 + sum2) % 10)
            if sum == int(self.check_digit):
                return True
            else:
                return False


Load.write_barcode('EAN-13.txt')
product1 = Products('Кроссовки', 340, 2, 4820024700016)
print(product1.price)
print(Products.calculate_discount(product1, 10))
print(product1)
print(product1.product_authenticity())
print()
cart1 = ShoppingCart()
cart1.add_product(product1)
print(cart1)
cart1.delete_product(product1)
print(cart1)
print()
product2 = Products('Платье', 1050, -1, 12345678912345)
print(product2.number)
print(product2.price)
print(product2.product_authenticity())
print()
product3 = Products('Носки', 100, 5)
product4 = Products('Юбка', 2340.9, 1)
cart1.add_product(product3)
cart1.add_product(product4)
print(cart1)
print(cart1.count_total_cost())
print(cart1.count_total_cost_discount(25))
print(cart1.count_total_number())
cart1.delete_product(product3)
print(cart1)
print()
Load.write_products('products.txt')
cart2 = ShoppingCart()
for item in Load.products_lst:
    print(item)
cart2.add_product(Load.products_lst[0])
cart2.add_product(Load.products_lst[1])
print(cart2.count_total_cost())
print(cart2.count_total_cost_discount(13))
print(Load.products_lst[1].product_authenticity())
print(Load.products_lst[2].product_authenticity())
cart2.output('output_products.txt')
