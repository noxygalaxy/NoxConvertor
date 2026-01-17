@echo off
REM Install FFmpeg via winget
winget install -e --id Gyan.FFmpeg

REM Install Python packages
pip install plyer
pip install pillow
pip install ffmpeg-python
pip install cairosvg

echo.
echo Done. You can close this window now.
pause