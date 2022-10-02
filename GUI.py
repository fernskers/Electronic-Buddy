from tkinter import *
from PIL import ImageTk,Image
import pyglet,tkinter
from playsound import playsound
import sys
import os

""" def startup_animation():
    while True:
        try:
            global photo
            global frame
            global label
            photo = PhotoImage(
                file = photo_path,
                format = "gif = {}".format(frame)
                )
            label.configure(image = nextframe)
            
            frame = frame + 1
            
        except Exception:
            frame = 1
            break """


# if os.environ.get('DISPLAY','') == '':
#     print('no display found. Using :0.0')
#     os.environ.__setitem__('DISPLAY', ':0.0')

#Creating the skeleton
gui = Tk()
gui.title('Electronic Buddy')
#gui.overrideredirect(True)
bgfile = PhotoImage(file = "backup.png")

#uploading 3d party fonts
pyglet.font.add_file('Playtime.otf')

#play music or whatever

def openDrawing():
    button_click_sound()
    C.destroy()
    drawing_screen()
    
def drawing_to_main():
    button_click_sound()
    D.destroy()
    mainscreen()

def button_click_sound():
    playsound('button.wav')

def paint( event ):
   python_green = "#476042"
   x1, y1 = ( event.x - 1 ), ( event.y - 1 )
   x2, y2 = ( event.x + 1 ), ( event.y + 1 )
   D.create_oval( x1, y1, x2, y2, fill = python_green )

def mainscreen():
    playsound('mus.wav', block=False)
    global C 
    C = Canvas(gui, bg="white", height = 600, width = 1024)
    C.create_image(0, 0, image = bgfile, anchor=NW)

    C.create_text(500, 50, text="Hi, I'm Electronic Buddy!", fill = "black", font=('Playtime', 40))
    C.create_text(500, 100, text="Try Pressing on any of my buttons below!", fill = "black", font=('Playtime', 28))

    #Exit button
    exit_button = Button(C, text = "EXIT", fg = 'black', bg='white', bd='5',
                        relief = "ridge", font=('Playtime', 18), command = gui.destroy)
    exit_button.place(x=920, y=10)

    #Main screen buttons
    hide_and_seek = Button(C, text = " Hide and Seek!  ", bd='5', fg = 'black',
                        bg='white', relief = "ridge", font=('Playtime', 25), command = button_click_sound)
    hide_and_seek.place(x = 375, y=175)

    matching = Button(C, text = "       Matching!     ", bd='5', fg = 'black',
                        bg = 'white', relief = "ridge", font=('Playtime', 25), command = button_click_sound)
    matching.place(x = 375, y=275)

    drawing = Button(C, text = "           Draw!         ", bd='5', fg = 'black',
                        bg = 'white', relief = "ridge",font=('Playtime', 25), command = openDrawing)
    drawing.place(x = 375, y=375)

    crosswords = Button(C, text = "   Watch Videos!  ", bd='5', fg = 'black',
                        bg = 'white', relief = "ridge", font=('Playtime', 25), command = button_click_sound)
    crosswords.place(x = 375, y=475)

    C.pack()

def drawing_screen():
    global D
    D = Canvas(gui, bg="white", height = 600, width = 1024)
    D.create_text(500, 50, text="Touch to Draw!", fill = "black", font=('Playtime', 40))

    back_drawing_button = Button(D, text = "BACK", fg = 'black', bg='white', bd='10',
                        relief = "ridge", font=('Playtime', 18), command = drawing_to_main)
    back_drawing_button.place(x=10, y=10)
    D.bind( "<B1-Motion>", paint )
    D.pack()



mainscreen()

#Settings Button
# settings_btn = Button(C, text = "Settings", bd='10', fg = 'white', bg='#808080', font=('Playtime', 12))
# settings_btn.place(x = 10, y=550)



#Interactivity 
#gui.iconbitmap('pathoficon')


#main = Label(image = PhotoImage(file = r"C:\Users\Fernando Leon\Code\images\robo.gif"))
#main.pack()

# my_img = ImageTk.PhotoImage(Image.open("back.jpg"))
# my_label = Label(image=my_img)
# my_label.pack()

# play_button = Button(gui, text="Play Song", font=("Helvetica", 24), command=play)
# play_button.pack(pady=20)

# button_quit = Button(gui, text = "Exit", command=gui.quit)
# button_quit.pack()
gui.mainloop()
