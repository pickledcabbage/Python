# Dmitriy Gutnk 77099786 and Qiaofen Yang 41065325. Lab Assignment 6. Section 12

#
#
# Part C
#
#

# C.1
def contains(x: str, y: str) -> bool:
    '''Checks in string x contains String y'''
    return y in x
assert contains('banana', 'ana')
assert not contains('racecar', 'ck')

# C.2
def change_to_letters(x:str) -> str:
    '''Changes string x to have only spaces and letters'''
    s = ''
    for i in x:
        if i in "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'":
            s+=i
        else:
            s+=' '
    return s

def sentence_stats(x:str):
    '''Prints statistics of string x'''
    print('Characters: ',len(x))
    word = False
    onlyletters = change_to_letters(x)
    L = str.split(onlyletters)
    letters = 0
    words = 0
    for word in L:
        letters+=len(word)
        words+=1
    print('Words: ',words)
    print('Average word length: ',letters/words)
  
    
sentence_stats("***The ?! quick brown fox:  jumps over the lazy dog.")
sentence_stats("I love UCI")
print('\n\n\n') 

#C.3
def initials(x:str)-> str:
    '''Takes a name(string x) and returns the initials of the name in upper case'''
    L = str.split(x)
    initials = ''
    for let in L:
        initials+=let[0]
    return str.upper(initials)
assert initials('Bill Cosby') == 'BC'
assert initials('Guido van Rossum') == 'GVR'
assert initials('alan turing') == 'AT'


#
#
# Part D
#
#

# D.1
from random import randrange
for i in range(0,50):
    print(randrange(1,7))

# D.2
def roll2dice()-> int:
    '''Returns the sum of 2 dice rolls'''
    return randrange(1,7) + randrange(1,7)
for i in range(0,50):
    print(roll2dice())
print('\n\n\n')

# D.3
def distribution_of_rolls(x:int):
    '''Prints out statistics of x rolls'''
    L = [0,0,0,0,0,0,0,0,0,0,0]
    for i in range(0,x):
        roll = roll2dice()
        L[roll-2]+=1
    counter = 2
    for i in L:
        print('%2.0f:'%counter,'%6.0f'%i,'(%4.1f'%(i*100.0/x)+'%)','*'*i)
        counter+=1
    print('-------------------')
    print('%10.0f'%x,'rolls')
distribution_of_rolls(200)
print('\n\n\n')

# E.1
def change(x:str,y:int)->str:
    '''Shifts char y by x spaces n the alphabet'''
    if ord(x)>=65 and ord(x)<=90:
        if(ord(x)+y%26>90):
            return chr(ord(x)+y%26-26)
        else:
            return chr(ord(x)+y%26)
    elif ord(x)>=97 and ord(x)<=122:
        if(ord(x)+y%26>122):
            return chr(ord(x)+y%26-26)
        else:
            return chr(ord(x)+y%26)
    return x

def Caesar_encrypt(s:str,y:int)->str:
    '''This function encrypts the str s by shifting every letter by y locations'''
    temp = ''
    for i in s:
        temp+=(change(i,y))
    return temp

def Caesar_decrypt(s:str,y:int)->str:
    '''This program deciphers the caesaring encryption by swhifting it back by y spaces'''
    return Caesar_encrypt(s,-1*y)

message = 'Abizjcksa'
for i in range(0,26):
    print('%2.0f'%i+': '+Caesar_decrypt(message,i))
print('\n\n\n')

#
#
# Part F
#
#

L = [ "Four score and seven years ago, our fathers brought forth on",
  "this continent a new nation, conceived in liberty and dedicated",
  "to the proposition that all men are created equal.  Now we are",
  "   engaged in a great 		civil war, testing whether that nation, or any",
  "nation so conceived and so dedicated, can long endure.        " ]

# F.1
def print_line_numbers(s:list):
    '''Prints the list of strings with each line number followed by the string itself'''
    counter = 1
    for i in s:
        print(str(counter)+": "+i)
        counter+=1
print_line_numbers(L)

# F.2
def stats(s:list):
    print(str(len(s))+" lines in the list")
    counter = 0
    characters = 0
    for i in s:
        characters += len(i)
        if i == '':
            counter+=1
    print(str(counter)+" empty lines")
    print(str(characters*1.0/len(s))+" average characters per line")
    print(str(characters*1.0/(len(s)-counter))+" average characters per non-empty line")

# F.3
def list_of_words(l:list)->list:
    '''This functions returns all the words in the given list in a list'''
    temp = []
    for i in l:
        temp.extend(str.split(i))
    return temp
print('\n\n\n')

