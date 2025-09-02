# Example file showing a basic pygame "game loop"
import pygame
import random
import sys

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1000, 600))
clock = pygame.time.Clock()
running = True
ball =  pygame.Rect(screen.get_width()/2-15,screen.get_height()/2-15,30,30)
ball_speed_x = 5*random.choice((1,-1))
ball_speed_y = 5*random.choice((1,-1))
player = pygame.Rect(10,screen.get_height()/2-50,20,100)
computer = pygame.Rect(screen.get_width()-30,screen.get_height()/2-50,20,100)
player_score = 0
computer_score = 0
player_speed = 0
computer_speed = 5
while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player_speed -= 5
            if event.key == pygame.K_DOWN:
                player_speed += 5

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                player_speed += 5
            if event.key == pygame.K_DOWN:
                player_speed -= 5
        
    player.centery += player_speed
    computer.centery += computer_speed
    ball.centerx += ball_speed_x
    ball.centery += ball_speed_y

    if computer.top<0 or computer.bottom>screen.get_height():
        computer_speed *= -1

    if ball.top<0:
        ball_speed_y *= -1
    if ball.bottom>screen.get_height():
        ball_speed_y *= -1
    if ball.left<0 or ball.right>screen.get_width():
        ball.centerx = screen.get_width()/2
        ball.centery = screen.get_height()/2


    if ball.colliderect(player) or ball.colliderect(computer):
        ball_speed_x *= -1
        ball_speed_y *= 1

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")

    # RENDER YOUR GAME HERE
    pygame.draw.aaline(screen, "white", [640,0], [640,720], True)
    pygame.draw.rect(screen, "white", ball, 0, border_radius=15)
    pygame.draw.rect(screen, "white", player, 0)
    pygame.draw.rect(screen, "white", computer, 0)
    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()
