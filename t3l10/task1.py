pets = {
    # pname: {
    #     "breed": breed,
    #     "age": age,
    #     "owner": owner
    # }
}



pname = input("enter your pet's name: ")
pets[pname] = {
    'breed': input("enter breed: "),
    'age': int(input("enter age: ")),
    'owner': input("enter owner: ")
        }
print(pets)
print(list(pets[pname].values())[1])

years = ''

if list(pets[pname].values())[1] % 10 == 1 and list(pets[pname].values())[1] % 100 != 11:
    years = 'год'
elif 1 < list(pets[pname].values())[1] % 10 < 5 and list(pets[pname].values())[1] % 100 not in range(10, 20):
    years = 'года'
else:
    years = 'лет'

print('Это', f'{list(pets[pname].values())[0]}', 'по кличке ', f'"{list(pets.keys())[0]}".', "Возраст питомца:", list(pets[pname].values())[1], f'{years}.', 'Имя владельца:', list(pets[pname].values())[2])