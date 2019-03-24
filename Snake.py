# -*- coding: UTF-8 -*-
import random, pygame, shelve
from pygame.locals import *

UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3
SCORE = 0

def on_grid_random():
    x = random.randint(0, 590)
    y = random.randint(0, 590)
    return (x//10 * 10, y//10 *10)

def collision(c1, c2):
    return (c1[0] == c2[0]) and  (c1[1] == c2[1])

def gameOver():
    screen.fill((0,0,0))
    
    gameover = font_gameover.render('VOCÊ PERDEU!', 1, (255, 0,0))
    screen.blit(gameover, (200,250))
    gameover = font_gameover.render('SEU SCORE FOI: %i' %SCORE, 1, (255, 0,0))
    screen.blit(gameover, (190, 275))
    font_playAgain = pygame.font.SysFont(font_standard, 20)
    playAgain = font_playAgain.render('APERTE ENTER PARA CONTINUAR OU ESC PARA SAIR.', 1, (0, 0,255))
    screen.blit(playAgain, (125, 300))
    pygame.display.update()
    
    key = None
    enter = False
    while not enter:
         for event in pygame.event.get():
            if event.type == QUIT:       
                pygame.quit()
            if event.type == KEYDOWN:
                if event.key == K_RETURN:
                    enter = True
                if event.key == K_ESCAPE:
                    pygame.quit()
                    
    play()

	    	
def play():
    global snake, my_direction, apple_pos, SCORE
    snake = [(200, 200), (210, 200), (220, 200)]
    my_direction = LEFT
    apple_pos = on_grid_random()
    SCORE = 0
        
   

pygame.init()
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption('Snake')

snake = [(200, 200), (210, 200), (220, 200)]


snake_skin = pygame.Surface((10, 10))
snake_skin.fill((255, 255, 255))

my_direction = LEFT

apple = pygame.Surface((10,10))
apple.fill((255,0,0))
apple_pos = on_grid_random()

clock = pygame.time.Clock()

pygame.font.init()
font_standard = pygame.font.get_default_font()
font_gameover = pygame.font.SysFont(font_standard, 35)
font_score = pygame.font.SysFont(font_standard, 25)

while True:
    clock.tick(20)
    
    for event in pygame.event.get():
        if event.type == QUIT:
                
            pygame.quit()
        if event.type == KEYDOWN:
            if event.key == K_UP and my_direction != DOWN:
                my_direction = UP
            if event.key == K_DOWN and my_direction != UP:
                my_direction = DOWN
            if event.key == K_RIGHT and my_direction != LEFT:
                my_direction = RIGHT
            if event.key == K_LEFT and my_direction != RIGHT:
                my_direction = LEFT
            
    if collision(snake[0], apple_pos):
        apple_pos = on_grid_random()
        snake.append((0,0))
        SCORE += 1
        
    if my_direction == UP:
        snake[0] = (snake[0][0], snake[0][1] - 10)
    if my_direction == DOWN:
        snake[0] = (snake[0][0], snake[0][1] + 10)
    if my_direction == RIGHT:
        snake[0] = (snake[0][0] + 10, snake[0][1])
    if my_direction == LEFT:
        snake[0] = (snake[0][0] - 10, snake[0][1])
        
    for i in range(len(snake)):
        if (i > 1) and (snake[i] == snake[0]):
            gameOver()
            break
        
    if (snake[0][0] < 0) or (snake[0][1] < 0) or (snake[0][0] > 590) or (snake[0][1] > 590):
        gameOver()
    
    for i in range(len(snake) - 1, 0, -1):
        snake[i] = (snake[i-1][0], snake[i-1][1])
            
    
    screen.fill((0, 0, 0))
    screen.blit(apple, apple_pos)
    score = font_score.render('PONTUAÇÃO: %i' %SCORE, 1, (255,255,255))
    screen.blit(score, (0,10))
    for pos in snake:
        screen.blit(snake_skin, pos)

    
    pygame.display.update()
