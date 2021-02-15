from Gui import *

class Human:
#Класс "Человек
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
	
    def get_course(self):
        """Возращает значение атрибута 'курс' объекта"""
        return self._course

    def set_course(self, course):
        """Устанавливает/изменяет значение атрибута 'курс' объекта. Параметр - курс"""
        self._course = course

    def study(self, subject = "математика"):
        """Метод учения. Один параметр - учебный предмет"""
        print(self._name, "учит предмет", subject)

    def info(self):
        """Сообщает общую информацию об объекте"""
        print("Меня зовут {}, мне {}, я учусь на {}-м курсе.".format(self._name, self._age, self._course))


class Schoolboy(Human):
    '''Класс "Школьник", наследуемый от класса "Человек"'''
    def __init__(self, name, age, grade, performance, school_number):
        super().__init__(name, age)
        self._grade = grade             # Атрибут - Класс
        self._performance = performance # Атрибут - Успеваемость
        self._school_number = school_number # Атрибут - номер школы

    def get_grade(self):
        return self._grade	

    def set_grade(self, grade):
        self._grade = grade
	
    def get_performance(self):
        return self._performance

    def set_performance(self, performance):
        self._performance = performance

    def get_school_number(self):
        return self._school_number
	
    def set_school_number(self, s_number):
        self._school_number = s_number

    def study(self, subject = "математика"):
        """Метод учения. Один параметр - учебный предмет"""
        print(self._name, "учит предмет", subject)

    def make_home_work(self):
        print(self._name, "выполняет домашнее задание")
    
    def info(self):
        print("Меня зовут {}, мне {}, я учусь в {}-м классе, я {}.".format(self._name, self._age, self._grade, self._performance))


class Programmer(Human):
    def __init__(self, name, age, level, favorite_lang):
        super().__init__(name, age)
        self._level = level
        self._favorite_lang = favorite_lang

    def get_level(self):
        return self._level
    
    def set_level(self, level):
        self._level = level

    def get_favorite_lang(self):
        return self._favorite_lang
    
    def set_favorite_lang(self, favorite_lang):
        self._favorite_lang = favorite_lang


class Doctors(Human):
    def __init__(self, name, age, kind):
        super().__init__(name, age)
        self._kind = kind

    def get_kind(self):
        return self._kind

    def set_kind(self, kind):
        self._kind = kind

    def health(self, human):
        print("Дкотор", _name, "лечит", human.get_name())



if __name__ == '__main__':
    Dima = Student("Дмитрий", 21, 3)
    Ahmad = Student("Ахмад", 20, 2)
    Jhon = Student("Джон", 19, 1)

    Dima.info()
    Ahmad.info()
    Jhon.info()

    Ali = Schoolboy("Али", 14, 8, "отличник", 3)

    print(Ali.get_age())    
    Ali.info()
    root.mainloop()