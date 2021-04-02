class Grades:
    def __gt__(self, other):
        return self.avg_grade() > other.avg_grade()

    def __lt__(self, other):
        return self.avg_grade() < other.avg_grade()

    def __ge__(self, other):
        return self.avg_grade() >= other.avg_grade()

    def __le__(self, other):
        self.avg_grade() <= other.avg_grade()


class Student(Grades):
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def avg_grade(self):
        avg = 0
        for grade, grade_list in self.grades.items():
            if len(grade_list) > 0:
                avg += sum(grade_list) / len(grade_list)
        return avg

    def __str__(self):
        courses_in_progress_string = ' ,'.join(self.courses_in_progress)
        finished_courses_string = ' ,'.join(self.finished_courses)

        return f'Имя: {self.name}\n' \
               f'Фамилия: {self.surname}\n' \
               f'Средняя оценка за домашние задания {self.avg_grade()}\n' \
               f'Курсы в процессе изучения: {courses_in_progress_string}\n'\
               f'Завершенные курсы: {finished_courses_string}'

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            lecturer.grades.setdefault(course, [])
            lecturer.grades[course] += [grade]
        else:
            return 'Ошибка'



class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []



class Lecturer(Grades, Mentor):
    def __init__(self, *args):
        self.grades = {}
        super(Lecturer, self).__init__(*args)
        pass

    def __cmp__(self, other):
        if isinstance(other, Lecturer):
            return self.avg_grade() - other.avg_grade()
        else:
            return None

    def avg_grade(self):
        avg = 0
        for grade, grade_list in self.grades.items():
            if len(grade_list) > 0:
                avg += sum(grade_list) / len(grade_list)
        return avg

    def __str__(self):
        return f'Имя: {self.name}\n' \
               f'Фамилия: {self.surname}\n' \
               f'Средняя оценка за лекции {self.avg_grade()}'



class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'



best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']

best_student1 = Student('Homer', 'Simpson', 'male')
best_student1.courses_in_progress += ['Python']

cool_mentor = Reviewer('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']

cool_lecturer = Lecturer('Another', 'Buddy')
cool_lecturer.courses_attached += ['Python']
best_student.rate_lecturer(cool_lecturer, 'Python', 10)


cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)

cool_mentor.rate_hw(best_student1, 'Python', 5)
cool_mentor.rate_hw(best_student1, 'Python', 5)
cool_mentor.rate_hw(best_student1, 'Python', 5)

print(best_student > best_student1)


print(cool_lecturer.grades)
print(cool_lecturer.name, cool_lecturer.surname, cool_lecturer.courses_attached)
print(best_student.grades)
print(best_student)