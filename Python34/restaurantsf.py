# Qiaofen Yang 41065325 and Dmitriy Gutnik 77099786. Lab Assignment 6. Section 12
__author__ = 'dgk'

# RESTAURANT COLLECTION PROGRAM
# ICS 31, UCI, David G. Kay, Fall 2012

# Implement Restaurant as a namedtuple, collection as a list

##### MAIN PROGRAM (CONTROLLER)

def restaurants():  # nothing -> interaction
    """ Main program
    """
    print("Welcome to the restaurants program!")
    our_rests = Collection_new()
    our_rests = handle_commands(our_rests)
    print("\nThank you.  Good-bye.")

MENU = """
Restaurant Collection Program --- Choose one
 n:  Add a new restaurant to the collection
 r:  Remove a restaurant from the collection
 s:  Search the collection for selected restaurants
 d:  Search the colelction for cuisine and average price
 p:  Print all the restaurants
 e:  Remove (erase) all the restaurants from the collection
 c:  Change prices for the dishes served
 q:  Quit
"""

add_dish = """
Do you want to add a dish?
"""

def handle_commands(C: list) -> list:
    """ Display menu, accept and process commands.
    """
    while True:
        response = input(MENU)
        if response=="q":
            return C
        elif response=='n':
            r = Restaurant_get_info()
            C = Collection_add(C, r)
        elif response=='r':
            n = input("Please enter the name of the restaurant to remove:  ")
            C = Collection_remove_by_name(C, n)
        elif response=='p':
            print(Collection_str(C))
        elif response=='s':
            n = input("Please enter the name of the restaurant to search for:  ")
            for r in Collection_search_by_name(C, n):
                print(Restaurant_str(r))
        elif response=='d':
            n = input("Please enter the name of the cuisine to search for:  ")
            n2 = float(input("Please enter the average price of the restaurant to search for:  "))
            for r in Collection_search_by_cuisine_average_price(C,n,n2):
                print(Restaurant_str(r))
        elif response=='e':
            C = Collection_remove(C)
        elif response=='c':
            n = float(input("Please enter the number of the price change:  "))
            C = Collection_change_price(C, n)
        else:
            invalid_command(response)

def invalid_command(response):  # string -> interaction
    """ Print message for invalid menu command.
    """
    print("Sorry; '" + response + "' isn't a valid command.  Please try again.")




##### Restaurant
from collections import namedtuple
Restaurant = namedtuple('Restaurant', 'name cuisine phone menu')
# Constructor:   r1 = Restaurant('Taillevent', 'French', '01-11-22-33-44', 'Escargots', 23.50)

def Restaurant_str(self: Restaurant) -> str:
    return (
        "Name:     " + self.name + "\n" +
        "Cuisine:  " + self.cuisine + "\n" +
        "Phone:    " + self.phone + "\n" +
        "Menu:\n" + Collection_str_dish(self.menu) + "\n" +
        "Avrage price: $" +str(Average_price(self.menu))+". Average calories: "+str(Average_calories(self.menu)))
def Average_price(s:list)->float:
    '''Takes list of dishes return their average price'''
    counter = 0.0
    for i in s:
        counter+=i.price
    return counter/len(s)

def Average_calories(s:list) ->float:
    '''Takes a list of dishes and returns average calories'''
    counter = 0.0
    for i in s:
        counter+=i.calories
    return counter/len(s)
def Restaurant_get_info() -> Restaurant:
    """ Prompt user for fields of Restaurant; create and return.
    """
    return Restaurant(
        input("Please enter the restaurant's name:  "),
        input("Please enter the kind of food served:  "),
        input("Please enter the phone number:  "),
        Menu_enter())

#### DISH
Dish = namedtuple("Dish","name price calories")

def Dish_str(self:Dish)->str:
    return(
        "Name:     " + self.name + "\n" +
        "Price:    ${:2.2f}".format(self.price) + "\n"
        "Calories: {:2.2f}".format(self.calories) + "\n\n")

def Dish_get_info() -> Dish:
    return Dish(
        input("Please enter the dish's name:  "),
        float(input("Please enter the price of that dish: ")),
        float(input("Please enter the calories of that dish:  ")))

def Dish_change_prices(d,n):
    d= Dish(d.name, d.price*0.01*n, d.calories)
    return d

def Restaurant_change_price(r,n):
    new_menu = []
    for dish in r.menu:
        new_menu.append(Dish_change_prices(dish,n))

    return r._replace(menu = new_menu)
    
def Collection_change_price(c,n):
    result = []
    for R in c:
        result.append(Restaurant_change_price(R,n))
    return result

#### MENU
def Menu_enter() -> list:
    Menu=[]
    while True:
        response = input(add_dish)
        if response == "yes":
            d = Dish_get_info()
            Menu.append(d)
        elif response == "no":
            print(Collection_str_dish(Menu))
            return Menu
            
#### COLLECTION
# A collection is a list of restaurants

def Collection_new() -> list:
    ''' Return a new, empty collection
    '''
    return [ ]

def Collection_str(C: list) -> str:
    ''' Return a string representing the collection
    '''
    s = ""
    for r in C:
        s = s + Restaurant_str(r)
    return s

def Collection_str_dish(C: list) -> str:
    s = ""
    for d in C:
        s = s + Dish_str(d)
    return s

def Collection_search_by_name(C: list, name: str) -> list:
    """ Return list of Restaurants in input list whose name matches input string.
    """
    result = [ ]
    for r in C:
        if r.name == name:
            result.append(r)
    return result
    # alternative (using a list comprehension):
    # return [r for r in C if r.name == name]
def Collection_search_by_cuisine_average_price(C: list, cui: str, f:float)->list:
    '''Searchestte collection for every restaurant with that cuisineand average price'''
    result = []
    for r in C:
        if r.cuisine == cui and Average_price(r.menu) == f:
            result.append(r)
    return result
def Collection_add(C: list, R: Restaurant) -> list:
    """ Return list of Restaurants with input Restaurant added at end.
    """
    C.append(R)
    return C

def Collection_remove_by_name(C: list, name: str) -> list:
    """ Given name, remove all Restaurants with that name from collection.
    """
    result = [ ]
    for r in C:
        if r.name != name:
            result.append(r)
    return result

def Collection_remove(C: list) -> list:
    result = [ ]
    return result

def Collection_change_prices(C: list, num: float) -> list:
    result = [ ]
    for r in C:
        a_r = r._replace(price = r.price + num)
        result.append(a_r)
    return result

    #    Alternative:
    #    return [r for r in self.rests if r.name != name]

restaurants()
