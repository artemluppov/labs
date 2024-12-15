import doctest
# TODO Написать 3 класса с документацией и аннотацией типов
class Car:
    def __init__(self, brand: str, model: str, year: int, mileage: (int, float)):
        """
        Создание и подготовка к работе объекта "Автомобиль"
        :param brand: марка автомобиля
        :param model: модель автомобиля
        :param year: год выпуска
        :param mileage: пробег автомобиля
        :raise TypeError: если типы данных неправильные, то ошибка
        :raise ValueError: пробег и год выпуска не могут быть отрицательными
        Примеры:
        >>> car = Car("Toyota", "Corolla", 2020, 15000)  # инициализация экземпляра класса
        >>> car.brand
        'Toyota'
        >>> car.year
        2020
        >>> car.mileage
        15000
        """
        if not isinstance(brand, str):
            raise TypeError("Brand should be string type")
        self.brand = brand
        if not isinstance(model, str):
            raise TypeError("Model should be string type")
        self.model = model
        if not isinstance(year, int):
            raise TypeError("Year should be int type")
        if year <= 0:
            raise ValueError("Year should be positive")
        self.year = year
        if not isinstance(mileage, (int, float)):
            raise TypeError("Mileage should be int or float type")
        if mileage < 0:
            raise ValueError("Mileage should be non-negative")
        self.mileage = mileage

    def car_age(self) -> int:
        """
        Рассчитывает возраст автомобиля.
        :return: возраст автомобиля
        Пример:
        >>> car = Car("Toyota", "Corolla", 2020, 15000)
        >>> car.car_age()
        4
        """
        current_year = 2024  # Для примера текущий год
        return current_year - self.year

    def is_low_mileage(self) -> bool:
        """
        Проверяет, является ли автомобиль с низким пробегом (меньше 50000 км).
        :return: Является ли автомобиль с низким пробегом
        Примеры:
        >>> car = Car("Toyota", "Corolla", 2020, 15000)
        >>> car.is_low_mileage()
        True
        >>> car = Car("Honda", "Civic", 2018, 60000)
        >>> car.is_low_mileage()
        False
        """
        return self.mileage < 50000


class Movie:
    def __init__(self, title: str, director: str, release_year: int, genre: str):
        """
        Создание и подготовка к работе объекта "Фильм"
        :param title: название фильма
        :param director: режиссёр фильма
        :param release_year: год выпуска
        :param genre: жанр фильма
        :raise TypeError: если типы данных неправильные, то ошибка
        :raise ValueError: год выпуска не может быть отрицательным
        Примеры:
        >>> movie = Movie("Inception", "Christopher Nolan", 2010, "Sci-Fi")
        >>> movie.title
        'Inception'
        >>> movie.director
        'Christopher Nolan'
        >>> movie.genre
        'Sci-Fi'
        """
        if not isinstance(title, str):
            raise TypeError("Title should be string type")
        self.title = title
        if not isinstance(director, str):
            raise TypeError("Director should be string type")
        self.director = director
        if not isinstance(release_year, int):
            raise TypeError("Release year should be int type")
        if release_year < 0:
            raise ValueError("Release year should be non-negative")
        self.release_year = release_year
        if not isinstance(genre, str):
            raise TypeError("Genre should be string type")
        self.genre = genre

    def get_description(self) -> str:
        """
        Возвращает краткое описание фильма
        :return: Строка с названием фильма, режиссёром и жанром
        Пример:
        >>> movie = Movie("Inception", "Christopher Nolan", 2010, "Sci-Fi")
        >>> movie.get_description()
        'Inception directed by Christopher Nolan, Genre: Sci-Fi'
        """
        return f"{self.title} directed by {self.director}, Genre: {self.genre}"

    def is_classic(self) -> bool:
        """
        Проверяет, является ли фильм классикой (выпущен до 2000 года).
        :return: Является ли фильм классикой
        >>> movie = Movie("The Matrix", "The Wachowskis", 1999, "Sci-Fi")
        >>> movie.is_classic()
        True
        >>> movie = Movie("Avatar", "James Cameron", 2009, "Sci-Fi")
        >>> movie.is_classic()
        False
        """
        return self.release_year < 2000


class Planet:
    def __init__(self, name: str, radius: (int, float), distance_from_sun: (int, float)):
        """
        Создание и подготовка к работе объекта "Планета"
        :param name: название планеты
        :param radius: радиус планеты
        :param distance_from_sun: расстояние от планеты до Солнца
        :raise TypeError: если типы данных неправильные, то ошибка
        :raise ValueError: радиус и расстояние не могут быть отрицательными
        Примеры:
        >>> planet = Planet("Earth", 6371, 149.6)
        >>> planet.name
        'Earth'
        >>> planet.radius
        6371
        >>> planet.distance_from_sun
        149.6
        """
        if not isinstance(name, str):
            raise TypeError("Name should be string type")
        self.name = name
        if not isinstance(radius, (int, float)):
            raise TypeError("Radius should be int or float type")
        if radius <= 0:
            raise ValueError("Radius should be positive")
        self.radius = radius
        if not isinstance(distance_from_sun, (int, float)):
            raise TypeError("Distance from sun should be int or float type")
        if distance_from_sun <= 0:
            raise ValueError("Distance from sun should be positive")
        self.distance_from_sun = distance_from_sun

    def surface_area(self) -> float:
        """
        Рассчитывает поверхность планеты.
        :return: площадь поверхности планеты
        Пример:
        >>> planet = Planet("Earth", 6371, 149.6)
        >>> planet.surface_area()
        510064041.07676
        """
        return 4 * 3.14159 * self.radius ** 2

    def is_terrestrial(self) -> bool:
        """
        Проверяет, является ли планета землеподобной (с радиусом от 3000 до 8000 км).
        :return: Является ли планета землеподобной
        Примеры:
        >>> planet = Planet("Earth", 6371, 149.6)
        >>> planet.is_terrestrial()
        True
        >>> planet = Planet("Jupiter", 69911, 778.5)
        >>> planet.is_terrestrial()
        False
        """
        return 3000 <= self.radius <= 8000


if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    doctest.testmod()
    pass