#Heran Patel (62984531) and Dmitriy Gutnik (77099786). ICS 31 Lab sec 12. Lab asst 3.

#
#
# Part (c)
#
#

print()
print()
print('---------- Part (c) ----------')
print()

#PART C1

def abbreviate(s: str) -> str:
    '''Returns first three characters of the string'''
    return s[0:3]
assert abbreviate('January') == 'Jan'
assert abbreviate('abril') == 'abr'


#PART C2

def find_area_square(n: int) -> int:
    '''returns area'''
    return n**2
assert find_area_square(1) == 1
assert find_area_square(5) == 25


#PART C3

def find_area_circle(n: int) -> float:
    '''returns area'''
    return (3.14159 * (n**2))
assert find_area_circle(1) == 3.14159
assert find_area_circle(5) == 78.53975


#PART C4

def print_even_numbers(L: list):
    '''print even numbers in list'''
    for x in range(0,len(L)):
        if L[x]%2 == 0:
            print(L[x])
print_even_numbers([2, 47, 31, 99, 20, 19, 23, 105, 710, 1004])


#PART C5

def calculate_shipping(w: float) -> float:
    if w <= 2:
        return 2.0
    if (2 < w and w <= 10):
        return 5.0
    else:
        return 5 + 1.5 * (w-10)
assert calculate_shipping(1.5) == 2.00
assert calculate_shipping(7) == 5.00
assert calculate_shipping(15) == 12.50

#PART C6

import tkinter
my_window1 = tkinter.Tk()  

my_canvas = tkinter.Canvas(my_window1, width=500, height=500) 
my_canvas.pack()

def create_square(x: int, y: int, s: int):
    my_canvas.create_rectangle(x,y,x + s, y+s)
create_square(100,200,50)

#PART C7

my_window2 = tkinter.Tk()  

my_canvas2 = tkinter.Canvas(my_window2, width=500, height=500) 
my_canvas2.pack()
def create_circle(x: int,y: int,d: int):
    my_canvas2.create_oval(x,y,x + d,y + d)
create_circle(5,5,10)

#PART D
print()
print()
print('---------- Part (d) ----------')
print()

#PART D.1
from collections import namedtuple
Restaurant = namedtuple('Restaurant', 'name cuisine phone dish price')
# Restaurant attributes: name, kind of food served, phone number, best dish, price of that dish
RC = [
    Restaurant("Thai Dishes", "Thai", "334-4433", "Mee Krob", 12.50),
    Restaurant("Nobu", "Japanese", "335-4433", "Natto Temaki", 5.50),
    Restaurant("Nonna", "Italian", "355-4433", "Stracotto", 25.50),
    Restaurant("Jitlada", "Thai", "324-4433", "Paht Woon Sen", 15.50),
    Restaurant("Nola", "New Orleans", "336-4433", "Jambalaya", 5.50),
    Restaurant("Noma", "Modern Danish", "337-4433", "Birch Sap", 35.50),
    Restaurant("Addis Ababa", "Ethiopian", "337-4453", "Yesiga Tibs", 10.50) ]

def restaurant_price(s: Restaurant) -> float:
    return s.price
print('The price field of restuarant is:',restaurant_price(RC[1]),'\n')
print("="*20, '\n')

#PART D.2

RC.sort(key = restaurant_price)
print('The following list is sorted by price: \n\n',RC,'\n')
print("="*20, '\n')

#PART D.3 - D.4
RC1 =[ Restaurant("Nola", "New Orleans", "336-4433", "Jambalaya", 5.50),
    Restaurant("Noma", "Modern Danish", "337-4433", "Birch Sap", 35.50),
    Restaurant("Addis Ababa", "Ethiopian", "337-4453", "Yesiga Tibs", 10.50)]

print('This is the RC1 unsorted list: \n\n',RC1,'\n')
def costliest(L: list) ->str:
    L.sort(key = restaurant_price)
    return L[-1].name
print('This is the costliest restaurant for the list above is: ',costliest(RC1))
print('The following is the RC1 sorted list: \n\n',RC1,'\n\n')
print("="*20, '\n')

#PART D.4
RC2 = [
    Restaurant("Thai Dishes", "Thai", "334-4433", "Mee Krob", 12.50),
    Restaurant("Nobu", "Japanese", "335-4433", "Natto Temaki", 5.50),
    Restaurant("Nonna", "Italian", "355-4433", "Stracotto", 2.50)]
def costliest2(L: list) ->str:
    return sorted(L,key = restaurant_price)[-1].name
print('The costliest restaurant in list RC2 is:',costliest2(RC2))
print('The RC2 list should not be sorted below: \n\n',RC2,'\n\n')
print("="*20, '\n')
    
#PART E
print()
print()
print('---------- Part (e) ----------')
print()

Book = namedtuple('Book', 'title author genre year price instock')
BSI =[
    Book('Frankenstein','Mary Shelley','Technology',1818,5,50),
    Book('Adventures of Phillip','Mark White','Fantasy',1989,10,100),
    Book('American Pop Culture','David Clarke','Technology',2001,20,37),
    Book('Horrors of Stockholm','Arthur Dent','Gothic',1990,14,40),
    Book('Sherlock Holmes Returns','Arthur Conan Doyle','Thriller',1910,12,40),
    Book('Do androids dream of electric sheep?','Phillip K. Dick','Science Fiction',1954,10,45)
]

#PART E.1

for x in BSI:
    print(x.title)
print('\n\n')

#PART E.2

def title(B: Book) -> str:
    return B.title
for y in sorted(BSI,key=title):
    print(y.title)
print('\n\n')

#PART E.3

for z in range(0,len(BSI)):
    BSI[z] = Book(BSI[z].title,BSI[z].author,BSI[z].genre,BSI[z].year,BSI[z].price*1.1,BSI[z].instock)
print('BSI with each price increased by 10%',BSI,'\n\n')

    
#PART E.4

for i in BSI:
    if i.genre == 'Technology':
        print(i.title)

#PART E.5

pre = []
post = []
for j in BSI:
    if j.year < 2000:
        pre.append(j)
    else:
        post.append(j)
        
if len(pre)>len(post):
    print('More titles before 2000','(',len(pre),'vs.',len(post),')')
elif len(post)>len(pre):
    print('More titles 2000 or later','(',len(post),'vs.',len(pre),')')

#PART E.6

def inventory_value(b: Book) -> int:
    return b.price*b.instock
def top_value(l: list) -> Book:
    number = 0;
    for i in range(1,len(l)):
        if inventory_value(l[i])>inventory_value(l[number]):
            number = i
    return l[number]
print('The highest value book is ',top_value(BSI).title,'by',top_value(BSI).author,'at a value of $',inventory_value(top_value(BSI)))

#PART F
print()
print()
print('---------- Part (f) ----------')
print()

my_window = tkinter.Tk()

my_canvas = tkinter.Canvas(my_window, width=500, height=500) 
my_canvas.pack() 
def draw_eye(x: int,y: int):
    my_canvas.create_oval(x+20,y+10,x+40,y+30)
    my_canvas.create_oval(x+10,y,x+50,y+40)
    my_canvas.create_oval(x,y,x+60,y+40)

def draw_nose(x: int,y: int):
    my_canvas.create_line(x+40,y,x,y+40)
    my_canvas.create_line(x,y+40,x+40,y+40)

def draw_mouth(x: int,y: int):
    my_canvas.create_line(x,y,x+60,y)

def draw_face(x: int, y:int):
    draw_eye(x+20,y+30)
    draw_eye(x+120,y+30)
    draw_nose(x+60,y+70)
    draw_mouth(x+70,y+140)
    my_canvas.create_oval(x,y,x+200,y+160)
draw_face(10,10)
draw_face(250,250)
