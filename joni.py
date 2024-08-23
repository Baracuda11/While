my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
a = 0
b = len([42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5])
while True:
    my_list = int(input("Введите число"))
    if my_list > 0:
        print(my_list)
        continue
    else:
        print("Конец цикла")
        break
