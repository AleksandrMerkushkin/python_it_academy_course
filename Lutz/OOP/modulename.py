# -*- coding: utf-8 -*-

class FirstClass:
    def setdata(self, value):
        self.data = value
    def display(self):
        print(self.data)

class SecondClass(FirstClass):
    def display(self):                              # Наследует setdata
        print('Current value = "%s" ' % self.data)  # Изменяет display

class ThirdClass(SecondClass):                      # Наследует SecondClass
    def __init__(self, value):                      # Вызывается из ThirdClass(value)
        self.data = value
    def __add__(self, other):                       # Для выражения “self + other"
        return ThirdClass(self.data + other)
    def __str__(self):                              # Вызывается из print(self), str()
        return "[ThirdClass: %s]" % self.data
    def mul(self, other):                           # Изменяет сам объект: обычный метод
        self.data *= other





if __name__ == "__main__":
    x = FirstClass()        # Создаются два экземпляра
    y = FirstClass()        # Каждый является отдельным пространтсвом имен

    x.setdata("King Artur") # Вызов метода: self - это х
    y.setdata(3.14159)      # Эквивалентно: FirstClass.setdata(y, 3.14159)

    x.display()             # В каждом экземпляре свое значение self.data
    y.display()

    x.data = "New value"    # Можно получать/записывать значения атрибутов
    x.display()             # И за пределами класса тоже

    x.anothername = "spam"  # Здесь также можно создавать новыйе атрибуты

    z = SecondClass()
    z.setdata(42)           # Найдет setdata в FirstClass
    z.display()             # Найдет переопределенный метод в SecondClass

    x.display()             # По-прежнему экземпляр FirstClass (старое обращение)

    a = ThirdClass("abc")   # Вызывается новый метод __init__
    a.display()             # Унаследованный метод
    print(a)                # __str__: возвращает строку

    b = a + "xyz"           # Новый __add__: создается новый экземпляр
    b.display()
    print(b)                # __str__: возвращает строку

    a.mul(3)                # mul: изменяется сам экземпляр
    print(a)