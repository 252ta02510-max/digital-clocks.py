# Digital Clock using Python

import tkinter as tk
import time


# Create window
window = tk.Tk()

window.title("Digital Clock")
window.geometry("500x200")

window.configure(bg="black")


# Clock label
clock = tk.Label(
    window,
    font=("Arial", 50, "bold"),
    bg="black",
    fg="lime"
)

clock.pack(expand=True)


# Function to update time
def update_clock():

    current_time = time.strftime("%H:%M:%S")

    clock.config(text=current_time)

    window.after(1000, update_clock)


# Start clock
update_clock()


# Run application
window.mainloop()
