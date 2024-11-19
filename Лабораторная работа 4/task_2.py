# TODO импортировать необходимые молули
import csv
import json

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    with open(INPUT_FILENAME, 'r') as csvfile: # TODO считать содержимое csv файла
        string = csv.DictReader(csvfile)
        array_of_dicts = [row for row in string]
    with open(OUTPUT_FILENAME, 'w') as jsonfile:# TODO Сериализовать в файл с отступами равными 4
        json.dump(array_of_dicts, jsonfile, indent=4)


if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
