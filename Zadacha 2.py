mesto = int(input("Введите номер вашего места: "))

if mesto < 1 or mesto > 54:
    print("Такого места не существует. Попробуйте снова")
else:
    if mesto <= 36:
        if mesto % 2 == 1:
            print("У вас нижнее место в купе")
        else:
            print("У вас верхнее место в купе")
    else:
        if mesto % 2 == 1:
            print("У вас нижнее боковое место")
        else:
            print("У вас верхнее боковое место")