# Заполните массив элементами арифметической прогрессии.
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры.
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

def fill_mass(a,n,d):
    array = []
    for i in range(0,d):
        array.insert(i,a + n * i)
    return (array)

a = int(input('Введите первый элемент арифметической прогрессии = '))
n = int(input('Введите разность элементов арифметической прогрессии = '))
d = int(input('Введите количество элементов арифметической прогрессии = '))

print(f"Арифметческая прогрессия -> {fill_mass(a,n,d)}")