import pygame
import random
import time
import mysql.connector
from numpy import character

pygame.font.init()

# Set up display
WIDTH, HEIGHT = 1000, 800
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flying Game")

# Load images
bg = pygame.transform.scale(pygame.image.load("background.jpeg"), (WIDTH, HEIGHT))
character_image = pygame.image.load("character.jpeg")
bell_image = pygame.image.load("bell.jpeg")
gift_image = pygame.image.load("gifts.jpeg")
bird_image = pygame.image.load("bird.jpeg")
blood_image = pygame.image.load("hat.jpeg")

# Player and object dimensions
PLAYER_WIDTH = 40
PLAYER_HEIGHT = 60
PLAYER_VEL = 5
OBJECT_VEL = 5

FONT = pygame.font.SysFont("Arial", 30)

# Initial game variables
score = 0
health = 5

# Database connection
def connect_to_db():
    connection = mysql.connector.connect(
        user="luoying",
        password="mypassword",
        host="localhost",
        port=3306,
        database="airport",
        autocommit=True,
        charset="utf8mb4",
        collation="utf8mb4_general_ci"
    )
    return connection

# Airport information retrieval
def get_airport_info(airport_codes):
    connection = connect_to_db()
    try:
        with connection.cursor() as cursor:
            sql = "SELECT ident, name, latitude_deg, longitude_deg FROM airport WHERE ident IN (%s)" % ','.join(['%s'] * len(airport_codes))
            cursor.execute(sql, airport_codes)
            results = cursor.fetchall()
            airport_info = {}
            for result in results:
                airport_info[result[0]] = {
                    "name": result[1],
                    "latitude": result[2],
                    "longitude": result[3]
                }
            return airport_info
    finally:
        connection.close()

def load_game_logo():
    win.blit(logo_image, (WIDTH // 2 - logo_image.get_width() // 2, HEIGHT // 2 - logo_image.get_height() // 2))
    pygame.display.update()
    time.sleep(2)

def draw_background(player, elapsed_time, gifts, birds):
    win.blit(bg, (0, 0))
    time_text = FONT.render(f"Time: {round(elapsed_time)}s", 1, "white")
    score_text = FONT.render(f"Score: {score}", 1, "white")
    health_text = FONT.render(f"Health: {health}", 1, "white")
    win.blit(time_text, (10, 10))
    win.blit(score_text, (10, 50))
    win.blit(health_text, (10, 90))
    pygame.draw.rect(win, "red", player)
    for gift in gifts:
        pygame.draw.rect(win, "green", gift)
    for bird in birds:
        pygame.draw.rect(win, "black", bird)
    pygame.display.update()

# Main function
def main():
    global score, health

    run = True
    player = pygame.Rect(200, HEIGHT - PLAYER_HEIGHT - 10, PLAYER_WIDTH, PLAYER_HEIGHT)

    clock = pygame.time.Clock()
    start_time = time.time()
    elapsed_time = 0

    gifts = []
    birds = []
    hit = False

    while run:
        elapsed_time = time.time() - start_time

        # Add gifts and birds periodically (similar logic as before)
        if random.randint(0, 100) < 5:  # Randomly spawn gifts
            gift_x = random.randint(0, WIDTH - 20)
            gifts.append(pygame.Rect(gift_x, -20, 20, 20))

        if random.randint(0, 100) < 3:  # Randomly spawn birds
            bird_x = random.randint(0, WIDTH - 50)
            birds.append(pygame.Rect(bird_x, -40, 50, 40))

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

        # Player movement
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player.x - PLAYER_VEL >= 0:
            player.x -= PLAYER_VEL