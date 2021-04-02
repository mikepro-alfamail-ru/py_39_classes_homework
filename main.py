class GradesCompare:
    '''
    Все-таки тронул немного класс Student. Вынес инициализацию словаря оценок и функцию определения средней оценки,
    т.к. они идентичны у студентов и у лекторов.

    Теперь этот класс GradesCompare - родительский для студентов и лекторов, хранит в себе функции сравнения, рассчет
    средней оценки и инициализацию словаря оценок.
    '''
    def __init__(self, *args):
        self.grades = {}

    def __eq__(self, other):
        if isinstance(other, type(self)):
            return self.avg_grade() == other.avg_grade()

    def __gt__(self, other):
        if isinstance(other, type(self)):
            return self.avg_grade() > other.avg_grade()

    def __ge__(self, other):
        if isinstance(other, type(self)):
            return self.avg_grade() >= other.avg_grade()

    def avg_grade(self):
        avg = 0
        for grade, grade_list in self.grades.items():
            if len(grade_list) > 0:
                avg += sum(grade_list) / len(grade_list)
        return avg



class Student(GradesCompare):
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        super().__init__()

    def __str__(self):
        courses_in_progress_string = ' ,'.join(self.courses_in_progress)
        finished_courses_string = ' ,'.join(self.finished_courses)

        return f'Имя: {self.name}\n' \
               f'Фамилия: {self.surname}\n' \
               f'Средняя оценка за домашние задания {self.avg_grade()}\n' \
               f'Курсы в процессе изучения: {courses_in_progress_string}\n'\
               f'Завершенные курсы: {finished_courses_string}'

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and \
                course in lecturer.courses_attached and \
                course in self.courses_in_progress:
            lecturer.grades.setdefault(course, [])
            lecturer.grades[course] += [grade]
        else:
            return 'Ошибка'



class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []



class Lecturer(GradesCompare, Mentor):
    def __init__(self, *args):
        super().__init__()
        Mentor.__init__(self, *args)

    def __cmp__(self, other):
        if isinstance(other, Lecturer):
            return self.avg_grade() - other.avg_grade()
        else:
            return None

    def __str__(self):
        return f'Имя: {self.name}\n' \
               f'Фамилия: {self.surname}\n' \
               f'Средняя оценка за лекции {self.avg_grade()}'



class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and \
                course in self.courses_attached and \
                course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

        def __str__(self):
            return f'Имя: {self.name}\n' \
                   f'Фамилия: {self.surname}\n'



def avg_grade_by_course(person_list, course):
    '''
    Так как структура словаря с оценками у лекторов и у студентов одинакова, решил сделать одну функцию
    '''
    grades_list = []
    for person in person_list:
        if course in person.grades:
            grades_list += person.grades[course]
    if len(grades_list) > 0:
        return sum(grades_list) / len(grades_list)
    else:
        return 0



best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']

best_student1 = Student('Homer', 'Simpson', 'male')
best_student1.courses_in_progress += ['Python']

cool_mentor = Reviewer('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']

cool_lecturer = Lecturer('Another', 'Buddy')
cool_lecturer.courses_attached += ['Python', 'Java']

cool_lecturer1 = Lecturer('Ash', 'Williams')
cool_lecturer1.courses_attached += ['Python', 'How to beat evil dead']

best_student.rate_lecturer(cool_lecturer, 'Python', 10)

cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)

cool_mentor.rate_hw(best_student1, 'Python', 8)
cool_mentor.rate_hw(best_student1, 'Python', 8)
cool_mentor.rate_hw(best_student1, 'Python', 8)

print('Проверка рассчета средней оценки:')
print(avg_grade_by_course([best_student, best_student1], 'Python'))
print(avg_grade_by_course([cool_lecturer, cool_lecturer1], 'Python'))
print()

print('Проверка вывода объекта на печать:')
print(cool_lecturer1)
print(best_student)
print()

print('Проверка оператора сравнения для класса')
print(cool_lecturer1 != cool_lecturer)