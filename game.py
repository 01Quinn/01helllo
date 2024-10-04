import pygame

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


