import sys
import os
import tkinter as tk
from tkinter import messagebox
from plyer import notification
import cairosvg

def convert_to_png(input_file, width, height):
    try:
        directory, filename = os.path.split(input_file)
        basename, _ = os.path.splitext(filename)
        output_file = os.path.join(directory, f"{basename}.png")

        cairosvg.svg2png(url=input_file, write_to=output_file, output_width=width, output_height=height)

        notification.notify(
            title="NoxConvertor",
            message=f"Converted {filename} to .png ({width}x{height}) successfully!",
            app_icon="C:\\Program Files\\NoxConvertor\\Assets\\icon.ico",
            timeout=1
        )
    
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred during conversion:\n{str(e)}")
        sys.exit(1)

def open_size_window(input_file):
    def submit_size():
        try:
            size_input = size_entry.get()
            width, height = map(int, size_input.lower().split('x'))
            if width > 0 and height > 0:
                convert_to_png(input_file, width, height)
                root.destroy()
            else:
                messagebox.showerror("Error", "Width and height must be positive integers.")
        except ValueError:
            messagebox.showerror("Error", "Invalid size format. Please enter in the format 'WIDTHxHEIGHT'.")
    
    root = tk.Tk()
    root.title("NoxConvertor - Specify Image Size")

    window_width = 300
    window_height = 150
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width // 2) - (window_width // 2)
    y = (screen_height // 2) - (window_height // 2)
    root.geometry(f'{window_width}x{window_height}+{x}+{y}')
    
    tk.Label(root, text="Enter Image Size (WIDTHxHEIGHT):").pack(pady=10)
    size_entry = tk.Entry(root, width=15)
    size_entry.pack(pady=5)
    size_entry.insert(0, "500x500")
    
    submit_button = tk.Button(root, text="Convert", command=submit_size)
    submit_button.pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    if len(sys.argv) > 1:
        input_file = sys.argv[1]
        if os.path.exists(input_file) and input_file.lower().endswith('.svg'):
            open_size_window(input_file)
        else:
            print("Please provide a valid SVG file for conversion.")
            sys.exit(1)
    else:
        print("No file provided for conversion.")
        sys.exit(1)
