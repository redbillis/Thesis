# setup #
import pygame, sys
from Classes.Characters import Hero, Enemy
from Classes.Weapons import Projectile

# setup pygame/window #
mainClock = pygame.time.Clock()
from pygame.locals import *

pygame.init()

pygame.display.set_caption('Physics Explanation')

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 700

win = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)
BG = pygame.transform.scale((pygame.image.load('Images/Arena/BG.png').convert_alpha()), (SCREEN_WIDTH, SCREEN_HEIGHT))
score_board = pygame.transform.scale((pygame.image.load('Images/Arena/ScoreBoard.png').convert_alpha()), (162, 80))  #119

# More images for the Nature around the Arena
tree_1 = pygame.transform.scale((pygame.image.load('Images/Arena/Tree_1.png').convert_alpha()), (116, 44))
tree_2 = pygame.transform.scale((pygame.image.load('Images/Arena/Tree_2.png').convert_alpha()), (282, 602))
tree_3 = pygame.transform.scale((pygame.image.load('Images/Arena/Tree_3.png').convert_alpha()), (282, 544))

bush_1 = pygame.image.load('Images/Arena/Bush (1).png')
bush_2 = pygame.image.load('Images/Arena/Bush (2).png')
bush_3 = pygame.image.load('Images/Arena/Bush (3).png')
bush_4 = pygame.image.load('Images/Arena/Bush (4).png')

stone = pygame.image.load('Images/Arena/Stone.png')

shroom_1 = pygame.image.load('Images/Arena/Mushroom_1.png')
shroom_2 = pygame.image.load('Images/Arena/Mushroom_2.png')

cave_left = pygame.image.load('Images/Arena/16.png')
cave_right = pygame.image.load('Images/Arena/12.png')

# The tiles with which the hero will collide.
blocks = [pygame.Rect(0, 415, 100, 20), pygame.Rect(1112, 415, 100, 20), pygame.Rect(0, 578, SCREEN_WIDTH, 128)]
ground = pygame.image.load('Images/Arena/2.png')
platform_left = pygame.image.load('Images/Arena/13.png')
platform_right = pygame.image.load('Images/Arena/15.png')
water = pygame.image.load('Images/Arena/17.png')

font = pygame.font.SysFont('comicsans', 30, True)   # The first argument is the font, next is size and then True to make our font bold.

bulletSound = pygame.mixer.Sound('gunshot.wav')
hitSound = pygame.mixer.Sound('hit.wav')

rainforest_sound = pygame.mixer.music.load('rainforest.mp3')
pygame.mixer.music.play(-1)     # -1 will ensure the song keeps looping

hero = Hero(30, 385, 106, 90, 100)    # (641 x 542)/6  (106 x 90)
dino = Enemy(1000, 435, 226, 157, 30)  # (680 x 472)/2.5  (272 x 188)

bullets = []

dino_score = 0
hero_score = 0

def redraw_window():
    global dino_score,hero_score
    for tile in blocks:
        pygame.draw.rect(win, (255, 0, 0), tile)

    win.blit(BG, (0, 0))  # This will draw our background image at (0,0)

    # drawing the ground
    for x in range(0, SCREEN_WIDTH, 128):
        win.blit(ground, (x, 572))
        
    for x in range(0, SCREEN_WIDTH, 128):
        win.blit(water, (x, 610))

    # Drawing more for the Arena
    # stone behind tree_1
    win.blit(stone, (770, 520))

    # drawing cavities
    win.blit(cave_left, (-70, 440))
    win.blit(cave_right, (1150, 440))
    
    # drawing bushes
    win.blit(bush_1, (200, 507))
    win.blit(bush_1, (600, 507))
    win.blit(bush_1, (946, 507))

    win.blit(bush_2, (460, 507))
    win.blit(bush_2, (356, 507))
    win.blit(bush_2, (856, 507))

    # drawing the trees
    # tree_1
    win.blit(tree_1, (700, 530))

    # drawing stones between trees
    win.blit(stone, (110, 520))
    win.blit(stone, (420, 520))

    # tree_2
    win.blit(tree_2, (-34, -29))
    win.blit(tree_2, (974, -29))
    win.blit(tree_2, (434, -29))

    # drawing stones between trees and bush_4 (far left and right)
    win.blit(stone, (-30, 520))
    win.blit(stone, (1130, 520))

    # drawing bush_4 in front of trees
    win.blit(bush_4, (20, 528))
    #win.blit(bush_4, (1120, 528))

    # tree_3
    win.blit(tree_3, (214, 28))
    win.blit(tree_3, (814, 28))

    # drawing the platforms
    win.blit(platform_right, (0, 410))
    win.blit(platform_left, (1072, 410))

    # drawing stones on platforms
    win.blit(stone, (-40, 356))
    win.blit(stone, (1140, 356))

    # drawing bush_3 on platforms
    win.blit(bush_3, (20, 364))
    win.blit(bush_3, (1100, 364))

    # drawing the mushrooms
    win.blit(shroom_2, (400, 532))
    win.blit(shroom_1, (150, 532))
    win.blit(shroom_1, (1120, 532))

    win.blit(score_board, (4, 4))
    #   Hero health points.
    text = font.render('Hero: ' + str(hero_score), 1, (104, 0, 0))  # Arguments are: text, anti-aliasing, color
    win.blit(text, (20, 15))
    #   Dino health points.
    text = font.render('Dino: ' + str(dino_score), 1, (51, 200, 51))  # Arguments are: text, anti-aliasing, color
    win.blit(text, (20, 50))


    if hero.health == 0:
        text_lost = font.render('YOU LOST!', 1, (255, 0, 0))
        win.blit(text_lost, (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))
        dino_score += 1
    if dino.health == 0:
        text_win = font.render('YOU WIN!', 1, (0, 100, 255))
        win.blit(text_win, (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))
        hero_score += 1

    #pygame.draw.rect(win, (0, 255, 0), hero.player_rect)
    hero.draw(win)
    #pygame.draw.rect(win, (0, 0, 255), dino.enemy_rect)
    dino.draw(win)

    for bullet in bullets:
        bullet.draw(win)

    pygame.display.update()

# Checks hero's movement and collision with tiles.
def test_collision(rect, blocks):
    colilision_list = []
    for block in blocks:
        if rect.colliderect(block):
            colilision_list.append(block)
    return colilision_list

def move(rect, movement, blocks):
    collision_types = {'top': False, 'bottom': False, 'right': False, 'left': False}
    rect.x += movement[0]
    collision_list = test_collision(rect, blocks)
    for block in collision_list:
        if movement[0] > 0:
            rect.right = block.left
            collision_types['right'] = True
        if movement[0] < 0:
            collision_types['left'] = True
            rect.left = block.right
    rect.y += movement[1]
    collision_list = test_collision(rect, blocks)
    for block in collision_list:
        if movement[1] > 0:
            rect.bottom = block.top
            collision_types['bottom'] = True
        if movement[1] < 0:
            rect.top = block.bottom
            collision_types['top'] = True
    return rect, collision_types

def main_menu(win):
    global hero, dino
    hero = Hero(30, 385, 106, 90, 100)  # (641 x 542)/6  (106 x 90)
    dino = Enemy(1000, 435, 226, 157, 30)  # (680 x 472)/2.5  (272 x 188)

    menu = True
    while menu:
        win.blit(BG, (0, 0))
        title_font = pygame.font.SysFont('comicsans', 160)
        game_label = title_font.render('DINO FIGHT!', 1, (0, 155, 100))
        win.blit(game_label, (SCREEN_WIDTH / 4, SCREEN_HEIGHT / 4))
        menu_key_txt = font.render("Press Down Arrow To Play", 1, (100, 70, 255))
        win.blit(menu_key_txt, ((SCREEN_WIDTH / 2) - 100, SCREEN_HEIGHT / 2))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                menu = False
            if event.type == pygame.KEYDOWN:
                if event.key == K_DOWN:
                    main(win)

    pygame.display.quit()

def main(win):
    vertical_mom = 0
    airTimer = 0
    run = True
    shootLoop = 0

    while run:
        if hero.health == 0:
            pygame.display.update()
            pygame.time.delay(2000)
            run = False
            for bullet in bullets:
                bullets.pop(bullets.index(bullet))
            main_menu(win)
        if dino.health == 0:
            pygame.display.update()
            pygame.time.delay(2000)
            run = False
            for bullet in bullets:
                bullets.pop(bullets.index(bullet))
            main_menu(win)

        # Character-Enemy Collision
        if dino.visible == True:
            if hero.hitbox[1] < dino.hitbox[1] + dino.hitbox[3] and hero.hitbox[1] + hero.hitbox[3] > dino.hitbox[1]:
                if hero.hitbox[0] + hero.hitbox[2] > dino.hitbox[0] and hero.hitbox[0] < dino.hitbox[0] + dino.hitbox[2]:
                    hitSound.play()
                    hero.hit()

        # Enemy movement.
        if hero.health > 0:
            if dino.enemy_rect.x != hero.player_rect.x:
                dino.standing = False
                if dino.vel > 0:  # If we are moving right
                    if dino.enemy_rect.x + dino.vel < hero.player_rect.x:  # If hero is right,dino moves right.
                        dino.enemy_rect.x += dino.vel
                        dino.right = True
                    else:  # Change direction and move back the other way
                        dino.vel = dino.vel * -1
                        dino.walkCount = 0
                elif dino.vel < 0:  # If we are moving left
                    if dino.enemy_rect.x - dino.vel > hero.player_rect.x:  # If hero is left,dino left.
                        dino.enemy_rect.x += dino.vel
                        dino.left = True
                    else:  # Change direction
                        dino.vel = dino.vel * -1
                        dino.walkCount = 0
            else:
                dino.standing = True
        else:
            dino.enemy_rect.x += dino.vel
            dino.right = True

        if shootLoop > 0:
            shootLoop += 1
        if shootLoop > 10:
            shootLoop = 0
            hero.shoot = False

        # Will move our bullets and remove them if they have left the screen.
        for bullet in bullets:
            # COLLISION (bullet to goblin)
            if bullet.y - bullet.radius < dino.hitbox[1] + dino.hitbox[3] and bullet.y + bullet.radius > dino.hitbox[1]:  # Checks x coords
                if bullet.x + bullet.radius > dino.hitbox[0] and bullet.x - bullet.radius < dino.hitbox[0] + dino.hitbox[2]:  # Checks y coords
                    dino.hit()  # calls enemy hit method
                    bullets.pop(bullets.index(bullet))  # removes bullet from bullet list

            if bullet.x < SCREEN_WIDTH and bullet.x > 0:
                bullet.x += bullet.vel              # Moves the bullet by its vel.
            else:
                bullets.pop(bullets.index(bullet))  # This will remove the bullet if it is off the screen.

        # Hero movement.
        movement = [0, 0]
        if hero.right == True and hero.player_rect.x < SCREEN_WIDTH - hero.player_rect.width - movement[0]:
            movement[0] += 7
            hero.standing = False
        elif hero.left == True and hero.player_rect.x > movement[0]:
            movement[0] -= 7
            hero.standing = False
        else:
            hero.standing = True
            hero.runCount = 0
        movement[1] += vertical_mom
        vertical_mom += 0.2
        if vertical_mom > 3:
            vertical_mom = 8

        hero.player_rect, collisions = move(hero.player_rect, movement, blocks)

        if collisions['bottom'] == True:
            airTimer = 0
            vertical_mom = 0
            hero.jump = False
        elif collisions['top'] == True:
            vertical_mom = 4
        else:
            airTimer += 1

        # event handling #
        for event in pygame.event.get():
            if event.type == QUIT:
                run = False
                pygame.quit()

            if event.type == KEYDOWN:
                if event.key == K_RIGHT:
                    hero.right = True
                    hero.face_left = False
                if event.key == K_LEFT:
                    hero.left = True
                    hero.face_right = False
                if event.key == K_UP:
                    if airTimer < 9 and hero.health > 0:
                        vertical_mom = -8.2
                        hero.jump = True
            if event.type == KEYUP:
                if event.key == K_RIGHT:
                    hero.right = False
                    hero.face_right = True

                if event.key == K_LEFT:
                    hero.left = False
                    hero.face_left = True

        keys = pygame.key.get_pressed()  # This will give us a dictonary where each key has a value of 1 or 0. Where 1 is pressed and 0 is not pressed.

        # Create a new if statement that will check if the space bar is pressed. If it is we will create a new bullet, give it a velocity and start moving it.
        if movement[0] == 0:
            if keys[pygame.K_SPACE] and shootLoop == 0:
                bulletSound.play()
                if hero.face_left == True:
                    facing = -1
                    if len(bullets) < 6:  # This will make sure we cannot exceed 5 bullets on the screen at once.
                        bullets.append(Projectile(round(hero.player_rect.x + hero.player_rect.width // 2), round(hero.player_rect.y + hero.player_rect.height // 2), 3, (0, 0, 0), facing))  # This will create a bullet starting at the middle of the character.
                        hero.shoot = True
                        hero.face_right = False
                elif hero.face_right == True:
                    facing = 1
                    if len(bullets) < 6:    # This will make sure we cannot exceed 5 bullets on the screen at once.
                        bullets.append(Projectile(round(hero.player_rect.x + hero.player_rect.width // 2), round(hero.player_rect.y + hero.player_rect.height // 2), 3, (0, 0, 0), facing))   # This will create a bullet starting at the middle of the character.
                        hero.shoot = True
                        hero.face_left = False
                shootLoop = 1


        # update display #
        redraw_window()
        mainClock.tick(60)

main_menu(win)