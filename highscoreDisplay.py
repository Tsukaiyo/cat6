#Currently just displays high scores for Tracer
import pygame

pygame.init()

# Colours
BLUE = (10, 20, 50)
TEAL = (69, 240, 233)
PURPLE = (138, 28, 124)
GREEN = (127, 231, 105)
PINK = (218, 65, 103)
WHITE = (255, 255, 255)
YELLOW = (237, 237, 63)
GREEN1 = (82, 220, 145)
GREEN2 = (171, 209, 45)
RED1 = (242, 84, 91)
RED2 = (211, 30, 85)

Height = 800
Width = 800
size = [Height, Width]
screen = pygame.display.set_mode(size)
pygame.display.set_caption("High Scores")
done = False

def centreText(words, size, colour, y):
    #create centred text
    myfont = pygame.font.SysFont('impact', size)
    textA = myfont.render(words, False, colour)
    text_rect = textA.get_rect(center=(800/ 2, y))
    screen.blit(textA, text_rect)
    
def text(words, font, size, colour, x, y):
    # create text
    myfont = pygame.font.SysFont(font, size)
    textA = myfont.render(words, False, colour)
    screen.blit(textA, (x, y))

def printHighScores():
    #Write out the top 7 scores to the screen
    f = open("gameFiles/Scoreboard.txt", "a+")
    with open("gameFiles/Scoreboard.txt", "r") as file1:
        f_list = [str(i) for line in file1 for i in line.split('\n') if i.strip()]
    # seperate out scores and times
    gameData = []
    scores = []
    times = []
    names = []
    colour = 0
    for i in range(len(f_list)):
        gameData.append(f_list[i].split(","))
    for i in range(len(gameData)):
        scores.append(int(gameData[i][0]))
        times.append(float(gameData[i][1]))
        names.append(gameData[i][2])
    numScores = min(len(scores), 7)
    for i in range(numScores):
        mins = int(times[i]/60)
        secs = int(times[i]%60)
        secs = str(secs)
        while len(secs) < 2:
            secs = "0" + secs
        txt = str(i+1) + ". " + names[i] + ": "+ str(scores[i]) + " Pts, " + str(mins) + ":" + str(secs)
        if i == 0:
            colour = RED2
        if i == 1:
            colour = RED1
        if i == 2:
            colour = YELLOW
        if i == 3:
            colour = GREEN
        if i == 4:
            colour = GREEN1
        if i == 5:
            colour = TEAL
        if i == 6:
            colour = PURPLE

        centreText(txt, 50, colour, (i*70)+ 250)
        
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            
    screen.fill(BLUE)
    text(" TRACER HIGH SCORES", 'impact', 80, PURPLE, 100, 75)
    text("TRACER HIGH SCORES", 'impact', 80, TEAL, 105, 80)
    printHighScores()
    pygame.display.flip()
    
pygame.quit()