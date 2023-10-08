class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def average_score(self):
        if len(self.grades.values()) == 0:
            return None
        grades_values = [int(x) for y in self.grades.values() for x in y]
        grade = sum(grades_values) / len(grades_values)
        return round(grade, 1)

    def rate_l(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress\
                and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        cour_in_pr = ', '.join(self.courses_in_progress)
        fin_cour = ', '.join(self.finished_courses)
        grade = self.average_score()
        name_some_student = f'Имя: {self.name}\nФамилия: {self.surname}\n\
        Средняя оценка за домашние задания: {grade}\n\
        Курсы в процессе изучения: {cour_in_pr}\n\
        Завершённые курсы: {fin_cour}'
        return name_some_student

    def __lt__(self, other):
        if not isinstance(other, Student):
            return None
        grade_s = self.average_score()
        grade_o = other.average_score()
        return grade_s > grade_o


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def average_score(self):
        if len(self.grades.values()) == 0:
            return None
        grades_values = [int(x) for y in self.grades.values() for x in y]
        grade = sum(grades_values) / len(grades_values)
        return round(grade, 1)

    def __str__(self):
        grade = self.average_score()
        name_some_lecturer = f'Имя: {self.name}\nФамилия: {self.surname}\n\
        Средняя оценка за лекции: {grade}\n'
        return name_some_lecturer

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            return None
        grade_s = self.average_score()
        grade_o = other.average_score()
        return grade_s > grade_o


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached\
                and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        name_some_reviewer = f'Имя: {self.name}\nФамилия: {self.surname}\n'
        return name_some_reviewer


students = []
lecturers = []

best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
best_student.finished_courses += ['Git']
students.append(best_student)

some_student = Student('Name', 'Surname', 'Gender')
some_student.courses_in_progress += ['Git']
some_student.finished_courses += ['Python']
students.append(some_student)

cool_reviewer = Reviewer('Some', 'Buddy')
cool_reviewer.courses_attached += ['Python']
some_reviewer = Reviewer('Some', 'Reviever')
some_reviewer.courses_attached += ['Python', 'Git']

cool_lecturer = Lecturer("Some", "Person")
cool_lecturer.courses_attached += ['Python']
lecturers.append(cool_lecturer)

some_lecturer = Lecturer('Some', 'Lecturer')
some_lecturer.courses_attached += ['Git']
lecturers.append(some_lecturer)

cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 9)
some_reviewer.rate_hw(some_student, 'Git', 10)
some_reviewer.rate_hw(some_student, 'Git', 8)
some_reviewer.rate_hw(some_student, 'Git', 6)

best_student.rate_l(cool_lecturer, 'Python', 8)
best_student.rate_l(cool_lecturer, 'Python', 10)
some_student.rate_l(some_lecturer, 'Git', 9)
some_student.rate_l(some_lecturer, 'Git', 10)


def st_avarage_scores(list_st_or_lec, course):
    grades = []
    for someone in list_st_or_lec:
        if course in someone.grades.keys():
            value = someone.grades[course]
            for num in value:
                grades.append(int(num))

    grade = sum(grades) / len(grades)
    avarage_score = round(grade, 1)
    if isinstance(list_st_or_lec[0], Student):
        return f'Средняя оценка по студентам на курсе {course}: {avarage_score}'
    if isinstance(list_st_or_lec[0], Lecturer):
        return f'Средняя оценка по лекторам на курсе {course}: {avarage_score}'


print(st_avarage_scores(list_st_or_lec=students, course='Git'))
print(st_avarage_scores(list_st_or_lec=lecturers, course='Python'))

print(best_student.grades)
print(some_student.grades)
print(cool_lecturer.grades)
print(some_lecturer.grades)
print(best_student.surname)

print(some_reviewer.courses_attached)
print(some_student.finished_courses)

print(some_reviewer)
print(best_student)
print(some_lecturer)

print(some_lecturer > cool_lecturer)
print(best_student > some_student)
