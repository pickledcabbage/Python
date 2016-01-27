# Dmitriy Gutnik 77099786 and Xiaochi Song
from collections import namedtuple
Dish = namedtuple('Dish', 'name price calories')

def print_caption(s:str):
    '''Prints captions for me :/ '''
    print('\n'*2+'*'*10+' Part: '+s+'*'*10+'\n'*2)
#
#
# Part C:
#
#

# C.1
print_caption('C.1')

def read_menu_with_count(s:str)->list:
    '''Returns the given menu in a dish list structure'''
    infile = open(s,'r')
    temp = []
    for line in infile:
        w = str.split(line,'\t')
        if len(w) > 1:
            temp.append(Dish(w[0],float(w[1][1:]),float(w[2].strip())))
    infile.close()
    return temp

print(read_menu_with_count('menu2.txt'))

# C.2
print_caption('C.2')

def read_menu(s:str)->list:
    '''Returns the given menu in a Dish list structure and amount of items isn't given'''
    infile = open(s,'r')
    temp = []
    for line in infile:
        w = str.split(line,'\t')
        temp.append(Dish(w[0],float(w[1][1:]),float(w[2].strip())))
    infile.close()
    return temp

print(read_menu('menu3.txt'))

# C.3
print_caption('C.3')

def write_menu(l:list,s:str):
    '''Print the menu in list form from l to file with name s'''
    outfile = open(s,'w')
    outfile.write(str(len(l))+'\n')
    for i in l:
        a = i.name+'\t$'+str(i.price)+'\t'+str(i.calories)+'\n'
        outfile.write(a)
    outfile.close()

write_menu(read_menu('menu3.txt'),'hello.txt')

#
#
# Part D:
#
#

Course = namedtuple('Course', 'dept num title instr units')
  # Each field is a string except the number of units
ics31 = Course('ICS', '31', 'Intro to Programming', 'Kay', 4.0)
ics32 = Course('ICS', '32', 'Programming with Libraries', 'Thornton', 4.0)
wr39a = Course('Writing', '39A', 'Intro Composition', 'Alexander', 4.0)
wr39b = Course('Writing', '39B', 'Intermediate Composition', 'Gross', 4.0)
bio97 = Course('Biology', '97', 'Genetics', 'Smith', 4.0)
mgt1  = Course('Management', '1', 'Intro to Management', 'Jones', 2.0)
  
Student = namedtuple('Student', 'ID name level major studylist')
  # All are strings except studylist, which is a list of Courses.
sW = Student('11223344', 'Anteater, Peter', 'FR', 'PSB', [ics31, wr39a, bio97, mgt1])
sX = Student('21223344', 'Anteater, Andrea', 'SO', 'CS', [ics31, wr39b, bio97, mgt1])
sY = Student('31223344', 'Programmer, Paul', 'FR', 'COG SCI', [ics32, wr39a, bio97])
sZ = Student('41223344', 'Programmer, Patsy', 'SR', 'PSB', [ics32, mgt1])
  
StudentBody = [sW, sX, sY, sZ]

# D.1
print_caption('D.1')

def Students_at_level(L:list,S:str)->list:
    '''Takes a list of students L and a string representing class level, S and returns
       a list of students that match that class level'''
    temp = []
    for student in L:
        if student.level == S:
            temp.append(student)
    return temp

print(Students_at_level(StudentBody,'FR'))

# D.2
print_caption('D.2')

def Students_in_majors(L:list,S:str)->list:
    '''Takes a list of students L and a string representing major, S and returns
       a list of students that match that majors'''
    temp = []
    for student in L:
        if student.major == S:
            temp.append(student)
    return temp

print(Students_in_majors(StudentBody,'CS'))

# D.3
print_caption('D.3')

def Course_equals(c1: Course, c2: Course) -> bool:
    ''' Return True if the department and number of c1 match the department and
	     number of c2 (and False otherwise)
    '''
    return (c1.dept == c2.dept and c1.num == c2.num)
    
def Course_on_studylist(c: Course, SL: 'list of Course') -> bool:
    ''' Return True if the course c equals any course on the list SL (where equality
	     means matching department name and course number) and False otherwise.
    '''
    for s in SL:
        if Course_equals(c,s):
            return True
    return False
def Student_is_enrolled(S: Student, department: str, coursenum: str) -> bool:
    ''' Return True if the course (department and course number) is on the student's
	     studylist (and False otherwise)
    '''
    return Course_on_studylist(Course(department,coursenum,'','',''),S.studylist)
def Students_in_class(L:list, D:str, CN:str) -> list:
    ''' Takes in: list of students L, department name D, and course number CN
        Returns: list of students in that class
    '''
    temp = []
    for s in L:
        if Student_is_enrolled(s,D,CN):
            temp.append(s)
    return temp

print(len(Students_in_class(StudentBody,'ICS','31')))
print(Students_in_class(StudentBody,'ICS','31'))

# D.4
print_caption('D.4')

def Students_names(L:list)->list:
    ''' Takes in: list of students L
        Returns: names of the students in L
    '''
    temp = []
    for s in L:
        temp.append(s.name)
    return temp

print(Students_names(Students_in_class(StudentBody,'ICS','31')))

# D.5
print_caption('D.5')

ICSmajors = ['CS', 'CSE', 'BIM', 'INFX', 'CGS', 'SE', 'ICS']

temp = []
for m in ICSmajors:
    temp.extend(Students_in_majors(StudentBody,m))
print(temp)
print('\n')

print(Students_names(temp))
print('\n')

print(Students_names(Students_at_level(temp,'SR')))
print('\n')

print(len(Students_at_level(temp,'SR')))
print('\n')

print(str(len(Students_at_level(temp,'SR'))*100.0/len(temp))+'%')
print('\n')

print(len(Students_at_level(Students_in_class(temp,'ICS','31'),'FR')))
print('\n')

def total_units_of_student(S:Student)-> float:
    ''' Takes in: Student S
        Returns: his/her total amount of units
    '''
    total = 0.0
    for c in S.studylist:
        total += c.units
    return total
def average_units_students(L:list)->float:
    ''' Takes in: list of students
        Returns: average number of units of those students
    '''
    total = 0.0
    for s in L:
        total += total_units_of_student(s)
    return total/len(L)

print(average_units_students(StudentBody))
print('\n')
