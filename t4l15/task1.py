class Transport:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

bus47 = Transport('Renaul Logan', 180, 12)
print(f'Название автомобиля: {bus47.name} Скорость: {bus47.max_speed} Пробег: {bus47.mileage}')
# Ожидаемый результат вывода:

# Название автомобиля: Renaul Logan Скорость: 180 Пробег: 12

