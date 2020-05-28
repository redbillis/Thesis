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

tiles = [pygame.Rect(0, 415, 128, 20), pygame.Rect(1072, 415, 128, 20), pygame.Rect(0, 578, SCREEN_WIDTH, 128)]  # 572
ground = pygame.image.load('Images/Arena/2.png')

platform_left = pygame.image.load('Images/Arena/13.png')
platform_right = pygame.image.load('Images/Arena/15.png')

font = pygame.font.SysFont('comicsans', 30, True)   # The first argument is the font, next is size and then True to make our font bold.

hero = Hero(30, 385, 106, 90, 100)    # (641 x 542)/6
dino = Enemy(1000, 435, 226, 157, 880, 100)  # (680 x 472)/2.5  (272 x 188)

vertical_momentum = 0
air_timer = 0

shootLoop = 0
bullets = []

def redraw_window():
    for tile in tiles:
        pygame.draw.rect(win, (255, 0, 0), tile)

    win.blit(BG, (0, 0))  # This will draw our background image at (0,0)

    win.blit(platform_right, (0, 410))
    #pygame.draw.rect(win, (255, 0, 0), left_plat_dim, 1)

    win.blit(platform_left, (1072, 410))
    #pygame.draw.rect(win, (255, 0, 0), right_plat_dim, 1)

    for x in range(0, SCREEN_WIDTH, 128): # drawing the ground
        win.blit(ground, (x, 572))
    #   Dino health points
    text = font.render('Dino: ' + str(dino.health), 1, (0, 0, 0))  # Arguments are: text, anti-aliasing, color
    win.blit(text, (1050, 10))
    #   Hero health pionts
    text = font.render('Hero: ' + str(hero.health), 1, (0, 0, 0))  # Arguments are: text, anti-aliasing, color
    win.blit(text, (50, 10))

    if hero.health == 0:
        text_lost = font.render('YOU LOST!', 1, (255, 0, 0))
        win.blit(text_lost, (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))
    if dino.health == 0:
        text_win = font.render('YOU WIN!', 1, (0, 100, 255))
        win.blit(text_win, (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))

    #pygame.draw.rect(win, (255, 0, 0), hero.player_rect)
    hero.draw(win)
    #pygame.draw.rect(win, (255, 0, 0), dino.enemy_rect)
    dino.draw(win)

    for bullet in bullets:
        bullet.draw(win)

    pygame.display.update()


def collision_test(rect, tiles):
    hit_list = []
    for tile in tiles:
        if rect.colliderect(tile):
            hit_list.append(tile)
    return hit_list


def move(rect, movement, tiles):  # movement = [5,2]
    collision_types = {'top': False, 'bottom': False, 'right': False, 'left': False}
    rect.x += movement[0]
    hit_list = collision_test(rect, tiles)
    for tile in hit_list:
        if movement[0] > 0:
            rect.right = tile.left
            collision_types['right'] = True
        if movement[0] < 0:
            collision_types['left'] = True
            rect.left = tile.right
    rect.y += movement[1]
    hit_list = collision_test(rect, tiles)
    for tile in hit_list:
        if movement[1] > 0:
            rect.bottom = tile.top
            collision_types['bottom'] = True
        if movement[1] < 0:
            rect.top = tile.bottom
            collision_types['top'] = True
    return rect, collision_types


# loop #
while True:
    # Character-Enemy Collision
    if dino.visible == True:
        if hero.player_rect.y < dino.enemy_rect.y + dino.enemy_rect.height and hero.player_rect.y + hero.player_rect.height > dino.enemy_rect.y:
            if hero.player_rect.x + hero.player_rect.width > dino.enemy_rect.x and hero.player_rect.x < dino.enemy_rect.x + dino.enemy_rect.width:
                hero.hit()

    # Enemy movement.
    if dino.enemy_rect.x != hero.player_rect.x:
        dino.standing = False
        if dino.vel > 0:  # If we are moving right
            if dino.enemy_rect.x + dino.vel < hero.player_rect.x:  # If we have not reached the furthest right point on our path.
                dino.enemy_rect.x += dino.vel
                dino.right = True
            else:  # Change direction and move back the other way
                dino.vel = dino.vel * -1
                dino.walkCount = 0
        else:  # If we are moving left
            if dino.enemy_rect.x - dino.vel > hero.player_rect.x:  # If we have not reached the furthest left point on our path
                dino.enemy_rect.x += dino.vel
                dino.left = True
            else:  # Change direction
                dino.vel = dino.vel * -1
                dino.walkCount = 0
    else:
        dino.standing = True

    if shootLoop > 0:
        shootLoop += 1
    if shootLoop > 10:
        shootLoop = 0
        hero.shoot = False

    # Will move our bullets and remove them if they have left the screen.
    for bullet in bullets:
        # COLLISION (bullet to goblin)
        if bullet.y - bullet.radius < dino.enemy_rect.y + dino.enemy_rect.height and bullet.y + bullet.radius > dino.enemy_rect.y:  # Checks x coords
            if bullet.x + bullet.radius > dino.enemy_rect.x and bullet.x - bullet.radius < dino.enemy_rect.x + dino.enemy_rect.width:  # Checks y coords
                #hitSound.play()
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
    movement[1] += vertical_momentum
    vertical_momentum += 0.2
    if vertical_momentum > 3:
        vertical_momentum = 8

    hero.player_rect, collisions = move(hero.player_rect, movement, tiles)

    if collisions['bottom'] == True:
        air_timer = 0
        vertical_momentum = 0
        hero.jump = False
    elif collisions['top'] == True:
        vertical_momentum = 4
    else:
        air_timer += 1

    # event handling #
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if event.type == KEYDOWN:
            if event.key == K_RIGHT:
                hero.right = True
                hero.face_left = False
            if event.key == K_LEFT:
                hero.left = True
                hero.face_right = False
            if event.key == K_UP:
                if air_timer < 9:
                    vertical_momentum = -8.2
                    hero.jump = True
        if event.type == KEYUP:
            if event.key == K_RIGHT:
                hero.right = False
                hero.face_right = True

            if event.key == K_LEFT:
                hero.left = False
                hero.face_left = True

    keys = pygame.key.get_pressed()  # This will give us a dictonary where each key has a value of 1 or 0. Where 1 is pressed and 0 is not pressed.

    # Create a new if statement that will check if the space bar is clicked. If it is we will create a new bullet, give it a velocity and start moving it.
    if movement[0] == 0:
        if keys[pygame.K_SPACE] and shootLoop == 0:
            #bulletSound.play()
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
    #pygame.display.update()
    mainClock.tick(60)
