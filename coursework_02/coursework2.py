
#Space Rocks Game

from tkinter import *
from random import randint as rand
from time import sleep

def configure_window():
	window.geometry("1920x1080")
	window.configure(background="black")
	window.title("SPACE ROCKS")

def canvas():
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

def asteroids():
	global asteroids 
	asteroids = []
	global num_asteroids 
	num_asteroids = rand(20,50)
	# print(num_asteroids)
	for i in range(num_asteroids):
		y = rand(0, 600)
		x = rand(100, 1700)
		xy = (x, y, x+50, y + 50)
		asteroids.append(canvas.create_oval(xy, fill="grey"))

def left(event):
	global object_test
	x = -20
	y = 0
	canvas.move(object_test, x, y)

def right(event):
	global object_test
	x = 20
	y = 0
	canvas.move(object_test, x, y)

def up(event):
	global object_test
	x = 0
	y = -20
	canvas.move(object_test, x, y)

def down(event):
	global object_test
	x = 0
	y = 20
	canvas.move(object_test, x, y)

def shot(event):
	global bullet
	x1_bullet = player_coords_live[0]
	y1_bullet = player_coords_live[1]
	x2_bullet = player_coords_live[2]
	y2_bullet = player_coords_live[3]
	bullet = canvas.create_line(x1_bullet, y1_bullet, x1_bullet, y1_bullet-20, fill="yellow", width = 5, tag="shooting")	
	window.after(70, shooting)

def shooting():
	canvas.move("shooting", 0, -20)
	canvas.update()
	window.after(70, shooting)
			


def game_loop():
	canvas()
	stars_background()
	
	current_score = 0
	score = canvas.create_text(100,100, text=("Score:", current_score), font=("Times New Roman Bold",30), fill="white")
	
	# spaceship = PhotoImage(file = "shuttle2.gif")
	# spaceship_sprite = canvas.create_image(750, 700, anchor="s", image = spaceship)

	# player_init_coords = canvas.coords(spaceship_sprite)
	xy = (700, 750, 750, 800)
	global object_test 
	object_test = canvas.create_oval(xy, fill="red")
	asteroids()

	

	X = [4] * num_asteroids
	Y = [4] * num_asteroids

	loop=True
	while loop==True:
		global player_coords
		player_coords = canvas.coords(object_test)
		#print(player_coords)
		for i in range(num_asteroids):
			pos = canvas.coords(asteroids[i])
		
			if pos[0] < 0 or pos[2] > 1820:
				X[i] = -X[i]

			

			if pos[0] < player_coords[2] and pos[2] > player_coords[0] and pos[1] < player_coords[3] and pos[3] > player_coords[1]:
				loop=False
				game_over()
				

		
			
		
			canvas.move(asteroids[i], -X[i], 0)

		sleep(0.00000000000001)
		window.update()

		window.bind("<Left>", left)
		window.bind("<Right>", right)
		window.bind("<Up>", up)
		window.bind("<Down>", down)

		global player_coords_live
		player_coords_live = canvas.coords(object_test)
		print(player_coords_live)

		window.bind('<space>', shot)




	

	


window = Tk()
configure_window()

title = Label(window, text="SPACE ROCKS", font=("Times New Roman Bold",50), bg="black", fg="dark blue")
title.place(x=500, y=100)

btn1 = Button(window, text="New Game", font=("Times New Roman Bold",10), width = 30, height = 1, command=lambda:game_loop(), background="dark blue")
btn1.place(x=550, y=200)

btn2 = Button(window, text="Load Game",font=("Times New Roman Bold",10), width = 30, height = 1, command=lambda:load_game(), background="dark blue")
btn2.place(x=550, y=300)

btn3 = Button(window, text="Leaderboard",font=("Times New Roman Bold",10), width = 30, height = 1, command=lambda:leaderboard(), background="dark blue")
btn3.place(x=550, y=400)

btn4 = Button(window, text="Quit Game",font=("Times New Roman Bold",10), width = 30, height = 1, command=lambda:quit_game(), background="dark blue")
btn4.place(x=550, y=500)





window.mainloop()
