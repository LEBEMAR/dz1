#простая задача

a = input("Введите первое число в двоичной системе: ")
b = input("Введите второе число в двочной системе: ")
summa = bin(int(a, 2) + int(b, 2))[2:]

print("Cумма равна ", summa)

#более сложная задача

number_column = int(input("Введите номер столбца "))
res = ""

while number_column > 0:
    r = n % 26
    if r == 0:
        r = 26
    res = chr(r + 64) + res
    number_column = (number_column - r) // 26
print(res)
    
    


