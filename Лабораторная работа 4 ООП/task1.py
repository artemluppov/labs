class MusicalInstrument:
    """
    Базовый класс для музыкальных инструментов.
    """

    def __init__(self, name: str, material: str, price: float) -> None:
        """
        Инициализация музыкального инструмента.
        :param name: Название инструмента
        :param material: Материал, из которого изготовлен инструмент
        :param price: Цена инструмента
        """
        self._name = name  # Закрытый атрибут, так как имя инструмента не должно изменяться извне
        self.material = material
        self.price = price

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str) -> None:
        if not isinstance(value, str):
            raise TypeError("Название инстумента должно быть строкой")
        self._name = value

    def play(self) -> str:
        """
        Метод, который описывает возможность игры на инструменте.
        :return: Строка с информацией об игре на инструменте
        """
        return f"Музыкант играет на {self._name}."

    def __str__(self) -> str:
        return f"{self._name} (Материал: {self.material}, Цена: {self.price} руб.)"

    def __repr__(self) -> str:
        return f"MusicalInstrument(name={self._name}, material={self.material}, price={self.price})"


class Guitar(MusicalInstrument):
    """
    Дочерний класс, представляющий гитару.
    """

    def __init__(self, name: str, material: str, price: float, string_count: int) -> None:
        """
        Инициализация гитары.
        :param name: Название инструмента
        :param material: Материал, из которого изготовлен инструмент
        :param price: Цена инструмента
        :param string_count: Количество струн на гитаре
        """
        super().__init__(name, material, price)
        self.string_count = string_count

    def play(self) -> str:
        """
        Переопределённый метод игры на инструменте.
        Причина переопределения: у гитары особенный способ игры - извлечение звуков с помощью струн.
        :return: Строка с информацией об игре на гитаре
        """
        return f"Музыкант играет на {self._name} с {self.string_count} струнами."

    def __str__(self) -> str:
        return f"{self._name} (Гитара, {self.string_count} струн, Материал: {self.material}, Цена: {self.price} руб.)"

    def __repr__(self) -> str:
        return f"Guitar(name={self._name}, material={self.material}, price={self.price}, string_count={self.string_count})"

if __name__ == "__main__":
    # Write your solution here
    pass
