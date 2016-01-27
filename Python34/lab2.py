# Emily Meneses 92621153 Dmitriy Gutnik 77099786. ICS 31 lab sec 12. Lab Asst 2.
#c
hours = int(input('How many hours?'))
print('This many hours:', hours)
rate = float(input('How many dollars per hour? $'))
print('This many dollars per hour:  $', rate)
print('Weekly salary:  $', hours * rate)
#c.2
name = input('Hello. What is your name?')
print('Hello', name)
print("It's nice to meet you.")
age = int(input('How old are you?'))
print('Next year you will be', (age + 1), 'years old.')
print('Good-bye!')
#d
print("Please provide this information:")
name = input("Business name: ")
euros = int(input("Number of euros: "))
pounds = int(input("Number of pounds: "))
dollars = int(input("Number of dollars: "))

print("\nCopenhagen Chamber of Commerece")
print("Business name: ", name)
krone1 = euros*7.46
krone2 = pounds*10.33
krone3 = dollars*6.66
total = krone1 + krone2 + krone3
print(euros," euros is ",krone1,"krone")
print(pounds," pounds is ",krone2,"krone")
print(dollars," dollars is ",krone3,"krone")
print("\nTotal krone:  ",total)
#e and g
from collections import namedtuple
Book = namedtuple('Book', 'title author year price')
favorite = Book('Adventures of Sherlock Holmes',
                'Arthur Conan Doyle', 1892, 21.50)
another = Book('Memoirs of Sherlock Holmes', 
               'Arthur Conan Doyle', 1894, 23.50)
still_another = Book('Return of Sherlock Holmes',
                     'Arthur Conan Doyle', 1905, 25.00)
booklist = [favorite, another, still_another]
print(booklist[0][3] < booklist[1][3])
print(booklist[0][2] > booklist[-1][2])

print(still_another[0])
print(another[3])
print((favorite[3]+another[3]+still_another[3])/3)
print(favorite[2] < 1900)
still_another = Book(still_another[0],
                     still_another[1], still_another[2], 26.00)
print(still_another[3])
still_another = Book(still_another[0],
                     still_another[1], still_another[2], still_another[3]*1.2)
print(still_another[3])
#f
#from collections import namedtuple
Animal = namedtuple('Animal', 'name species age weight food')
elephant = Animal('Jumbo', 'elephant', 50, 1000, 'peanuts')
print(elephant)

platypus = Animal('Perry', 'platypus', 7, 1.7, 'shrimp')
print(platypus)
print(elephant[2] < platypus[2])
#h
#from collections import namedtuple     # If this line is in your file already, you don't need it again
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
print(RC[2][0])
print(RC[0][1]==RC[3][1])
print(RC[-1][4])
RC.sort()
print(RC)
print(RC[-1][4])
NewList = [RC[0],RC[1],RC[-2],RC[-1]]
print(NewList)
#i
import tkinter              # Load the library; do this just once per program

my_window = tkinter.Tk()    # Create the graphics window

my_canvas = tkinter.Canvas(my_window, width=500, height=500)  # Create a 500x500 canvas to draw on
my_canvas.pack()            # Put the canvas into the window

my_canvas.create_line(100, 100, 300, 300, fill='orange') # Draw orange line
my_canvas.create_line(300, 100, 100, 300, fill='blue')   # Draw blue line

my_canvas.create_line(100,200,200,100,fill='blue')
my_canvas.create_line(200,100,300,200,fill='blue')
my_canvas.create_line(300,200,200,300,fill='blue')
my_canvas.create_line(200,300,100,200,fill='blue')



my_canvas.create_line(100,100,300,100,fill='red')
my_canvas.create_line(300,100,300,300,fill='red')
my_canvas.create_line(300,300,100,300,fill='red')
my_canvas.create_line(100,300,100,100,fill='red')
my_canvas.create_line(50,100,200,50,fill='brown')
my_canvas.create_line(200,50,350,100,fill='brown')
my_canvas.create_line(350,100,50,100,fill='brown')

my_canvas.create_line(200,300,200,200,fill='brown')
my_canvas.create_line(200,200,275,200,fill='brown')
my_canvas.create_line(275,200,275,300,fill='brown')

my_canvas.create_line(125,150,175,150,fill='blue')
my_canvas.create_line(175,150,175,250,fill='blue')
my_canvas.create_line(175,250,125,250,fill='blue')
my_canvas.create_line(125,250,125,150,fill='blue')
my_canvas.create_line(150,150,150,250,fill='blue')
my_canvas.create_line(125,200,175,200,fill='blue')

my_canvas.create_oval(100,100,300,200,fill='white')
my_canvas.create_oval(150,100,250,200,fill='green')
my_canvas.create_oval(175,125,225,175,fill='black')

tkinter.mainloop()          # Combine all the elements and display the window
