# -*- coding: utf-8 -*-

# Файл makedb.py: сохраняет объекты Person в хранилище

from person import Person, Manager                      # Импортирует наши классы
bob = Person('Bob Smith')                               # Создание объектов для сохранения
sue = Person('Sue Jones', job='dev', pay=100000)
tom = Manager('Tom Jones', 50000)

import shelve
db = shelve.open('persondb')                            # Имя файла хранилища, создает  файл в рабочем каталоге
for object in (bob, sue, tom):                          # В качестве ключа использовать атрибут name
    db[object.name] = object                            # Сохранить объект в хранилище
db.close()                                              # Закрыть после внесения изменений
