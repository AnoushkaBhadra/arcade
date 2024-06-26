

import pygame as pg
from random import randrange

def run_snake_game():
    # Constants
    WINDOW = 750
    TILE_SIZE = 35
    RANGE = (TILE_SIZE // 2, WINDOW - TILE_SIZE // 2, TILE_SIZE)
    get_random_position = lambda: (randrange(*RANGE), randrange(*RANGE))

    # Initializing Pygame
    pg.init()

    # Fonts
    font = pg.font.SysFont('Arial', 30)
    score_font = pg.font.SysFont('Arial', 40)

    # Set up
    snake = pg.Rect(0, 0, TILE_SIZE - 2, TILE_SIZE - 2)
    snake.center = get_random_position()
    length = 1
    segments = [snake.copy()]
    snake_dir = (0, 0)
    time, time_step = 0, 110
    food = snake.copy()
    food.center = get_random_position()
    score = 0

    # Colors
    bg_color = (173, 216, 153)
    snake_color = (51, 115, 87)
    food_color = (238, 66, 102)
    score_color = (240, 117, 170)

    # Screen set up
    screen = pg.display.set_mode([WINDOW] * 2)
    clock = pg.time.Clock()
    dirs = {pg.K_w: 1, pg.K_s: 1, pg.K_a: 1, pg.K_d: 1}

    # Game states
    running = True
    game_active = False

    def draw_text(text, font, color, surface, x, y):
        textobj = font.render(text, True, color)
        textrect = textobj.get_rect()
        textrect.topleft = (x, y)
        surface.blit(textobj, textrect)

    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_RETURN and not game_active:
                    game_active = True
                    score = 0
                if game_active:
                    if event.key == pg.K_w and dirs[pg.K_w]:
                        snake_dir = (0, -TILE_SIZE)
                        dirs = {pg.K_w: 1, pg.K_s: 0, pg.K_a: 1, pg.K_d: 1}
                    if event.key == pg.K_s and dirs[pg.K_s]:
                        snake_dir = (0, TILE_SIZE)
                        dirs = {pg.K_w: 0, pg.K_s: 1, pg.K_a: 1, pg.K_d: 1}
                    if event.key == pg.K_a and dirs[pg.K_a]:
                        snake_dir = (-TILE_SIZE, 0)
                        dirs = {pg.K_w: 1, pg.K_s: 1, pg.K_a: 1, pg.K_d: 0}
                    if event.key == pg.K_d and dirs[pg.K_d]:
                        snake_dir = (TILE_SIZE, 0)
                        dirs = {pg.K_w: 1, pg.K_s: 1, pg.K_a: 0, pg.K_d: 1}
                if event.key == pg.K_r and not game_active:
                    game_active = True
                    snake.center = get_random_position()
                    food.center = get_random_position()
                    length = 1
                    snake_dir = (0, 0)
                    segments = [snake.copy()]

        if game_active:
            screen.fill(bg_color)

            # Check for borders and self-eating:
            self_eating = pg.Rect.collidelist(snake, segments[:-1]) != -1
            if snake.left < 0 or snake.right > WINDOW or snake.top < 0 or snake.bottom > WINDOW or self_eating:
                game_active = False

            # Check for food
            if snake.center == food.center:
                food.center = get_random_position()
                length += 1
                score += 1

            # Draw food
            pg.draw.rect(screen, food_color, food)

            # Draw snake
            [pg.draw.rect(screen, snake_color, segment) for segment in segments]

            time_now = pg.time.get_ticks()
            if time_now - time > time_step:
                time = time_now
                snake.move_ip(snake_dir)
                segments.append(snake.copy())
                segments = segments[-length:]

            # Draw score
            draw_text(f'Score: {score}', score_font, score_color, screen, 10, 10)

        else:
            screen.fill(bg_color)
            draw_text('Press Enter to Start', font, snake_color, screen, WINDOW // 4, WINDOW // 3)
            draw_text(f'Your Score: {score}', font, score_color, screen, WINDOW // 4, WINDOW // 2)
            draw_text('Press R to Restart', font, snake_color, screen, WINDOW // 4, WINDOW // 1.5)
            draw_text('Move Up: W', font, snake_color, screen, WINDOW // 4, WINDOW // 1.3)
            draw_text('Move Down: S', font, snake_color, screen, WINDOW // 4, WINDOW // 1.25)
            draw_text('Move Left: A', font, snake_color, screen, WINDOW // 4, WINDOW // 1.185)
            draw_text('Move Right: D', font, snake_color, screen, WINDOW // 4, WINDOW // 1.1)

        pg.display.flip()
        clock.tick(60)

    pg.quit()

if __name__ == '__main__':
    run_snake_game()
