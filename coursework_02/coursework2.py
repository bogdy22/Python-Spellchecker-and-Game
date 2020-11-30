
#Space Rocks Game

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
	stars = []
	 
	for i in range(450):
		x = rand(1, 1919)
		y = rand(1, 1079)

		size = rand(2,4)
		xy = (x, y, x+size, y+size)

		star = canvas.create_oval(xy, fill="#FFFF00")

		stars.append(star)

def create_asteroids():
	global asteroids 
	asteroids = []
	global num_asteroids 
	num_asteroids = rand(20,35)
	for i in range(num_asteroids):
		y = rand(0, 600)
		x = rand(100, 1700)
		xy = (x, y, x+50, y + 50)
		asteroids.append(canvas.create_oval(xy, fill="grey"))

def left(event):
	global object_test
	x = -20
	y = 0
	if player_coords_live[0] > 0:
		canvas.move(object_test, x, y)

def right(event):
	global object_test
	x = 20
	y = 0
	if player_coords_live[2] < 1430:
		canvas.move(object_test, x, y)

# def up(event):
# 	global object_test
# 	x = 0
# 	y = -20
# 	canvas.move(object_test, x, y)

# def down(event):
# 	global object_test
# 	x = 0
# 	y = 20
# 	canvas.move(object_test, x, y)

def shot(event):
	global bullet
	global bullet_coords
	x1_bullet = player_coords_live[0]
	y1_bullet = player_coords_live[1]
	x2_bullet = player_coords_live[2]
	y2_bullet = player_coords_live[3]
	bullet = canvas.create_line(x1_bullet, y1_bullet, x1_bullet, y1_bullet-20, fill="yellow", width = 5, tag="shooting")	
	window.after(100, shooting)	

def shooting():
	global current_score
	global final_score
	canvas.move("shooting", 0, -20)
	bullet_coords = canvas.coords(bullet)
	for i in range(num_asteroids):
		pos = canvas.coords(asteroids[i])
		hit = asteroids[i]
		if pos[0] < bullet_coords[2] and pos[2] > bullet_coords[0] and pos[1] < bullet_coords[3] and pos[3] > bullet_coords[1]:
			canvas.delete(bullet)
			current_score += 10
			canvas.itemconfig(score, text="Score:" + str(current_score))
			# asteroids.remove(hit)
			final_score = current_score	
	canvas.update()
	window.after(100, shooting)	
	

def pause(event):
	global canvas2
	canvas2 = Canvas(canvas, width=1920, height=1080, bg="black")
	canvas2.pack()
	pause = canvas2.create_text(700, 300, text="Game paused", fill="#080341", font=("Times New Roman Bold", 70))
	button_pause1 = Button(canvas2, text="Resume", font=("Times New Roman Bold",10), width = 30, height = 1, command=lambda:resume(), bg="black", fg="#080341")
	button_pause1.place(x=650,y=400)
	button_pause2 = Button(canvas2, text="Save and quit", font=("Times New Roman Bold",10), width = 30, height = 1, command=lambda:back_to_menu(), bg="black", fg="#080341")
	button_pause2.place(x=650, y=450)

def empty(event):
	pass

def resume():
	canvas2.destroy()

def back_to_menu():
	canvas.destroy()
	print(final_score)

def menu(event):
	canvas.destroy()

def load_game():	
	game_loop()

def game_loop():
	canvas_game()
	stars_background()
	global score
	global current_score
	global final_score
	current_score = 0
	score = canvas.create_text(100,100, text="Score: 0", font=("Times New Roman Bold",30), fill="white")
	
	# spaceship = PhotoImage(file = "shuttle2.gif")
	# spaceship_sprite = canvas.create_image(750, 700, anchor="s", image = spaceship)

	# player_init_coords = canvas.coords(spaceship_sprite)
	xy = (700, 750, 750, 800)
	global object_test 
	object_test = canvas.create_oval(xy, fill="red")
	create_asteroids()

	window.bind('<p>', pause)
	
	X = [4] * num_asteroids
	Y = [4] * num_asteroids

	global loop
	loop=True
	while loop==True:
		global player_coords
		global pos
		player_coords = canvas.coords(object_test)
		#print(player_coords)
		for i in range(num_asteroids):
			pos = canvas.coords(asteroids[i])

			if pos[0] < 0 or pos[2] > 1820:
				X[i] = -X[i]

			canvas.move(asteroids[i], -X[i], 0)

		sleep(0.00000000000001)
		window.update()
		# window.bind("<Up>", up)
		# window.bind("<Down>", down)

		window.bind("<space>", shot)
		global player_coords_live
		player_coords_live = canvas.coords(object_test)
		
		window.bind("<Left>", left)
	
		window.bind("<Right>", right)
		# if current_score == 20:
		# 	loop = False
		# 	back_to_menu()
		# print(player_coords_live)

def destroy_entry():
	e.destroy()
	btn.destroy()
	label.destroy()
	game_loop()

def get_input():
	global e
	global player_name
	player_name = e.get()
	destroy_entry()

def user_name():
	global e
	global btn
	global label
	e = Entry(window, width=100)
	e.pack()
	btn = Button(window, text="Start Game", command=lambda:get_input())
	btn.pack()
	label = Label(window, text="Enter your name")
	label.pack()

def leaderboard():
	canvas_game()
	window.bind('<q>', menu)
	

def quit_game():
	window.destroy()

window = Tk()
configure_window()

leaderboard_data = {}
# file=open('leaderboard.json')
# leaderboard_data = json.load(file)

title = Label(window, text="SPACE ROCKS", font=("Times New Roman Bold",50), bg="black", fg="#080341")
title.place(x=500, y=100)


btn1 = Button(window, text="New Game", font=("Times New Roman Bold",10), width = 30, height = 1, command=lambda:user_name(), bg="black", fg="#080341")
btn1.place(x=550, y=200)

btn2 = Button(window, text="Load Game",font=("Times New Roman Bold",10), width = 30, height = 1, command=lambda:load_game(), bg="black", fg="#080341")
btn2.place(x=550, y=300)

btn3 = Button(window, text="Leaderboard",font=("Times New Roman Bold",10), width = 30, height = 1, command=lambda:leaderboard(), bg="black", fg="#080341")
btn3.place(x=550, y=400)

btn4 = Button(window, text="Quit Game",font=("Times New Roman Bold",10), width = 30, height = 1, command=lambda:quit_game(), bg="black", fg="#080341")
btn4.place(x=550, y=500)






window.mainloop()
