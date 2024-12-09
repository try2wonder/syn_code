my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ,11 ,12 ,13 ,14, 15, 16]

   
def recf(x):
    if len(x) == 0:
        print('Конец списка')
        return
    print(x.pop(0))
    recf(x)
    
recf(my_list)