
# MainScene
class MainScene(object):
    # Initialize Main Scene
    def __init__(self):
        # Initialize Modules
        pygame.init()
        # Initialize Clock
        self.clock = pygame.time.Clock()
        # Initialize Game Window
        self.scene = pygame.display.set_mode((SCENE_W, SCENE_H))
        # Set Window Title
        pygame.display.set_caption("Flying North")
        # Initialize Game Elements
        self.init_elements()
    # Initialize Game Elements
    def init_elements(self):
        # Initialize Game Map
        pass


    # Calculate Position
    def calc_position(self):
        pass
    # Draw Elements
    def draw_elements(self):
        pass
    # Handle Events
    def handle_events(self):
        pass
    # Collision Detection
    def detect_collision(self):
        pass


    # Main Loop
    def run(self):
        while True:
            # Collision Detection
            self.detect_conlision()
            # calculate the positions of game elements
            self.calc_position()
            # draw images of game elements
            self.draw_elements()
            # Handle Events
            self.handle_events()
            # refreshing the display
            pygame.display.update()
            # Controlling the frame rate
            self.clock.tick(60)


import pygame
import random

# Initialize Pygame
pygame.init()

# Set up display
WIDTH, HEIGHT = 800, 600
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flying North")

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Define player, gift, bell, and bird dimensions
PLAYER_WIDTH, PLAYER_HEIGHT = 50, 50
ITEM_WIDTH, ITEM_HEIGHT = 30, 30

# Load fonts
font = pygame.font.SysFont(None, 36)

# Game variables
player_x, player_y = WIDTH // 2, HEIGHT - PLAYER_HEIGHT - 10
player_speed = 5
score = 0
health = 5

# Create objects (gift, bell, bird)
gifts = [{'x': random.randint(0, WIDTH - ITEM_WIDTH), 'y': random.randint(0, HEIGHT // 2)} for _ in range(3)]
bells = [{'x': random.randint(0, WIDTH - ITEM_WIDTH), 'y': random.randint(0, HEIGHT // 2)} for _ in range(2)]
birds = [{'x': random.randint(0, WIDTH - ITEM_WIDTH), 'y': random.randint(0, HEIGHT // 2)} for _ in range(2)]

# Game Over flag
game_over = False

def draw_window():
    win.fill(WHITE)

    # Draw player
    pygame.draw.rect(win, BLACK, (player_x, player_y, PLAYER_WIDTH, PLAYER_HEIGHT))

    # Draw gifts
    for gift in gifts:
        pygame.draw.rect(win, (0, 255, 0), (gift['x'], gift['y'], ITEM_WIDTH, ITEM_HEIGHT))

    # Draw bells
    for bell in bells:
        pygame.draw.rect(win, (0, 0, 255), (bell['x'], bell['y'], ITEM_WIDTH, ITEM_HEIGHT))

    # Draw birds
    for bird in birds:
        pygame.draw.rect(win, RED, (bird['x'], bird['y'], ITEM_WIDTH, ITEM_HEIGHT))

    # Display score and health
    score_text = font.render(f"Score: {score}", True, BLACK)
    health_text = font.render(f"Health: {health}", True, BLACK)
    win.blit(score_text, (10, 10))
    win.blit(health_text, (10, 50))

    # If game over, display game over message
    if game_over:
        game_over_text = font.render("Game Over!", True, RED)
        win.blit(game_over_text, (WIDTH // 2 - 100, HEIGHT // 2))

    pygame.display.update()

def check_collision(player_x, player_y, item_x, item_y, width, height):
    """Check if player collides with an item."""
    return (player_x < item_x + width and
            player_x + PLAYER_WIDTH > item_x and
            player_y < item_y + height and
            player_y + PLAYER_HEIGHT > item_y)

def main():
    global player_x, player_y, score, health, game_over
    clock = pygame.time.Clock()
    running = True

    while running:
        clock.tick(30)  # Limit FPS to 30

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Handle player movement
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player_x - player_speed > 0:
            player_x -= player_speed
        if keys[pygame.K_RIGHT] and player_x + player_speed + PLAYER_WIDTH < WIDTH:
            player_x += player_speed
        if keys[pygame.K_UP] and player_y - player_speed > 0:
            player_y -= player_speed
        if keys[pygame.K_DOWN] and player_y + player_speed + PLAYER_HEIGHT < HEIGHT:
            player_y += player_speed

        # Check collisions with gifts and bells
        for gift in gifts[:]:
            if check_collision(player_x, player_y, gift['x'], gift['y'], ITEM_WIDTH, ITEM_HEIGHT):
                gifts.remove(gift)  # Remove the gift after collision
                score += 1  # Increment score

        for bell in bells[:]:
            if check_collision(player_x, player_y, bell['x'], bell['y'], ITEM_WIDTH, ITEM_HEIGHT):
                bells.remove(bell)  # Remove the bell after collision
                score += 1  # Increment score

        # Check collisions with birds
        for bird in birds[:]:
            if check_collision(player_x, player_y, bird['x'], bird['y'], ITEM_WIDTH, ITEM_HEIGHT):
                birds.remove(bird)  # Remove the bird after collision
                health -= 1  # Decrease health
                if health == 0:
                    game_over = True  # Trigger game over

        # Draw everything
        draw_window()

        # If game over, stop the game
        if game_over:
            pygame.time.delay(2000)  # Wait for 2 seconds
            running = False

    pygame.quit()

if __name__ == "__main__":
    main()


