import os
import pygame
import time
import ctypes

pygame.init()

# Set up the window
screen_width = 640
screen_height = 600

# Load font
font = pygame.font.SysFont("Arial", 32)


# Initialize timer and card swipe input


class Data:
    def __init__(self):
        self.start_time = time.time()
        self.card_swipe = ""
        self.card_swiped = False
        self.windowOpen = False
        self.filename = ""
        self.attempts = 0
        self.validOneCard = False

    def refresh(self):
        self.card_swipe = ""
        self.card_swiped = False
        self.windowOpen = False
        self.filename = ""
        self.attempts = 0
        self.validOneCard = False


def getFiles():
    # Check for high score files
    high_score_files = []
    for filename in os.listdir("gameFiles"):
        if "AllHighscores.txt" in filename:
            high_score_files.append(filename)
    return high_score_files


def get_last_line(file_path):
    with open(file_path, 'rb') as file:
        # Seek to end of file
        file.seek(-2, os.SEEK_END)
        # Loop backwards until new line is found
        while file.read(1) != b'\n':
            file.seek(-2, os.SEEK_CUR)
        # Return last line
        return file.readline().decode().strip()


def centreText(words, size, colour, y):
    # create centred text
    myfont = pygame.font.SysFont('impact', size)
    textA = myfont.render(words, False, colour)
    text_rect = textA.get_rect(center=(screen_width / 2, y))
    screen.blit(textA, text_rect)

def getFiles():
    # Check for high score files
    high_score_files = []
    for root, dirs, files in os.walk("gameFiles"):
        for filename in files:
            if "AllHighscores.txt" in filename:
                high_score_files.append(os.path.join(root, filename))
    return high_score_files

def draw():
    # Load background
    background = pygame.image.load("checkerBackground.png")
    screen.blit(background, (0, 0))
    centreText("Please swipe your OneCard", 40, (255, 255, 255), 50)
    centreText("The highest score for the Game of the Month", 25, (255, 255, 255), 100)
    centreText("with an associated OneCard wins a prize", 25, (255, 255, 255), 140)
    input_box = pygame.Rect(0, 0, 300, 50)
    input_box.center = (screen_width // 2, screen_height // 2)
    input_text = font.render(data.card_swipe, True, (0, 0, 0))
    text_rect = input_text.get_rect()
    text_rect.center = input_box.center
    screen.fill((255, 255, 255), input_box)
    pygame.draw.rect(screen, (0, 0, 0), input_box, 2)
    screen.blit(input_text, text_rect)
    if data.attempts > 0:
        centreText("Invalid OneCard, please try again", 32, (255, 0, 0), 500)
    timeRemaining = data.start_time + 60 - time.time()
    centreText("To skip, wait for timeout", 32, (255, 255, 255), 400)
    centreText(str(int(timeRemaining)), 24, (255, 255, 255), 450)
    pygame.display.flip()


def acceptOneCard():
    print("OneCard accepted")
    # Read last line of high score file
    with open("gameFiles/" + filename, "r") as f:
        lines = f.readlines()
        new_high_score = lines[-1].strip()
    # Add new high score and OneCard number to student high score file
    student_high_score_file = filename.replace("AllHighscores", "StudentHighscores")
    with open(f"gameFiles/{student_high_score_file}", "a") as f:
        f.write(new_high_score + " : " + data.card_swipe + "\n")


def rejectOneCard():
    print("Invalid OneCard")
    data.attempts = data.attempts + 1
    data.card_swipe = ""


def close():
    data.start_time = time.time()
    pygame.display.quit()
    data.refresh()


# Check high score files for changes
data = Data()

while True:
    data.refresh()
    high_score_files = getFiles()
    for filename in high_score_files:
        last_modified = os.path.getmtime(filename)
        if last_modified > data.start_time:
            # Open window
            if not data.windowOpen:
                screen = pygame.display.set_mode((screen_width, screen_height), pygame.NOFRAME)
                pygame.display.set_caption("High Score Checker")
                data.windowOpen = True
                pygame.event.set_grab(True)
                # Bring the Pygame window to the foreground (Windows-specific)
                hwnd = pygame.display.get_wm_info()["window"]
                ctypes.windll.user32.SetForegroundWindow(hwnd)
            # Update start time
            data.start_time = last_modified

            data.card_swiped = False
            while data.attempts < 3 and not data.validOneCard:

                # Wait for OneCard swipe or timeout
                waiting = True
                while waiting:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
                            quit()
                        elif event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_RETURN and data.card_swipe != "":
                                data.card_swiped = True
                                waiting = False
                                break
                            elif event.key == pygame.K_BACKSPACE:
                                data.card_swipe = data.card_swipe[:-1]
                            else:
                                data.card_swipe += event.unicode
                    draw()
                    # Timeout after 60 seconds
                    timeRemaining = data.start_time + 60 - time.time()
                    if timeRemaining <= 0:
                        print("Timed out")
                        pygame.display.quit()
                        close()
                        waiting = False
                        break

                # Check OneCard input    
                if data.card_swiped:
                    print(data.card_swipe)
                    if len(data.card_swipe.strip()) == 10 and data.card_swipe.startswith(
                            "50") and data.card_swipe.isnumeric():
                        data.validOneCard = True
                        acceptOneCard()
                    else:
                        rejectOneCard()

            close()

    time.sleep(1)
