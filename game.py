import pygame

class Game:

    def __init__(self, author, title, year, playerCount, thumbnail,
                 launchCode):
        self.author = author
        self.title = title
        self.year = year
        self.playerCount = playerCount
        self.thumbnail = pygame.image.load(thumbnail)
        self.launchCode = launchCode
