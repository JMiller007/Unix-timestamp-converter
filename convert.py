import tkinter as tk
from tkinter import messagebox
import datetime

def convert_timestamp():
    hex_timestamp = entry.get()
    try:
        # Convert hex to decimal (Unix timestamp)
        unix_timestamp = int(hex_timestamp, 16)
        
        # Convert Unix timestamp to a human-readable date
        human_readable_date = datetime.datetime.utcfromtimestamp(unix_timestamp)
        
        # Display the result in a message box
        messagebox.showinfo("Result", f"The compilation date is: {human_readable_date} (UTC)")
    except ValueError:
        messagebox.showerror("Error", "Invalid hexadecimal value. Please enter a valid hex timestamp.")

# Create the main window
root = tk.Tk()
root.title("Hexadecimal Timestamp Converter")

# Create and place the label
label = tk.Label(root, text="Enter Hexadecimal TimeDateStamp:")
label.pack(pady=10)

# Create and place the entry box
entry = tk.Entry(root, width=30)
entry.pack(pady=10)

# Create and place the Convert button
convert_button = tk.Button(root, text="Convert", command=convert_timestamp)
convert_button.pack(pady=10)

# Run the main loop
root.mainloop()
