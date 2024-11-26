import sys
import ffmpeg
import os
from plyer import notification

def convert_to_mp4(input_file):
    try:
        directory, filename = os.path.split(input_file)
        basename, _ = os.path.splitext(filename)
        output_file = os.path.join(directory, f"{basename}.mp4")
        
        ffmpeg.input(input_file).output(output_file).run()
        
        notification.notify(
            title="NoxConvertor",
            message=f"Converted to .mp4 Successfully!",
            app_icon="C:\\Program Files\\NoxConvertor\\Assets\\icon.ico",
            timeout=1
        )
    
    except ffmpeg.Error as e:
        print(f"An error occurred during conversion: {e.stderr.decode()}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        input_file = sys.argv[1]
        convert_to_mp4(input_file)
    else:
        print("No file provided for conversion.")
        sys.exit(1)
