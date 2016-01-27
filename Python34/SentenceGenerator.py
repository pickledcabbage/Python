from collections import namedtuple
from random import randrange
Word = namedtuple('Word', 'word after')
inputfile = open('Dracula.txt','r') #Which file to write in
words = []
worddict = {}
PUNCTUATION2 = [".",";",":","!","?","/","\\",",","#","@","$","&",")","(","\"","\n","_","'"]
for line in inputfile:
    for punct in PUNCTUATION2:
            line = line.replace(punct,"")
    line = line.lower()
    broken = str.split(line)
    for x in broken:
        if (x in worddict) == False:
            worddict[x] = []
        words.append(x)
for i in range(1,len(words)):
    worddict[words[i-1]].append(words[i])

def generate_sentence(s:str,num:int)->str:
    start = s
    counter = s
    for amount in range(0,num):
        dist = len(worddict[counter])
        counter = worddict[counter][randrange(0,dist)]
        start += " " + counter
    return start

print(generate_sentence('pure',50))
