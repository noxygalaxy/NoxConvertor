import sys
import tkinter as tk
import os
from PIL import Image
from plyer import notification

def convert_to_jpg(input_file, quality=85):
    try:
        with Image.open(input_file) as img:
            directory, filename = os.path.split(input_file)
            basename, _ = os.path.splitext(filename)
            output_file = os.path.join(directory, f"{basename}.jpg")
            
            if img.mode in ('RGBA', 'LA'):
                background = Image.new('RGB', img.size, (255, 255, 255))
                background.paste(img, mask=img.split()[-1])
                img = background
            
            img.save(
                output_file, 
                'JPEG', 
                quality=quality,
                optimize=True,
                progressive=True
            )
        
        notification.notify(
            title="NoxConvertor",
            message=f"Converted to .jpg Successfully!\nQuality: {quality}",
            app_icon="C:\\Program Files\\NoxConvertor\\Assets\\icon.ico",
            timeout=1
        )
    
    except Exception as e:
        print(f"An error occurred during conversion: {str(e)}")
        sys.exit(1)

def open_compression_window(input_file):
    def submit_compression():
        try:
            quality = int(quality_entry.get())
            if 1 <= quality <= 95:
                convert_to_jpg(input_file, quality)
                root.destroy()
            else:
                tk.messagebox.showerror("Error", "Quality must be between 1-95")
        except ValueError:
            tk.messagebox.showerror("Error", "Please enter a valid number")

    root = tk.Tk()
    root.title("NoxConvertor - Image Quality")
    
    window_width = 300
    window_height = 150
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width // 2) - (window_width // 2)
    y = (screen_height // 2) - (window_height // 2)
    root.geometry(f'{window_width}x{window_height}+{x}+{y}')

    tk.Label(root, text="Enter JPEG Quality Level (1-95):").pack(pady=10)
    quality_entry = tk.Entry(root, width=10)
    quality_entry.pack(pady=5)
    quality_entry.insert(0, "85")

    submit_button = tk.Button(root, text="Convert", command=submit_compression)
    submit_button.pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    if len(sys.argv) > 1:
        input_file = sys.argv[1]
        open_compression_window(input_file)
    else:
        print("No file provided for conversion.")
        sys.exit(1)