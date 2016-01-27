# Dmitriy Gutnik 77099786 and Kenny Nguyen 56639848. Lab Assignment 9. Sect. 12

from random import choice
from random import randrange
from collections import namedtuple

NUMBER_OF_STUDENTS = 200
NUMBER_OF_QUESTIONS = 20
NUMBER_OF_CHOICES = 4  # 3 choices is A/B/C, 4 choices is A/B/C/D, 5 is A/B/C/D/E
CORRECT_ANSWERS = 'CCDDACABCACDCDBAADBA'

# C.1
ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
def generate_answers()->str:
    '''Returns a string of letters randomly assigned from chosen choices'''
    s = ''
    for i in range(0,NUMBER_OF_QUESTIONS):
        s += choice(ALPHABET[:NUMBER_OF_CHOICES])
    return s
print(generate_answers())

# C.2
Student = namedtuple('Student', 'name answers')
def random_students() -> list:
    '''Returns a list of random students'''
    temp = []
    for student in range(0, NUMBER_OF_STUDENTS):
        temp.append(Student(randrange(1000,9999), generate_answers()))
    return temp 

# C.3
Student = namedtuple('Student', 'name answers scores total')
def random_students() -> list:
    '''Returns a list of random students'''
    temp = []
    for student in range(0, NUMBER_OF_STUDENTS):
        holder = generate_answers()
        holder2 = correctly_answered(holder)
        temp.append(Student(randrange(1000,9999), holder,holder2,total_correct(holder2)))
    return temp 

def correctly_answered(S:str)->list:
    temp = []
    for i in range(0,NUMBER_OF_QUESTIONS):
        if S[i] == CORRECT_ANSWERS[i]:
            temp.append(1)
        else:
            temp.append(0)
    return temp

def total_correct(L:list)->int:
    total = 0
    for i in L:
        total+=i
    return total

def get_total(S:Student)->int:
    return S.total

temporary = sorted(random_students(),key=get_total,reverse=True)[0:10]
for stud in temporary:
    print(stud.name)

# C.4
def generate_weighted_student_answer(c:str) -> str:
    s = ''
    s += choice(ALPHABET[:NUMBER_OF_CHOICES] + randrange(0,8) * c)
    return s

def random_students2() -> list:
    '''Returns a list of random students'''
    temp = []
    for student in range(0, NUMBER_OF_STUDENTS):
        holder = generate_answers2()
        holder2 = correctly_answered(holder)
        temp.append(Student(randrange(1000,9999), holder,holder2,total_correct(holder2)))
    return temp 

def generate_answers2()->str:
    '''Returns a string of letters randomly assigned from chosen choices'''
    s = ''
    for i in range(0,NUMBER_OF_QUESTIONS):
        s += generate_weighted_student_answer(CORRECT_ANSWERS[i])
    return s

temporary = sorted(random_students2(),key=get_total,reverse=True)[0:10]
print(temporary)
for stud in temporary:
    print(stud.name)

# C.5
def question_weights(SL:list)->list:
    temp = []
    for i in range(0,NUMBER_OF_QUESTIONS):
        temp.append(0)
    for s in SL:
        temp = add_to_weight(s.scores,temp)
    return temp

def add_to_weight(AL:list,W:list)->list:
    for i in range(0,NUMBER_OF_QUESTIONS):
        if (AL[i]==0):
            W[i]+=1
    return W

def Student_weighted_score(S:Student,WL:list)-> Student:
    total = 0
    for i in range(0,NUMBER_OF_QUESTIONS):
        total+=S.scores[i]*WL[i]
    return Student(S.name,S.answers,S.scores,total)

temporary = random_students2()
weights = question_weights(temporary)
for num in range(0,NUMBER_OF_STUDENTS):
    temporary[num] = Student_weighted_score(temporary[num],weights)
temporary = sorted(temporary,key=get_total,reverse=True)[0:10]
print(temporary)
for stud in temporary:
    print(str(stud.name) + ' ' + str(stud.total))

# D.1a
letter_grades = 'ABCDF'
letter_weights = [4,3,2,1,0]
def calculate_GPA(grades:list) -> float:
    
    GPA = 0
    for grade in grades:
        GPA += letter_weights[str.find(letter_grades,grade)]
    return GPA*1.0/len(grades)

grade_values = {'A':4, 'A+':4, 'A-':3.7, 'B+':3.3, 'B':3, 'B-':2.7, 'C+':2.3, 'C':2, 'C-':1.7, 'D+':1.3, 'D':1, 'D-':0.7, 'F':0}
def calculate_GPA2(grades:list) -> float:
    GPA = 0
    for grade in grades:
        GPA += grade_values[grade]
    return GPA*1.0/len(grades)

# D.2
def flatten_2D_list(l:list)-> list:
    temp = []
    for item in l:
        temp.extend(item)
    return temp

# D.3a
def skip_every_third_item(L:list)->None:
    '''Prints every third item in the given list'''
    for i in range(0,len(L)):
        if (i+1)%3!=0:
            print(L[i])
L = ['If', 'you', '432234', 'did', 'the', '9834234', 'exercise', 'correctly', '534523423', 
		 'this', 'should', '1044323', 'be', 'readable']
skip_every_third_item(L)

# D.3b
def skip_every_nth_item(L:list,n:int)->None:
    '''Prints every third item in the given list'''
    for i in range(0,len(L)):
        if (i+1)%n!=0:
            print(L[i])

# D.4a
def tally_days_worked(L:list)->dict:
    '''Takes in a list of amount of times people worked returns them in a tallied dict'''
    temp = {L[0]:1}
    for i in range(1,len(L)):
        if L[i] in temp:
            holder = L[i]
            temp[holder]+=1
        else:
            temp.update({L[i]:1})
    return temp

work_week = ['Bob', 'Jane', 'Kyle', 'Larry', 'Brenda', 'Samantha', 'Bob', 
             'Kyle', 'Larry', 'Jane', 'Samantha', 'Jane', 'Jane', 'Kyle', 
             'Larry', 'Brenda', 'Samantha']


# D.4b
hourly_wages = {'Kyle': 13.50, 'Brenda': 8.50, 'Jane': 15.50, 'Bob': 30.00, 'Samantha': 8.50, 'Larry': 8.50, 'Huey': 18.00}
workers = tally_days_worked(work_week)

def pay_employees(h:dict, w:dict)-> None:
    for key in h:
        print(key + ' will be paid ${:6.2f} for {:2d} hours of work at ${:4.2f} per hour.'.format(h[key] * 8 * w[key], h[key] * 8, w[key]))

pay_employees(workers, hourly_wages)

# D.5
def reverse_dict(D:dict)->dict:
    '''Reverse keys and values of a dictionary'''
    temp = {}
    for key in D:
        temp.update({D[key]:key})
    return temp

print(reverse_dict({'a': 'one', 'b': 'two', 'c': 'three', 'd': 'four', 'e': 'five', 'f': 'six'}))
