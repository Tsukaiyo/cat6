from gameStates import *
from style import colours
import pygame
from maze import Maze

pygame.init


class GameData(object):
    infoObject = pygame.display.Info()
    width = infoObject.current_w
    height = infoObject.current_h
    currentState = MainMenu
    rockets = []
    team = False
    players = 0
    speed = 5
    winner = 0
    maze = None
    mazeMode = False
    startTime = 0
    mazeHeight = 8
    mazeWidth = 12
    points = 0
    lives = 5
    finalTime = 0

    def __init__(self):
        self.team = False
        self.maze = False
        self.currentState = MainMenu
        self.players = 0
        self.keys = 0
        self.startTime = 0
        self.speed = 5
        self.width = pygame.display.Info().current_w
        self.height = pygame.display.Info().current_h
        self.rockets = []
        self.winner = 0

    def generateRockets(self):
        # Creates rocket objects
        speed = 5
        del self.rockets[:]
        if not self.team:
            self.rockets.append(Rocket(colours["purple"], 1, self.width * 0.25, self.height * 0.25, self.speed, self.width, self.height))
            self.rockets.append(Rocket(colours["teal"], 2, self.width * 0.5, self.height * 0.25,  self.speed, self.width, self.height))
            if self.players >= 3:
                self.rockets.append(Rocket(colours["green"], 3,  self.width * 0.4, self.height * 0.75,  self.speed, self.width, self.height))
            if self.players == 4:
                self.rockets.append(Rocket(colours["pink"], 4, self.width * 0.5, self.height * 0.75,  self.speed, self.width, self.height))
        else:
            self.rockets.append(Rocket(team_colours["green1"], 1, self.width * 0.25, self.height * 0.25,  self.speed, self.width, self.height))
            self.rockets.append(Rocket(team_colours["green2"], 2, self.width * 0.5, self.height * 0.25,  self.speed, self.width, self.height))
            self.rockets.append(Rocket(team_colours["red1"], 3, self.width * 0.25, self.height * 0.75,  self.speed, self.width, self.height))
            self.rockets.append(Rocket(team_colours["red2"], 4, self.width * 0.5, self.height * 0.75,  self.speed, self.width, self.height))

    def genMazeRockets(self):
        self.speed = 3
        #self.bloops.append(Bloop(int((x + 0.5) * screenwidth / self.width),
        #                         int((y + 1.5) * screenheight / self.height)))

        #In 10x10, rockets should be in [3,3], [7,7], [3,7], and [7,3]
        #screenwidth = 1280
        #screenheight = 800
        #In 12x8 grid, widths: (int(12*0.3)+0.5)*1280/12, (int(12*0.7)+0.5)*1280/12     heights:
        x1 = (int(self.mazeWidth*0.3)-1) * self.width / self.mazeWidth
        y1 = (int(self.mazeHeight*0.3)+0.2) * self.height / self.mazeHeight
        x2 = (int(self.mazeWidth*0.7)-0.4) * self.width / self.mazeWidth
        y2 = (int(self.mazeHeight*0.7)+0.7) * self.height / self.mazeHeight
        row1 = 0.3 * self.width
        row2 = 0.7 * self.width
        column1 = 0.3 * self.height
        column2 = 0.7 * self.height

        del self.rockets[:]
        self.rockets.append(Rocket(colours["purple"], 1, x1, y1, self.speed, self.width, self.height))
        self.rockets.append(Rocket(colours["teal"], 2, x2, y1, self.speed, self.width, self.height))
        if self.players >= 3:
            self.rockets.append(Rocket(colours["green"], 3, x1, y2, self.speed, self.width, self.height))
        if self.players == 4:
            self.rockets.append(Rocket(colours["pink"], 4, x2, y2, self.speed, self.width,self.height))

    def clear(self):
        self.team = False
        self.mazeMode = False
        self.players = 0
        self.keys = 0
        self.startTime = 0
        self.rockets = []
        self.points = 0
        self.lives = 5

    def refresh(self):
        self.startTime = 0
        self.rockets = []
        self.points = 0
        self.lives = 5

    def changeState(self, newState):
        # For any changes that need to be made once when changing states
        if newState == MainMenu:
            self.clear(self)
            self.currentState = MainMenu
        if newState == Instructions:
            self.currentState = Instructions
        if newState == ViewHighScores:
            self.currentState = ViewHighScores
        if newState == ToggleMaze:
            self.currentState = ToggleMaze
        if newState == ToggleTeam:
            self.currentState = ToggleTeam
        if newState == Play:
            self.refresh(self)
            self.generateRockets(self)
            self.currentState = Play
        if newState == PlayMaze:
            self.refresh(self)
            self.genMazeRockets(self)
            self.maze = Maze(self.mazeHeight, self.mazeWidth)
            self.maze.genGrid()
            self.maze.makeMaze()
            self.maze.makeBloops()
            self.startTime = time.time()
            self.currentState = PlayMaze
        if newState == End:
            self.currentState = End
        if newState == EndMaze:
            self.finalTime = time.time() - self.startTime
            self.currentState = EndMaze
            self.currentState.name = ""

        self.currentState.selection = 0
