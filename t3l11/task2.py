import collections

def get_pet(ID):
    return pets[ID] if ID in pets.keys() else False

# Я знаю, что get_pet_name костыль, но я не нашел другого способа "выбить" имя животного, имея в распоряжении только ID. 
# Так как зачением к ключу является целый словарь, то и выводится при запросе value целый словарь "Мухтар, со всему его парами ключ-значение", а мне нужно было только имя
# Ну и костыль тут в том, что это работает благодаря тому, что в каждом ID у нас только одно имя
def get_pet_name(ID):
    for name in pets[ID].keys():
        return name

def get_suffix(age):
    suffix = ''
    if age % 10 == 1 and age % 100 != 11:
        suffix = 'год'
        return suffix
    elif 1 < age % 10 < 5 and age % 100 not in range(10, 20):
        suffix = 'года'
        return suffix
    else:
        suffix = 'лет'
        return suffix
    
def pets_list():
    for key in pets:
        print(pets[key])

def create():

    last = collections.deque(pets, maxlen=1)[0]
    pname = input("Введите имя питомца: ")
    pets[last+1] = {
        pname:{
            'Вид питомца': input("Введите породу питомца: "),
            'Возраст питомца': int(input("Введите возраст питомца: ")),
            'Имя владельца': input("Введите имя владельца питомца: ")
        }
            }
    last += 1
    return
    

def read():
    ID = int(input("Введите ID питомца: "))
    print('Это', f'{pets[ID][get_pet_name(ID)]['Вид питомца']}', 
          'по кличке ', f'"{get_pet_name(ID)}".', 
          "Возраст питомца:", f'{pets[ID][get_pet_name(ID)]['Возраст питомца']}', f'{get_suffix(pets[ID][get_pet_name(ID)]['Возраст питомца'])}.', 
          'Имя владельца:', f'{pets[ID][get_pet_name(ID)]['Имя владельца']}')
    return
        

def update():
    ID = int(input("Введите ID питомца: "))
    pname = input("Введите новое имя питомца: ")
    pets[ID] = {
        pname:{
            'Вид питомца': input("Введите новую породу питомца: "),
            'Возраст питомца': int(input("Введите новый возраст питомца: ")),
            'Имя владельца': input("Введите новое имя владельца питомца: ")
        }
            }
    return

def delete():
    ID = int(input("Введите ID питомца: "))
    pets.pop(ID)
    return

def instruction():
    print("Введите одну из команд:")
    print(" 'создать', чтобы добавить питомца в базу данных")
    print(" 'читать', чтобы получить информацию о нём")
    print(" 'обновить', чтобы обновить информацию о нём")
    print(" 'удалить', чтобы удалить информацию о нём")
    print(" 'stop', чтобы выйти из программы")
    return

pets = {

    1:
        {
            "Мухтар": {
                "Вид питомца": "Собака",
                "Возраст питомца": 9,
                "Имя владельца": "Павел"
            },
        },
    2:
        {
            "Каа": {
                "Вид питомца": "желторотый питон",
                "Возраст питомца": 19,
                "Имя владельца": "Саша"
            },
        },
}

# pets_list() для проверки исхода
pets_list()
instruction()

command = input()
while command != 'stop':
    if command == 'создать':
        create()
        instruction()
        command = input()
    if command == 'читать':
        read()
        instruction()
        command = input()
    if command == 'обновить':
        update()
        instruction()
        command = input()
    if command == 'удалить':
        delete()
        instruction()
        command = input()
    


pets_list()



