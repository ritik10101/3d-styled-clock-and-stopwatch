from tkinter import *
import time
import math

# Initialize the main window
root = Tk()
root.title("3D Styled Clock and Stopwatch")
root.geometry("800x600")
root.configure(bg="#a8dadc")  # Background color for the main window

# Stopwatch variables
running = False
counter = 0
is_24_hour_format = True  # Track the current clock format

# Update the display for the stopwatch
def update_display():
    minutes, seconds = divmod(counter, 60)
    hours, minutes = divmod(minutes, 60)
    display_time = f"{hours:02}:{minutes:02}:{seconds:02}"
    timer_label.config(text=display_time)

# Start the stopwatch
def start():
    global running
    if not running:
        running = True
        run_timer()

# Stop the stopwatch
def stop():
    global running
    running = False

# Reset the stopwatch
def reset():
    global counter, running
    running = False
    counter = 0
    update_display()

# Run the timer
def run_timer():
    global counter
    if running:
        counter += 1
        update_display()
        root.after(1000, run_timer)

# Update the clock display with 12/24-hour format toggle
def update_clock():
    if is_24_hour_format:
        current_time = time.strftime("%H:%M:%S")  # 24-hour format
    else:
        current_time = time.strftime("%I:%M:%S %p")  # 12-hour format with AM/PM

    clock_label.config(text=current_time)
    update_analog_clock()  # Update the analog clock
    root.after(1000, update_clock)

# Toggle between 12-hour and 24-hour format
def toggle_format():
    global is_24_hour_format
    is_24_hour_format = not is_24_hour_format
    format_button.config(text="24-Hour" if is_24_hour_format else "12-Hour")

# Draw and update the analog clock hands
def update_analog_clock():
    canvas.delete("hands")
    
    # Get the current time
    seconds = int(time.strftime("%S"))
    minutes = int(time.strftime("%M"))
    hours = int(time.strftime("%I"))
    
    # Calculate the angles for the hands
    sec_angle = math.radians(seconds * 6 - 90)
    min_angle = math.radians(minutes * 6 - 90)
    hour_angle = math.radians((hours % 12) * 30 + minutes * 0.5 - 90)
    
    # Calculate the hand positions
    sec_x, sec_y = 150 + 90 * math.cos(sec_angle), 150 + 90 * math.sin(sec_angle)
    min_x, min_y = 150 + 70 * math.cos(min_angle), 150 + 70 * math.sin(min_angle)
    hour_x, hour_y = 150 + 50 * math.cos(hour_angle), 150 + 50 * math.sin(hour_angle)
    
    # Draw the clock hands with colors and smooth second hand
    canvas.create_line(150, 150, sec_x, sec_y, fill="red", width=1, tags="hands")  # Second hand in red
    canvas.create_line(150, 150, min_x, min_y, fill="gold", width=3, tags="hands")  # Minute hand in gold
    canvas.create_line(150, 150, hour_x, hour_y, fill="gold", width=6, tags="hands")  # Hour hand in gold

# Gradient Background Frame
gradient_frame = Frame(root, bg="#a8dadc")
gradient_frame.place(relwidth=1, relheight=1)

# 3D clock frame with shadow effect
clock_frame = Frame(root, bg="#457b9d", bd=12, relief=RIDGE)
clock_frame.pack(pady=20, padx=20, fill=BOTH, expand=True)

# Label for "Stopwatch" with shadow
stopwatch_label = Label(clock_frame, text="Stopwatch", font=("Helvetica", 18, "bold"), bg="#457b9d", fg="white")
stopwatch_label.pack(pady=(10, 0))

# Display label for the stopwatch in 3D style with shadow effect
timer_label = Label(clock_frame, text="00:00:00", font=("Helvetica", 30, "bold"), bg="#1d3557", fg="white", relief=RIDGE, bd=6)
timer_label.pack(pady=(10, 20))

# Label for "Clock" with shadow
clock_text_label = Label(clock_frame, text="Clock", font=("Helvetica", 18, "bold"), bg="#457b9d", fg="white")
clock_text_label.pack(pady=(0, 5))

# Display label for the digital clock with shadow effect
clock_label = Label(clock_frame, text="", font=("Helvetica", 24, "italic bold"), bg="#1d3557", fg="white", relief=RIDGE, bd=6)
clock_label.pack(pady=(0, 20))

# Canvas for the analog clock with green circular background and blue outline
canvas = Canvas(clock_frame, width=300, height=300, highlightthickness=0, bg="#457b9d")
canvas.pack(pady=10)

# Draw the circular green clock face with gold border
canvas.create_oval(50, 50, 250, 250, outline="gold", width=4, fill="green")  # Green face with gold outline

# Draw hour markers in gold and smaller minute markers in light gold
for i in range(60):
    angle = math.radians(i * 6 - 90)
    x_start, y_start = 150 + 95 * math.cos(angle), 150 + 95 * math.sin(angle)
    if i % 5 == 0:  # Hour markers
        x_end, y_end = 150 + 100 * math.cos(angle), 150 + 100 * math.sin(angle)
        canvas.create_line(x_start, y_start, x_end, y_end, fill="gold", width=3, tags="markers")
    else:  # Minute markers
        x_end, y_end = 150 + 100 * math.cos(angle), 150 + 100 * math.sin(angle)
        canvas.create_line(x_start, y_start, x_end, y_end, fill="#d4af37", width=1, tags="markers")

# Toggle format button with vibrant styling and shadow effect
format_button = Button(clock_frame, text="24-Hour", command=toggle_format, font=("Helvetica", 14, "bold"), width=10, bg="#e63946", fg="white", relief=RAISED, bd=6, activebackground="#ff7f50")
format_button.pack(pady=5)

# Button frame inside the 3D frame
button_frame = Frame(clock_frame, bg="#a8dadc")
button_frame.pack(pady=10)

# Buttons for stopwatch control with updated styling and shadow effect
start_button = Button(button_frame, text="Start", command=start, font=("Helvetica", 14, "bold"), width=8, bg="#2a9d8f", fg="white", relief=RAISED, bd=6, activebackground="#00b894")
start_button.grid(row=0, column=0, padx=5)

stop_button = Button(button_frame, text="Stop", command=stop, font=("Helvetica", 14, "bold"), width=8, bg="#2a9d8f", fg="white", relief=RAISED, bd=6, activebackground="#00b894")
stop_button.grid(row=0, column=1, padx=5)

reset_button = Button(button_frame, text="Reset", command=reset, font=("Helvetica", 14, "bold"), width=8, bg="#2a9d8f", fg="white", relief=RAISED, bd=6, activebackground="#00b894")
reset_button.grid(row=0, column=2, padx=5)

# Start the clock and stopwatch
update_clock()
root.mainloop()
