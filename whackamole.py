### Jarrod Cruz
### Nov 13, 2024
### COP3502C 12152
### Lab 10

import pygame
import random


def draw_grid(screen):
    # draw vertical lines
    for i in range(1, 20):
        pygame.draw.line(
            screen,
            "dark green",
            (i*32, 0),
            (i*32, 512),
            1
        )
    # draw horizontal lines
    for i in range(1, 20):
        pygame.draw.line(
            screen,
            "dark green",
            (0, i * 32),
            (640, i * 32),
            1
        )



def main():
    try:
        # Initialize pygame, graphics, and mole
        pygame.init()
        mole_image = pygame.image.load("mole.png")
        screen = pygame.display.set_mode((640, 512))
        clock = pygame.time.Clock()
        running = True
        mole_pos = (0, 0)

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                # If mouse clicks on mole (calculated by if click position
                # matches mole position when both integer-divided by the grid size 32)...
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.pos[0] // 32 == (mole_pos[0]//32) and event.pos[1] // 32 == (mole_pos[1]//32):

                        # Randomly generate new mole position and print mole
                        mole_pos = (random.randrange(0, 20)*32, random.randrange(0, 16)*32)
                        screen.blit(mole_image, mole_image.get_rect(topleft=mole_pos))

            # Sets up graphics and first mole placement
            screen.fill("light green")
            draw_grid(screen)
            screen.blit(mole_image, mole_image.get_rect(topleft=mole_pos))
            pygame.display.flip()
            clock.tick(60)

    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
