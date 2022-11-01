class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades1 = {}

    def summ_lec(self):
        totalStringLength = 0
        summ = 0
        for item in self.grades1.values():
            totalStringLength += len(item)
            summ += sum(item)
            self.sr_sum = round(summ / totalStringLength, 1)
        return self.sr_sum


    def __str__(self):
        res = f'Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка: {self.summ_lec()}'
        return res

    def __lt__(self, other):
        if self.summ_lec() > other.summ_lec() == True:
            return print("Средняя лектора больше средней ученика")
        else:
            return print("Средняя ученика больше чем средняя лектора")

class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f'Имя: {self.name} \nФамилия: {self.surname}'
        return res

class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lc(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades1:
                lecturer.grades1[course] += [grade]
            else:
                lecturer.grades1[course] = [grade]
        else:
            return 'Ошибка'

    def summ_lec(self):
        totalStringLength = 0
        summ = 0
        for item in self.grades.values():
            totalStringLength += len(item)
            summ += sum(item)
            self.sr_sum = round(summ / totalStringLength, 1)
        return self.sr_sum

    def progres(self):
        self.cours_prog = ",".join(self.courses_in_progress)
        return self.cours_prog
    def finish(self):
        self.finish_prog = ",".join(self.finished_courses)
        return self.finish_prog

    def __str__(self):
        res = f'Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка: {self.summ_lec()} \nКурсы в процессе изучения: {self.progres()} \nЗавершенные курсы: {self.finish()}'
        return res


best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python', 'Git']
best_student.courses_in_progress += ['Git']#курс который проходит ученик
best_student.finished_courses += ['Введение в программирование']
best_student2 = Student('Nikita', 'Effer', 'your_gender')
best_student2.courses_in_progress += ['Python']
best_student2.courses_in_progress += ['Git'] #курс который проходит ученик
best_student2.finished_courses += ['Дизайн и верстка']

cool_mentor = Reviewer('Some', 'Buddy') #проверяющий который ставит оценку
cool_mentor.courses_attached += ['Python']
cool_mentor.courses_attached += ['Git']#курс который ведет ментор
cool_mentor2 = Reviewer('Rita', 'Sunny') #проверяющий который ставит оценку
cool_mentor2.courses_attached += ['Python'] #курс который ведет ментор

cool_mentor.rate_hw(best_student, 'Python', 10) #выставление оценки ученику
cool_mentor.rate_hw(best_student, 'Python', 10) #выставление оценки ученику
cool_mentor.rate_hw(best_student, 'Git', 10) #выставление оценки ученику

cool_mentor2.rate_hw(best_student2, 'Python', 3) #выставление оценки ученику
cool_mentor2.rate_hw(best_student2, 'Python', 3) #выставление оценки ученику
cool_mentor2.rate_hw(best_student2, 'Python', 4) #выставление оценки ученику

lecturer_mentor = Lecturer('Nina', 'Petrova') # Лектор которму ставят оценку
lecturer_mentor.courses_attached += ['Python', 'Git']
lecturer_mentor2 = Lecturer('Katay', 'Katau') # Лектор которму ставят оценку
lecturer_mentor2.courses_attached += ['Python', 'Git']

best_student.rate_lc(lecturer_mentor, 'Python', 9)#выставление оценки ментору
best_student.rate_lc(lecturer_mentor, 'Python', 9)#выставление оценки ментору
best_student.rate_lc(lecturer_mentor, 'Git', 1)#выставление оценки ментору

best_student2.rate_lc(lecturer_mentor2, 'Python', 9)#выставление оценки ментору
best_student2.rate_lc(lecturer_mentor2, 'Python', 5)#выставление оценки ментору
best_student2.rate_lc(lecturer_mentor2, 'Git', 1)#выставление оценки ментору

# # для подсчета средней оценки за домашние задания по всем студентам в рамках конкретного курса
# # (в качестве аргументов принимаем список студентов и название курса);

# print(lecturer_mentor.grades1)
print(best_student.grades)
print(best_student2.grades)
# print('')
# print(cool_mentor)
# print('')
# print(cool_mentor2)
# print('')
# print(lecturer_mentor)
# print('')
# print(lecturer_mentor2)
# print('')
# print(best_student)
# print('')
# print(best_student2)
# print('')
# print(lecturer_mentor < best_student)

def summ_all(list_st, name_course):
    totalStringLength = 0
    summ = 0
    for items in list_st:
        for x in items.grades[name_course]:
            totalStringLength += 1
            summ += x
    return round(summ/totalStringLength, 1)

def summ_lector(list_lector, name_course):
    totalStringLength = 0
    summ = 0
    for items in list_lector:
        for x in items.grades1[name_course]:
            totalStringLength += 1
            summ += x
    return round(summ/totalStringLength, 1)

print(f' Средняя оцепок студентов {summ_all([best_student, best_student2], "Python")}')
print(f' Средняя оцепок лекторов {summ_lector([lecturer_mentor, lecturer_mentor2], "Python")}')