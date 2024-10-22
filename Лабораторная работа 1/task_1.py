numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
n = 0
for i in numbers:
    if i != None:
        n += i
numbers[numbers.index(None)] = n/len(numbers)
# TODO заменить значение пропущенного элемента средним арифметическим

print("Измененный список:", numbers)
