# Dmitriy Gutnik 77099786 and Jeremy Bibeau 94276852. ICS Lab sec 12. Assignment# 4

#
#
# PART C
#
#
print("-----------PART C-----------")
print("\n")

# C.1
def test_number(i: int,s: str)-> bool:
    """Checks given number according to the given condition"""
    if s == 'even':
        return i%2==0
    elif s == 'odd':
        return i%2==1
    elif s == 'positive':
        return i>=0
    elif s == 'negative':
        return i<0
print(test_number(12,'even'))
assert test_number(14, 'even')
assert not test_number(100, 'odd')
assert test_number(33, 'positive')
assert not test_number(100, 'negative')

# C.2
print()
def display():
    """Prints every character in the wordd in a seperate line"""
    s = input('Enter a word:')
    for i in s:
        print(i)
display()

# C.3
print()
def square_list(l: list):
    '''Takes in a list of numbers and squares them'''
    for i in l:
        print(i**2)
square_list([2,3,4,10])

# C.4
print()
def match_first_letter(c: str, l: list):
    '''Prints every string in the list that starts with the given character'''
    for i in l:
        if c == i[0]:
            print(i)
match_first_letter('I', ['Iron Man', 'Iron Man 2', 'The Avengers', 'Superman', 'I am Legend'])

# C.5
print()
def match_area_code(ac: list, numbers: list):
    '''Prints every phone number with given area code'''
    for i in numbers:
        for c in ac:
            if i[1:4]==c:
                print(i)
match_area_code(['949','714'],['(714)824-1234', '(419)312-8732', '(949)555-1234'])

# C.6
print()
def matching_area_codes(ac: list, numbers: list) -> list:
    '''Returns list of phone numbers that begin with any area codes in the list of area codes'''
    match = []
    for i in numbers:
        for c in ac:
            if i[1:4]==c:
                match.append(i)
    return match
print(matching_area_codes(['949','714'],['(714)824-1234', '(419)312-8732', '(949)555-1234']))

#
#
# PART D
#
#
print("-----------PART D-----------")
print("\n")

# D.1
print()
def is_vowel(s: str)-> bool:
    '''Returns true if character is a vowel'''
    return s in 'aoeuiAOUIE'
print(is_vowel('a'))

# D.2
print()
def print_nonvowels(s: str):
    '''Prints only the non-vowels of the string'''
    for i in s:
        if (is_vowel(i))==False:
            print(i)
print_nonvowels('Anteater')

# D.3
print()
def nonvowels(s: str) -> str:
    '''Returns original string without vowels'''
    nv = ""
    for i in s:
        if (is_vowel(i))==False:
            nv = nv +i
    return nv
print(nonvowels('Anteareresdsds'))

'''
assert double(0) == 0
assert double(17.5) == 35
assert double(-223344) == -446688'''
assert is_vowel('a') 
assert is_vowel('U')
assert not is_vowel('X')
assert not is_vowel('?')

# D.4
print()
def consonants(s: str) -> str:
    '''Returns string with only consonants'''
    c = ""
    for i in s:
        if i in 'qwrtypsdfghjklzxcvbnmQWRTYPSDFGHJKLZXCVBNM':
            c = c+i
    return c
print(consonants('The_Anteater!'))

# D.5
print()

def select_letters(par: str, word: str)-> str:
    '''Returns the given word with only consonants or vowels'''
    ret = ""
    if par == 'v':
        for i in word:
            if is_vowel(i):
                ret = ret + i
    elif par == 'c':
        ret = consonants(word)
    return ret
print(select_letters('c', 'facetiously'))
print(select_letters('v', 'facetiously'))

# D.6
print()

def hide_vowels(word: str) -> str:
    '''Replaces vowels in original string with -'''
    ret = ""
    for i in word:
        if is_vowel(i):
            ret = ret + '-'
        else:
            ret = ret + i
    return ret
print(hide_vowels('ChairTable'))

#
#
# PART E
#
#
print("-----------PART E-----------")
print("\n")

# E
from collections import namedtuple
# Restaurant attributes: name, kind of food served, phone number,
#	best dish, price of that dish
Restaurant = namedtuple('Restaurant','name cuisine phone dish price')

R1 = Restaurant("Taillevent", "French", "343-3434", "Escargots", 24.50)
R2 = Restaurant("La Tour D'Argent", "French", "343-3344", "Ris de Veau", 48.50)
R3 = Restaurant("Pascal", "French", "333-4444", "Bouillabaisse", 32.00)
R4 = Restaurant("Thai Touch", "Thai", "444-3333", "Mee Krob", 10.95)
R5 = Restaurant("Thai Dishes", "Thai", "333-4433", "Paht Woon Sen",  8.50)
R6 = Restaurant("Thai Spoon", "Thai", "334-3344", "Mussamun", 9.00)
R7 = Restaurant("McDonald's", "Burgers", "333-4443", "Big Mac", 3.95)
R8 = Restaurant("Burger King", "Burgers", "444-3344", "Whopper", 3.75)
R9 = Restaurant("Wahoo's", "Fish Tacos", "443-4443", "Mahi Mahi Burrito", 7.50)
R10 = Restaurant("In-N-Out Burger", "Burgers", "434-3344", "Cheeseburger", 2.50)
R11 = Restaurant("The Shack", "Burgers", "333-3334", "Hot Link Burger", 4.50)
R12 = Restaurant("Gina's", "Pizza", "334-4433", "Combo Pizza", 12.95)
R13 = Restaurant("Peacock, Room", "Indian", "333-4443", "Rogan Josh", 12.50)
R14 = Restaurant("Gaylord", "Indian", "333-3433", "Tandoori Chicken", 13.50)
R15 = Restaurant("Mr. Chow", "Chinese", "222-3333", "Peking Duck", 24.50)
R16 = Restaurant("Chez Panisse", "California", "222-3322", "Grilled Duck Breast", 25.00)
R17 = Restaurant("Spago", "California", "333-2222", "Striped Bass", 24.50)
R18 = Restaurant("Sriped Bass", "Seafood", "333-2233", "Cedar Plank Salmon", 21.50)
R19 = Restaurant("Golden Pagoda", "Chinese", "232-3232", "Egg Foo Young", 8.50)
R20 = Restaurant("Langer's", "Delicatessen", "333-2223", "Pastrami Sandwich", 11.50)
R21 = Restaurant("Nobu", "Japanese", "335-4433", "Natto Temaki", 5.50)
R22 = Restaurant("Nonna", "Italian", "355-4433", "Stracotto", 25.50)
R23 = Restaurant("Jitlada", "Thai", "324-4433", "Paht Woon Sen", 15.50)
R24 = Restaurant("Nola", "New Orleans", "336-4433", "Jambalaya", 5.50)
R25 = Restaurant("Noma", "Modern Danish", "337-4433", "Birch Sap", 35.50)
R26 = Restaurant("Addis Ababa", "Ethiopian", "337-4453", "Yesiga Tibs", 10.50) 


RL = [R1, R2, R3, R4, R5, R6, R7, R8, R9, R10, R11, R12, R13, R14, R15, R16,
	R17, R18, R19, R20, R21, R22, R23, R24, R25, R26]


def Restaurant_change_price(r: Restaurant, num: int)-> Restaurant:
    '''Returns the given Restaurant with the new price'''
    return Restaurant(r.name,r.cuisine,r.phone,r.dish,num)
print(Restaurant_change_price(R1,50))

#
#
# PART F
#
#
print("-----------PART F-----------")
print("\n")

# F.1
print()
def alphabetical(l: list) ->list:
    '''Returns list of sorted Restaurats by name'''
    Q = sorted(l)
    return Q
print(alphabetical(RL))

# F.2
print()
def alphabetical_names(l: list)-> list:
    '''Returns list of Restaurant names sorted alphabetically'''
    names = []
    q = alphabetical(l)
    for i in q:
        names.append(i.name)
    return names
print(alphabetical_names(RL))

# F.3
print()
def all_Thai(l: list) -> list:
    '''Returns list of all thai restaurants'''
    Thai = []
    for i in l:
        if i.cuisine == 'Thai':
            Thai.append(i)
    return Thai
print(all_Thai(RL))

# F.4
print()
def select_cuisine(s: str, l: list) -> list:
    '''Returns list of Retaurants of the specified cuisine'''
    a = []
    for i in l:
        if i.cuisine == s:
            a.append(i)
    return a
print(select_cuisine('French',RL))

# F.5
print()
def select_cheaper(l: list, f: float) -> list:
    '''Returns list of Restaurants cheaper than the given price'''
    p = []
    for i in l:
        if i.price < f:
            p.append(i)
    return p
print(select_cheaper(RL, 10))

# F.6
print()
def average_price(l: list) -> float:
    '''Returns average price of restaurants in given list'''
    ave = 0.0
    for i in l:
        ave +=  i.price
    return ave/len(l)
print(average_price(RL))

# F.7
print()
print(average_price(select_cuisine('Indian', RL)))

# F.8
print()
temp = select_cuisine('Thai',RL)
temp1 = select_cuisine('Chinese',RL)
temp.extend(temp1)
print(average_price(temp))

# F.9
print()
y = []
cheap = select_cheaper(RL,15)
for i in cheap:
    y.append(i.name)
print(y)

#
#
# PART G
#
#
print("-----------PART G-----------")
print("\n")

# G
import tkinter              # Load the library; do this just once per program

my_window = tkinter.Tk()    # Create the graphics window

my_canvas = tkinter.Canvas(my_window, width=500, height=500)  # Create a 500x500 canvas to draw on
my_canvas.pack()            # Put the canvas into the window

def create_rectangle_from_center(x: int, y: int, h: int, w: int):
    '''Creates a rectangle using center coordinates and height and width'''
    my_canvas.create_rectangle(x-w/2,y-h/2,x+w/2,y+h/2)
create_rectangle_from_center(100,150,50,100)

tkinter.mainloop()          # Combine all the elements and display the window
