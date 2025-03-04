god = int(input("Введите год "))
if (god % 4 == 0 and god % 100 is not 0) or(god % 400 == 0):
    print("Год високосный")
else:
    print("Это не високосный год")