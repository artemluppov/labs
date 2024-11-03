# TODO Напишите функцию find_common_participants
def find_common_participants(string1, string2, mark=','):
    return sorted(list(set(string1.split(mark)).intersection(string2.split(mark))))

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой
print(find_common_participants(participants_first_group, participants_second_group, '|'))