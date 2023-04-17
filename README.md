# cat6
Community Arcade Table 6

Consists of a game launcher and high score system. 

To add a new game:
Create a .game file in the gameFiles folder. This can be done by making a text file, then changing the extension from .txt to .game
The contents of the .game file should be exactly 6 lines, in this format:
Author
Title
Year published
Players
Thumbnail image location
launch code

Student high score tracking:
Currently, CAT6 is set up to check for TMU student numbers (10 digits, starts with "50"). 
This check is on this line of highscoreChecker.py:
if len(card_swipe.strip()) == 10 and card_swipe.startswith("50") and card_swipe.isnumeric():

To set up a game for student high score tracking:
The game must write scores to a file with a name containing "AllHighscores.txt", such as "tracerHighscores.txt".
The scores must be written chronologically, as the checker associates the student number with the LAST line of the AllHighscores file.
If a valid student card ("OneCard") is swiped, the new score and associated student number will be written to a file with the same name as the AllHighscores.txt file,
but with "All" replaced with "Student". 

To disable student high score tracking:
In main.py, remove or comment out this line: highscore_checker_process = subprocess.Popen(["python", "highscoreChecker.py"])