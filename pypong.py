import pygame
import random


pygame.init()

WIDTH = 800
HEIGHT = 500
window = pygame.display.set_mode((WIDTH, HEIGHT))

TITLE = "Pong"
pygame.display.set_caption(TITLE)

# COLORS
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)

# FONTS
small_font = pygame.font.SysFont("courier", 20)
large_font = pygame.font.SysFont("courier", 60, True)


class Paddle:
    def __init__(self, x, y, width, height, vel, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = vel
        self.color = color

    def draw(self, window):
        pygame.draw.rect(window, self.color, (self.x, self.y, self.width, self.height), 0)

class Ball:
    def __init__(self, x, y, side, vel, color):
        self.x = x
        self.y = y
        self.side = side
        self.vel = vel
        self.color = color
        self.lower_right = False
        self.lower_left = True
        self.upper_right = False
        self.upper_left = False
        self.ball_bag = []
        self.last_movement = 'ball.lower_right'

    def draw(self, window):
        pygame.draw.rect(window, self.color, (self.x, self.y, self.side, self.side), 0)

    def move_lower_right(self):
        self.x += self.vel
        self.y += self.vel
    def move_upper_right(self):
        self.x += self.vel
        self.y -= self.vel

    def move_upper_left(self):
        self.x -= self.vel
        self.y -= self.vel

    def move_lower_left(self):
        self.x -= self.vel
        self.y += self.vel

    def start(self):
        self.lower_right = True
        self.lower_left = False
        self.upper_right = False
        self.upper_left = False

        self.last_movement = 'ball.lower_left'
def main():
    run = True
    fps = 60
    clock = pygame.time.Clock()

    # Initializing Paddles

    left_paddle = Paddle(20, 100, 10, 50, 5, white)
    right_paddle = Paddle(770, 350, 10, 50, 5, white)

    balls = []

    def redraw_window():
        window.fill(black)

        left_paddle.draw(window)
        right_paddle.draw(window)
        for ball in balls:
            ball.draw(window)

        player_A_text = small_font.render("Player A: " + str(score_A), 1, white)
        player_B_text = small_font.render("Player B: " + str(score_B), 1, white)
        window.blit(player_A_text, (320 - int(player_A_text.get_width() / 2), 10))
        window.blit(player_B_text, (480 - int(player_B_text.get_width() / 2), 10))

        pygame.draw.rect(window, white, (20, 450, 760, 1), 0)
        pygame.draw.rect(window, white, (20, 49, 760, 1), 0)
        pygame.draw.rect(window, white, (19, 50, 1, 400), 0)
        pygame.draw.rect(window, white, (780, 50, 1, 400), 0)
        
        pygame.display.update()
        
    while run:
        score_A = 0
        score_B = 0
        clock.tick(fps)

        if len(balls) == 0:
            ball = Ball(random.randrange(320, 465), random.randrange(200, 285), 15, 3, white)
            balls.append(ball)
        if ball.lower_left:
            ball.move_lower_left()

            if ball.last_movement == 'ball.lower_right':
                if ball.y + ball.side > HEIGHT - 50:
                    ball.lower_left = False
                    ball.last_movement = 'ball.lower_left'
                    ball.upper_left = True

            if ball.last_movement == 'ball.upper_left':
                if ball.x < 30:
                    if left_paddle.x < ball.x < left_paddle.x + left_paddle.width:
                        if left_paddle.y < ball.y + ball.side < left_paddle.y + left_paddle.height:
                            ball.lower_left = False
                            ball.last_movement = 'ball.lower_left'
                            ball.lower_right = True
                    else:
                        score_B += 1
                        balls.remove(ball)
                        #ball.start()
                
                if ball.y + ball.side > HEIGHT - 50:
                    ball.lower_left = False
                    ball.last_movement = 'ball.lower_left'
                    ball.upper_left = True
        if ball.upper_left:
            ball.move_upper_left()

            if ball.last_movement == 'ball.lower_left':
                if ball.x < 30:
                    if left_paddle.x < ball.x < left_paddle.x + left_paddle.width:
                        if left_paddle.y < ball.y + ball.side < left_paddle.y + left_paddle.height:
                            ball.upper_left = False
                            ball.last_movement = 'ball.upper_left'
                            ball.upper_right = True
                    else:
                        score_B += 1
                        balls.remove(ball)
                        #ball.start()

                if ball.y < 50:
                    ball.upper_left = False
                    ball.last_movement = 'ball.upper_left'
                    ball.lower_left = True

            if ball.last_movement == 'ball.upper_right':
                if ball.y < 50:
                    ball.upper_left = False
                    ball.last_movement = 'ball.upper_left'
                    ball.lower_left = True

        if ball.upper_right:
            ball.move_upper_right()

            if ball.last_movement == 'ball.upper_left':
                if ball.y < 50:
                    ball.upper_right = False
                    ball.last_movement = 'ball.upper_right'
                    ball.lower_right = True

            if ball.last_movement == 'ball.lower_right':
                if ball.x + ball.side > WIDTH - 30:
                    if right_paddle.x + right_paddle.width > ball.x + ball.side > right_paddle.x:
                        if right_paddle.y < ball.y + ball.side < right_paddle.y + right_paddle.height:
                            ball.upper_right = False
                            ball.last_movement = 'ball.upper_right'
                            ball.upper_left = True
                    else:
                        score_A += 1
                        balls.remove(ball)
                        #ball.start()

                if ball.y < 50:
                    ball.upper_right = False
                    ball.last_movement = 'ball.upper_right'
                    ball.lower_right = True

        if ball.lower_right:
            ball.move_lower_right()

            if ball.last_movement == 'ball.upper_right':
                if ball.y + ball.side > HEIGHT - 50:
                    ball.lower_right = False
                    ball.last_movement = 'ball.lower_right'
                    ball.upper_right = True

                if ball.x + ball.side > WIDTH - 30:
                    if right_paddle.x + right_paddle.width > ball.x + ball.side > right_paddle.x:
                        if right_paddle.y < ball.y + ball.side < right_paddle.y + right_paddle.height:
                            ball.lower_right = False
                            ball.last_movement = 'ball.lower_right'
                            ball.lower_left = True
                    else:
                        score_A += 1
                        balls.remove(ball)
                        #ball.start()

            if ball.last_movement == 'ball.lower_left':
                if ball.y + ball.side > HEIGHT - 50:
                    ball.lower_right = False
                    ball.last_movement = 'ball.lower_right'
                    ball.upper_right = True

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                quit()

        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP] and right_paddle.y > 50:
            right_paddle.y -= right_paddle.vel
        if keys[pygame.K_w] and left_paddle.y > 50:
            left_paddle.y -= left_paddle.vel
        if keys[pygame.K_DOWN] and right_paddle.y + right_paddle.height < HEIGHT - 50:
            right_paddle.y += right_paddle.vel
        if keys[pygame.K_s] and left_paddle.y + left_paddle.height < HEIGHT - 50:
            left_paddle.y += left_paddle.vel
        if keys[pygame.K_SPACE]:
            pass

        redraw_window()

    quit()


def main_menu():
    run = True

    play_button = Button(green, 100, 350, 150, 75, "Play Pong")
    quit_button = Button(red, 550, 350, 150, 75, "Quit")

    pong_text = large_font.render("Let's Play Pong!!!", 1, black)

    while run:
        window.fill(white)

        play_button.draw(window, black)
        quit_button.draw(window, black)

        window.blit(pong_text, (int(WIDTH / 2 - pong_text.get_width() / 2), 100))

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                quit()

            if event.type == pygame.MOUSEMOTION:
                if play_button.hover(pygame.mouse.get_pos()):
                    play_button.color = (0, 200, 0)
                else:
                    play_button.color = green
                if quit_button.hover(pygame.mouse.get_pos()):
                    quit_button.color = (200, 0, 0)
                else:
                    quit_button.color = red

            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_button.hover(pygame.mouse.get_pos()):
                    main()
                if quit_button.hover(pygame.mouse.get_pos()):
                    run = False
                    quit()


main_menu()