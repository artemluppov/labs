# TODO решите задачу
import json
def task(file_path) -> float:
    with open(file_path, 'r') as file:
        json_data = json.load(file)
    result = 0.0
    for elem in json_data:
        score = elem.get("score")
        weight = elem.get("weight")
        result += score * weight
    return round(result, 3)

file_path = 'input.json'
print(task(file_path))
