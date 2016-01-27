import tkinter              # Load the library; do this just once per program

my_window = tkinter.Tk()    # Create the graphics window

my_canvas = tkinter.Canvas(my_window, width=500, height=500)  # Create a 500x500 canvas to draw on
my_canvas.pack()            # Put the canvas into the window

def create_square(x: int, y: int, s: int):
    my_canvas.create_rectangle(x,y,x+s,y+s,fill='blue')
create_square(100,100,100)

tkinter.mainloop()          # Combine all the elements and display the window
