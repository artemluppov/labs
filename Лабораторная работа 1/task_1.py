numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

n = sum(numbers[:numbers.index(None)]) + sum(numbers[numbers.index(None) + 1:])
numbers[numbers.index(None)] = n/len(numbers)
# TODO заменить значение пропущенного элемента средним арифметическим

print("Измененный список:", numbers)
