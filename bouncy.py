from tkinter import *

long_speed = 1
tall_speed = 1

def animate():
    global x_speed
    global y_speed
    coordinates = canvas.coords(ball)

    if coordinates[0] <= 0:
        x_speed = long_speed
    elif coordinates[2] >= 500:
        x_speed = -long_speed
    
    if coordinates[1] <= 0:
        y_speed = tall_speed
    elif coordinates[3] >= 500:
        y_speed = -tall_speed
    
    canvas.move(ball, x_speed, y_speed)
    window.after(10, animate)

def launch_settings():
    def get_boxes(*args):
        global long_speed
        global tall_speed

        long_speed = int(speed_entry.get())
        tall_speed = int(speed_entry2.get())
        canvas.itemconfig(ball, fill=color_entry.get())

        window2.destroy()

    window2 = Toplevel()

    settings_label = Label(window2, text="Configure x speed, y speed, and color of ball, must enter all at once, leave no blanks")
    settings_label.pack()

    speed_entry = Entry(window2)
    speed_entry.pack()

    speed_entry2 = Entry(window2)
    speed_entry2.pack()

    color_entry = Entry(window2)
    color_entry.pack()

    window2.bind("<Return>", get_boxes)
    window2.mainloop()

window = Tk()

canvas = Canvas(window, height=500, width=500, bg="white")
canvas.pack()

ball = canvas.create_oval(0,0,50,50,fill="black")

settings_button = Button(window, text="conifgure settings", command=launch_settings)
settings_button.pack()

animate()

window.mainloop()