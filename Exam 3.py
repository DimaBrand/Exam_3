Напишите функцию, которая проверяет: является ли слово палиндром

a = input('Введите слово: ')
if str(a) == str(a[::-1]):
    print('Это слово - ПАЛИНДРОМ')
else:
    print('Это слово НЕ палиндром')


Напишите функцию, которая будет принимать номер
кредитной карты и показывать только последние 4 цифры.
Остальные цифры должны заменяться звездочками

def karta(k):
    return '*' * len(k[:-4]) + k[-4:]

print(karta('1234 1234 1234 1234'))

"Класс Gardener
1. Создайте класс Gardener
2. Создайте метод __init__(), внутри которого будут определены два динамических
свойства: 1) name - передается параметром, является публичным и 2) _plant -
принимает объект класса Tomato, является protected
3. Создайте метод work(), который заставляет садовника работать, что позволяет
растению становиться более зрелым
4. Создайте метод harvest(), который проверяет, все ли плоды созрели. Если все -
садовник собирает урожай. Если нет - метод печатает предупреждение.
5. Создайте статический метод knowledge_base(), который выведет в консоль справку
по садоводству."""


class Gardener:
    def __init__(self, name, plant):
        self.name = name
        self._plant = plant

    def work(self):
        self._plant.grow_all()

    def harvest(self):
        if self._plant.all_are_ripe():
            self._plant.give_away_all()
            print('Урожай созрел и собран.')
            return True
        else:
            print('Ещё не дозрели помидорки! Не трожь!!!')
            return False

    @staticmethod
    def knowledge_base():
        print('OK Google:"Справка по садоводству."')


"""Тесты:
1. Вызовите справку по садоводству
2. Создайте объекты классов TomatoBush и Gardener
3. Используя объект класса Gardener, поухаживайте за кустом с помидорами
4. Попробуйте собрать урожай
5. Если томаты еще не дозрели, продолжайте ухаживать за ними
6. Соберите урожай"""


Gardener.knowledge_base()
bush_obj = TomatoBush(21)
gardener_obj = Gardener('Tomas', bush_obj)
while True:
    gardener_obj.work()
    if not gardener_obj.harvest():
        continue
    break
