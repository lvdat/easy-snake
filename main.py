import pygame
import time
import random

pygame.init()

GAME_NAME = 'Snake Fake'
BLUE = (0, 0, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

DIS_WIDTH = 800
DIS_HEIGHT = 600

FONT_STYLE = pygame.font.Font("fonts/Inconsolata.ttf", 20)

dis = pygame.display.set_mode((DIS_WIDTH, DIS_HEIGHT))
pygame.display.update()
pygame.display.set_caption(GAME_NAME)
clock = pygame.time.Clock()

def score (score):
    value = FONT_STYLE.render('Score: ' + str(score), True, RED)
    dis.blit(value, [0, 0])

def snake (SNAKE_BLOCK, SNAKE_LIST):
    for x in SNAKE_LIST:
        pygame.draw.rect(dis, BLACK, [x[0], x[1], SNAKE_BLOCK, SNAKE_BLOCK])

def message (msg, color):
    mess = FONT_STYLE.render(msg, True, color)
    dis.blit(mess, [5, DIS_HEIGHT - 60])

def game ():
    x1 = DIS_WIDTH / 2
    y1 = DIS_HEIGHT / 2
    x1_change = 0
    y1_change = 0
    SNAKE_BLOCK = 10
    SNAKE_SPEED = 30
    GAME_END = False
    GAME_CLOSE = False
    
    SNAKE = []
    SNAKE_LENGTH = 1
    
    # location of food
    foodx = round(random.randrange(0, DIS_WIDTH - SNAKE_BLOCK) / 10.0) * 10
    foody = round(random.randrange(0, DIS_HEIGHT - SNAKE_BLOCK) / 10.0) * 10
    
    while not GAME_END:
        while GAME_CLOSE == True:
            dis.fill(WHITE)
            message('You Lost! Press Q to Quit or C to play again!', RED)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        GAME_END = True
                        GAME_CLOSE = False
                    elif event.key == pygame.K_c:
                        game()
                        
        for event in pygame.event.get():
            # detect Quit action of player
            if event.type == pygame.QUIT:
                GAME_END = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    x1_change = -SNAKE_BLOCK
                    y1_change = 0
                elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    x1_change = SNAKE_BLOCK
                    y1_change = 0
                elif event.key == pygame.K_UP or event.key == pygame.K_w:
                    x1_change = 0
                    y1_change = -SNAKE_BLOCK
                elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    x1_change = 0
                    y1_change = SNAKE_BLOCK    
        
        # check location of snake with limit of map
        if x1 >= DIS_WIDTH or x1 < 0 or y1 >= DIS_HEIGHT or y1 < 0:
            GAME_CLOSE = True
        
        # update location
        x1 += x1_change
        y1 += y1_change
        
        dis.fill(WHITE)
        
        # Draw food
        pygame.draw.rect(dis, BLUE, [foodx, foody, SNAKE_BLOCK, SNAKE_BLOCK])
        
        SNAKE_HEAD = []
        SNAKE_HEAD.append(x1)
        SNAKE_HEAD.append(y1)
        SNAKE.append(SNAKE_HEAD)
        
        if len(SNAKE) > SNAKE_LENGTH:
            del SNAKE[0]
            
        for x in SNAKE[:-1]:
            if x == SNAKE_HEAD:
                GAME_CLOSE = True
        
        snake(SNAKE_BLOCK, SNAKE)
        score(SNAKE_LENGTH - 1)
        pygame.display.update()
        
        if x1 == foodx and y1 == foody:
            print('+1')
            foodx = round(random.randrange(0, DIS_WIDTH - SNAKE_BLOCK) / 10.0) * 10
            foody = round(random.randrange(0, DIS_HEIGHT - SNAKE_BLOCK) / 10.0) * 10
            SNAKE_LENGTH += 1
        
        clock.tick(SNAKE_SPEED)

    pygame.quit()
    quit()
    
game()