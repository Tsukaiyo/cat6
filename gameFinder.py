import os
from game import Game

#In the code above, we've defined a find_games function that reads all the files in the gameFiles folder and creates a list of game objects. We're assuming that each game's information is stored in a separate text file with the author, title, year, player count, thumbnail file path, and launch code on separate lines.

#For each file that ends with .txt, we're opening the file, reading the game information, creating a Game object with the information, and appending it to the games list.


def find_games():
    game_files = os.listdir("gameFiles")
    games = []

    for file in game_files:
        if file.endswith(".game"):
            with open(os.path.join("gameFiles", file), "r") as f:
                game_info = f.readlines()
                author, title, year, playerCount, thumbnail, launchCode = game_info
                game = Game(author.strip(), title.strip(), year.strip(),
                            playerCount.strip(), thumbnail.strip(),
                            launchCode.strip())
                games.append(game)
                print(game.title)

    return games
