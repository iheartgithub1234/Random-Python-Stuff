from tkinter import *
import random
import time

print("WELCOME TO SNAKE GAME")
print("CODED IN PYTHON WITH TKINTER AND RANDOM")
print()

print("WOULD YOU LIKE TO CUSTOMIZE SETTINGS OR HAVE REGULAR SETTINGS")
ask_to_customize = input("'y' OR 'n': ")
print()

if ask_to_customize == "y":
    print("ENTER GAME WIDTH")
    game_width = int(input("RECOMENDED IS 500: "))
    print()

    print("ENTER GAME HEIGHT")
    game_height = int(input("RECOMENDED IS 500: "))
    print()

    print("ENTER SNAKE SPEED")
    speed = int(input("RECOMENDED IS 100, HIGHER NUMBERS ARE SLOWER, LOWER NUMBERS ARE FASTER: "))
    print()

    print("ENTER SPACE SIZE")
    space_size = int(input("RECOMENDED IS 30: "))
    print()

    print("ENTER STARTING BODY PARTS")
    body_parts = int(input("RECOMENDED IS 3: "))
    print()

    print("ENTER SNAKE COLOR")
    snake_color = input("RECOMENDED IS 'green': ")
    print()

    print("ENTER FOOD COLOR")
    food_color = input("RECOMENDED IS 'red': ")
    print()

    print("ENTER BACKGROUND COLOR")
    background_color = input("RECOMENDED IS 'black': ")
    print()
else:
    game_width = 500
    game_height = 500
    speed = 100
    space_size = 30
    body_parts = 3
    snake_color = "green"
    food_color = "red"
    background_color = "black"

print("SETTINGS:")
print()
print("WIDTH: " + str(game_width))
print("HEIGHT: " + str(game_height))
print("SPEED: " + str(speed))
print("SPACE SIZE: " + str(space_size))
print("STARTING BODY PARTS: " + str(body_parts))
print("SNAKE COLOR:" + snake_color)
print("FOOD COLOR: " + food_color)
print("BACKGROUND COLOR: " + background_color)
print()

print("ARROW KEYS TO MOVE")
print("STARTING IN")
time.sleep(1)
print("3")
time.sleep(1)
print("2")
time.sleep(1)
print("1")
print()

print("OPENING WINDOW")
print()

class Snake:
    def __init__(self):
        self.body_size = body_parts
        self.coordinates = []
        self.squares = []

        for i in range(0, body_parts):
            self.coordinates.append([0, 0])
        
        for x, y in self.coordinates:
            square = canvas.create_rectangle(x, y, x + space_size, y + space_size, fill=snake_color, tag="snake")
            self.squares.append(square)

class Food:
    def __init__(self):
        x = random.randint(0, (game_width // space_size)-1) * space_size
        y = random.randint(0, (game_height // space_size)-1) * space_size
        self.coordinates = [x, y]
        
        canvas.create_oval(x, y, x+ space_size, y + space_size, fill=food_color, tag="food")

def next_turn(snake, food):
    x, y = snake.coordinates[0]

    if direction == "up":
        y -= space_size
    elif direction == "down":
        y += space_size
    elif direction == "left":
        x -= space_size
    elif direction == "right":
        x += space_size
    
    snake.coordinates.insert(0, (x, y))

    square = canvas.create_rectangle(x, y, x + space_size, y + space_size, fill=snake_color)

    snake.squares.insert(0, square)

    if x == food.coordinates[0] and y == food.coordinates[1]:
        global score
        score += 1
        label.config(text=("SCORE: " + str(score)))

        canvas.delete("food")

        food = Food()
    else:
        del snake.coordinates[-1]
        canvas.delete(snake.squares[-1])
        del snake.squares[-1]

    if check_collisions(snake):
        game_over()
    else:
        window.after(speed, next_turn, snake, food)

def change_direction(new_direction):
    global direction

    if new_direction == "left":
        if direction != "right":
            direction = new_direction
            print("SNAKE IS GOING LEFT")
    elif new_direction == "right":
        if direction != "left":
            direction = new_direction
            print("SNAKE IS GOING RIGHT")
    elif new_direction == "up":
        if direction != "down":
            direction = new_direction
            print("SNAKE IS GOING UP")
    elif new_direction == "down":
        if direction != "up":
            direction = new_direction
            print("SNAKE IS GOING DOWN")

def check_collisions(snake):
    x, y = snake.coordinates[0]

    if x < 0 or x >= game_width:
        return True
    elif y < 0 or y >= game_height:
        return True
    
    for body_part in snake.coordinates[1:]:
        if x == body_part[0] and y == body_part[1]:
            return True
    
    return False

def kill_window():
    print()
    print("CLOSING WINDOW")
    window.destroy()

def game_over():
    print()
    print("GAME OVER")
    print("YOUR SCORE WAS " + str(score))
    canvas.delete(ALL)
    canvas.create_text(canvas.winfo_width()/2, canvas.winfo_height()/2, font=("Impact", 50,), text="GAME OVER", tag="gameover", fill="red")
    window.after(1000, kill_window)

window = Tk()
window.resizable(False, False)

score = 0
direction = "down"

label = Label(window, text=("SCORE: " + str(score)), font=("Impact", 25))
label.pack()

canvas = Canvas(window, bg=background_color, height=game_height, width=game_width)
canvas.pack()

window.update()

window.bind("<Left>", lambda event: change_direction("left"))
window.bind("<Right>", lambda event: change_direction("right"))
window.bind("<Up>", lambda event: change_direction("up"))
window.bind("<Down>", lambda event: change_direction("down"))

window.bind("<a>", lambda event: change_direction("left"))
window.bind("<d>", lambda event: change_direction("right"))
window.bind("<w>", lambda event: change_direction("up"))
window.bind("<s>", lambda event: change_direction("down"))

snake = Snake()
food = Food()

next_turn(snake, food)

window.mainloop()