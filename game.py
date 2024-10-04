import pygame
import random
import time

pygame.font.init()

# Set up display
WIDTH, HEIGHT = 1000, 800
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flying North")

# Load background image
bg = pygame.transform.scale(pygame.image.load("background.jpeg"), (WIDTH, HEIGHT))

# Player and object dimensions
PLAYER_WIDTH = 40
PLAYER_HEIGHT = 60
PLAYER_VEL = 5

GIFT_WIDTH = 20
GIFT_HEIGHT = 20
BIRD_WIDTH = 50
BIRD_HEIGHT = 40
OBJECT_VEL = 5

FONT = pygame.font.SysFont("Arial", 30)

# Initial game variables
score = 0
health = 5


def draw_background(player, elapsed_time, gifts, birds):
    win.blit(bg, (0, 0))

    # Display time, score, and health
    time_text = FONT.render(f"Time: {round(elapsed_time)}s", 1, "white")
    score_text = FONT.render(f"Score: {score}", 1, "white")
    health_text = FONT.render(f"Health: {health}", 1, "white")

    win.blit(time_text, (10, 10))
    win.blit(score_text, (10, 50))
    win.blit(health_text, (10, 90))

    # Draw player, gifts, and birds
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

    gift_add_increment = 2000  # Time interval for spawning gifts
    bird_add_increment = 3000  # Time interval for spawning birds
    gift_count = 0
    bird_count = 0

    gifts = []
    birds = []
    hit = False

    while run:
        gift_count += clock.tick(60)
        bird_count += gift_count  # Use the same clock ticks for birds
        elapsed_time = time.time() - start_time

        # Add gifts periodically
        if gift_count > gift_add_increment:
            for i in range(2):
                gift_x = random.randint(0, WIDTH - GIFT_WIDTH)
                gift = pygame.Rect(gift_x, -GIFT_HEIGHT, GIFT_WIDTH, GIFT_HEIGHT)
                gifts.append(gift)

            gift_add_increment = max(200, gift_add_increment - 50)
            gift_count = 0

        # Add birds periodically
        if bird_count > bird_add_increment:
            bird_x = random.randint(0, WIDTH - BIRD_WIDTH)
            bird = pygame.Rect(bird_x, -BIRD_HEIGHT, BIRD_WIDTH, BIRD_HEIGHT)
            birds.append(bird)

            bird_add_increment = max(1000, bird_add_increment - 50)
            bird_count = 0

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

        # Player movement
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player.x - PLAYER_VEL >= 0:
            player.x -= PLAYER_VEL
        if keys[pygame.K_RIGHT] and player.x + PLAYER_VEL + player.width <= WIDTH:
            player.x += PLAYER_VEL

        # Move gifts and birds
        for gift in gifts[:]:
            gift.y += OBJECT_VEL
            if gift.y > HEIGHT:
                gifts.remove(gift)
            elif gift.y + gift.height >= player.y and gift.colliderect(player):
                gifts.remove(gift)
                score += 1  # Gain 1 point for collecting a gift

        for bird in birds[:]:
            bird.y += OBJECT_VEL
            if bird.y > HEIGHT:
                birds.remove(bird)
            elif bird.y + bird.height >= player.y and bird.colliderect(player):
                birds.remove(bird)
                health -= 1  # Lose 1 health point when colliding with a bird
                if health <= 0:
                    hit = True
                    break

        if hit:
            lost_text = FONT.render("Game Over! You lost!", 5, "white")
            win.blit(lost_text, (WIDTH / 2 - lost_text.get_width() / 2, HEIGHT / 2 - lost_text.get_height() / 2))
            pygame.display.update()
            pygame.time.delay(5000)
            break

        draw_background(player, elapsed_time, gifts, birds)

    pygame.quit()


if __name__ == '__main__':
    main()
