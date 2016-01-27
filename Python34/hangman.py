#Trying to make an unbeatable version of hangman

def main():
    number_of_letters = int(input('Enter the number of letters: '))
    words = get_words(number_of_letters)
    
    
    
    word = []
    for i in range(0,number_of_letters):
        word.append('_')
    done = False
    tries = 6
    chosen = ''
    used_letters = []
    test_mode = input("Enter 'yes' if you want to run in test mode: ")=='yes'
    
    while done == False:
        if test_mode:
            print_words(words)
        print()
        print('Number of tries left: '+str(tries))
        temp = ''
        for let in word:
            temp+=let
        print('Your word: '+temp)
        print('')
        chosen = input('Enter your guess letter: ')
        used_letters.append(chosen)
        best_case = assimilate(chosen,words,number_of_letters)
        words = filter_out_words(best_case,words,chosen)
        print(best_case)
        if check_not_included(best_case):
            tries-=1
        else:
            word = change_word(word,chosen,best_case)
        
        

def get_words(length:int)->list:
    infile = open('wordlist.txt','r')
    temp = []
    for line in infile:
        w = str.split(line)
        if ("'" in w[0]) == False and len(w[0])==length:
            temp.append(w[0])
    return temp

def change_word(word:list,let:str,bits:list)->list:
    temp = word
    for i in range(0,len(temp)):
        if (bits[i] == 1):
            temp[i] = let
    return temp

def assimilate(let:str,words:list,length:int)->list:
    best_case = 0
    best_arrangement = []
    #strength = []
    #locations = []
    for i in range(0,2**length):
        temp = []
        num = i
        #print(num)
        for a in range(0,length):
            temp.append(num%2)
            num = int(num/2)
        stg = get_strength(temp,words,let)
        if stg >=best_case:
            best_case = stg
            best_arrangement = temp
        #locations.append(temp)
        #strength.append(get_strength(temp,words,let))
    return best_arrangement

def check_not_included(bits:list)->bool:
    return (1 in bits)==False

def get_strength(bits:list,words:list,let:str)->int:
    temp = 0
    for i in words:
        k = True
        for a in range(0,len(bits)):
            if ((bits[a]==1) == (i[a]==let))==False:
                k = False
                break
        if k:
            temp+=1
    return temp

def filter_out_words(bits:list,words:list,let:str)->list:
    temp = []
    for i in words:
        k = True
        for a in range(0,len(bits)):
            if ((bits[a]==1) == (i[a]==let))==False:
                k = False
                break
        if k:
            temp.append(i)
    return temp

def print_words(words:list):
    count = 1
    for i in range(0,len(words),7):
        temp = ''
        for a in words[i:i+7]:
            temp += a + ' '
        print(temp)
        
main()
