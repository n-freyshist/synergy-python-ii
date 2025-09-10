# Есть родительский класс:
# class Transport:
#   def __init__(self, name, max_speed, mileage):
#       self.name = name
#       self.max_speed = max_speed
#       self.mileage = mileage
#
# Создайте объект Autobus, который унаследует все переменные и методы родительского класса Transport, и выведеите его.
# Ожидаемый результат вывода:
# Название автомобиля: Renaul Logan Скорость: 180 Пробег: 12

class Transport:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

class Autobus(Transport):
    pass


bus = Autobus("Renaul Logan", 180, 12)
print("Название автомобиля: {0} Скорость: {1} Пробег: {2}" .format(bus.name, bus.max_speed, bus.mileage))