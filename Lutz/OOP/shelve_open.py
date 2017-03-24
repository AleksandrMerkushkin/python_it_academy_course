# -*- coding: utf-8 -*-


import shelve
db = shelve.open('persondb')                                          # Открыть хранилище
print len(db)                                                         # Количество записей в хранилище

print list(db.keys())                                                 # keys – это оглавление
                                                                      # Функция list используется, чтобы получить список в 3.0

bob = db['Bob Smith']                                                 # Извлечь объект bob по ключу
print(bob)                                                            # Вызовет __str__ из AttrDisplay
rec = db['Sue Jones']                                                 # Извлечь объект по ключу
print(rec)
print rec.lastName()
print rec.pay, '\n'

print bob.lastName()                                                  # Вызовет lastName из Person

for key in db:                                                        # Итерации, извлечение, вывод
    print(key, '=>', db[key])

for key in sorted(db):
    print(key, '=>', db[key])                                         # Итерации через отсортированный список ключей
