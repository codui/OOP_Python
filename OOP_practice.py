# class Cat:
#     def __init__(self, name: str):
#         print(f"Кота по имени {name} создали!")
#         self.name = name
#         self.satiety = 5  # Начальное состояние сытости

#     # Метод для чтения атрибутов
#     def show_status(self):
#         print(f"Имя: {self.name}, Сытость: {self.satiety}")

#     # Метод для изменения атрибута
#     def eat(self):
#         print(f"{self.name} есть вкусняшку...")
#         # Использовать self, чтобы получить доступ к атрибуту этого же объекта
#         self.satiety = self.satiety + 3
#         print(f"Сытость {self.name} увеличилась!")


# barsik = Cat("Барсик")

# # В этот момент Python передает ссылку на 'barsik' в метод 'show_status' как 'self'.
# barsik.show_status()

# # В этот момент Python передает ссылку на 'barsik' в метод 'eat' как 'self'.
# barsik.eat()

# barsik.show_status()


"""
Как работает self:
"""


# class Player:
#     def __init__(self):
#         self.name = ""
#         self.health = 0

#     def take_damage(self, damage: int):
#         self.health -= damage


# # Создаем "пустые" объекты
# warrior = Player()
# mage = Player()

# # Вручную дадим им атрибуты (пока без __init__)
# warrior.name = "Конан"
# warrior.health = 100

# mage.name = "Гэндальф"
# mage.health = 70

# warrior.take_damage(20)
"""
Вот что происходит за кулисами.
Когда пишем код
! warrior.take_damage(20)
Python видит это и автоматически, неявно для нас, преобразует этот вызов в такой:
! Player.take_damage(warrior, 20)

Python сам берет объект, стоящий слева от точки (warrior), и передает его первым аргументом в метод take_damage.
Именно поэтому в определении метода мы обязаны предусмотреть место для этого аргумента.

И по всеобщему соглашению программистов на Python, этот первый параметр,
который принимает сам объект, всегда называется self.
"""
# print(warrior.health)  # 80


"""
Атрибуты экземпляра и атрибуты класса
"""

# class Character:
#     character_count = 0

#     def __init__(self, name):
#         self.name = name
#         self.__class__.character_count += 1


# char_1 = Character("Joe")
# print(f"{char_1.character_count=}")
# print(f"{Character.character_count=}")


# class Employee:
#     company = "Stepik"

#     def __init__(self, name, position):
#         self.name = name
#         self.position = position

#     def get_info(self):
#         return f"{self.name} работает в компании {self.__class__.company} на должности {self.position}."


# worker_1 = Employee("John", "director")
# # print(f"{worker_1.__dict__}")
# print(worker_1.get_info())


# class Config:
#     theme = "light"

#     def __init__(self, app_name):
#         self.app_name = app_name

#     def get_theme(self):
#         return self.theme


# conf1 = Config("Discord")

# conf2 = Config("Viber")
# conf2.theme = "dark"

# print(f"\n{conf1.get_theme()}")
# print(f"{conf2.get_theme()}")

# print(f"\n{conf1.get_theme()}")


"""
Публичный интерфейс.
Безопасные методы deposit (внести) и withdraw (снять), которые будут публичным интерфейсом.
"""


# class SafeBankAccount:
#     def __init__(self, owner, balance):
#         self.owner = owner
#         self.balance = balance

#     # Публичный интерфейс
#     def deposit(self, amount):
#         """Вносит деньги на счет. Сумма должна быть положительной."""
#         if amount > 0:
#             self.balance += amount
#         else:
#             print("Ошибка: сумма для пополнения должна быть положительной.")

#     def withdraw(self, amount):
#         """Снимает деньги со счета. Сумма должна быть положительной и не превышать баланс."""
#         if amount <= 0:
#             print("Ошибка: сумма для снятия должна быть положительной.")
#         elif self.balance >= amount:
#             self.balance -= amount
#             print(f"Со счета снято {amount}. Новый баланс: {self.balance}")
#         else:
#             print(f"Ошибка: недостаточно средств. Баланс: {self.balance}")

#     def get_balance(self):
#         """Возвращает текущий баланс."""
#         return self.balance


# safe_account = SafeBankAccount("Анна", 1000)

# safe_account.deposit(500)
# safe_account.withdraw(200)  # Со счета снято 200. Новый баланс: 1300
# safe_account.withdraw(1500)  # Ошибка: недостаточно средств. Баланс: 1300
# safe_account.withdraw(-100)  # Ошибка: сумма для снятия должна быть положительной.

# print(f"\nИтоговый баланс: {safe_account.get_balance()}")


# class User:
#     def __init__(self):
#         self._age = 0

#     def get_age(self):
#         return self._age

#     def set_age(self, new_age):
#         if type(new_age) is int and new_age >= 0:
#             self._age = new_age


# user_1 = User()
# print(user_1.__dict__)

# user_1.set_age(20)
# print(user_1.__dict__)


"""
Геттеры и сеттеры
"""
# class Thermostat:
#     def __init__(self, temp):
#         self._temperature = self.set_temperature(temp)

#     def get_temperature(self):
#         return self._temperature

#     def set_temperature(self, new_temp):
#         if 0 <= new_temp <= 100:
#             self._temperature = new_temp


# temperauture = Thermostat(-1)
# print(temperauture.__dict__)

# temperauture.set_temperature(100)
# print(temperauture.__dict__)


"""
Использование защищенных атрибутов (атрибуты с одним подчеркиванием self._attribute ).
"""


# class BankAccount:
#     def __init__(self, owner, balance):
#         self.owner = owner  # Публчный атрибут - имя владельца можно читать
#         # Защищенный атрибут - баланс напрямую трогать не нужно!
#         self._balance = balance

#     # --- Публичный интерфейс ---
#     def deposit(self, amount):
#         if amount > 0:
#             self._balance += amount
#             print(f"Счет пополнен. Новый баланс: {self._balance}")
#         else:
#             print("Ошибка: сумма должна быть положительной.")

#     def withdraw(self, amount):
#         if 0 < amount <= self._balance:
#             self._balance -= amount
#             print(f"Снятие успешно. Новый баланс: {self._balance}")
#         else:
#             print("Ошибка: некорректная сумма или недостаточно средств.")

#     def get_balance(self):
#         """Единственный 'официальный' способ узнать баланс."""
#         return self._balance


# account = BankAccount("Вася", 1000)
# account.deposit(500)
# print(f"Текущий баланс: {account.get_balance()}")


"""
Использование приватных атрибутов.
"""


# class DatabaseConnector:
#     def __init__(self):
#         self.is_connected = False

#     def _establish_connection(self):
#         self.is_connected = True

#     def connect(self):
#         return self._establish_connection()


# class APIClient:
#     def __init__(self, api_key):
#         self.__api_key = api_key


# class Component:
#     def __init__(self, name, version, id):
#         self.name = name
#         self._id = id
#         self.__version = version


# class Worker:
#     def __init__(self):
#         self.__salary = 50000

#     def get_info(self):
#         return f"Зарплата: {self.__salary}"

""" Пример сеттера."""


# class User:
#     def __init__(self, name, age):
#         self.name = name
#         self._age = 0  # Задать безопасное значение по умолчанию
#         # Установить переданное значение age, если пройдет валидацию в сеттере
#         self.set_age(age)

#     def get_age(self):
#         """Геттер для атрибута _age"""
#         return self._age

#     def set_age(self, new_age):
#         """Сеттер для атрибута _age. Он проверят данные перед установкой."""
#         print(f"Попытка установить возраст: {new_age}")

#         # Проверка на тип данных
#         if not isinstance(new_age, int):
#             print("Ошибка: возраст должен быть целым числом.")
#             return  # Прервать выполнение метода

#         # Проверка на диапазон значения
#         if 0 <= new_age <= 120:
#             # Если все проверки пройдены, то сохранить значение
#             self._age = new_age
#             print("Возраст успешно изменен.")
#         else:
#             # Если данные не корректные, то отклонить изменения
#             print("Ошибка: возраст должен быть в диапазоне от 0 до 120.")

#     def show_info(self):
#         print(f"Пользователь: {self.name}, Возраст: {self._age}")


# user = User("Иван", 30) # Вывод: Попытка... Возраст успешно изменен.
# user.show_info() # Пользователь: Иван, Возраст: 30
# print("---")

# # Попытка №1: Установить корректный возраст
# user.set_age(35)
# user.show_info() # Пользователь: Иван, Возраст: 35
# print("---")

# # Попытка №2: Установить некорректное (нелогичное) значение
# user.set_age(-5)
# user.show_info() # Пользователь: Иван, Возраст: 35 <-- Состояние объекта НЕ изменилось!
# print("---")

# # Попытка №3: Установить некорректный тип данных
# user.set_age("сорок")  # Попытка установить возраст: сорок
# # Ошибка: возраст должен быть целым числом.
# user.show_info() # Пользователь: Иван, Возраст: 35 <-- Состояние объекта снова НЕ изменилось!


# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self._age = 0
#         self.set_age(age)

#     def set_age(self, new_age):
#         if isinstance(new_age, (int, float)) and 0 <= new_age <= 120:
#             self._age = new_age

#     def get_age(self):
#         return self._age


"""
! При наследовании дочерний класс наследует все публичные и защищенные атрибуты и методы своего родителя.
"""
# from pprint import pprint


# class Device:
#     # Атрибут класса (публичный)
#     company = "FutureTech"

#     def __init__(self, model_name, power):
#         # Атрибуты экземпляра (публичные и защищенный)
#         self.model_name = model_name
#         self._power_level = power  # Защищенный
#         self.__secret_code = "XYZ123"  # Приватный

#     # Публичный метод
#     def turn_on(self):
#         print(f"Устройство {self.model_name} включено.")

#     # Защищенный метод
#     def _run_diagnostics(self):
#         print(f"Запуск диагностики... Уровень мощности: {self._power_level}")

#     # Приватный метод
#     def __get_secret_code(self):
#         return self.__secret_code


# class CoffeeMachine(Device):
#     """Кофемашина наследует от Устройства."""

#     def make_coffee(self):
#         print("\n--- Готовлю кофе ---")
#         # 1. Доступ к публичным членам родителя: УСПЕХ
#         print(f"Производитель: {self.company}")
#         print(f"Модель: {self.model_name}")
#         self.turn_on()  # Вызов публичного метода родителя

#         # 2. Доступ к защищенным членам родителя: УСПЕХ
#         # (Так можно делать, потому что мы "семья" - дочерний класс)
#         print(f"Текущая мощность: {self._power_level}")
#         self._run_diagnostics()  # Вызов защищенного метода родителя

#         # 3. Доступ к приватным членам родителя: ОШИБКА!
#         try:
#             print(self.__secret_code)
#         except AttributeError as e:
#             print(f"Не удалось получить доступ к __secret_code: {e}")


# car = Device("BMW", 3000)
# print(f"{car.__dict__=}")
# pprint(dir(car))

# coffe_machine_1 = CoffeeMachine("Jacobs", 1200)
# print(f"{coffe_machine_1.__dict__=}")
# pprint(dir(coffe_machine_1))


"""
Получение инициализатора родителя и добавления своих данных в инициализатор дочернего класса.
"""
# class Person:
#     def __init__(self, name):
#         self.name = name


# class Student(Person):
#     def __init__(self, name, student_id):
#         super().__init__(name)
#         self.student_id = student_id


# class Shape:
#     def __init__(self, color):
#         self.color = color

#     def get_color(self):
#         return self.color


# class Polygon(Shape):
#     def __init__(self, color, num_sides):
#         super().__init__(color)
#         self.num_sides = num_sides


# class Square(Polygon):
#     def __init__(self, color, side_length):
#         super().__init__(color, 4)
#         self.side_length = side_length


# *
# class Worker:
#     def __init__(self, name, position):
#         self._name = name
#         self._position = position


# class HRManager(Worker):
#     def get_employee_info(self):
#         return f"Имя: {self._name}, Должность: {self._position}"


"""
super() — это функция, которая возвращает "прокси-объект",
позволяющий получить доступ к методам родительского класса (суперкласса).
"""


# class Animal:
#     def __init__(self, name):
#         self.name = name
#         self.hunger_level = 10

#     def eat(self):
#         self.hunger_level -= 1
#         print(f"{self.name} ест. Уровень голода: {self.hunger_level}")


# class Dog(Animal):
#     def eat(self):
#         # 1. Сначала мы вызываем родительскую версию метода eat().
#         # Она выполнит всю свою логику (уменьшит голод и выведет сообщение).
#         super().eat()

#         # 2. А ЗАТЕМ мы добавляем нашу, уникальную для собаки, функциональность.
#         print(f"{self.name} виляет хвостом.")


# my_dog = Dog("Рекс")
# print(f"Начальный уровень голода: {my_dog.hunger_level}")

# print("\n--- Собака ест ---")
# my_dog.eat()

# print(f"\nКонечный уровень голода: {my_dog.hunger_level}")

"""
Самый частый и критически важный случай применения super() — это переопределение метода-инициализатора __init__.
"""


# class Logger:
#     def log(self, message):
#         return f"[LOG]: {message}"


# class TimestampLogger(Logger):
#     def log(self, message):
#         return super().log(message) + " (timestamp)"


# * Another Task
# class Product:
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price


# class DiscountedProduct(Product):
#     def __init__(self, name, price, discount):
#         super().__init__(name, price)
#         self.discount = discount


# * Another Task
# class Vehicle:
#     def __init__(self, brand):
#         self.brand = brand

#     def start_engine(self):
#         return "Двигатель запущен"

#     def honk(self):
#         return "Общий сигнал!"


# class Car(Vehicle):
#     def start_engine(self):
#         return f"{super().start_engine()}... Проверка систем автомобиля."

#     def honk(self):
#         return "Би-бип!"


# * Another Task
# class Product:
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price


# class DiscountedProduct(Product):
#     def __init__(self, name, price, discount):
#         super().__init__(name, price)
#         self.discount = discount

#     def get_price_with_discount(self):
#         return self.price - (self.price * self.discount / 100)


"""
! Проверка принадлежности к классу: isinstance()
! синтаксис: isinstance(объект_для_проверки, Класс_или_кортеж_классов)

isinstance(object, classinfo) — это встроенная функция, которая проверяет,
является ли object экземпляром класса classinfo или любого из его дочерних классов.
Возвращает True или False.

! isinstance() - "Этот объект принадлежит к этому семейству классов?".  isinstance(объект, класс)
"""


# class Animal:
#     pass


# class Dog(Animal):
#     pass


# rex = Dog()
# print(type(rex) is Dog)  # True
# print(type(rex) is Animal)  # False

# print(isinstance(rex, Dog))  # True
# print(isinstance(rex, Animal))  # True


"""
! issubclass(class, classinfo) — это встроенная функция, которая проверяет,
! является ли class дочерним классом (подклассом) classinfo. Возвращает True или False.
    Синтаксис: issubclass(Дочерний_класс_?, Родительский_класс_?)
Особенности:
    1. Работает с классами, а не с объектами.
В функцию передаются сами классы (их имена), а не созданные экземпляры.
    2. Считает класс потомком самого себя. issubclass(Dog, Dog) вернет True.
    Это логично, так как класс является "нулевым" потомком самого себя.

! issubclass() - "Этот класс является потомком другого класса?".    issubclass(класс, класс)
"""


# # Уровень 0 (Вершина иерархии)
# class Entity:
#     pass


# # Уровень 1
# class Animal(Entity):
#     pass


# class Plant(Entity):
#     pass


# # Уровень 2
# class Mammal(Animal):
#     pass


# class Fish(Animal):
#     pass


# # Уровень 3
# class Dog(Mammal):
#     pass


# # --- Прямое наследование ---
# print("--- Прямые потомки ---")
# print(f"Является ли Dog потомком Mammal?   {issubclass(Dog, Mammal)}")  # True
# print(f"Является ли Mammal потомком Animal? {issubclass(Mammal, Animal)}")  # True
# print(f"Является ли Animal потомком Entity? {issubclass(Animal, Entity)}")  # True

# # --- Непрямое (транзитивное) наследование ---
# # issubclass() проходит всю цепочку наверх!
# print("\n--- Дальние родственники ---")
# print(f"Является ли Dog потомком Animal?   {issubclass(Dog, Animal)}")  # True
# print(f"Является ли Dog потомком Entity?   {issubclass(Dog, Entity)}")  # True

# # --- Проверка на самого себя ---
# print("\n--- Проверка на самого себя ---")
# print(f"Является ли Dog потомком Dog?      {issubclass(Dog, Dog)}")  # True

# # --- Отрицательные проверки ---
# print("\n--- Отрицательные проверки ---")
# print(
#     f"Является ли Mammal потомком Dog?  {issubclass(Mammal, Dog)}"
# )  # False (наоборот!)
# print(
#     f"Является ли Fish потомком Mammal? {issubclass(Fish, Mammal)}"
# )  # False (они "братья")
# print(
#     f"Является ли Plant потомком Animal? {issubclass(Plant, Animal)}"
# )  # False (они "братья")


"""
При проэктировании иерархии классов нужно создать "контракт".
! "контракт" — базовый класс, который описывает, что должен уметь делать любой обработчик.
"""


# # Базовый класс (наш "контракт")
# class BaseHandler:
#     def process(self, data):
#         # Этот метод должны будут переопределить все потомки
#         raise NotImplementedError("Дочерний класс должен реализовать метод process()!")


# # Конкретные классы-обработчики
# class TextFileHandler(BaseHandler):
#     def process(self, text_data):
#         print(f"{text_data}: Обработка {len(text_data)} символов...")
#         # ... какая-то логика ...
#         return "TEXT_OK"


# class JsonHandler(BaseHandler):
#     def process(self, json_data):
#         print(f"[JSON]: Найдено ключей: {len(json_data.keys())}")
#         # ... какая-то логика ...
#         return "JSON_OK"


# text_file_handler = TextFileHandler()
# text_file_handler.process("Some interesting and important text.")


# # * Функция-"фабрика", которая будет принимать на вход данные и сама решать, какой обработчик использовать.
# # * Она будет работать с любыми типами данных, для которых у нас есть обработчик.
# # Наша "фабрика"
# def process_data(data):
#     print(f"\nПолучены данные типа: {type(data)}")

#     # Создаем экземпляры всех наших обработчиков
#     handlers = [TextFileHandler(), JsonHandler()]

#     # А теперь ищем подходящий
#     for handler in handlers:
#         # Вот здесь мы используем isinstance() для гибкости!
#         if isinstance(data, str) and isinstance(handler, TextFileHandler):
#             print("Найден обработчик для текста.")
#             return handler.process(data)
#         elif isinstance(data, dict) and isinstance(handler, JsonHandler):
#             print("Найден обработчик для JSON (словаря).")
#             return handler.process(data)

#     print("Ошибка: Подходящий обработчик не найден.")
#     return None


# # --- Тестируем ---
# text_from_file = "Это пример простого текстового файла."
# json_from_web = {"user_id": 123, "status": "active", "items": [1, 2, 3]}
# list_from_db = [10, 20, 30]

# process_data(text_from_file)
# process_data(json_from_web)
# process_data(list_from_db)  # Для этого типа у нас нет обработчика


"""
! Another class
"""


# class Document:
#     def display(self):
#         return "Отображение документа"


# class PdfDocument(Document):
#     def display(self):
#         return "Отображение PDF документа"


# class WordDocument(Document):
#     def display(self):
#         return "Отображение Word документа"


"""
! Утиная типизация - это когда у независимых объектов есть одинаковый метод.
"""


# class Fish:
#     def move(self):
#         return "Я плыву"


# class Bird:
#     def move(self):
#         return "Я лечу"


# def make_it_move(creature):
#     return creature.move()


# fish = Fish()
# bird = Bird()

# print(make_it_move(fish))
# print(make_it_move(bird))


"""
! Полиморфная функция для обработки данных
"""


# class StringSource:
#     def __init__(self, string):
#         self.string = string

#     def get_length(self):
#         return len(self.string)


# class ListSource:
#     def __init__(self, lst):
#         self.lst = lst

#     def get_length(self):
#         return len(self.lst)


# def print_source_length(source):
#     print(f"Длина источника: {source.get_length()}")


"""
! Полиморфизм встроенных операторов
"""


# def get_count(data_structure):
#     return len(data_structure)


"""
! Практический пример "Экспорт данных"
"""


# class JsonExporter:
#     def export(self, data):
#         return f"Экспорт в JSON: {data}"


# class CsvExporter:
#     def export(self, data):
#         return f"Экспорт в CSV: {data}"


# def export_data(exporter, data):
#     return exporter.export(data)


"""
Финальные задачи по ООП Часть 1:
! https://stepik.org/lesson/2010820/step/1?unit=2039017
"""


# class Vehicle:
#     vehicles_created = 0

#     def __init__(self, brand, _max_speed):
#         Vehicle.vehicles_created += 1
#         self.brand = brand
#         self._max_speed = _max_speed
#         self._mileage = 0

#     def get_max_speed(self):
#         return self._max_speed

#     def get_mileage(self):
#         return self._mileage

#     def drive(self, distance):
#         self._mileage += distance

#     def display_info(self):
#         print(
#             f"Марка: {self.brand}\nМакс. скорость: {self._max_speed} км/ч\nПробег: {self._mileage} км"
#         )


# class Car(Vehicle):
#     def __init__(self, brand, _max_speed, engine_type):
#         super().__init__(brand, _max_speed)
#         self.engine_type = engine_type

#     def display_info(self):
#         super().display_info()
#         print(f"Тип двигателя: {self.engine_type}")


# class Bicycle(Vehicle):
#     def __init__(self, brand, _max_speed, frame_material):
#         super().__init__(brand, _max_speed)
#         self.frame_material = frame_material

#     def display_info(self):
#         super().display_info()
#         print(f"Материал рамы: {self.frame_material}")


# # Создаем объекты разных классов
# tesla = Car("Tesla", 250, "Электро")
# bmw = Car("BMW", 280, "Бензин")
# trek = Bicycle("Trek", 40, "Карбон")

# # Демонстрируем полиморфизм: работаем с разными объектами через общий интерфейс
# vehicles = [tesla, bmw, trek]
# for vehicle in vehicles:
#     print("---")
#     vehicle.display_info()  # Один и тот же вызов - разное поведение
#     vehicle.drive(100)
#     print(f"Пробег после поездки: {vehicle.get_mileage()} км")

# print("\n" + "=" * 30)
# # Демонстрируем работу атрибута класса
# print(f"Всего создано транспортных средств: {Vehicle.vehicles_created}")


"""
! Another Task
"""

# class Animal:
#     pass


# class Cat(Animal):
#     pass


# class Dog(Animal):
#     pass


# def is_pet(animal_object):
#     return isinstance(animal_object, (Cat, Dog))

"""
! Another Task
"""


# class Vehicle:
#     pass


# class Car(Vehicle):
#     pass


# class Boat(Vehicle):
#     pass


# def is_land_vehicle(vehicle_class):
#     return issubclass(vehicle_class, Car)


"""
! Another task
"""


# class Shape:
#     pass


# class Circle(Shape):
#     pass


# class Square(Shape):
#     pass


# def get_shape_type(shape_object):
#     if isinstance(shape_object, Circle):
#         return "Это круг"
#     elif isinstance(shape_object, Square):
#         return "Это квадрат"
#     elif isinstance(shape_object, Shape):
#         return "Это общая фигура"

"""
! Another task
"""


# class Exception:
#     pass


# class NetworkError(Exception):
#     pass


# class HttpError(NetworkError):
#     pass


# def get_network_error_classes(classes_list):
#     return [class_ for class_ in classes_list if issubclass(class_, NetworkError)]


# classes_list = [NetworkError, HttpError]
# print(get_network_error_classes(classes_list))


"""
! Another task
"""


# class User:
#     def __init__(self, username):
#         self.username = username


# class Admin(User):
#     def __init__(self, username, access_level):
#         super().__init__(username)
#         self.access_level = access_level


# def get_user_description(user_object):
#     if isinstance(user_object, Admin):
#         return f"Администратор {user_object.username} с уровнем доступа {user_object.access_level}"
#     elif isinstance(user_object, User):
#         return f"Пользователь {user_object.username}"


# admin = Admin("Dima", "admin")
# user = User("Joe")
# print(get_user_description(admin))
# print(get_user_description(user))


"""
! Финальная задача 2:
https://stepik.org/lesson/2010820/step/2?unit=2039017
"""


# class Publication:
#     def __init__(self, title, author, year):
#         self.title = title
#         self._author = author
#         self._year = year

#     def get_info(self):
#         return f'"{self.title}" ({self._author}, {self._year})'


# class Book(Publication):
#     def __init__(self, title, _author, _year, isbn):
#         super().__init__(title, _author, _year)
#         self.isbn = isbn

#     def get_info(self):
#         return f"{super().get_info()}, ISBN: {self.isbn}"


# class Magazine(Publication):
#     def __init__(self, title, editor, year, issue_number):
#         super().__init__(title, editor, year)
#         self.issue_number = issue_number

#     def get_info(self):
#         return f'"{self.title}" (Ред. {self._author}, {self._year}), Выпуск №{self.issue_number}'


# # Создаем объекты разных классов
# book = Book("Война и мир", "Лев Толстой", 1869, "978-5-389-06254-2")
# magazine = Magazine("National Geographic", "Сьюзан Голдберг", 2021, 8)

# # Демонстрируем полиморфизм
# publications = [book, magazine]
# for pub in publications:
#     # Один и тот же вызов - разное поведение
#     print(pub.get_info())


"""
! Финальная задача 3:
https://stepik.org/lesson/2010820/step/3?unit=2039017

Иерархия Персонажей в Игре:
"""


# class Character:
#     def __init__(self, name, damage):
#         self.name = name
#         self._damage = damage
#         self._health = 100

#     def attack(self, target):
#         if hasattr(target, "take_damage"):
#             target.take_damage(self._damage)

#     def take_damage(self, amount):
#         self._health -= amount

#     def get_status(self):
#         return f"Имя: {self.name}, Здоровье: {self._health}"


# class Warrior(Character):
#     def __init__(self, name, damage, armor):
#         super().__init__(name, damage)
#         self.armor = armor

#     def take_damage(self, amount):
#         real_damage = amount - self.armor
#         if real_damage < 0:
#             real_damage = 0
#         self._health -= real_damage


# class Mage(Character):
#     def __init__(self, name, damage, mana):
#         super().__init__(name, damage)
#         self.mana = mana

#     def attack(self, target):
#         if self.mana >= 10:
#             self.mana -= 10
#             super().attack(target)


# # Создаем персонажей
# warrior = Warrior("Конан", 15, 5) # Урон 15, Броня 5
# mage = Mage("Раистлин", 20, 100) # Урон 20, Мана 100

# print(warrior.get_status())
# print(mage.get_status())
# print("--- Битва ---")

# # Маг атакует воина
# mage.attack(warrior)
# print(warrior.get_status()) # Воин должен получить 15 урона (20 - 5 брони)

# # Воин атакует мага
# warrior.attack(mage)
# print(mage.get_status()) # Маг должен получить 15 урона

# # Проверка логики мага
# mage.mana = 5 # Устанавливаем мало маны
# mage.attack(warrior)
# print(warrior.get_status()) # Здоровье воина не должно измениться


"""
! Метод __repr__: "однозначное" представление для отладки.
https://stepik.org/lesson/2022452/step/3?unit=2050875

Флаг !r в f-строках Python используется для преобразования объекта в его строковое представление,
полученное с помощью метода __repr__().
В отличие от стандартного преобразования, которое использует __str__() (обычный вывод), !r добавляет
кавычки вокруг строк и позволяет увидеть «официальное» или «отладочное» представление объекта.

    ! Основное назначение !r:
Флаг заставляет f-строку вызвать repr(obj) вместо str(obj). Это крайне полезно при отладке,
когда нужно отличить, например, строку '10' от числа 10, или увидеть экранированные символы.

! Придерживаться правил:
1. __repr__ должен возвращать строку, которая является валидным Python-кодом для воссоздания объекта (по возможности).

2. Всегда использовать флаг !r в f-строках внутри __repr__ ({self.field!r}).
Это гарантирует правильную расстановку кавычек для строк и корректное отображение других типов данных.

3. Реализовывать __repr__ в своих классах всегда — это значительно упростит отладку.
__str__ добавлять по необходимости.
"""


# class User:
#     def __init__(self, username, email):
#         self.username = username
#         self.email = email

#     def __str__(self):
#         # "Человекочитаемое" представление
#         return f"Пользователь {self.username}"

#     def __repr__(self):
#         # "Однозначное" представление для разработчика
#         # Обратите внимание на !r после имен атрибутов
#         # ! Флаг !r в f-строке принудительно вызывает функцию repr() для подставляемой переменной,
#         # ! вместо стандартной str().

#         # ! В моем понимании флаг !r добавляет кавычки и позволяет получить данные в виде объекта.
#         return f"User(username={self.username!r}, email={self.email!r})"
#         # return f"User(username={self.username}, email={self.email})"


# user_1 = User("Rambo", "rambo@email.com")
# print(user_1, type(user_1))  # Пользователь Rambo <class '__main__.User'>

# user_2 = eval(repr(user_1))
# print(user_2, type(user_2))  # Пользователь Rambo <class '__main__.User'>

# # ! Печать контейнера использует __repr__ для своих элементов
# user_lst = [user_1, user_2]
# print(user_lst)  # * [User(username='Rambo', email='rambo@email.com')]


"""
Another task about __repr__
"""


# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def __repr__(self):
#         return f"{self.__class__.__name__}(x={self.x!r}, y={self.y!r})"


# class Order:
#     def __init__(self, order_id, amount):
#         self.order_id = order_id
#         self.amount = amount

#     def __str__(self):
#         return f"Заказ №{self.order_id}"

#     def __repr__(self):
#         return f"{self.__class__.__name__}(order_id={self.order_id!r}, amount={self.amount!r})"


# class Transaction:
#     def __init__(self, amount: int | float, currency: str):
#         self.amount = amount
#         self.currency = currency

#     def __str__(self):
#         return f"Транзакция на сумму {self.amount:.2f} {self.currency}"


# trans = Transaction(200, "RUB")
# print(trans)


"""
! Задача 1: Сложение векторов (__add__)
https://stepik.org/lesson/2022453/step/5?unit=2050876
"""


# class Vector:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def __repr__(self):
#         return f"{self.__class__.__name__}({self.x!r}, {self.y!r})"

#     def __add__(self, other):
#         if not isinstance(other, Vector):
#             return NotImplemented
#         new_x = self.x + other.x
#         new_y = self.y + other.y
#         return self.__class__(new_x, new_y)


"""
! Задача 2: Сравнение объектов (__eq__)
https://stepik.org/lesson/2022453/step/6?unit=2050876
"""


# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def __eq__(self, other):
#         if not isinstance(other, self.__class__):
#             return False
#         return self.name == other.name and self.age == other.age


"""
! Задача 3: Получение длины (__len__)
https://stepik.org/lesson/2022453/step/7?unit=2050876
"""


# class Playlist:
#     def __init__(self, title: str, songs: list[str]):
#         self.title = title
#         self.songs = songs

#     def __len__(self):
#         return len(self.songs)


"""
! Задача 4: Доступ по индексу (__getitem__)
https://stepik.org/lesson/2022453/step/8?unit=2050876
"""


# class Grades:
#     def __init__(self):
#         self._grades = {"math": 5, "history": 4}

#     def __getitem__(self, subject: str):
#         if subject not in self._grades and type(subject) is not str:
#             raise KeyError
#         return self._grades[subject]


"""
! Задача 5: Сортировка объектов (__lt__)
https://stepik.org/lesson/2022453/step/9?unit=2050876
"""


# class Item:
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price

#     def __repr__(self):
#         return f'{self.__class__.__name__}({self.name!r}, {self.price!r})'

#     def __lt__(self, other):
#         if not isinstance(other, self.__class__):
#             return NotImplemented
#         return self.price < other.price


"""
! Задача 1: Простой @property (Только для чтения):
! Превратить метод-геттер в атрибут "только для чтения" с помощью декоратора @property.
https://stepik.org/lesson/2022454/step/4?unit=2050877
"""


# class Circle:
#     def __init__(self,  radius):
#         self._radius = radius

#     @property
#     def area(self):
#         """Здесь area работает как атрибут только для чтения.
#         Попытка присвоить значение через area - приведёт к ошибке. """
#         return 3.14159 * self._radius ** 2


# circle = Circle(5)
# print(circle.area)


"""
# ! Задача 2: @property и @*.setter
https://stepik.org/lesson/2022454/step/5?unit=2050877
"""


# class Temperature:
#     def __init__(self):
#         self._celsius = 0

#     @property
#     def celsius(self):
#         return self._celsius

#     @celsius.setter
#     def celsius(self, new_celsius):
#         if new_celsius > -273.15:
#             self._celsius = new_celsius


"""
# ! Задача 3: Вычисляемое свойство
https://stepik.org/lesson/2022454/step/6?unit=2050877
"""


# class Rectangle:
#     def __init__(self,  width, height):
#         self.width = width
#         self.height = height

#     @property
#     def area(self):
#         return self.width * self.height


"""
# ! Задача 4: Сеттер с преобразованием типа
https://stepik.org/lesson/2022454/step/7?unit=2050877
"""


# class Config:
#     def __init__(self):
#         self._port = 80

#     def __repr__(self):
#         return f"{self.__class__.__name__}({self._port!r})"

#     @property
#     def port(self):
#         return self._port

#     @port.setter
#     def port(self, new_port):
#         try:
#             self._port = int(new_port)
#         except Exception:
#             pass


# config = Config()
# print(config)

# config.port = "abc"
# print(config)


"""
# ! Задача 5: Полный цикл: два связанных свойства
https://stepik.org/lesson/2022454/step/8?unit=2050877
"""


# class Converter:
#     def __init__(self):
#         self._meters = 0

#     @property
#     def meters(self):
#         return self._meters

#     @meters.setter
#     def meters(self, new_meters):
#         self._meters = new_meters

#     @property
#     def kilometers(self):
#         return self._meters / 1000

#     @kilometers.setter
#     def kilometers(self, new_kmeters):
#         self._meters = new_kmeters * 1000


"""
# ! 1.6 __slots__: Оптимизация памяти и производительности.
https://stepik.org/lesson/2026571/step/1?unit=2055051

# ! Шаг 2: Введение в __slots__: синтаксис и основной эффект
https://stepik.org/lesson/2026571/step/2?unit=2055051

__slots__ — это атрибут класса, которому присваивается кортеж (или список) строк с именами атрибутов,
которые будут иметь экземпляры этого класса.
"""

# !
# class MyClass:
#     # ! Объявление что у экземпляров этого класса будут только атрибуты 'attr1' и 'attr2'
#     __slots__ = ('attr1', 'attr2')

#     def __init__(self, val1, val2):
#         self.attr1 = val1
#         self.attr2 = val2


"""
__slots__ — это инструмент оптимизации.

Использование __slots__ привело к двум ключевым изменениям в поведении:
1. __dict__ исчез. Python больше не создает этот словарь для каждого экземпляра,
    что и приводит к экономии памяти.
2. Набор атрибутов стал фиксированным. Мы больше не можем добавлять новые атрибуты к объекту после его создания.
    Попытка сделать это приводит к AttributeError.

# ! Проблемы с множественным наследованием:
# ! Использование __slots__ в иерархиях с множественным наследованием может быть сложным.

Используйте __slots__, когда выполняются оба следующих условия:

1. Вы планируете создавать огромное количество экземпляров.
"Огромное" — это не 100 и даже не 1000. Речь идет о сотнях тысяч, миллионах или даже десятках миллионов объектов, которые должны одновременно находиться в памяти.

2. Класс является простой "структурой данных" с фиксированным набором атрибутов.
Класс не имеет сложной логики и служит в основном для хранения небольшого, заранее известного набора данных.

# ! Идеальные кандидаты для __slots__:

# !     Графические и научные вычисления:
# ! Point(x, y)
# ! Vector(x, y, z)
# ! Particle(mass, charge, position)

# !     Обработка больших объемов данных:
# ! Классы, представляющие одну строку из большой таблицы или CSV-файла, которую вы загрузили в память.
# ! Record(field1, field2, ...)

# !     Сетевые приложения:
# ! Простые объекты для передачи данных (DTO), представляющие, например, узел в дереве JSON-ответа.

# ! В этих случаях экономия памяти от __slots__ будет максимальной и оправданной.
"""


# # Класс 1: Обычный, с __dict__
# class PointWithDict:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y


# # Класс 2: Оптимизированный, со __slots__
# class PointWithSlots:
#     # Объявляем фиксированный набор атрибутов
#     __slots__ = ("x", "y")

#     def __init__(self, x, y):
#         self.x = x
#         self.y = y


# # --- Тестируем обычный класс ---
# print("--- PointWithDict ---")
# p_dict = PointWithDict(10, 20)
# print(f"Атрибуты: x={p_dict.x}, y={p_dict.y}")

# # У него есть __dict__
# print(f"__dict__: {p_dict.__dict__}")

# # Мы можем добавлять новые атрибуты на лету
# p_dict.z = 30
# print(f"Новый атрибут z: {p_dict.z}")
# print(f"__dict__ после добавления: {p_dict.__dict__}")


# # --- Тестируем класс со слотами ---
# print("\n--- PointWithSlots ---")
# p_slots = PointWithSlots(10, 20)
# print(f"Атрибуты: x={p_slots.x}, y={p_slots.y}")

# # Попытка получить доступ к __dict__
# try:
#     print(p_slots.__dict__)
# except AttributeError as e:
#     print(f"Попытка доступа к __dict__: Ошибка! {e}")

# # Попытка добавить новый атрибут
# try:
#     p_slots.z = 30
# except AttributeError as e:
#     print(f"Попытка добавить новый атрибут: Ошибка! {e}")
# print(p_slots.__slots__, type(p_slots.__slots__))  # ('x', 'y') <class 'tuple'>


"""
# ! Задача 1: Простейшее использование __slots__
https://stepik.org/lesson/2026571/step/5?unit=2055051
"""


# class Point:
#     __slots__ = ("x", "y")

#     def __init__(self, x, y):
#         self.x = x
#         self.y = y


"""
# ! Задача 2: Фиксированный набор атрибутов
https://stepik.org/lesson/2026571/step/6?unit=2055051
"""


# class User:
#     __slots__ = ("username")

#     def __init__(self, username) -> None:
#         self.username = username


"""
# ! Задача 3: Наследование и __slots__:
    Если родительский класс использует __slots__ (и не имеет __dict__),
    а дочерний класс не определяет свой собственный __slots__,
    то экземпляры дочернего класса снова получат стандартный __dict__.
https://stepik.org/lesson/2026571/step/7?unit=2055051
"""


# class Base:
#     __slots__ = "x"

#     def __init__(self, x):
#         self.x = x


# class Child(Base):
#     pass


# base_class = Base(5)
# child_class = Child(10)

# try:
#     print(base_class.__dict__)
# except Exception as err:
#     print(f"Ошибка: {err}")  # ! Ошибка: 'Base' object has no attribute '__dict__'

# try:
#     # ! В дочернем классе существует __dict__, что и требовалось доказать
#     print(child_class.__dict__)  # {}
# except Exception as err:
#     print(f"Ошибка: {err}")


"""
# ! Задача 4: Расширение __slots__ при наследовании:
    Чтобы сохранить оптимизацию по памяти в дочернем классе, он должен сам определить __slots__.
    При этом в дочернем __slots__ нужно указывать только новые, добавляемые атрибуты, а не повторять родительские.
https://stepik.org/lesson/2026571/step/8?unit=2055051
"""


# class GameObject:
#     __slots__ = ('x', 'y')

#     def __init__(self, x, y):
#         self.x = x
#         self.y = y


# class Player(GameObject):
#     __slots__ = ('nickname')

#     def __init__(self, x, y, nickname):
#         super().__init__(x, y)
#         self.nickname = nickname


# gameobj = GameObject(5, 10)
# player = Player(7, 777, 'Arrakis')

# try:
#     print(f"{gameobj.__dict__=}")
# except Exception as err:
#     print(f"Ошибка: {err}")  # ! Ошибка: 'GameObject' object has no attribute '__dict__'

# try:
#     print(f"{player.__dict__=}")
# except Exception as err:
#     print(f"Ошибка: {err}")  # ! Ошибка: 'Player' object has no attribute '__dict__'


"""
# ! Задача 5: __slots__ и __dict__ вместе:
    Иногда требуется компромисс: оптимизировать хранение известных атрибутов через __slots__,
    но сохранить возможность добавлять новые, динамические атрибуты.
    Этого можно достичь, добавив строку '__dict__' в сам __slots__.
https://stepik.org/lesson/2026571/step/9?unit=2055051
"""


# class FlexibleObject:
#     __slots__ = ('fixed_attribute', '__dict__')

#     def __init__(self, value):
#         self.fixed_attribute = value


# flex_obj = FlexibleObject("Fixed attribute.")

# print(f"flex_obj.__dict__: {flex_obj.__dict__}")  # ! flex_obj.__dict__: {}
# print(f"flex_obj.__slots__: {flex_obj.__slots__}")  # ! flex_obj.__slots__: ('fixed_attribute', '__dict__')


"""
# ! 2.1 Методы класса (@classmethod).
# ! Отличие от обычных методов: параметр cls вместо self

Метод класса (@classmethod) создается с помощью декоратора @classmethod.
- Он привязан не к объекту, а к самому классу.
- Вместо self он всегда получает cls — ссылку на сам класс.
- он нужен для работы с состоянием класса (общие атрибуты) или для создания новых экземпляров.
https://stepik.org/lesson/2022455/step/1?unit=2050878
"""


# class MyClass:
#     def instance_method(self):
#         # 'self' - это конкретный объект, например, 'obj1'
#         print(f"Это обычный метод, вызванный у объекта {self}")


# obj1 = MyClass()
# # Стандартный вызов:
# obj1.instance_method()
# # Python неявно делает так: MyClass.instance_method(obj1)


# # ! Пример @classmethod
# class MyClass:
#     # Атрибут класса
#     class_attribute = "Я принадлежу классу"

#     def __init__(self, instance_attribute):
#         self.instance_attribute = instance_attribute

#     # --- Обычный метод ---
#     def instance_method(self):
#         """Работает с 'self' (объектом)."""
#         print(f"Атрибут экземпляра: {self.instance_attribute}")

#     # --- Метод класса ---
#     @classmethod
#     def class_method(cls):
#         """Работает с 'cls' (классом)."""
#         # 'cls' здесь - это сам класс MyClass
#         print(f"Это метод класса {cls}")
#         print(f"Атрибут класса: {cls.class_attribute}")


# # Создаем объект
# obj = MyClass("Я принадлежу объекту")

# print("--- Обычный метод ---")
# obj.instance_method()
# # Если попытаться вызвать через класс без аргументов:
# # MyClass.instance_method()
# # Ошибка! TypeError: пропущен обязательный аргумент 'self'

# print("\n--- Метод класса ---")
# # Способ 1: Через сам класс (Основной способ)
# MyClass.class_method()

# # Способ 2: Через объект (Тоже сработает)
# obj.class_method()


"""
# ! Основное применение: создание "альтернативных конструкторов".

# ! У методов класса есть очень мощное и частое применение — создание "альтернативных конструкторов"
# ! или же "фабричных методов", как их еще называют.
https://stepik.org/lesson/2022455/step/2?unit=2050878

! @classmethod идеально подходит для создания методов, которые возвращают экземпляр самого класса,
! но используют для этого логику, отличную от основного __init__.
! Это их самое главное и самое мощное применение.
"""


# class Date:
#     def __init__(self, day, month, year):
#         self.day = day
#         self.month = month
#         self.year = year

#     def __str__(self):
#         return f"{self.day:02d}.{self.month:02d}.{self.year}"

#     # --- Вот наш альтернативный конструктор ---
#     @classmethod
#     def from_string(cls, date_string):
#         """
#         Создает объект Date из строки формата 'ДД-ММ-ГГГГ'.
#         'cls' здесь - это сам класс Date.
#         """
#         # 1. Разбираем строку на части
#         day, month, year = map(int, date_string.split("-"))

#         # 2. Используем 'cls' для создания и возврата нового экземпляра
#         return cls(day, month, year)


# # 1. Основной способ, через __init__
# d1 = Date(25, 12, 2023)
# print(f"Создан через __init__: {d1}")

# # 2. Альтернативный способ, через наш @classmethod
# date_as_string = "28-10-2025"
# d2 = Date.from_string(date_as_string)
# print(f"Создан из строки '{date_as_string}': {d2}")


"""
! Практический пример: создаем класс Date.

! Это паттерн ("фабричный метод класса"), он является
! одним из самых мощных и часто используемых в объектно-ориентированном Python.

https://stepik.org/lesson/2022455/step/3?unit=2050878
"""


# class Date:
#     """
#     Класс для представления и работы с датами.
#     """

#     # --- 1. Основной конструктор ---
#     def __init__(self, day, month, year):
#         """
#         Инициализирует объект Date из трех целых чисел.
#         Это основной способ создания.
#         """
#         print(f"-> Вызван __init__ с ({day}, {month}, {year})")
#         self.day = day
#         self.month = month
#         self.year = year

#     # --- Метод для красивого вывода ---
#     def __str__(self):
#         """Возвращает дату в формате ДД.ММ.ГГГГ."""
#         return f"{self.day:02d}.{self.month:02d}.{self.year}"  # :02d - форматирует, добавляя 0 к числу

#     # --- 2. Альтернативный конструктор (фабричный метод) ---
#     @classmethod
#     def from_string(cls, date_string):
#         """
#         Создает и возвращает объект Date из строки формата 'ДД-ММ-ГГГГ'.

#         Параметры:
#         cls: ссылка на сам класс Date (передается автоматически)
#         date_string: строка с датой, например, "28-10-2025"
#         """
#         print(f"-> Вызван @classmethod from_string с '{date_string}'")

#         # Шаг A: Разбираем строку на компоненты
#         day_str, month_str, year_str = date_string.split("-")

#         # Шаг B: Преобразуем компоненты в числа
#         day = int(day_str)
#         month = int(month_str)
#         year = int(year_str)

#         # Шаг C: Используем 'cls' для вызова основного конструктора __init__
#         # и создаем новый экземпляр. 'cls' здесь эквивалентно 'Date'.
#         # Эта строка эквивалентна: return Date(day, month, year)
#         return cls(day, month, year)


# print("--- Способ 1: Создание через __init__ ---")
# # Мы напрямую вызываем конструктор
# new_year_eve = Date(2, 1, 2023)
# print(f"Полученный объект: {new_year_eve}\n")


# print("--- Способ 2: Создание через @classmethod ---")
# # Мы вызываем метод класса
# some_day_str = "01-09-2024"
# first_day_of_autumn = Date.from_string(some_day_str)
# print(f"Полученный объект: {first_day_of_autumn}")


"""
! Задача 1: Простой @classmethod
https://stepik.org/lesson/2022455/step/4?unit=2050878
"""


# class GameCharacter:
#     def __init__(self, name, level):
#         self.name = name
#         self.level = level

#     @classmethod
#     def create_default_character(cls):
#         return cls(name="Guest", level=1)

"""
! Задача 2: Создание из строки (from_string)
https://stepik.org/lesson/2022455/step/5?unit=2050878
"""


# class User:
#     def __init__(self, username, email) -> None:
#         self.username = username
#         self.email = email

#     @classmethod
#     def from_string(cls, user_data_string):
#         """
#         Метод принимает строку в формате "username,email"
#         """
#         try:
#             username, email = user_data_string.split(",")
#             return cls(username, email)
#         except Exception as err:
#             print(f"Ошибка: {err}")


"""
! Задача 3: Создание из словаря (from_dict):
! Еще один популярный сценарий — создание объекта из словаря (например, полученного из JSON).
https://stepik.org/lesson/2022455/step/6?unit=2050878
"""


# class Product:
#     def __init__(self, name, price) -> None:
#         self.name = name
#         self.price = price

#     def __repr__(self):
#         return f"{self.__class__.__name__}({self.name!r}, {self.price!r})"

#     @classmethod
#     def from_dict(cls, product_dict):
#         try:
#             name, price = product_dict.get('name', 'John'), product_dict.get('price', 500)
#             return cls(name, price)
#         except Exception as err:
#             print(f"Ошибка: {err}")


"""
! Задача 4: @classmethod и атрибуты класса
https://stepik.org/lesson/2022455/step/7?unit=2050878
"""


# class Car:
#     total_cars = 0

#     def __init__(self, brand, model) -> None:
#         self.brand = brand
#         self.model = model
#         self.__class__.total_cars += 1

#     def __repr__(self):
#         return f"{self.__class__.__name__}({self.brand!r}, {self.model!r})"

#     @classmethod
#     def get_total_cars(cls):
#         return cls.total_cars


# car = Car("BMW", "X7")
# print(car, car.get_total_cars())

# car2 = Car("Porshe", "911")
# print(car2, car2.get_total_cars())


"""
! Задача 5: @classmethod в иерархии
https://stepik.org/lesson/2022455/step/8?unit=2050878
"""


# class Website:
#     @classmethod
#     def get_description(cls):
#         return "Это общий сайт."


# class Shop(Website):
#     @classmethod
#     def get_description(cls):
#         return "Это интернет-магазин."


# site = Website.get_description()
# shop = Shop.get_description()
# print(site)
# print(shop)


"""
! Что такое статический метод - функция "внутри" класса, которая не зависит ни от self, ни от cls.

! Статический метод нужен для размещения вспомогательных функций-утилит, которые логически связаны с классом,
! но для своей работы не требуют доступа ни к состоянию объекта, ни к состоянию класса.
https://stepik.org/lesson/2022456/step/1?unit=2050879
https://stepik.org/lesson/2022456/step/2?unit=2050879
"""


# class User:
#     def __init__(self, username, email):
#         self.username = username
#         # Теперь мы вызываем нашу "внутреннюю" утилиту
#         if self.__class__.is_valid_email_format(email):
#             self.email = email
#         else:
#             raise ValueError("Некорректный формат email")

#     def __str__(self):
#         return f"User({self.username}, {self.email})"

#     # --- Вот наша вспомогательная утилита ---
#     @staticmethod
#     def is_valid_email_format(email_string):
#         """
#         Проверяет, содержит ли строка символ '@'.
#         Это статический метод, он не зависит ни от какого User.
#         """
#         print(f"Проверка email: '{email_string}'")
#         # Простая проверка для примера
#         return isinstance(email_string, str) and "@" in email_string


# # # ! 1-й вариант использования
# # user1 = User("Alex", "alex@stepik.org")  # Работает
# # user2 = User("Bob", "bob_at_stepik.org")  # ValueError


# # ! 2-й вариант использования
# # 1. Использование внутри класса (как в __init__)
# print("--- Создаем пользователя ---")
# user1 = User("Alex", "alex@stepik.org")
# print(user1)

# try:
#     print("\n--- Пытаемся создать пользователя с неверным email ---")
#     user2 = User("Bob", "bob_at_stepik.org")
# except ValueError as e:
#     print(f"Поймали ошибку: {e}")

# # 2. Использование снаружи класса (как самостоятельной утилиты)
# print("\n--- Используем метод как утилиту ---")
# is_ok = User.is_valid_email_format("test@test.com")
# print(f"test@test.com - это корректный формат? {is_ok}")

# is_bad = User.is_valid_email_format("просто_текст")
# print(f"просто_текст - это корректный формат? {is_bad}")


"""
! Практический пример: класс-библиотека MathUtils.

! Один из самых чистых и понятных сценариев использования статических методов —
! это создание классов-библиотек или классов-пространств имен.
https://stepik.org/lesson/2022456/step/3?unit=2050879

! Этот паттерн (класс-библиотека со статическими методами) очень часто применяется для группировки связанных функций:
! StringUtils для работы со строками,
! FileUtils для работы с файлами,
! ValidationUtils для валидации данных и так далее.
"""


# class MathUtils:
#     """
#     Класс-библиотека, содержащий полезные математические утилиты.
#     Нам не нужно создавать экземпляры этого класса.
#     """
#     @staticmethod
#     def average(numbers):
#         """Вычисляет среднее значение списка чисел."""
#         if not numbers:
#             return 0
#         return sum(numbers) / len(numbers)

#     @staticmethod
#     def factorial(n):
#         """Вычисляет факториал числа."""
#         if not isinstance(n, int) or n < 0:
#             raise ValueError("Факториал определен только для неотрицательных целых чисел")
#         if n == 0:
#             return 1
#         else:
#             res = 1
#             for i in range(1, n + 1):
#                 res *= i
#             return res

#     @staticmethod
#     def power(base, exp):
#         """Возводит число в степень."""
#         return base ** exp
"""
Теперь не нужно создавать объект mu = MathUtils().
Просто использовать сам класс как "контейнер" или "пространство имен" для вызова наших утилит.
! Это делает код очень чистым и организованным.
"""

"""
! Задача 1: Простая утилита
https://stepik.org/lesson/2022456/step/5?unit=2050879
"""


# class Formatter:
#     @staticmethod
#     def format_email(email):
#         if isinstance(email, str):
#             return email.strip().lower()


# print(Formatter.format_email(" STOPWAR@mail.com  "))


"""
! Задача 2: Класс-библиотека
https://stepik.org/lesson/2022456/step/6?unit=2050879
"""


# class Validator:
#     @staticmethod
#     def is_positive(number):
#         if isinstance(number, int):
#             return number > 0
#         return "Ошибка. Это не число!"

#     @staticmethod
#     def is_even(number):
#         if isinstance(number, int):
#             return number % 2 == 0


# print(Validator.is_positive(5))
# print(Validator.is_even(7))


"""
! Задача 3: Использование статического метода внутри класса
https://stepik.org/lesson/2022456/step/7?unit=2050879
"""


# class Circle:
#     def __init__(self, radius):
#         if Circle._is_valid_radius(radius):
#             self.radius = radius
#         else:
#             raise ValueError("Некорректный радиус")

#     def __repr__(self) -> str:
#         return f"{self.__class__.__name__}({self.radius!r})"

#     @staticmethod
#     def _is_valid_radius(radius):
#         return isinstance(radius, (int, float)) and radius > 0


# circle = Circle(5)
# print(circle)


"""
! Задача 4: Сравнение всех трех типов методов
https://stepik.org/lesson/2022456/step/8?unit=2050879
"""


# class Counter:
#     total_count = 0

#     def __init__(self) -> None:
#         self.instance_count = 0
#         self.__class__.total_count += 1

#     def increment(self):
#         self.instance_count += 1

#     @classmethod
#     def get_total_count(cls):
#         return cls.total_count

#     @staticmethod
#     def get_description():
#         return "Это класс для подсчета."


"""
! Задача 5: Практический пример: DateConverter
https://stepik.org/lesson/2022456/step/9?unit=2050879
"""


# class DateConverter:
#     @staticmethod
#     def to_iso_format(date_string):
#         """Принимает дату в формате "ДД.ММ.ГГГГ" (например, "25.12.2023")
#         и возвращает ее в формате ISO "ГГГГ-ММ-ДД" (например, "2023-12-25")"""
#         date, month, year = date_string.split(".")
#         return f"{year}-{int(month):02d}-{int(date):02d}"

#     @staticmethod
#     def from_iso_format(date_string):
#         """Принимает дату в формате "ГГГГ-ММ-ДД" и возвращает ее в формате "ДД.ММ.ГГГГ"."""
#         year, month, date = date_string.split("-")
#         return f"{int(date):02d}.{int(month):02d}.{year}"


# date_1 = "1.2.2023"
# date_2 = "2023-1-2"
# res_date1 = DateConverter.to_iso_format(date_1)
# res_date2 = DateConverter.from_iso_format(date_2)
# print(f"Was {date_1} - now: {res_date1}")
# print(f"Was {date_2} - now: {res_date2}")


"""
! Наследование представляет тип связи (отношение) - "является" (is-a)
    Dog is a Animal
    Car is a Vehicle

! Композиция представляет тип связи (отношение) - "состоит из" или "имеет" (is-composed-of или has-a).
    Man has a Heart
    Comp has a Processor

! Композиция — это техника проектирования, при которой один сложный объект
! состоит из одного или нескольких других, более простых объектов.
https://stepik.org/lesson/2022457/step/2?unit=2050880
"""


# # ! 1. Сначала определяем независимые "компоненты":
# class Engine:
#     """Компонент: Двигатель"""

#     def start(self):
#         print("Двигатель запущен.")

#     def stop(self):
#         print("Двигатель остановлен.")


# class Wheel:
#     """Компонент: Колесо"""

#     def rotate(self):
#         print("Колесо вращается.")


# # ! 2. Затем создаем класс-"контейнер", который их использует:
# class Car:
#     """Контейнер: Машина. Машина ИМЕЕТ двигатель и колеса."""

#     def __init__(self, model):
#         self.model = model

#         # --- Вот и вся композиция! ---
#         # Мы создаем экземпляры других классов ПРЯМО ВНУТРИ __init__
#         # и сохраняем их в атрибуты.
#         self.engine = Engine()  # Car HAS-A Engine
#         self.wheels = [Wheel(), Wheel(), Wheel(), Wheel()]  # Car HAS-A list of Wheels

#     def start_car(self):
#         """Машина делегирует запуск своему двигателю."""
#         print(f"Запускаем машину {self.model}...")
#         self.engine.start()

#     def stop_car(self):
#         """Машина делегирует остановку своему двигателю."""
#         self.engine.stop()

#     def drive(self):
#         """Машина делегирует вращение своим колесам."""
#         print("Машина едет...")
#         for wheel in self.wheels:
#             wheel.rotate()


# # --- Тестируем ---
# my_car = Car("Tesla")
# my_car.start_car()
# my_car.drive()
# my_car.stop_car()


"""
! Преимущества композиции и девиз "Предпочитайте композицию наследованию"
https://stepik.org/lesson/2022457/step/3?unit=2050880
"""

# class Engine:
#     def start(self): print("Двигатель (150 л.с.) запущен.")

# class SportEngine(Engine): # SportEngine IS-A Engine
#     def start(self): print("Спортивный двигатель (500 л.с.) взревел!")

# class Car:
#     def __init__(self, model, engine):
#         self.model = model
#         self.engine = engine # Мы получаем двигатель извне!

#     def start_car(self):
#         self.engine.start()

# # --- Демонстрация гибкости ---
# standard_engine = Engine()
# my_car = Car("Ford", standard_engine)
# my_car.start_car() # Вывод: Двигатель (150 л.с.) запущен.

# # А теперь "тюнингуем" машину, просто заменив один атрибут!
# print("\n--- Производим тюнинг ---")
# sport_engine = SportEngine()
# my_car.engine = sport_engine
# my_car.start_car() # Вывод: Спортивный двигатель (500 л.с.) взревел!


"""
! Задача 1: Простое отношение "has-a"
https://stepik.org/lesson/2022457/step/4?unit=2050880
"""


# class Brain:
#     pass


# class Person:
#     def __init__(self, name) -> None:
#         self.name = name
#         self.brain = Brain()

#     def __repr__(self) -> str:
#         data_obj_as_str = ""
#         for key, value in self.__dict__.items():
#             data_obj_as_str = data_obj_as_str + f"{value!r}, "
#         return f"{type(self).__name__}({data_obj_as_str.strip(', ')})"


# person = Person("John")
# print(person)


"""
! Задача 2: Делегирование вызова.
Условие:
    Заставить наши составные объекты взаимодействовать.
    Класс-контейнер должен "просить" свой компонент выполнить действие.
https://stepik.org/lesson/2022457/step/5?unit=2050880
"""


# class CPU:
#     def calculate(self):
#         return "Вычисления..."


# class Computer:
#     def __init__(self) -> None:
#         self.cpu = CPU()

#     def run(self):
#         return self.cpu.calculate()


# comp = Computer()
# print(f"{comp.run()}")


"""
! Задача 3: Композиция из нескольких объектов.
Условие:
    Сложный объект может состоять из нескольких разных компонентов.
https://stepik.org/lesson/2022457/step/6?unit=2050880
"""


# class Engine:
#     def start(self):
#         return "Двигатель запущен"


# class Wheels:
#     def rotate(self):
#         return "Колеса вращаются"


# class Car:
#     def __init__(self) -> None:
#         self.engine = Engine()
#         self.wheels = Wheels()

#     def drive(self):
#         return f"{self.engine.start()} и {self.wheels.rotate()}"


"""
! Задача 4: Композиция со списком объектов.
Условие:
    Объект может содержать не один компонент, а целый список.
https://stepik.org/lesson/2022457/step/7?unit=2050880
"""


# class Chapter:
#     def __init__(self, title: str) -> None:
#         self.title = title

#     def get_title(self):
#         return self.title

#     def parse_object(self):
#         obj_as_str = ""
#         for value in self.__dict__.values():
#             obj_as_str = obj_as_str + f"{value}, "
#         return obj_as_str.strip(", ")

#     def __str__(self) -> str:
#         obj_as_str = self.parse_object()
#         return obj_as_str


# class Book(Chapter):
#     def __init__(self, title: str, chapters: list[str]) -> None:
#         self.title = title
#         self.chapters = [Chapter(chapter_title) for chapter_title in chapters]

#     def get_table_of_contents(self):
#         line_table_of_contents = f"{self.title}"
#         for i, chaper in enumerate(self.chapters, 1):
#             line_table_of_contents += f"\nГлава {i}: {chaper}"
#         return line_table_of_contents


# book = Book("Jungle Book", ["Title 1", "Title 2"])
# print(book.get_table_of_contents())


"""
! Задача 5: Гибкая композиция (Dependency Injection).
Условие:
    Это продвинутая задача.
    Вместо того чтобы создавать компоненты внутри, класс-контейнер будет получать их извне.
    Это делает систему гораздо более гибкой.
https://stepik.org/lesson/2022457/step/8?unit=2050880
"""


# class PetrolEngine:
#     def start(self):
#         return "Бензиновый двигатель запущен"


# class ElectricEngine:
#     def start(self):
#         return "Электрический двигатель активирован"


# class Car:
#     def __init__(self, model, engine) -> None:
#         self.model = model
#         self.engine = engine

#     def start_car(self):
#         return self.engine.start()


# car_bmw = Car("BMW", PetrolEngine())
# print(car_bmw.start_car())

# car_porshe = Car("Porshe", ElectricEngine())
# print(car_porshe.start_car())


"""
https://stepik.org/lesson/2022458/step/2?unit=2050881
'Проблема ромба' (проблема множественного наследования) и как Python ее решает с помощью MRO.

! MRO — это линейный, упорядоченный список всех классов в иерархии, который Python вычисляет для каждого класса.
! Когда вы вызываете метод, Python просто ищет его последовательно в этом списке.
! Как только он находит метод, он останавливается и выполняет его.

! Этот список строится по специальному алгоритму (C3-линеаризация), который гарантирует, что:
!     1) Дочерние классы всегда проверяются раньше родительских.
!     2) Если есть несколько родителей, они проверяются в том порядке,
! в котором они указаны в определении класса (слева направо).
!     3) Каждый класс в иерархии появляется в списке ровно один раз.
"""


# #   Вершина ромба
# #       (A)
# class PoweredDevice:
#     def turn_on(self):
#         print("PoweredDevice: Включено.")


# #   Два потомка от A
# #  (B)           (C)
# class Scanner(PoweredDevice):
#     def turn_on(self):
#         super().turn_on()  # Вызываем родителя
#         print("Scanner: Готов к сканированию.")


# class Printer(PoweredDevice):
#     def turn_on(self):
#         super().turn_on()  # Вызываем родителя
#         print("Printer: Готов к печати.")


# #   Низ ромба: потомок от B и C
# #       (D)
# class MFD(Scanner, Printer):  # МФУ (Многофункциональное устройство)
#     def turn_on(self):
#         super().turn_on()
#         print("MFD: Готово к работе.")


# # print(MFD.mro())  # или print(MFD.__mro__)

# mfd = MFD()
# mfd.turn_on()


"""
https://stepik.org/lesson/2022458/step/3?unit=2050881
    Паттерн "Миксин" (Mixin): "подмешивание" функциональности
! Миксин — это небольшой, сфокусированный класс, который предоставляет одну конкретную порцию дополнительной
! функциональности, но при этом не предназначен для самостоятельного использования.

! Правила хорошего Миксина:
    1. Маленький и сфокусированный:
Он решает одну, очень конкретную задачу
(например, только сериализацию, только логирование, только красивую печать).
    2. Не имеет собственного состояния:
У хорошего миксина обычно нет своего __init__ и своих уникальных атрибутов.
Он работает с атрибутами того класса, к которому его "подмешали" (то есть через self).
    3. Не предназначен для создания экземпляров:
Вы никогда не будете создавать объект самого миксина: obj = JsonMixin().
Он существует только для того, чтобы передать свое поведение другим.
    4. В названии часто есть слово "Mixin":
Это соглашение, которое помогает сразу понять роль класса (JsonSerializableMixin, ReprMixin).

    Итоги:
! Миксины — это предпочтительный и "питонический" способ использования множественного наследования.
! Они позволяют "подмешивать" небольшие, переиспользуемые порции функциональности в разные классы.
! Это отличная альтернатива созданию глубоких и запутанных иерархий наследования.
"""
# ! Миксин для сериализации в словарь


# class DictMixin:
#     """
#     Миксин, который добавляет метод to_dict() к любому классу.
#     Он не имеет своего __init__ и атрибутов.
#     """

#     def to_dict(self):
#         # __dict__ - это спец атрибут, который хранит все атрибуты экземпляра в виде словаря.
#         # Отфильтруем "служебные" атрибуты которые начинаются с нижнего подчеркивания '_'
#         return {
#             key: value
#             for key, value in self.__dict__.items()
#             if not key.startswith("_")
#         }


# class Person:
#     def __init__(self, name, age):
#         self.name = (name,)
#         self.age = (age,)
#         self._secret = "не должно попасть в словарь"


# class Car:
#     def __init__(self, model, year, top_speed) -> None:
#         self.model = model,
#         self.year = year
#         self.top_speed = top_speed


# # PersonWithDict является Person и вдобавок может превращаться в словарь
# class PersonWithDict(Person, DictMixin):
#     pass


# # CarWithDict является Car и может превращаться в словарь
# class CarWithDict(Car, DictMixin):
#     pass


# # Создать объекты "улучшенных" классов
# person = PersonWithDict("Alice", 30)
# car = CarWithDict("Tesla Model S", 2022, 250)

# # Вызвать метод, который пришел из миксина
# print(person.to_dict())
# print(car.to_dict())


"""
https://stepik.org/lesson/2022458/step/4?unit=2050881
! Практический пример: создание миксина JsonMixin
    Миксин для преобразования объекта в JSON-строку.
Можно использовать, например, для отправки данных по сети в API.
"""


# import json

# my_dict = {"name": "Alice", "age": 30}
# json_string = json.dumps(my_dict, ensure_ascii=False, indent=4)
# print(json_string)
# # {
# #     "name": "Alice",
# #     "age": 30
# # }


# # ! Миксин 1: Превращение в словарь
# class DictMixin:
#     """Предоставляет метод to_dict()."""

#     def to_dict(self):
#         return {
#             key: value
#             for key, value in self.__dict__.items()
#             if not key.startswith("_")
#         }


# # ! Миксин 2: Превращение в JSON (использует Миксин 1)
# class JsonMixin(DictMixin):
#     """
#     Предоставляет метод to_json().
#     Наследует от DictMixin, чтобы переиспользовать его логику.
#     """

#     def to_json(self):
#         """Превращает словарь, полученный из to_dict(), в JSON-строку."""
#         # self.to_dict() будет доступен, т.к. он унаследован
#         dict_representation = self.to_dict()
#         return json.dumps(dict_representation, ensure_ascii=False, indent=4)


# # Основные бизнес-классы (никак не связаны друг с другом)
# class Book:
#     def __init__(self, title, author, year) -> None:
#         self.title = title
#         self.author = author
#         self.year = year
#         self._internal_id = "some-private-id"  # Этот атрибут не должен попасть в JSON


# class Employee:
#     def __init__(self, name, position, skills) -> None:
#         self.name = name
#         self.position = position
#         self.skills = skills


# # Подмешивание функциональности к классам
# # Теперь классы умеют превращатьс и в словарь, и в JSON.
# class JsonBook(Book, JsonMixin):
#     pass


# class JsonEmployee(Employee, JsonMixin):
#     pass


# print(" Книга в формате JSON")
# book = JsonBook("Гарри Поттер", "Дж. К. Роулинг", 1997)
# print(book.to_json())

# print("\n Сотрудник в формате JSON")
# employee = JsonEmployee("Иван", "Разработчик", ["Python", "Git", "SQL"])
# print(employee.to_json())


"""
https://stepik.org/lesson/2022458/step/5?unit=2050881
! Задача 1: Простое множественное наследование
"""

# from pprint import pprint


# class Swimmer:
#     def swim(self):
#         return "Я плыву"


# class Walker:
#     def walk(self):
#         return "Я иду"


# class Amphibian(Swimmer, Walker):
#     pass


# amphibian = Amphibian()
# pprint(amphibian.swim())
# pprint(amphibian.walk())


"""
https://stepik.org/lesson/2022458/step/6?unit=2050881
! Задача 2: Порядок наследования (MRO)
"""


# class Radio:
#     def play(self):
#         return "Радио играет"


# class Speaker:
#     def play(self):
#         return "Колонка играет"


# class Boombox(Radio, Speaker):
#     pass


# boombox = Boombox()
# print(dir(boombox))
# print(boombox.play())


"""
https://stepik.org/lesson/2022458/step/7?unit=2050881
! Задача 3: "Проблема ромба" и super()
"""


# class Base:
#     def get_info(self):
#         # print("Base work")
#         return "Base"


# class Left(Base):
#     def get_info(self):
#         # print("Left work")
#         return super().get_info() + "-Left"


# class Right(Base):
#     def get_info(self):
#         # print("Right work")
#         return super().get_info() + "-Right"


# class Child(Left, Right):
#     def get_info(self):
#         # print("Child work")
#         return super().get_info() + "-Child"


# child = Child()
# # print(Child.mro())
# print(child.get_info())


"""
https://stepik.org/lesson/2022458/step/8?unit=2050881
! Задача 4: Простой Миксин (ReprMixin)
"""


# class ReprMixin:
#     def __repr__(self):
#         """
#         Должен возвращать строку вида:
#             ! "ClassName(attr1=val1, attr2=val2...)"
#         """
#         res = ', '.join([f'{key}={value!r}' for key, value in self.__dict__.items() if not key.startswith('_')])
#         return f'{self.__class__.__name__}({res})'


# class SomeClass:
#     def __init__(self, name, age) -> None:
#         self.name = name
#         self.age = age


# class PrettyClass(SomeClass, ReprMixin):
#     pass


# pretty_class = PrettyClass("John", 33)
# print(pretty_class)


"""
https://stepik.org/lesson/2022458/step/9?unit=2050881
! Задача 5: Практический Миксин (DictMixin)
"""


# class DictMixin:
#     def to_dict(self):
#         return {
#             key: value
#             for key, value in self.__dict__.items() if not key.startswith('_')
#         }


# class User:
#     def __init__(self, name, email) -> None:
#         self.name = name
#         self.email = email
#         self._password_hash = "ty9875rthfjnsfkdfhewdkjl"


# class SerializableUser(User, DictMixin):
#     pass


# serializable_user = SerializableUser("John", 133)
# print(serializable_user.to_dict())


"""
https://stepik.org/lesson/2022459/step/1?unit=2050882
! 4.1 Абстрактные базовые классы (ABC).
! Проблема "утиной типизации": неявные контракты

! Абстрактный базовый класс (АБК) — это специальный тип класса, который предназначен не для создания объектов,
! а для того, чтобы служить шаблоном, "контрактом" или "интерфейсом" для других, дочерних классов.
"""


# class Dog:
#     def speak(self):
#         print("Гав!")


# class Cat:
#     def speak(self):
#         print("Мяу!")


# def make_it_speak(animal):
#     animal.speak()  # Просто доверяем, что метод .speak() существует


# make_it_speak(Dog())
# make_it_speak(Cat())


"""
https://stepik.org/lesson/2022459/step/2?unit=2050882
! Ключевые инструменты модуля abc:
    Класс ABC:
    Специальный класс, от которого мы должны унаследовать наш абстрактный класс,
чтобы "включить" для него всю магию АБК.
    Декоратор @abstractmethod: Декоратор, которым мы помечаем методы в нашем АБК.
Он говорит: "Этот метод — просто объявление.
Каждый конкретный (не абстрактный) дочерний класс обязан переопределить и реализовать его".
"""


# from abc import ABC, abstractmethod


# # Класс наследует от ABC, чтобы стать абстрактным
# class ISpeakable(ABC):
#     """
#     Буква I в начале — это популярное, но не обязательное соглашение для интерфейсов.
#     Абстрактный базовый класс (интерфейс), который определяет,
#     что все его потомки должны ументь 'говорить'.
#     """

#     # Объявить метод и пометить его как абстрактный
#     @abstractmethod
#     def speak(self):
#         # Тело абастрактного метода может быть пустым (pass)
#         # или содержать raise NotImplementedError
#         pass


# # Этот класс "подписывает контракт" ISpeakable и ВЫПОЛНЯЕТ его
# class Dog(ISpeakable):
#     def speak(self):  # Реализация обязательного метода
#         print("Гав!")


# # Этот класс тоже "подписывает" и ВЫПОЛНЯЕТ контракт
# class Cat(ISpeakable):
#     def speak(self):  # Реализация обязательного метода
#         print("Мяу!")


# dog = Dog()
# cat = Cat()
# dog.speak()
# cat.speak()


"""
! Декоратор @abstractmethod:
! как заставить дочерние классы обязательно реализовывать методы.

! Всегда, когда используется @abstractmethod, нужно явно наследовать класс от ABC (из модуля abc).
! Это активирует механизм проверки.
"""

# ! Пример 1.
# from abc import ABC, abstractmethod


# class ISpeakable(ABC):
#     @abstractmethod
#     def speak(self):
#         pass


# # Правильная реализация
# class Dog(ISpeakable):
#     def speak(self):
#         print("Гав!")


# # Неправильная реализация!
# class Fish(ISpeakable):
#     # Унаследовано от ISpeakable пообещав реализовать speak(), но это не сделано.
#     def swim(self):
#         print("Я плыву.")


# # 1. Попытка создать "правильный" класс
# try:
#     my_dog = Dog()
#     print("Объект Dog успешно создан.")
#     my_dog.speak()
# except Exception as e:
#     print(f"Ошибка при создании Dog: {e}")

# print("-" * 20)

# # 2. Попытка создать "недоделанный" класс
# try:
#     my_fish = Fish() # Вот здесь и произойдет ошибка!
#     print("Объект Fish успешно создан.")
# except TypeError as e:
#     print(f"Ошибка при создании Fish: {e}")


"""
Пример 2
"""

# from abc import ABC, abstractmethod


# class ISpeakable(ABC):
#     @abstractmethod
#     def speak(self):
#         pass


# # Правильная реализация
# class Dog(ISpeakable):
#     def speak(self):
#         print("Гав!")


# # Неправильная реализация!
# class Fish(ISpeakable):
#     # Унаследовано от ISpeakable пообещав реализовать speak(), но это не сделано.
#     def swim(self):
#         print("Я плыву.")


# def make_it_speak(animal: ISpeakable):
#     # Мы можем быть УВЕРЕНЫ, что у любого объекта, который сюда попадет,
#     # есть метод .speak(), потому что иначе его просто не удалось бы создать.
#     animal.speak()


# # Этот код выполнится без проблем
# make_it_speak(Dog())

# # А этот код даже не дойдет до вызова функции, так как объект my_fish
# # просто не сможет быть создан. Ошибка будет обнаружена гораздо раньше!
# my_fish = Fish()
# make_it_speak(my_fish)


"""
https://stepik.org/lesson/2022459/step/5?unit=2050882
! Задача 1: Создание простого абстрактного класса
"""


# from abc import ABC, abstractmethod


# class Shape(ABC):
#     @abstractmethod
#     def area(self):
#         pass


"""
https://stepik.org/lesson/2022459/step/6?unit=2050882
! Задача 2: Реализация абстрактного класса
"""


# from abc import ABC, abstractmethod


# class Shape(ABC):
#     @abstractmethod
#     def area(self):
#         pass


# class Square(Shape):
#     def __init__(self, side) -> None:
#         self.side = side

#     def area(self):
#         return self.side * self.side


"""
https://stepik.org/lesson/2022459/step/7?unit=2050882
! Задача 3: Контракт из нескольких методов
"""


# from abc import ABC, abstractmethod


# class DataSource(ABC):
#     @abstractmethod
#     def read(self):
#         pass

#     @abstractmethod
#     def write(self, data):
#         pass


# class FileStorage(DataSource):
#     def read(self):
#         return "Чтение из файла"

#     def write(self, data):
#         return f"Запись в файл: {data}"


"""
https://stepik.org/lesson/2022459/step/8?unit=2050882
! Задача 4: Абстрактный класс с конкретными методами
"""


# from abc import ABC, abstractmethod


# class Instrument(ABC):
#     def __init__(self, brand) -> None:
#         self.brand = brand

#     def show_brand(self):
#         return f"Бренд: {self.brand}"

#     @abstractmethod
#     def play(self):
#         pass


# class Guitar(Instrument):
#     def play(self):
#         return "Играет мелодия на гитаре"


"""
https://stepik.org/lesson/2022459/step/9?unit=2050882
! Задача 5: Практический пример "Плагины"
"""

# from abc import ABC, abstractmethod


# class Plugin:
#     @abstractmethod
#     def execute(self, data):
#         pass


# class UpperCasePlugin(Plugin):
#     def execute(self, data):
#         return data.upper()


# class LowerCasePlugin(Plugin):
#     def execute(self, data):
#         return data.lower()


# def run_plugins(plugins: list, data):
#     return [obj_plugin.execute(data) for obj_plugin in plugins]


"""
https://stepik.org/lesson/2022460/step/1?unit=2050883
! 4.2 Датаклассы (@dataclass). Декоратор @dataclass появился в Python 3.7

https://stepik.org/lesson/2022460/step/2?unit=2050883
! Декоратор @dataclass: автоматическая генерация магических методов

Декоратор @dataclass "сканирует" класс на предмет аннотаций типов и
на их основе автоматически генерирует за нас несколько самых важных магических методов:
__init__: Конструктор, который принимает аргументы для всех полей и присваивает их.
__repr__: Информативное представление для отладки.
__eq__: Корректное сравнение объектов по значениям их полей.
...а также некоторые другие (__ne__, __lt__, __gt__, и т.д., если указать order=True).
"""
# from dataclasses import dataclass


# # ! Обычный класс
# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def __repr__(self):
#         return f"Point(x={self.x}, y={self.y})"

#     def __eq__(self, other):
#         if not isinstance(other, Point):
#             return NotImplemented
#         return (self.x, self.y) == (other.x, other.y)


# # ! Такой же клас по функционалу, но с использованием синтаксиса дата-классов
# @dataclass
# class Point:
#     # ! Вместо объявления в __init__ в датаклассе нужно просто объявить какие поля и какого они типа
#     x: int
#     y: int


# # 1. __init__ был сгенерирован автоматически
# p1 = Point(1, 2)
# print(f"Объект создан: {p1}")

# # 2. __repr__ тоже создан и работает также

# # 3. __eq__ тоже работает "из коробки"
# p2 = Point(1, 2)
# p3 = Point(3, 4)

# print(f"p1 == p2: {p1 == p2}")  # Выведет: True
# print(f"p1 == p3: {p1 == p3}")  # Выведет: False


"""
https://stepik.org/lesson/2022460/step/3?unit=2050883
Настройка датаклассов: поля по умолчанию, неизменяемые объекты и другие возможности.
    ! Важное правило:
! Поля без значений по умолчанию должны идти ПЕРЕД полями со значениями по умолчанию.
"""


# from dataclasses import dataclass


# @dataclass
# class Point:
#     x: int
#     y: int = 0  # y теперь имеет значение по умолчанию
#     z: int = 0  # z тоже


# # Теперь мы можем создавать объекты, не указывая y и z
# p1 = Point(10)
# print(p1)  # Выведет: Point(x=10, y=0, z=0)

# # Мы можем переопределить только одно из значений
# p2 = Point(10, 20)
# print(p2)  # Выведет: Point(x=10, y=20, z=0)


"""Другой пример"""

# from dataclasses import dataclass, field


# @dataclass
# class User:
#     name: str
#     # ! ПРАВИЛЬНЫЙ способ для изменяемых типов
#     # * default_factory=list говорит датаклассу,
#     # * что для каждого нового объекта нужно вызывать list() для создания нового, пустого списка.
#     friends: list[str] = field(default_factory=list)


"""
Чтобы создать объект, который нельзя изменить после его создания нужно использовать @dataclass(frozen=True)
"""
# from dataclasses import dataclass


# @dataclass(frozen=True)
# class ImmutablePoint:
#     x: int
#     y: int


# p = ImmutablePoint(10, 20)
# print(p)

# # Любая попытка изменить атрибут вызовет ошибку!
# try:
#     p.x = 30
# except Exception as e:
#     print(f"\nОшибка при попытке изменить p.x: {e}")
# except Exception as e:
#     print(f"\nОшибка при попытке изменить p.x: {e}")
# except Exception as e:
#     print(f"\nОшибка при попытке изменить p.x: {e}")


"""
! Параметр order=True - автоматически генерирует методы __lt__ (less than), __le__ (less or equal),
! __gt__ (greater than) и __ge__ (greater or equal).

! Сортировка происходит сначала по первому полю (price), а при равенстве — по второму (name), и так далее.
"""

# from dataclasses import dataclass


# @dataclass(order=True)
# class Product:
#     # Поля сравниваются последовательно, сверху вниз
#     price: float
#     name: str


# p1 = Product(99.9, "Чайник")
# p2 = Product(150.0, "Кофеварка")
# p3 = Product(99.9, "Утюг")

# # Сравнение по цене:
# print(f"p1 < p2: {p1 < p2}")  # True, потому что 99.9 < 150.0

# # Сравнение при одинаковой цене (работает алфавитный порядок):
# # В алфавите 'У' (Утюг) стоит раньше, чем 'Ч' (Чайник).
# # Значит, "Утюг" < "Чайник".
# print(
#     f"p1 > p3: {p1 > p3}"
# )  # True. Цена равна, но "Чайник" > "Утюг" (так как 'Ч' идет позже 'У')

# # Сортировка списка
# products = [p2, p1, p3]
# print(f"\nОтсортированный список: {sorted(products)}")
# print(f"\nОтсортированный список: {sorted(products)}")
# print(f"\nОтсортированный список: {sorted(products)}")

"""
Итоги:
- @dataclass — это не просто генератор кода, а гибкий инструмент.

- Значения по умолчанию задаются как в обычных функциях.

- field(default_factory=...) используется для изменяемых типов (списки, словари).

- @dataclass(frozen=True) создает неизменяемые объекты.

- @dataclass(order=True) автоматически делает объекты сортируемыми.
"""


"""
https://stepik.org/lesson/2022460/step/4?unit=2050883
! Задача 1: Простой датакласс
"""
# from dataclasses import dataclass


# @dataclass
# class Point:
#     x: int
#     y: int


"""
https://stepik.org/lesson/2022460/step/5?unit=2050883
! Задача 2: Датакласс со значениями по умолчанию
"""
# from dataclasses import dataclass


# @dataclass
# class User:
#     username: str
#     is_active: bool = True
#     level: int = 1


"""
https://stepik.org/lesson/2022460/step/6?unit=2050883
! Задача 3: "Замороженный" датакласс (frozen=True)
"""
# from dataclasses import dataclass


# @dataclass(frozen=True)
# class APIConfig:
#     base_url: str
#     api_key: str


"""
https://stepik.org/lesson/2022460/step/7?unit=2050883
! Задача 4: Сортируемый датакласс (order=True)
"""
# from dataclasses import dataclass


# @dataclass(order=True)
# class Employee:
#     salary: int
#     name: str


"""
https://stepik.org/lesson/2022460/step/8?unit=2050883
! Задача 5: Датакласс с изменяемым полем по умолчанию
"""
# from dataclasses import dataclass, field


# @dataclass
# class Team:
#     name: str
#     members: list[str] = field(default_factory=list)

"""
https://stepik.org/lesson/2026658/step/1?unit=2055134
! 4.3 Дескрипторы: __get__, __set__, __delete__

Дескриптор — это любой объект, который реализует хотя бы один из трех специальных методов:
    __get__, __set__ или __delete__.
Он позволяет "перехватывать" и настраивать поведение при доступе к атрибутам.

Дескриптор — это не какой-то специальный тип, а просто любой объект, который реализует протокол дескриптора.
Этот протокол состоит из трех магических методов.
Классу достаточно реализовать хотя бы один из них, чтобы стать дескриптором.

    ! "Магия" @property — это на самом деле протокол дескриптора.

    ! Декоратор @property — это просто удобный способ создать экземпляр класса property,
! который является встроенным дескриптором.

    ! При обращении к атрибуту, который является дескриптором,
! Python вызывает его специальный метод __get__ вместо того, чтобы просто вернуть значение атрибута.
"""


"""
https://stepik.org/lesson/2026658/step/2?unit=2055134
! 2: Протокол дескриптора: объяснение __get__, __set__ и __delete__
"""


# class GetDescriptor:
#     def __get__(self, instance, owner):
#         print("Вызван __get__:")
#         print(f"  - self:     {self}")
#         print(f"  - instance: {instance}")
#         print(f"  - owner:    {owner}")
#         return "Значение из __get__"


# class Owner:
#     attr = GetDescriptor()


# obj = Owner()
# print(f"Результат obj.attr: {obj.attr}")


"""
https://stepik.org/lesson/2026658/step/5?auth=login&unit=2055134
! Задача 1: Дескриптор для константы (только для чтения)
"""


# class ConstantDescriptor:
#     def __init__(self, value) -> None:
#         self.value = value

#     def __get__(self, instance, owner):
#         return self.value

#     def __set__(self, instance, value):
#         raise AttributeError(f"Атрибут {self.value} изменять нельзя")


# class MyClass:
#     PI = ConstantDescriptor(3.14159)


# my_class_1 = MyClass()
# my_class_2 = MyClass()

# print(my_class_1.PI)
# print(my_class_2.PI)

# my_class_1.PI = 7  # ! Здесь всегда будет ошибка


"""
https://stepik.org/lesson/2026658/step/6?auth=login&unit=2055134
! Задача 2: Правильный дескриптор с __get__ и __set__
"""


# class ManagedAttribute:
#     def __set_name__(self, owner, name):
#         self.private_name = '_' + name

#     def __get__(self, instance, owner):
#         print(f"Work __get__ with {self.private_name=}")
#         # return instance.__dict__[self.private_name]  # ! Так можно, но лучше так не делать, могут быть проблемы
#         return getattr(instance, self.private_name, None)

#     def __set__(self, instance, value):
#         print(f"Work __set__ with {value=}")
#         # instance.__dict__[self.private_name] = value  # ! Так можно, но лучше так не делать, могут быть проблемы
#         setattr(instance, self.private_name, value)


# class Some:
#     attr = ManagedAttribute()


# some = Some()
# some.attr = 15
# print(some.attr)


"""
https://stepik.org/lesson/2026658/step/7?auth=login&unit=2055134
! Задача 3: Правильное хранение значения в дескрипторе
"""


# class ValidatedString:
#     def __set_name__(self, owner, name):
#         self.private_name = "_" + name

#     def __get__(self, instance, owner):
#         return getattr(instance, self.private_name, None)

#     def __set__(self, instance, value):
#         print(f"{value=}, {type(value)}")
#         if type(value) is not str:
#             raise TypeError
#         setattr(instance, self.private_name, value)


# class Some:
#     attr = ValidatedString()


# some = Some()
# some.attr = "Python"


"""
https://stepik.org/lesson/2026658/step/8?auth=login&unit=2055134
! Задача 4: Дескриптор-валидатор NonNegative
"""


# class NonNegative:
#     def __set_name__(self, owner, name):
#         self.private_name = "_" + name

#     def __get__(self, instance, owner):
#         return getattr(instance, self.private_name, None)

#     def __set__(self, instance, value):
#         if not isinstance(value, (int, float)) or value < 0:
#             raise ValueError("Значение должно быть положительным числом!")
#         setattr(instance, self.private_name, value)


# class Some:
#     attr = NonNegative()


# some = Some()
# some.attr = 777
# print(f"{some.attr=}")


"""
https://stepik.org/lesson/2026658/step/9?auth=login&unit=2055134
! Задача 5: Дескриптор-логгер
"""


# class LoggedAccess:
#     def __set_name__(self, owner, name):
#         self.public_name = name
#         self.private_name = "_" + name

#     def __get__(self, instance, owner):
#         print(f"Чтение атрибута '{self.public_name}'")
#         return getattr(instance, self.private_name, None)

#     def __set__(self, instance, value):
#         print(f"Запись атрибута '{self.public_name}', новое значение = {value}")
#         setattr(instance, self.private_name, value)


# class Some:
#     attr = LoggedAccess()


# obj = Some()
# obj.attr = "Python"
# print(f"{obj.attr=}")


"""
https://stepik.org/lesson/2022461/step/1?auth=login&unit=2050884
! 5.1 Создание собственных исключений

! Преимущества собственных исключений:
- Семантическая ясность:
    InsufficientFundsError гораздо лучше описывает суть проблемы, чем ValueError. Код становится самодокументируемым.

- Точная обработка ошибок:
    Можно писать отдельные блоки except для каждого конкретного типа ошибки, не анализируя текстовые сообщения.

- Создание иерархии ошибок:
    Можно построить целое "дерево" ошибок (об этом в следующих шагах), что позволяет ловить как конкретные ошибки,
    так и целые их группы.

- Разделение ответственности:
    Созданный API или библиотека может предоставить пользователю набор своих собственных исключений,
    и ему не придется гадать, какие ValueError или KeyError могут "вылететь" из кода.
"""


# class Account:
#     id_list = []

#     def __init__(self, money: int | float = 0) -> None:
#         self.balance = money
#         self.is_locked = False
#         self.id = hex(id(self))
#         self.id_list.append(self.id)

#     def __repr__(self) -> str:
#         return f"{self.__class__.__name__} with id {self.id} has data: {self.__dict__}"

#     def set_balance(self, amount_money: int | float):
#         self.balance += amount_money

#     def withdraw_from_balance(self, amount_money: int | float):
#         if self.balance is None:
#             raise ValueError
#         self.balance -= amount_money


# account1 = Account(100)
# account2 = Account(2000)


# # Определяем наши собственные типы ошибок
# class InsufficientFundsError(Exception):
#     pass


# class AccountLockedError(Exception):
#     pass


# class SelfTransferError(Exception):
#     pass


# def make_payment_v2(from_account, to_account, amount):
#     if from_account.balance < amount:
#         raise InsufficientFundsError("Недостаточно средств")

#     if to_account.is_locked:
#         raise AccountLockedError("Счет получателя заблокирован")

#     if from_account.id == to_account.id:
#         raise SelfTransferError("Нельзя перевести деньги на тот же счет")
#     from_account.withdraw_from_balance(amount)
#     to_account.set_balance(amount)


# try:
#     make_payment_v2(account1, account2, 1000)
# except InsufficientFundsError:
#     print("Пожалуйста, пополните баланс.")
# except AccountLockedError:
#     print("Операция невозможна. Свяжитесь с поддержкой.")
# except SelfTransferError:
#     print("Выберите другой счет для перевода.")
# except Exception as e:
#     print(f"Произошла неизвестная ошибка. {e}")

# print(account1)
# print(account2)


"""
https://stepik.org/lesson/2022461/step/2?unit=2050884
! Создание иерархии классов исключений

    ! Пример: Иерархия ошибок для веб-приложения
    Спроектируем "дерево" ошибок:
- Корень: MyAppError — базовое исключение для всех ошибок нашего приложения.
- Ветви: ApiError и DatabaseError — группы ошибок, связанные с API и базой данных. Они наследуются от MyAppError.
- Листья: AuthError и NotFoundError — очень конкретные ошибки API. Они наследуются от ApiError.
"""


# # --- Уровень 0: Базовое исключение для всего приложения ---
# class MyAppError(Exception):
#     """Общий предок для всех исключений нашего приложения."""

#     pass


# # --- Уровень 1: Группы ошибок ---
# class ApiError(MyAppError):
#     """Ошибка, связанная с внешним API."""

#     pass


# class DatabaseError(MyAppError):
#     """Ошибка, связанная с базой данных."""

#     pass


# # --- Уровень 2: Конкретные, специфичные ошибки ---
# class AuthError(ApiError):
#     """Ошибка аутентификации в API (например, неверный токен)."""

#     pass


# class NotFoundError(ApiError):
#     """Ошибка, когда ресурс в API не найден (404)."""

#     pass


# def get_data_from_api(token):
#     if token == "invalid":
#         raise AuthError("Неверный API токен")
#     if token == "not_found":
#         raise NotFoundError("Пользователь не найден")
#     if token == "db_fail":
#         raise DatabaseError("База данных недоступна")
#     return {"data": "some data"}


"""
Пример 1
"""
# # ! Здесь реагируем только на AuthError.
# # ! Если функция выбросит NotFoundError, этот блок except его не поймает.
# try:
#     get_data_from_api("invalid")
# except AuthError:
#     print("Проблема с аутентификацией. Пожалуйста, перелогиньтесь.")


"""
Пример 2
"""
# # ! Ловим целую группу ошибок, связанную с API
# # ! Здесь не нужно писать except (AuthError, NotFoundError, ...):.
# # ! Просто ловим их общего предка.
# try:
#     # get_data_from_api("invalid")  # Сработает
#     get_data_from_api("not_found")  # Тоже сработает
# except ApiError as e:
#     # Этот блок поймает и AuthError, и NotFoundError,
#     # потому что они ОБА являются потомками ApiError!
#     print(f"Произошла ошибка API: {e}. Попробуйте позже.")


"""
! Пример 3 - правильный порядок обработки:
Except блоки проверяются по порядку.
Всегда нужно ловить более специфичные исключения раньше, чем их родительские.
"""


# try:
#     get_data_from_api("invalid")
# except AuthError:
#     # Этот блок сработает первым, потому что он более конкретный
#     print("Ошибка аутентификации. Обновите ваш токен.")
# except ApiError:
#     # ! Этот блок НЕ сработает, хотя AuthError и является ApiError
#     print("Произошла общая ошибка API.")
#     # ! Если AuthError и ApiError поменять местами, except ApiError: поймал бы AuthError первым,
#     # ! и более специфичный блок никогда бы не выполнился.


"""
https://stepik.org/lesson/2022461/step/3?unit=2050884
! Использование raise для генерации собственных ошибок в методах
"""


# class WalletError(Exception):
#     """Базовое исключение для всех ошибок кошелька."""

#     pass


# class InsufficientFundsError(WalletError):
#     """Выбрасывается, когда на счете недостаточно средств."""

#     pass


# class NegativeAmountError(WalletError):
#     """Выбрасывается при попытке операции с отрицательной суммой."""

#     pass


# class Wallet:
#     def __init__(self, balance):
#         self._balance = balance

#     @property
#     def balance(self):
#         return self._balance

#     def deposit(self, amount):
#         """Положить деньги на счет."""
#         if amount <= 0:
#             # Если сумма не корректна, генерируем исключение
#             raise NegativeAmountError("Сумма для пополнения должна быть положительной.")
#         self._balance += amount
#         print(f"Счет пополнен на {amount}. Баланс: {self._balance}")

#     def withdraw(self, amount):
#         """Снять деньги со счета."""
#         if amount <= 0:
#             # Снова проверить корректность суммы
#             raise NegativeAmountError("Сумма для снятия должна быть положительной.")

#         if self._balance < amount:
#             # Если денег не хватает, генерируется другое исключение
#             raise InsufficientFundsError(
#                 f"Недостаточно средств. Запрошено: {amount}, доступно: {self._balance}"
#             )

#         self._balance -= amount
#         print(f"Снято со счета {amount}. Баланс: {self._balance}")


# my_wallet = Wallet(100)

# try:
#     print("--- Попытка снять 50 ---")
#     my_wallet.withdraw(50)  # Успешно

#     print("\n--- Попытка снять 200 ---")
#     my_wallet.withdraw(200)  # InsufficientFundsError

#     print("\n--- Этот код не выполнится ---")

# except NegativeAmountError as e:
#     # Этот блок не сработает, т.к. ошибка другого типа
#     print(f"Перехвачена ошибка некорректной суммы: {e}")

# except InsufficientFundsError as e:
#     # А вот этот блок сработает!
#     print(f"Перехвачена ошибка нехватки средств: {e}")
#     print("Пожалуйста, пополните ваш кошелек.")

# except WalletError as e:
#     # Этот блок поймал бы любую из наших ошибок, если бы мы не поймали ее раньше
#     print(f"Произошла общая ошибка кошелька: {e}")

# finally:
#     # Этот блок выполнится в любом случае
#     print(f"\nОперация завершена. Итоговый баланс: {my_wallet.balance}")


"""
https://stepik.org/lesson/2022461/step/4?unit=2050884
! Задача 1: Создание простого исключения
"""


# class MyCustomError(Exception):
#     pass


# def cause_error():
#     raise MyCustomError


# cause_error()


"""
https://stepik.org/lesson/2022461/step/5?unit=2050884
! Задача 2: Исключение с сообщением
"""


# class InvalidDataError(Exception):
#     pass


# def process_data(data):
#     if type(data) is not dict:
#         raise InvalidDataError("Данные должны быть словарем")


# process_data([])


"""
https://stepik.org/lesson/2022461/step/6?unit=2050884
! Задача 3: Иерархия исключений
"""


# class ApiError(Exception):
#     pass


# class AuthError(ApiError):
#     pass


# class TimeoutError(ApiError):
#     pass


# def make_request(should_fail_with: str):
#     if should_fail_with == "auth":
#         raise AuthError("Ошибка авторизации!")
#     if should_fail_with == "timeout":
#         raise TimeoutError("Ошибка истечения времени")
#     if type(should_fail_with) is str or should_fail_with is None:
#         pass


# make_request("auth")
# make_request("timeout")
# make_request("")


"""
https://stepik.org/lesson/2022461/step/7?unit=2050884
! Задача 4: Использование raise в методе класса
"""


# class InvalidAgeError(ValueError):
#     pass


# class Person:
#     def __init__(self, name, age) -> None:
#         self.name = name
#         self.age = age

#     @property
#     def age(self):
#         return self._age

#     @age.setter
#     def age(self, new_age):
#         if new_age < 0:
#             raise InvalidAgeError("Возраст не может быть отрицательным")
#         self._age = new_age


"""
https://stepik.org/lesson/2022461/step/8?unit=2050884
! Задача 5: Практический пример "Банкомат"
"""


# class AtmError(Exception):
#     pass


# class InsufficientFundsError(AtmError):
#     pass


# class InvalidPinError(AtmError):
#     pass


# class ATM:
#     def __init__(self, balance, pin) -> None:
#         self.balance = balance
#         self.pin = pin

#     def withdraw(self, amount, entered_pin):
#         if entered_pin != self.pin:
#             raise InvalidPinError("Вы ввели не верный пин-код!")
#         if amount > self.balance:
#             raise InsufficientFundsError("Недостаточно денег на счету!")
#         self.balance -= amount
#         return self.balance
