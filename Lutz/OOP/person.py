# -*- coding: utf-8 -*-

# Предусмотреть возможность импортировать файл и запускать его, как
# самостоятельный сценарий для самотестирования
# Добавлены методы, инкапсулирующие операции, для удобства в сопровождении
# Добавлен метод __str__, реализующий вывод объектов
# Добавлен подкласс, адаптирующий поведение суперкласса
# Добавлен адаптированный конструктор в подкласс
# Объединение объектов в составной объект

from classtools import AttrDisplay                          # Импортирует обобщенный инструмент

class Person(AttrDisplay):

    """
    Создает и обрабатывает записи с информацией о людях
    """

    def __init__(self, name, job=None, pay=0):              # Normal function args
        self.name = name                                    # Заполняет поля при создании
        self.job = job                                      # self - новый экземпляр класса
        self.pay = pay
    def lastName(self):                                     # Методы, реализующие поведение экземпляров
        return self.name.split()[-1]                        # self – подразумеваемый экземпляр, предполагается, что фамилия указана последней
    def giveRaise(self, percent):                           # Процент – величина в диапазоне 0..1
        self.pay = int(self.pay * (1 + percent))            # Изменения придется вносить только в одном месте

    # def __str__(self):                                      # Добавленный метод
    #     return '[Person: %s, %s]' % (self.name, self.pay)   # Строка для вывода c оператором форматирования %

# Этот программный код означает, что при создании экземпляров класса Person
# нам достаточно будет передавать только значение аргумента name, а аргументы
# job и pay теперь являются необязательными – они по умолчанию будут полу-
# чать значения None и  0.
# Аргумент self, как обычно, будет заполняться интер-
# претатором автоматически, и  в нем будет передаваться ссылка на экземпляр
# созданного объекта  – присваивание значений атрибутам объекта self будет
# присоединять их к новому экземпляру.
# Пока все идет неплохо – к настоящему моменту наш класс фактически играет
# роль фабрики записей – он создает записи и заполняет их поля (атрибуты экзем-
# пляров, если говорить на языке Python).

class Manager(Person):                                      # Определить подкласс класса Person и наследует атрибута класса Person

    """
    Версия класса Person, адаптированная в соответствии
    со специальными требованиями
    """
    def __init__(self, name, pay):                          # Переопределенный конструктор
        Person.__init__(self, name, 'mgr', pay)             # Вызов оригинального конструктора со значением ‘mgr’ в аргументе job
    def giveRaise(self, percent, bonus=.10):                # Переопределить метода для адаптации
        Person.giveRaise(self, percent + bonus)             # Правильно: дополняет оригинал, вызов версии из  класса Person                                                                                             # класса Person



if __name__ == '__main__':                                  # Только когда файл запускается для тестирования
                                                            # реализация самотестирования
    #
    # bob = Person('Bob Smith')                               # Тестирование класса
    # sue = Person('Sue Jones', job='dev', pay=100000)        # Запустит __init__ автоматически
    # print(bob.name, bob.pay)                                # Извлечет атрибуты
    # print(sue.name, sue.pay),                          '\n' # Атрибуты в объектах sue и отличаются
    #
    # print(bob)                                              # Объект целиком
    # print(sue),                                        '\n' # Объект целиком
    #
    # print('{0} {1}'.format(bob.name, bob.pay))              # Новый метод format
    # print('{0} {1}'.format(sue.name, sue.pay)),        '\n'
    #
    # print('%s %s' % (bob.name, bob.pay))                    # Выражение форматирования
    # print('%s %s' % (sue.name, sue.pay)),              '\n'
    #
    # print('%s %s' % (bob.lastName(), sue.lastName()))       # Вместо жестко определенных
    # sue.giveRaise(.10)                                      # операций используются методы
    # print(sue.pay),                                    '\n'
    #
    # print(sue),                                        '\n' # Объект целиком
    #
    # tom = Manager('Tom Jones', 50000)                       # Экземпляр Manager: __init__
    #                                                         # указывать должность не требуется, подразумевается/
    #                                                         # устанавливается классом
    # tom.giveRaise(.10)                                      # Вызов адаптированной версии
    # print(tom.lastName())                                   # Вызов унаследованного метода
    # print(tom),                                        '\n' # Вызов унаследованного __str__

    # print('--All three--')
    # for object in (bob, sue, tom):                          # Обработка объектов обобщенным способом
    #     object.giveRaise(.10)                               # Вызовет метод giveRaise этого объекта
    #     print(object)                                       # Вызовет общий метод __str__
    #
    # class Department:
    #     def __init__(self, *args):
    #         self.members = list(args)
    #     def addMember(self, person):
    #         self.members.append(person)
    #     def giveRaises(self, percent):
    #         for person in self.members:
    #             person.giveRaise(percent)
    #     def showAll(self):
    #         for person in self.members:
    #             print(person)
    #
    # development = Department(bob, sue)                      # Встраивание объектов в составной объект
    # development.addMember(tom)
    # development.giveRaises(.10)                             # Вызов метода giveRaise вложенных объектов
    # development.showAll()                                   # Вызов метода __str__ вложенных объектов

    bob = Person('Bob Smith')
    sue = Person('Sue Jones', job='dev', pay=100000)
    print(bob)
    print(sue)
    print(bob.lastName(), sue.lastName())
    sue.giveRaise(.10)
    print(sue)
    tom = Manager('Tom Jones', 50000)
    tom.giveRaise(.10)
    print(tom.lastName())
    print(tom)