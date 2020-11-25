#Space Rocks Game 

from tkinter import Tk, PhotoImage, Canvas, Label
from random import randint as rand
from time import sleep



def configure_window():
	window.geometry("1920x1080")
	window.configure(background="black")
	window.title("SPACE ROCKS")

def left(event):
	x = -20
	y = 0
	canvas.move(spaceship_sprite, x, y)

def right(event):
	x = 20
	y = 0
	canvas.move(spaceship_sprite, x, y)

def up(event):
	x = 0
	y = -20
	canvas.move(spaceship_sprite, x, y)

def down(event):
	x = 0
	y = 20
	canvas.move(spaceship_sprite, x, y)

# def original_coords():
# 	y = rand(200, 800)
# 	xy = (1300, y, 1400, y + 100)
# 	asteroids.append(canvas.create_oval(xy, fill="grey"))


window = Tk()
configure_window()

canvas = Canvas(window, width=1920, height=1080)


canvas.config(bg="#080341")

stars = []
 
for i in range(450):
	x = rand(1, 1919)
	y = rand(1, 1079)

	size = rand(2,4)
	xy = (x, y, x+size, y+size)

	star = canvas.create_oval(xy, fill="#FFFF00")

	stars.append(star)

spaceship = PhotoImage(file = "shuttle2.gif")
spaceship_sprite = canvas.create_image(750, 700, anchor="s", image = spaceship)

asteroids = []
num_asteroids = rand(10,30)

for i in range(num_asteroids):
	y = rand(0, 600)
	x = rand(100, 1700)
	xy = (x, y, x+50, y + 50)
	asteroids.append(canvas.create_oval(xy, fill="grey"))


canvas.pack()

X = [4] * num_asteroids
Y = [4] * num_asteroids

while True:
	for i in range(num_asteroids):
		pos = canvas.coords(asteroids[i])
		
		if pos[0] < 0 or pos[2] > 1820:
			X[i] = -X[i]

		canvas.move(asteroids[i], -X[i], 0)

	sleep(0.00000000000001)
	window.update()

	window.bind("<Left>", left)
	window.bind("<Right>", right)
	# window.bind("<Up>", up)
	# window.bind("<Down>", down)



	



window.mainloop()
