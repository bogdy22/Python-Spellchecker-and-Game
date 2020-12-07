# SPACE ROCKS GAME

# If it is the case, please set the resolution to 1920x1080


from tkinter import *
from random import randint as rand
from time import sleep
import json


def configure_window():
    window.geometry("1920x1080")
    window.configure(background="black")
    window.title("SPACE ROCKS")


def canvas_game():
    global canvas
    canvas = Canvas(window, width=1920, height=1080)
    canvas.config(bg="#080341")
    canvas.pack()


def stars_background():
    for i in range(450):
        x = rand(1, 1919)
        y = rand(1, 1079)

        size = rand(2, 4)
        xy = (x, y, x+size, y+size)

        star = canvas.create_oval(xy, fill="#FFFF00")


def create_asteroids():
    global asteroids
    asteroids = []
    global num_asteroids
    num_asteroids = rand(10, 25)

    for i in range(num_asteroids):
        y = rand(0, 600)
        x = rand(100, 1700)
        xy = (x, y, x+50, y + 50)
        asteroids.append(canvas.create_oval(xy,
                                              fill="grey"))
        # create asteroids of the same diameter at random positions on the canvas


def left(event):
    global object_test
    x = -20
    y = 0
    if player_coords_live[0] > 0:
        canvas.move(spaceship_sprite, x, y)         
        # move the player left


def right(event):
    global object_test
    x = 20
    y = 0
    if player_coords_live[1] < 1430:
        canvas.move(spaceship_sprite, x, y)                        # move the player right


# empty function to cancel some key binds menus
def empty(event):
    pass


def shot(event):
    global bullet
    global bullet_coords
    x_bullet = player_coords_live[0]
    y_bullet = player_coords_live[1]
    if cheat == 1:
        width_var = 15
    else:
        width_var = 5
    bullet = canvas.create_line(x_bullet, y_bullet-30, x_bullet, y_bullet-50, fill="yellow", width = width_var, tag="shooting")        # create the bullet
    window.after(100, shooting)        # after a delay of 100ns, shoot the bullet


def shooting():
    global current_score
    global final_score
    canvas.move("shooting", 0, -20)        # shoot the bullet
    bullet_coords = canvas.coords(bullet)
    for i in range(num_asteroids):
        pos = canvas.coords(asteroids[i])
        if pos[0] < bullet_coords[2] and pos[2] > bullet_coords[0] and pos[1] < bullet_coords[3] and pos[3] > bullet_coords[1]:
            canvas.delete(bullet)          # make the bullet dissapear
            current_score += 10
            canvas.itemconfig(score, text="Score:" + str(current_score))
        final_score = current_score
        with open("load_game_score.txt", 'w') as file:
            file.write(str(final_score))
        scores.append(final_score)
        leaderboard_scores[player_name] = final_score   # save the final score of the player for the leaderboard  
    with open("leaderboard.json", "w") as lead_file:            
        json.dump(leaderboard_scores, lead_file)             # update the leaderboard file
    canvas.update()
    window.after(100, shooting)        # shoot next bullet after the delay


def pause(event):
    global canvas2
    canvas2 = Canvas(canvas, width=1920, height=1080, bg="black")
    canvas2.pack()
    pause = canvas2.create_text(900, 400, text="Game paused", fill="dark blue", font=("Times New Roman Bold", 40))
    button_pause1 = Button(canvas2, text="Resume", font=("Times New Roman Bold",10), width = 30, height = 1, command=lambda:resume(), highlightbackground="black", fg="#080341")
    button_pause1.place(x=650, y=500)
    button_pause2 = Button(canvas2, text="Save and quit", font=("Times New Roman Bold",10), width = 30, height = 1, command=lambda:back_to_menu(), highlightbackground="black", fg="#080341")
    button_pause2.place(x=650, y=650)


def resume():
    canvas2.destroy()


def back_to_menu():
    canvas.destroy()
    

def menu(event):
    canvas.destroy()


def menu_from_bosskey(event):
    canvas3.destroy()

def cheat_code(event):
    global cheat
    if cheat == 0:
        cheat = 1
    else:
        cheat = 0          # when cheat is active the bullets will be significantly bigger 

def boss_key(event):
    global code
    global canvas3
    canvas.destroy()
    window.bind('<q>', menu_from_bosskey)
    canvas3 = Canvas(window, width=1920, height=1080, bg="black")
    code = canvas3.create_text(900, 500, text="<p id=example1-description>\n</p>\n<figure>\n<figcaption id='example1-caption'>\n</figcaption>\n<pre\n aria-labelledby='example1-caption'\n aria-describedby='example1-description'><code>function getToSleep()\n{\n while(noise &lt;= 10 &amp;&amp; sleep !== 'zzz')\n{\nsheep ++;\n}\nif(noise &gt; 10)\n{\nreturn false;\n }\nreturn true;\n}</code></pre>\n</figure>", fill="white", font=("Terminal", 15))     #some random code so that the boss thinks you are working
    canvas3.pack()


def load_game():    
    canvas_game()
    stars_background()

    global score
    global current_score
    global final_score
    global spaceship
    global spaceship_sprite
    global player_name
    with open("leaderboard_data.txt") as f:         # the name of the last player who played the game
        player_name = f.read()


    with open("load_game_score.txt", 'r') as file:
        tmp_score = file.read()                      # get the last score so the player can continue from where he left off
    current_score = int(tmp_score)
    score = canvas.create_text(120,50, text=("Score:" +str(current_score)), font=("Times New Roman Bold",20), fill="white")
    
    spaceship = PhotoImage(file = "shuttle2.png")
    spaceship_sprite = canvas.create_image(950, 900, anchor="s", image = spaceship)      

    player_init_coords = canvas.coords(spaceship_sprite)
    
    create_asteroids()

    window.bind('<p>', pause)
    
    X = [2] * num_asteroids
    Y = [2] * num_asteroids

    # move the asteroids created
    while True:
        global player_coords
        global pos
        player_coords = canvas.coords(spaceship_sprite)

        for i in range(num_asteroids):
            pos = canvas.coords(asteroids[i])

            if pos[0] < 0 or pos[2] > 1920:
                X[i] = -X[i]

            canvas.move(asteroids[i], -X[i], 0)

        sleep(0.00000000000001)
        window.update()

        if key1 == 1:                                        # verify if player changed controls for a key
            new_key = '<' + user_key_choice + '>'
            window.bind(new_key, shot)
        else:
            window.bind(shoot_key, shot)
        
        global player_coords_live
        player_coords_live = canvas.coords(spaceship_sprite)

        if key2 == 1:
            new_key = '<' + user_key_choice + '>'
            window.bind(new_key, right)
        else:
            window.bind(move_right_key, right)
    
        if key3 == 1:
            new_key = '<' + user_key_choice + '>'
            window.bind(new_key, left)
        else:
            window.bind(move_left_key, left)

        window.bind('<c>', cheat_code)
    
def game_loop():
    canvas_game()
    stars_background()
    
    global score
    global current_score
    global final_score
    global spaceship_sprite
    global pause_key
    global shoot_key
    global move_left_key
    global move_right_key

    current_score = 0
    score = canvas.create_text(120,50, text="Score: 0", font=("Times New Roman Bold",20), fill="white")

    spaceship = PhotoImage(file = "shuttle2.png")
    spaceship_sprite = canvas.create_image(950, 900, anchor="s", image = spaceship)

    player_init_coords = canvas.coords(spaceship_sprite)

    create_asteroids()

    window.bind('<p>', pause)
    
    X = [2] * num_asteroids
    Y = [2] * num_asteroids

    
    while True:
        global player_coords
        global pos
        player_coords = canvas.coords(spaceship_sprite)
        for i in range(num_asteroids):
            pos = canvas.coords(asteroids[i])

            if pos[0] < 0 or pos[2] > 1920:
                X[i] = -X[i]

            canvas.move(asteroids[i], -X[i], 0)

        sleep(0.00000000000001)
        window.update()
        
        if key1 == 1:
            new_key = '<' + user_key_choice + '>'
            window.bind(new_key, shot)
        else:
            window.bind(shoot_key, shot)
        


        global player_coords_live
        player_coords_live = canvas.coords(spaceship_sprite)

        if key2 == 1:
            new_key = '<' + user_key_choice + '>'
            window.bind(new_key, right)
        else:
            window.bind(move_right_key, right)
    
        if key3 == 1:
            new_key = '<' + user_key_choice + '>'
            window.bind(new_key, left)
        else:
            window.bind(move_left_key, left)
        
        window.bind('<c>', cheat_code)

def destroy_entry():
    e.destroy()
    btn.destroy()
    label.destroy()
    game_loop()


#get the name of the player saved in a file
def get_input():
    global e
    global player_name
    player_name = e.get()
    player_name_list.append(player_name)
    with open("leaderboard_data.txt", 'w') as f:
        f.write(player_name + "\n")
    destroy_entry()


#ask for the name of the player
def user_name():
    global e
    global btn
    global label
    e = Entry(window, width=100)
    e.pack()
    btn = Button(window, text="Start Game", command=lambda:get_input(), highlightbackground="black")
    btn.pack()
    label = Label(window, text="Enter your name")
    label.pack()


def leaderboard():
    canvas_game()
    global lead_image
    global lead_img
    window.bind('<q>', menu)
    top = canvas.create_text(900, 100,
                             text="TOP 5", font=("Times New Roman Bold", 50), 
                             fill="yellow")
    with open('leaderboard.json', 'r') as lead_file:
        leaderboard_output = json.load(lead_file)
    # sorting the dictionary within the leaderboard file descending after the scorres values
    sorted_leaderboard = sorted(leaderboard_output.items(),
                                key=lambda x: x[1], reverse=True)   
    canvas.create_text(900, 900,
                       text="Press Q to go back to menu",
                       fill="yellow", font=("Times New Roman Bold",20))
    canvas.create_text(900, 250,
                       text=("1. " + str(sorted_leaderboard[0][0]) + " : " + str(sorted_leaderboard[0][1])),
                       fill="yellow", font=("Times New Roman ", 30))
    canvas.create_text(900, 350,
                       text=("2. " +str(sorted_leaderboard[1][0]) + " : " + str(sorted_leaderboard[1][1])),
                       fill="yellow", font=("Times New Roman ", 30))
    canvas.create_text(900, 450,
                       text=("3. " + str(sorted_leaderboard[2][0]) + " : " + str(sorted_leaderboard[2][1])),
                       fill="yellow", font=("Times New Roman ", 30))
    canvas.create_text(900, 550,
                       text=("4. " +str(sorted_leaderboard[3][0]) + " : " + str(sorted_leaderboard[3][1])),
                       fill="yellow", font=("Times New Roman ", 30))
    canvas.create_text(900, 650,
                       text=("5. " + str(sorted_leaderboard[4][0]) + " : " + str(sorted_leaderboard[4][1])),
                       fill="yellow", font=("Times New Roman ", 30))
    
    window.bind("<space>", empty)


def change_setting(key):
    global key1
    global key2
    global key3
    if change_set == "shoot":
        shoot_key = user_key_choice
        key1 = 1
    elif change_set == "move right":
        move_right_key = user_key_choice
        key2 = 1
    elif change_set == "move left":
        move_left_key = user_key_choice
        key3 = 1


def input2():
    global user_key_choice
    user_key_choice = change_entry2.get()
    change_entry2.destroy()
    change_label2.destroy()
    btn7.destroy()
    change_entry.destroy()
    change_label.destroy()
    canvas.destroy()
    change_setting(user_key_choice)    


def input():
    global change_set
    global change_entry2
    global change_label2
    global btn7
    change_set = change_entry.get()
    btn6.destroy()
    if(change_set == "shoot" or change_set == "move right"
    or change_set == "move left"):
        change_entry2 = Entry(canvas)
        change_entry2.pack()
        change_label2 = Label(canvas,
                              text="Enter the key you want to use for the action")
        change_label2.pack()
        btn7 = Button(canvas, text="Change option",
                      font=("Times New Roman Bold", 10), width=40, height=1,
                      command=lambda: input2(), highlightbackground="black",
                      fg="#080341")
        btn7.pack()
    else:
        change_entry.destroy()
        change_label.destroy()


def change_controls():
    global change_entry
    global change_label
    global btn6
    change_entry = Entry(canvas)
    canvas.create_window(500, 100, window=change_entry)
    change_entry.pack()
    change_label = Label(canvas,
                         text="Enter which setting do you want to change (the name of the action) ")
    change_label.pack()
    btn6 = Button(window, text="Change",
                  command=lambda: input(), highlightbackground="black")
    btn6.pack()


def game_options():
    global canvas
    canvas_game()
    window.bind('<q>', menu)
    # window.bind('<Escape>', boss_key)
    canvas.create_text(900, 100, text="Game Controls",
                       font=("Times New Roman Bold", 30), fill="yellow")
    canvas.create_text(900, 200, text="In-game controls",
                       font=("Times New Roman ", 20), fill="yellow")
    canvas.create_text(900, 250, text="LEFT ARROW KEY - Move left",
                       font=("Times New Roman ", 20), fill="yellow")
    canvas.create_text(900, 300, text="RIGHT ARROW KEY - Move right",
                       font=("Times New Roman ", 20), fill="yellow")
    canvas.create_text(900, 350, text="SPACE - Shoot",
                       font=("Times New Roman ", 20), fill="yellow")
    canvas.create_text(900, 400, text="P - pause game",
                       font=("Times New Roman ", 20), fill="yellow")
    canvas.create_text(900, 800, text="Press Q to go back",
                       font=("Times New Roman Bold", 20), fill="yellow")
    canvas.create_text(900, 1000,
                       text="Press C for supershoot (cheat code) and ESC for bosskey (Q for back)",
                       fill="yellow", font=("Times New Roman", 10))
    btn_change = Button(canvas, text="Change controls",
                        font=("Times New Roman Bold", 10), width=40, height=1,
                        command=lambda: change_controls(),
                        highlightbackground="black",
                        fg="#080341")
    btn_change.place(x=600, y=500)


def quit_game():
    window.destroy()


window = Tk()
configure_window()

global scores
global player_name_list 
global leaderboard_scores
global lead_file
scores = []
player_name_list = []

leaderboard_scores = {}
lead_file = open("leaderboard.json")
leaderboard_scores = json.load(lead_file)

window.bind('<Escape>', boss_key)

pause_key = "<p>"              # default keys for control
move_left_key = "<Left>"
move_right_key = "<Right>"
shoot_key = "<space>"
key1 = 0
key2 = 0
key3 = 0
cheat = 0


title = Label(window, text="SPACE ROCKS",
              font=("Times New Roman Bold", 50), bg="black",
              fg="dark blue")
title.place(x=500, y=100)


btn1 = Button(window, text="New Game",
              font=("Times New Roman Bold", 10), width=30, height=1,
              command=lambda: user_name(), highlightbackground="black",
              fg="#080341")
btn1.place(x=650, y=300)

btn2 = Button(window, text="Load Game",
              font=("Times New Roman Bold", 10), width=30, height=1,
              command=lambda: load_game(), highlightbackground="black",
              fg="#080341")
btn2.place(x=650, y=400)

btn3 = Button(window, text="Leaderboard",
              font=("Times New Roman Bold", 10), width=30, height=1,
              command=lambda: leaderboard(), highlightbackground="black",
              fg="#080341")
btn3.place(x=650, y=500)

btn4 = Button(window, text="Options",
              font=("Times New Roman Bold", 10), width=30, height=1,
              command=lambda: game_options(), highlightbackground="black",
              fg="#080341")
btn4.place(x=650, y=600)

btn5 = Button(window, text="Quit Game",
              font=("Times New Roman Bold", 10), width=30, height=1,
              command=lambda: quit_game(), highlightbackground="black",
              fg="#080341")
btn5.place(x=650, y=700)


window.mainloop()


# The images used in this game were downloaded from opengameart.org 
# The code used by the bosskey was taken from sitepoint.com, with no copyright law infrigements.
