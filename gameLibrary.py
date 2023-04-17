import pygame
import subprocess
from gameFinder import find_games

pygame.init()

# Set up the window
screen_width = 1366
screen_height = 768
is_fullscreen = False  # added flag for fullscreen
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Community Arcade Table 6")

# Load the background image
background = pygame.image.load("background.png").convert()

# Load the games
games = find_games()

# Set up the grid
grid_width = 5
grid_height = 3
cell_size = 150
padding = 20
grid_x = (screen_width - (cell_size * grid_width + padding *
                          (grid_width - 1))) / 2
grid_y = (screen_height - (cell_size * grid_height + padding *
                           (grid_height - 1))) / 2 * 1.5

# Initialize the highlighted game
highlighted_game = 0

# Draw the games
clock = pygame.time.Clock()
done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                done = True
            elif event.key == pygame.K_RETURN:
                game = games[highlighted_game]
                subprocess.run(game.launchCode, shell=True)

            # Move the highlighted game
            elif event.key == pygame.K_UP:
                highlighted_game = max(0, highlighted_game - grid_width)
            elif event.key == pygame.K_DOWN:
                highlighted_game = min(
                    len(games) - 1, highlighted_game + grid_width)
            elif event.key == pygame.K_LEFT:
                highlighted_game = max(0, highlighted_game - 1)
            elif event.key == pygame.K_RIGHT:
                highlighted_game = min(len(games) - 1, highlighted_game + 1)

            # Toggle fullscreen
            elif event.key == pygame.K_f:
                is_fullscreen = not is_fullscreen
                if is_fullscreen:
                    screen = pygame.display.set_mode((screen_width, screen_height), pygame.FULLSCREEN)
                else:
                    screen = pygame.display.set_mode((screen_width, screen_height))

    # Draw the background
    background_x = (screen_width - background.get_width()) / 2
    screen.blit(background, (background_x, 0))

    # Draw the games
    for i, game in enumerate(games):
        x = i % grid_width
        y = i // grid_width
        rect = pygame.Rect(grid_x + x * (cell_size + padding),
                        grid_y + y * (cell_size + padding), cell_size,
                        cell_size)

        # Highlight the selected game
        if i == highlighted_game:
            # Calculate new rect for highlight
            highlight_size_increase = 10  # Increase in size of highlight
            new_rect = pygame.Rect(rect.x - highlight_size_increase,
                                rect.y - highlight_size_increase,
                                rect.width + 2 * highlight_size_increase,
                                rect.height + 2 * highlight_size_increase)
            pygame.draw.rect(screen, (255, 255, 0), new_rect, 5)

        thumbnail = pygame.transform.scale(game.thumbnail,
                                        (cell_size, cell_size))
        screen.blit(thumbnail, rect)


    # Draw the details of the highlighted game
    game = games[highlighted_game]
    font = pygame.font.SysFont("Arial", 24)
    title_text = font.render("Title: " + game.title, True, (255, 255, 255))
    author_text = font.render("Author: " + game.author, True, (255, 255, 255))
    year_text = font.render("Year: " + str(game.year), True, (255, 255, 255))
    year_text = font.render("Year: " + str(game.year), True, (255, 255, 255))
    player_count_text = font.render("Player count: " + str(game.playerCount),
                                    True, (255, 255, 255))
    screen.blit(title_text, (20, 20))
    screen.blit(author_text, (20, 50))
    screen.blit(year_text, (20, 80))
    screen.blit(player_count_text, (20, 110))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
