from tkinter import *
from PIL import ImageTk,Image
import pyglet,tkinter
from playsound import playsound
import sys
import os
import random
import vlc

#Creating the skeleton
gui = Tk()
gui.title('Electronic Buddy')
gui.overrideredirect(True)
bgfile = PhotoImage(file = "bg.png")
drawbgfile = PhotoImage(file = "drawbg.png")

#uploading 3d party fonts
pyglet.font.add_file('Playtime.otf')

#matching game variables
tile_state = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] #tile state variable, 0 = tile is not flipped, 1 = tile is flipped
pick_num = 1 #keeps track of if the current tile is the first or second to be flipped. 1 = first, 2 = second
prev_tile = 16 #keeps track of the previously selected tile
tiles = [1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8] #variable to determine image and match of a tile. index refers to button number, number indicates the image on the tile

#tic tac toe variables
player_turn = 0 #keeps track of which players turn it is, 0 = player 1, 1 = player 2, 2 = game is over
board_status = [0,0,0,0,0,0,0,0,0]#tl=0,tm=1,tr=2,ml=3,mm=4,mr=5,bl=6,bm=7,br=8, position is 0 when empty 1 when p1 and 2 when p2
player1_token = PhotoImage(file = "x.png") #player 1's token
player2_token = PhotoImage(file = "o.png") #player 2's token
blank_space = PhotoImage(file = "board_space.png") #image for before a token has been placed

#simon says variables
score = 0 #number of correct responses the user gave
round_num = 0 #the number of rounds that have been played
current_prompt = 0 #what is the user currently being prompted to do, 0 == press red, 1 == press green, 2 == press blue

#create class for matching game tile
class tile(tkinter.Button):
    def __init__(self, master=None, image1=None, image2=None, tile_num=None, **kwargs):
        self.command = kwargs.pop('command', None)
        super().__init__(master, **kwargs)
        self.image1 = tkinter.PhotoImage(file=image1)
        self.image2 = tkinter.PhotoImage(file=image2)
        self.config(image=self.image1, command=self.on_click)
        self.tile_num = tile_num

    def on_click(self):
        global tile_state
        global pick_num
        global prev_tile
        global tiles
        if tile_state[self.tile_num] == 0: #check that the tile is not currently flipped
            self.config(image=self.image2) #change the image
            tile_state[self.tile_num] = 1 #set the tile state to flipped
            if pick_num == 1: #if tile is the first to be flipped
                pick_num = 2 #set variable so next tile flipped is the second one
                prev_tile = self.tile_num #set the previous tile to the number of the tile flipped
            else:
                pick_num = 1 #reset pick_num so next pick will be the first
                if tiles[self.tile_num] == tiles[prev_tile]:#check if tiles match
                    game_over_check()#if tiles match, check for game over
                else:#if tiles do not match, unflip tile and previous tile
                    tile_state[self.tile_num] = 0
                    tile_state[prev_tile] = 0
                    self.after(400, self.after_click)#schedule unflip of tiles after 1 second
        
    def after_click(self):
        self.config(image=self.image1)#flip the current tile
        if prev_tile == 0:#find and flip the previous tile
            b0.config(image = b0.image1)
        elif prev_tile == 1:
            b1.config(image = b1.image1)
        elif prev_tile == 2:
            b2.config(image = b2.image1)
        elif prev_tile == 3:
            b3.config(image = b3.image1)
        elif prev_tile == 4:
            b4.config(image = b4.image1)
        elif prev_tile == 5:
            b5.config(image = b5.image1)
        elif prev_tile == 6:
            b6.config(image = b6.image1)
        elif prev_tile == 7:
            b7.config(image = b7.image1)
        elif prev_tile == 8:
            b8.config(image = b8.image1)
        elif prev_tile == 9:
            b9.config(image = b9.image1)
        elif prev_tile == 10:
            b10.config(image = b10.image1)
        elif prev_tile == 11:
            b11.config(image = b11.image1)
        elif prev_tile == 12:
            b12.config(image = b12.image1)
        elif prev_tile == 13:
            b13.config(image = b13.image1)
        elif prev_tile == 14:
            b14.config(image = b14.image1)
        elif prev_tile == 15:
            b15.config(image = b15.image1)

#create class for tic tac toe game board places
class board(tkinter.Button):
    def __init__(self, master=None, board_location=None, **kwargs):
        self.command = kwargs.pop('command',None)
        super().__init__(master,**kwargs)
        self.config(image=blank_space, command=self.on_click)
        self.board_location = board_location

    def on_click(self):
        global player_turn
        global board_status
        
        if board_status[self.board_location] == 0:
            if player_turn == 0:#if it's the player's turn
                self.config(image=player1_token)#place an x
                player_turn = 1 #change to cpu turn so player can't place tokens
                board_status[self.board_location] = 1 #
            win_check()
            full_check()
            self.after(500, self.after_click)

    def after_click(self):
        #variables
        global board_status
        global player_turn
        free_spaces = [i for i in range(len(board_status)) if board_status[i] == 0]#find places on the board that have no peice on them

        if player_turn == 1: #ensure it is player 2's turn
            chosen_spot = random.choice(free_spaces)
            if chosen_spot == 0:
                tl.config(image = player2_token) #put player 2's token in the spot
                player_turn = 0 #change player turn
                board_status[0] = 2 #p2 token in this location
            elif chosen_spot == 0:
                tl.config(image = player2_token) #put player 2's token in the spot
                player_turn = 0 #change player turn
                board_status[0] = 2 #p2 token in this location
            elif chosen_spot == 1:
                tm.config(image = player2_token) #put player 2's token in the spot
                player_turn = 0 #change player turn
                board_status[1] = 2 #p2 token in this location
            elif chosen_spot == 2:
                tr.config(image = player2_token) #put player 2's token in the spot
                player_turn = 0 #change player turn
                board_status[2] = 2 #p2 token in this location
            elif chosen_spot == 3:
                ml.config(image = player2_token) #put player 2's token in the spot
                player_turn = 0 #change player turn
                board_status[3] = 2 #p2 token in this location
            elif chosen_spot == 4:
                mm.config(image = player2_token) #put player 2's token in the spot
                player_turn = 0 #change player turn
                board_status[4] = 2 #p2 token in this location
            elif chosen_spot == 5:
                mr.config(image = player2_token) #put player 2's token in the spot
                player_turn = 0 #change player turn
                board_status[5] = 2 #p2 token in this location
            elif chosen_spot == 6:
                bl.config(image = player2_token) #put player 2's token in the spot
                player_turn = 0 #change player turn
                board_status[6] = 2 #p2 token in this location
            elif chosen_spot == 7:
                bm.config(image = player2_token) #put player 2's token in the spot
                player_turn = 0 #change player turn
                board_status[7] = 2 #p2 token in this location
            elif chosen_spot == 8:
                br.config(image = player2_token) #put player 2's token in the spot
                player_turn = 0 #change player turn
                board_status[8] = 2 #p2 token in this location
            win_check()
            full_check()

#matching game functions
#function to check for matching game game over
def game_over_check():
    if tile_state.count(1) == 16:#if all tiles have been matched
        root.destroy()
        game_win_b.grid(row = 0, column = 0, columnspan = 4, rowspan = 4)#display game win screen
        #reset_board()

#funtion for game over button of matching game
def game_over_button():
    #root.destroy()#close game
    game_win_b.destroy()
    mainscreen()

#function to set images on matching game tiles
def image_set(image_num):
    if image_num == 1: #checks the number passed to find the corresponding image
        return 'angry.png'
    elif image_num == 2:
        return 'confused.png'
    elif image_num == 3:
        return 'happy.png'
    elif image_num == 4:
        return 'sad.png'
    elif image_num == 5:
        return 'sick.png'
    elif image_num == 6:
        return 'shy.png'
    elif image_num == 7:
        return 'tired.png'
    elif image_num == 8:
        return 'surprised.png'

#functions for tic tac toe
#function to check for if tic tac toe was won
def win_check():
    #variables
    global board_status
    global player_turn
    winner = 0 #0 = no winner, 1 = p1 win, 2 = p2 win
    
    #determine who won and where
    if board_status[0] == board_status[1] and board_status[1] == board_status[2]: #top row check
        winner = board_status[0] #winner is whoever has their token in these spots
    elif board_status[0] == board_status[4] and board_status[4] == board_status[8]: #top left to bottom right diagonal check
        winner = board_status[0] #winner is whoever has their token in these spots
    elif board_status[0] == board_status[3] and board_status[3] == board_status[6]: #left column check
        winner = board_status[0] #winner is whoever has their token in these spots
    elif board_status[1] == board_status[4] and board_status[4] == board_status[7]: #middle column check
        winner = board_status[1] #winner is whoever has their token in these spots
    elif board_status[2] == board_status[5] and board_status[5] == board_status[8]: #right column check
        winner = board_status[5] #winner is whoever has their token in these spots
    elif board_status[3] == board_status[4] and board_status[4] == board_status[5]: #middle row check
        winner = board_status[3] #winner is whoever has their token in these spots
    elif board_status[6] == board_status[7] and board_status[7] == board_status[8]: #bottom row check
        winner = board_status[6] #winner is whoever has their token in these spots
    elif board_status[6] == board_status[4] and board_status[4] == board_status[2]: #bottom left to top right diagonal check
        winner = board_status[6] #winner is whoever has their token in these spots

    #if there was a winner make sure no more tokens can be placed
    if winner != 0:
        player_turn = 2 
    #display winner message   
    if winner == 1:
        window.destroy()
        p1_win.grid(row = 0, column = 0, columnspan = 3, rowspan = 4)#display player 1 wins message
    elif winner == 2:
        window.destroy()
        p2_win.grid(row = 0, column = 0, columnspan = 3, rowspan = 4)#display player 2 wins message

#function that checks if the board is full
def full_check():
    #variables
    global board_status
    global player_turn

    if player_turn != 2:#make sure the game isn't already over
        #board is full when all the status variables are not 0
        if board_status[0] != 0 and board_status[1] != 0 and board_status[2] != 0 and board_status[3] != 0 and board_status[4] !=0 and board_status[5] !=0 and board_status[6] != 0 and board_status[7] != 0 and board_status[8] != 0:
            window.destroy()
            player_turn = 2
            draw.grid(row = 0, column = 0, columnspan = 3, rowspan = 4)#display draw message

#game over screen
def game_over():
    window.destroy()#close game when pressed
    p1_win.destroy()
    p2_win.destroy()
    draw.destroy()
    mainscreen()

#simaon says fucntions
#functions that change the action that the user is prompted to do
def change_prompt():
    #variables
    global current_prompt
    global round_num

    #remove previous prompt
    if current_prompt == 0:
        Simon_red.grid_forget()
    elif current_prompt == 1:
        Simon_green.grid_forget()
    elif current_prompt == 2:
        Simon_blue.grid_forget()
    #display a new prompt
    current_prompt = random.randrange(0,3,1)#randomly choose an integer in the range of 0 and 2 to decide new prompt 
    if current_prompt == 0:#prompt for red was chosen
        Simon_red.grid(row = 1, column = 1)
    elif current_prompt == 1:#prompt for green was chosen
        Simon_green.grid(row = 1, column = 1)
    elif current_prompt == 2:#prompt for blue was chosen
        Simon_blue.grid(row = 1, column = 1)
    #iterate number of rounds played, check if number of rounds has reached desired number
    round_num += 1
    if round_num > 15: #change this number to the number of desired rounds
        game_over.config(text = "You Win! Final score: " + str(score) + " out of " + str(round_num - 1))
        game_over.grid(row = 0, column = 0, columnspan = 3, rowspan = 3)#display game over message

#button commands
def red_pressed():
    #variables
    global score
    global current_prompt

    if current_prompt == 0: #prompted user to press red
        score += 1 #increase score
        score_display['text'] = "Score: " +str(score)#update score display
    change_prompt()#get a new prompt

def green_pressed():
    #variables
    global score
    global current_prompt

    if current_prompt == 1: #prompted user to press green
        score += 1 #increase score
        score_display['text'] = "Score: " +str(score)#update score display
    change_prompt()#get a new prompt

def blue_pressed():
    #variables
    global score
    global current_prompt

    if current_prompt == 2: #prompted user to press red
        score += 1 #increase score
        score_display['text'] = "Score: " +str(score)#update score display
    change_prompt()#get a new prompt

def game_end():
    game_over.destroy()
    simon_canvas.destroy()
    mainscreen()

#video player functions
#these two functions basically just load a video into the VLC video player. change the path in the 'Media = Instance.media_new('path')' line to change the video
def play_sand():
    global display
    global frame
    select_menu.destroy()#remove menu
    create_player()
    Media = Instance.media_new('Hidden in the Sand.mp4')#load Video
    player.set_hwnd(display.winfo_id())#set video player window
    player.set_media(Media)#load video into player
    player.play()#begin playing video
 
    
def play_banana():
    global display
    global frame
    select_menu.destroy()#remove menu
    create_player()
    Media = Instance.media_new('Banana Man.mp4')#load Video
    player.set_hwnd(display.winfo_id())#set video player window
    player.set_media(Media)#load video into player
    player.play()#begin playing video

def back_button():
    global display
    global frame
    player.stop()
    frame.destroy()
    #select_menu.pack()
    create_select()

#menu button functions
def openDrawing():
    #button_click_sound()
    C.destroy()
    drawing_screen()
    
def drawing_to_main():
    #button_click_sound()
    D.destroy()
    mainscreen()

def button_click_sound():
    playsound('button.wav')

def paint( event ):
   python_green = "#476042"
   x1, y1 = ( event.x - 2 ), ( event.y - 2 )
   x2, y2 = ( event.x + 2 ), ( event.y + 2 )
   D.create_oval( x1, y1, x2, y2, fill = python_green )

def matching_game():
    C.destroy()
    create_matching()
    root.pack()

def simon_says():
    C.destroy()
    create_simon()
    simon_canvas.pack()
    change_prompt()

def tic_tac_toe():
    C.destroy()
    create_tic()
    window.pack()

def video_menu():
    C.destroy()
    create_select()

def exit_video():
    global select_menu
    select_menu.destroy()
    mainscreen()

def mainscreen():
    #playsound('mus.wav', block=False)
    global C 
    C = Canvas(gui, bg="white", height = 1080, width = 1920)
    C.create_image(0, 0, image = bgfile, anchor=NW)

    C.create_text(1000, 50, text="Hi, I'm Electronic Buddy!", fill = "black", font=('Playtime', 50))
    C.create_text(1000, 125, text="Try Pressing on any of my buttons below!", fill = "black", font=('Playtime', 32))

    #Exit button
    exit_button = Button(C, text = "EXIT", fg = 'black', bg='white', bd='3',
                        relief = "ridge", font=('Playtime', 20), command = gui.destroy)
    exit_button.place(x=1800, y=10)
    #e6f9fd is the color of the bg
    #Main screen buttons
    simon_says_button = Button(C, text = "    Simon Says!     ", bd='3', fg = 'black',
                        bg='white', relief = "ridge", font=('Playtime', 60), command = simon_says)
    simon_says_button.place(x = 675, y=175)

    matching = Button(C, text = "        Matching!     ", bd='3', fg = 'black',
                        bg = 'white', relief = "ridge", font=('Playtime', 60), command = matching_game)
    matching.place(x = 675, y=350)

    tic_tac_toe_button = Button(C, text = "    Tic Tac Toe!     ", bd='3', fg = 'black',
                        bg='white', relief = "ridge", font=('Playtime', 60), command = tic_tac_toe)
    tic_tac_toe_button.place(x = 675, y=525)

    drawing = Button(C, text = "            Draw!         ", bd='3', fg = 'black',
                        bg = 'white', relief = "ridge",font=('Playtime', 60), command = openDrawing)
    drawing.place(x = 675, y=700)

    crosswords = Button(C, text = "    Watch Videos!  ", bd='3', fg = 'black',
                        bg = 'white', relief = "ridge", font=('Playtime', 60), command = video_menu)
    crosswords.place(x = 675, y=875)

    C.pack()

def drawing_screen():
    global D
    D = Canvas(gui, bg="white", height = 1080, width = 1920)
    D.create_image(0, 0, image = drawbgfile, anchor=NW)
    D.create_text(1000, 50, text="Touch to Draw!", fill = "black", font=('Playtime', 60))

    back_drawing_button = Button(D, text = "BACK", fg = 'black', bg='white', bd='3',
                        relief = "ridge", font=('Playtime', 40), command = drawing_to_main)
    back_drawing_button.place(x=1700, y=950)
    D.bind( "<B1-Motion>", paint )
    D.pack()

#create matching game screen
def create_matching():
    global root
    global b0
    global b1
    global b2
    global b3
    global b4
    global b5
    global b6
    global b7
    global b8
    global b9
    global b10
    global b11
    global b12
    global b13
    global b14
    global b15
    global game_win_b
    global tile_state
    global tile

    tile_state = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]#reset state of tiles
    random.shuffle(tiles)#randomize tile positons
    root = Canvas(gui, bg="white", height = 1920, width = 1080)
    #4x4 grid, button 0 is top left, going right and down increases index ex) top right is 3, bottom left is 12, bottom right is 15
    b0 = tile(root, 'tile.png', image_set(tiles[0]), 0)
    b1 = tile(root, 'tile.png', image_set(tiles[1]), 1)
    b2 = tile(root, 'tile.png', image_set(tiles[2]), 2)
    b3 = tile(root, 'tile.png', image_set(tiles[3]), 3)
    b4 = tile(root, 'tile.png', image_set(tiles[4]), 4)
    b5 = tile(root, 'tile.png', image_set(tiles[5]), 5)
    b6 = tile(root, 'tile.png', image_set(tiles[6]), 6)
    b7 = tile(root, 'tile.png', image_set(tiles[7]), 7)
    b8 = tile(root, 'tile.png', image_set(tiles[8]), 8)
    b9 = tile(root, 'tile.png', image_set(tiles[9]), 9)
    b10 = tile(root, 'tile.png', image_set(tiles[10]), 10)
    b11 = tile(root, 'tile.png', image_set(tiles[11]), 11)
    b12 = tile(root, 'tile.png', image_set(tiles[12]), 12)
    b13 = tile(root, 'tile.png', image_set(tiles[13]), 13)
    b14 = tile(root, 'tile.png', image_set(tiles[14]), 14)
    b15 = tile(root, 'tile.png', image_set(tiles[15]), 15)
    #game finished screen
    game_win_b = tkinter.Button(text="You Win!", fg = "white", bg = "#500000", width = 88, height = 26, font = ('Playtime', 60), command = game_over_button)
    #place buttons
    b0.grid(row = 0, column = 0)
    b1.grid(row = 0, column = 1)
    b2.grid(row = 0, column = 2)
    b3.grid(row = 0, column = 3)
    b4.grid(row = 1, column = 0)
    b5.grid(row = 1, column = 1)
    b6.grid(row = 1, column = 2)
    b7.grid(row = 1, column = 3)
    b8.grid(row = 2, column = 0)
    b9.grid(row = 2, column = 1)
    b10.grid(row = 2, column = 2)
    b11.grid(row = 2, column = 3)
    b12.grid(row = 3, column = 0)
    b13.grid(row = 3, column = 1)
    b14.grid(row = 3, column = 2)
    b15.grid(row = 3, column = 3)

#create tic-tac-toe screen
def create_tic():
    global window
    global tl
    global tm
    global tr
    global ml
    global mm
    global mr
    global bl
    global bm
    global br
    global p1_win
    global p2_win
    global draw
    global board_status
    global player_turn
    
    board_status = [0,0,0,0,0,0,0,0,0]#reset board status
    player_turn = 0 #reset player turn
    window = Canvas(gui, bg="white", height = 1920, width = 1080)
    #create buttons
    #top left button
    tl = board(window, 0)
    #top middle button
    tm = board(window, 1)
    #top right button
    tr = board(window, 2)
    #middle left button
    ml = board(window, 3)
    #middle middle button
    mm = board(window, 4)
    #middle right button
    mr = board(window, 5)
    #bottom left button
    bl = board(window, 6)
    #bottom middle button
    bm = board(window, 7)
    #bottom right button
    br = board(window, 8)
    #game over messages
    p1_win = tkinter.Button(text="You Won!", fg = "white", bg = "#500000", width = 88, height = 26, font = ('Playtime', 60), command=game_over)
    p2_win = tkinter.Button(text="EB Won!", fg = "white", bg = "#500000", width = 88, height = 26, font = ('Playtime', 60), command=game_over)
    draw = tkinter.Button(text="Draw!", fg = "white", bg = "#500000", width = 88, height = 26, font = ('Playtime', 60), command=game_over)
    #place buttons
    tl.grid(row = 1, column = 0)
    tm.grid(row = 1, column = 1)
    tr.grid(row = 1, column = 2)
    ml.grid(row = 2, column = 0)
    mm.grid(row = 2, column = 1)
    mr.grid(row = 2, column = 2)
    bl.grid(row = 3, column = 0)
    bm.grid(row = 3, column = 1)
    br.grid(row = 3, column = 2)

#create simon says screen
def create_simon():
    global simon_canvas
    global Simon_red
    global Simon_green
    global Simon_blue
    global game_over
    global score_display
    global score
    global round_num
    
    #reset variables
    score = 0
    round_num = 0
    #canvas
    simon_canvas = Canvas(gui, bg="white", height = 1920, width = 1080)
    simon_canvas.create_image(0, 0, image = bgfile, anchor=NW)
    #messages
    Simon_red = tkinter.Label(simon_canvas, text = "Simon says press the red button", font = ('Playtime', 60))
    Simon_green = tkinter.Label(simon_canvas, text = "Simon says press the green button", font = ('Playtime', 60))
    Simon_blue = tkinter.Label(simon_canvas, text = "Simon says press the blue button", font = ('Playtime', 60))
    score_display = tkinter.Label(simon_canvas, text = "Score: 0", font = ('Playtime', 60))
    #buttons
    button_red = tkinter.Button(simon_canvas, bg = "red", width = 100, height = 75, command = red_pressed)
    button_green = tkinter.Button(simon_canvas,bg = "green", width = 100, height = 75,command = green_pressed)
    button_blue = tkinter.Button(simon_canvas,bg = "blue", width = 100, height = 75,command = blue_pressed)
    game_over = tkinter.Button(simon_canvas,text="You Win! Final score: " + str(score) + " out of " + str(round_num), fg = "white", bg = "#500000", width = 88, height = 26, font = ('Playtime', 60), command = game_end)
    exit_game = tkinter.Button(simon_canvas, text = "BACK",fg = 'black', bg='white', bd='3',
                        relief = "ridge", font=('Playtime', 40), command = game_end)
    #place objects
    button_red.grid(row = 2, column = 0)
    button_green.grid(row = 2, column = 1)
    button_blue.grid(row = 2, column = 2)
    score_display.grid(row = 0, column = 0)
    exit_game.place(x=1700, y=950)

#create video player select menu
# Change the text value in 'banana_button'/'sand_button' to match the names of the videos
def create_select():
    global select_menu
    #canvas
    select_menu = Canvas(gui, bg="white", height = 1080, width = 1920)
    select_menu.create_image(0, 0, image = bgfile, anchor=NW)
    #make text
    select_menu.create_text(1000, 50, text="Choose a video to play!", fill = "black", font=('Playtime', 50))
    #make buttons
    banana_button = Button(select_menu, text = "       Banana Man      ",bd='3', fg = 'black',
                            bg='white', relief = "ridge", font=('Playtime', 60), command = play_banana)
    sand_button = Button(select_menu, text = "Hidden in the Sand", bd='3', fg = 'black',
                            bg='white', relief = "ridge", font=('Playtime', 60), command = play_sand)
    exit_button = Button(select_menu, text = "EXIT", fg = 'black', bg='white', bd='3',
                            relief = "ridge", font=('Playtime', 20), command = exit_video)
    #place buttons
    banana_button.place(x = 675, y = 175)
    sand_button.place(x = 675, y = 350)
    exit_button.place(x=675, y=825)

    select_menu.pack()

#creates display that playes videos. videos need to be loaded using a seperate command
def create_player():
    global frame
    global display
    global player
    global Instance
    #create player
    frame = Canvas(gui, width=1920, height=1080)
    frame.create_image(0, 0, image = bgfile, anchor=NW)
    display = Frame(frame, bd=5)
    Instance = vlc.Instance()
    player = Instance.media_player_new()
    back = Button(frame, text = "back", fg = 'black',
                            bg='white', relief = "ridge", font=('Playtime', 60), command = back_button)
    frame.pack()#place player frame
    display.place(relwidth = 1, relheight = 0.8)#place video player
    back.place(x=675, y=785)

mainscreen()
gui.mainloop()