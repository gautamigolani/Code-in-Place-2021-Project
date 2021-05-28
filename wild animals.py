# Import modules
from tkinter import *
import pygame
from tkinter.tix import *

"""
Root window configuration
"""
# Initialization
root = Tk()
#Set icon for the GUI window
root.iconbitmap("icon.ico")

#Set dimensions of the window such that it opens at the centre of the screen
main_window_width = 320
main_window_height = 430
main_screen_width = root.winfo_screenwidth()
main_screen_height = root.winfo_screenheight()

main_x = (main_screen_width / 2) - (main_window_width / 2)
main_y = (main_screen_height / 2) - (main_window_height / 2)

root.geometry('%dx%d+%d+%d' % (main_window_width, main_window_height, main_x, main_y))

# Disable resizing of the window
root.resizable(width=False, height=False)

# Set title of the window
root.title("Wild Animals")

# Define heading of the program
heading = Label(root, text = "Welcome to the world of Wild Animals!")
heading.pack(pady = 10)
heading.config(font=("Helvetica", 12, 'bold'))

# Insert an image
image = PhotoImage(file="logo.png")
setting = Label(root, image = image)
setting.pack(pady = 10)

# Define tooltip for the image
tip = Balloon(root)
tip.bind_widget(setting, balloonmsg="Made by: Meeka Ella Marasigan Ilagan")

"""
Create a new window when RULES is clicked
"""
def create_window_one():
    window_one = Toplevel(root)
    window_one.title("About")

    second_window_width = 600
    second_window_height = 230
    second_screen_width = window_one.winfo_screenwidth()
    second_screen_height = window_one.winfo_screenheight()

    second_window_x = (second_screen_width / 2) - (second_window_width / 2)
    second_window_y = (second_screen_height / 2) - (second_window_height / 2)

    window_one.geometry('%dx%d+%d+%d' % (second_window_width, second_window_height, second_window_x, second_window_y))
    
    window_one.resizable(width=False, height=False)
    
    # Display text in the form of labels                    
    tb1 = Label(window_one, text = "This program has been created as part of the final project for Stanford's Code in Place 2021 program.")
    tb1.config(font=("Helvetica", 8, 'bold'))
    tb1.pack()
    tb2 = Label(window_one, text = "It has been inspired from Wild Planets which is and audio library ad is available on your Amazon devices. \n This program can be used for educational purposes for kids (Do try it out!).")
    tb2.pack()
    tb3 = Label(window_one, text = "1. Simply click the Start button and enter the world of animals!")
    tb3.pack()
    tb4 = Label(window_one, text = "2. You will see an image of an animal along with its name.")
    tb4.pack()
    tb5 = Label(window_one, text = "3. Below the image will be a button which when clicked will play the sound of that animal.")
    tb5.pack()
    tb6 = Label(window_one, text = "4. You can also read a fun fact about each animal provided.")
    tb6.pack()
    tb7 = Label(window_one, text = "5. Press next to explore other animals available as part of this project.")
    tb7.pack()
    tb8 = Label(window_one, text = "Sit back, relax, play and enjoy!")
    tb8.pack()

    # Create a CLOSE button
    closeb = Button(window_one, text="Close", command=window_one.destroy, width = 5)
    closeb.config(font=("Helvetica", 10, 'bold'))
    closeb.pack(pady = 10)
    
    window_one.mainloop()

# Create an ABOUT button
about = Button(root, text="About", command=create_window_one, width = 5)
about.config(font=("Helvetica", 10, 'bold'))
about.pack(pady = 10) 

"""
Create a new window when START is clicked
"""
def create_window_two():
    global window_two
    global var
    global playb
    window_two = Toplevel(root)
    window_two.iconbitmap("icon.ico")
    window_two.title("Wild Animals")

    third_window_width = 430
    third_window_height = 440
    third_screen_width = window_two.winfo_screenwidth()
    third_screen_height = window_two.winfo_screenheight()

    third_window_x = (third_screen_width / 2) - (third_window_width / 2)
    third_window_y = (third_screen_height / 2) - (third_window_height / 2)

    window_two.geometry('%dx%d+%d+%d' % (third_window_width, third_window_height, third_window_x, third_window_y))
    
    window_two.resizable(width=False, height=False)
    
    # Define heading of an animal                    
    heading_two = Label(window_two, text = "ANIMAL NAME: LION")
    heading_two.pack(pady = 10)
    heading_two.config(font=("Helvetica", 12, 'bold'))
    
    # Insert image of an animal
    image_two = PhotoImage(file="lion.png")
    setting_two = Label(window_two, image = image_two)
    setting_two.pack(pady = 10)
    setting_two.image = image_two
    
    tip_one = Balloon(window_two)
    tip_one.bind_widget(setting_two, balloonmsg="Source: Scientific American Blogs")
    
    # Create a PLAY
    pygame.mixer.init()
    playb = Button(window_two, text = "Play", command=playstop, width = 10)
    playb.config(font=("Helvetica", 12, 'bold'))
    playb.pack(pady = 10)

    # Create a FUN FACT button
    fun_fact = Button(window_two, text="Fun Fact", command = lambda root = window_two: funfact_one(window_two), width = 10)
    fun_fact.config(font=("Helvetica", 10, 'bold'))
    fun_fact.pack(pady = 10)

    # Create a NEXT button
    nextb = Button(window_two, text="Next", command=second, width = 5)
    nextb.config(font=("Helvetica", 10, 'bold'))
    nextb.pack(side = RIGHT, anchor = SE, padx=10, pady = 10)
    
    # Create a QUIT button
    quitb = Button(window_two, text="Quit", command=window_two.destroy, width = 5)
    quitb.config(font=("Helvetica", 10, 'bold'))
    quitb.pack(side = LEFT, anchor = SW, padx=10, pady = 10)
    
    window_two.mainloop()

# Define label for fun fact
def funfact_one(window_two):
    ff = Label(window_two, text = "A lion’s roar can be heard up to eight kilometres away. \n (Source: folly-farm.co.uk)")
    ff.pack()
    
"""
Create a new window when NEXT is clicked
"""
def secondpage():
    global window_three
    global var
    global playb
    window_three = Toplevel(root)
    window_three.iconbitmap("icon.ico")
    window_three.title("Wild Animals")

    fourth_window_width = 430
    fourth_window_height = 440
    fourth_screen_width = window_three.winfo_screenwidth()
    fourth_screen_height = window_three.winfo_screenheight()

    fourth_window_x = (fourth_screen_width / 2) - (fourth_window_width / 2)
    fourth_window_y = (fourth_screen_height / 2) - (fourth_window_height / 2)

    window_three.geometry('%dx%d+%d+%d' % (fourth_window_width, fourth_window_height, fourth_window_x, fourth_window_y))
    
    window_three.resizable(width=False, height=False)
    
    heading_two = Label(window_three, text = "ANIMAL NAME: GORILLA")
    heading_two.pack(pady = 10)
    heading_two.config(font=("Helvetica", 12, 'bold'))

    image_two = PhotoImage(file="gorilla.png")
    setting_two = Label(window_three, image = image_two)
    setting_two.pack(pady = 10)
    setting_two.image = image_two

    tip_one = Balloon(window_three)
    tip_one.bind_widget(setting_two, balloonmsg="Source: Wikipedia")
    
    pygame.mixer.init()
    playb = Button(window_three, text = "Play", command=playstop_two, width = 10)
    playb.config(font=("Helvetica", 12, 'bold'))
    playb.pack(pady = 10)

    funf = Button(window_three, text="Fun Fact", command = lambda root = window_three: funfact_two(window_three), width = 10)
    funf.config(font=("Helvetica", 10, 'bold'))
    funf.pack(pady = 10)

    quitb = Button(window_three, text="Quit", command=window_three.destroy, width = 5)
    quitb.config(font=("Helvetica", 10, 'bold'))
    quitb.pack(side = RIGHT, anchor = SE, padx=10, pady = 10)

    prevb = Button(window_three, text="Previous", command=previouspage, width = 8)
    prevb.config(font=("Helvetica", 10, 'bold'))
    prevb.pack(side = LEFT, anchor = SW, padx=10, pady = 10)

    window_three.mainloop()

def funfact_two(window_three):
    ff = Label(window_three, text = "Gorillas are our second closest \n relatives, sharing about 98% of our DNA. \n (Source: bbc.com)")
    ff.pack()
    
# Define function to close second window when NEXT is clicked to launch the third window
def second():
    window_two.destroy()
    secondpage()
    
# Define function to close third window when PREVIOUS is clicked to launch the second window
def previouspage():
    window_three.destroy()
    create_window_two()
    
# Add PLAY and RESUME in one button
pause = False
counter = 0
def playstop():
    global index, counter
    global pause
    counter += 1
    if pause == False:
        pygame.mixer.music.load("Lion.mp3")
        pygame.mixer.music.play()
        playb.config(text="Play")
        pause = True
    else:
        pygame.mixer.music.stop()
        playb.config(text="Resume")
        pause = False

def playstop_two():
    global index, counter
    global pause
    counter += 1
    if pause == False:
        pygame.mixer.music.load("Gorilla.mp3")
        pygame.mixer.music.play()
        playb.config(text="Play")
        pause = True
    else:
        pygame.mixer.music.stop()
        playb.config(text="Resume")
        pause = False
    
# Create a START button
startb = Button(root, text="START", command=create_window_two, width = 10)
startb.config(font=("Helvetica", 14, 'bold'))
startb.pack(pady = 10)

# Create an EXIT button
exit_bmain = Button(root, text="Exit", command=root.destroy, width = 5)
exit_bmain.config(font=("Helvetica", 10, 'bold'))
exit_bmain.pack(side = LEFT, anchor = SW, padx=10, pady = 10)

root.mainloop()
