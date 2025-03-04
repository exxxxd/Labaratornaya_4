mesto = int(input("Ведите номер вашего места"))
if mesto < 1 or mesto > 54:
    print("Такого места не существует. Попробуйте снова")
if mesto <= 36 and mesto % 2==1:
        print("У вас нижнее место в купе")
else:
        print ("У вас верхнее место в купе")
if mesto > 36:
    print("У вас боковое место")