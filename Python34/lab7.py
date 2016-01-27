# Dmitriy Gutnik 77099786 and Patrick Mang 58086269. Lab Assignment 7. Lab Section 12


surnames = []
femalenames = []
malenames = []

from collections import namedtuple
from random import randrange
Namedata = namedtuple('Namedata','name percent amount')

infile = open('surnames.txt','r')
for q in infile:
    w = str.split(q)
    surnames.append(Namedata(w[0],w[1],w[2]))

totalfemales = 0
infile = open('femalenames.txt','r')
for  q in infile:
    w = str.split(q)
    totalfemales+=int(w[2].replace(',',''))
    femalenames.append(Namedata(w[0],w[1],w[2].replace(',','')))

totalmales = 0
infile = open('malenames.txt','r')
for q in infile:
    w = str.split(q)
    totalmales+=int(w[2].replace(',',''))
    malenames.append(Namedata(w[0],w[1],w[2].replace(',','')))
    
infile.close()

# C.1-C.3
def get_name()-> str:
    skew = randrange(0,totalmales+totalfemales)
    first = 0
    if skew > totalmales:
        first = femalenames[randrange(0,len(femalenames))].name
    else:
        first = malenames[randrange(0,len(malenames))].name
    return surnames[randrange(0,len(surnames))].name+', '+first
def random_names(numb: int)->list:
    '''Returns (numb) amount of names in format: LastName, FirstName with skew based on amount of females vs males'''
    temp = []
    for i in range(numb):
        temp.append(get_name())
    return temp
print(random_names(10))

#
#
# Part D
#
#

# D.1
infile = open('wordlist.txt','r')
dictionary = []
for q in infile:
    w = str.split(q)
    dictionary.append(w[0])

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

def test_string(s:str)->int:
    '''Test string according to dictionary'''
    temp = str.split(s)
    counter = 0
    for i in temp:
        if i in dictionary:
            counter+=1
    return counter
def decipher(s:str)->str:
    '''Deciphers code'''
    tempstrings = []
    bestcase = 0
    highest = 0 
    for i in range(26):
        tempstrings.append(Caesar_decrypt(s,i))
        temp = test_string(tempstrings[i].lower())
        if highest < temp:
            bestcase = i
            highest = temp
    return tempstrings[bestcase]
        
print(decipher('Gur oneore jrag qbja gb gur ubbq naq phg unve sbe serr'))


#
#
# Part E
#
#

# E.1
import math
def copy_file(s:str):
    '''
    Copies given file to given new location
    if Gutenburgtrim is passed as s the file is trimmed just to the story
    if line numbers is passed as s line numbers are displayed
    if statistics is passed as s, statistics are written at the end ofthe file
    '''
    infile_name = input("Please enter the name of the file to copy: ")
    infile = open(infile_name, 'r')
    text = []
    characters = 0
    empty = 0
    for line in infile:
        if line == '\n':
            empty+=1
        characters+=len(line)
        text.append(line)
    if s == 'Gutenburg trim':
        start = 0
        end = len(text)-1
        for i in range(len(text)):
            if '*** START' in text[i]:
                start = i
            if '*** END' in text[i]:
                end = i
                break
        text = text[start:end+1]
    outfile_name = input("Please enter the name of the new copy:  ")
    outfile = open(outfile_name, 'w')
    shift = '{0:'+str(int(math.log(len(text),10)+1))+'}: '
    lines = 1
    for i in range(len(text)):
        if s == 'line numbers':
            temp = shift.format(lines)
        else:
            temp = ''
        outfile.write(temp+text[i])
        lines+=1
    if s == 'statistics':
        shift = '{0:'+str(int(math.log(len(text),10)+1))+'} '
        outfile.write("\n\n")
        outfile.write(shift.format(len(text))+'   lines in the file\n')
        outfile.write(shift.format(empty)+'   empty lines\n')
        shift = '{0:'+str(int(math.log(len(text),10)+3))+'.1f} '
        outfile.write(shift.format(characters/len(text))+' average chararcters per line\n')
        outfile.write(shift.format(characters/(len(text)-empty))+" average characters per non-empty line\n")
        
    infile.close()
    outfile.close()
        
