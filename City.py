class Human:
#Класс "Человек"
	def __init__(self, name, age):
		"""Данный конструктор принимает 2 параметра - имя и возраст"""
		self._name = name
		self._age = age


	def get_name(self):
		"""Возвращает имя объекта"""
		return self._name


	def set_name(self, name):
		"""Устанавливает/изменяет имя объект. Параметр - имя"""
		self._name = name


	def get_age(self):
		"""Возвращает возраст объекта"""
		return self._age


	def set_age(self, age):
		"""Устанавливает/изменяет возраст объект. Параметр - возраст"""
		self._age = age


	def go(self, speed = None):
		"""Метод ходьбы. Если параметр скорости задан, то выводится скорость ходьбы."""
		if type(speed) == type(None):
			print(self._name, "ходит")
		else:
			print(self._name, "ходит со скоростью", speed)


	def eat(self, food = "xлеб"):
		"""Метод питания. Принимает один параметр - еда"""
		print(self._name, "ест", food)


class Student(Human):
#Класс "Студент", наследуемый от класса "Человек"
    def __init__(self, name, age, course):
        """Перегруженный конструктор. Три параметра - имя, возраст, курс"""
        super().__init__(name, age)
        self._course= course


    def study(self, subject = "математика"):
        """Метод учения. Один параметр - учебный предмет"""
        print(self._name, "учит предмет", subject)


    def get_course(self):
        """Возращает значение атрибута 'курс' объекта"""
        return self._course


    def set_course(self, course):
        """Устанавливает/изменяет значение атрибута 'курс' объекта. Параметр - курс"""
        self._course = course

    def info(self):
        """Сообщает общую информацию об объекте"""
        print("Меня зовут {}, мне {}, я учусь на {}-м курсе.".format(self._name, self._age, self._course))


class Schoolboy(Human):
    '''Класс "Школьник", наследуемый от класса "Человек"'''
    def __init__(self, name, age, grade, performance):
        super().__init__(name, age)
        self.grade = grade             # Атрибут - Класс
        self.performance = performance # Атрибут - Успеваемость
        self.school_number = school_number() # Атрибут - номер школы


Dima = Student("Дмитрий", 21, 3)
Ahmad = Student("Ахмад", 20, 2)
Jhon = Student("Джон", 19, 1)

Dima.info()
Ahmad.info()
Jhon.info()