import os
import subprocess

# Start gameLibrary.py in a subprocess
os.environ['SDL_VIDEO_WINDOW_POS'] = f"{0}, {0}"
game_process = subprocess.Popen(["python", "gameLibrary.py"])

# Start highscoreChecker.py in a subprocess
highscore_checker_process = subprocess.Popen(["python", "highscoreChecker.py"])

# Start highscoreDisplay.py in a subprocess
os.environ['SDL_VIDEO_WINDOW_POS'] = f"{1920}, {0}"
highscore_process = subprocess.Popen(["python", "highscoreDisplay.py"])

# Wait for the game subprocess to finish
game_process.wait()

# Terminate the other subprocesses
highscore_checker_process.terminate()
highscore_process.terminate()
