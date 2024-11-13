import pygame


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
    # draw vertical lines
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
        pygame.init()
        mole_image = pygame.image.load("mole.png")
        screen = pygame.display.set_mode((640, 512))
        clock = pygame.time.Clock()
        running = True


        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            screen.fill("light green")
            draw_grid(screen)
            # You can draw the mole with this snippet:
            screen.blit(mole_image, mole_image.get_rect(topleft=(0, 0)))

            # if pygame.MOUSEBUTTONDOWN():
            #     x, y = event.pos
            #     if abs(event.pos[0] -

            pygame.display.flip()
            clock.tick(60)
    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
