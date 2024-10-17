first=int(input('Введите число: '))
second=int(input('Введите число:'))
third=int(input('Введите число: '))
if first==second and second==third:
    print("Все числа равны между собой")
elif first==second or second==third or first==third:
    print(2,"из", 3,"введенных числла равны между собой")
else:
    print("Равных чисел нет")