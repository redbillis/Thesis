import pygame

class Hero():
    def __init__(self, x, y, width, height, health):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

        self.health = health

        self.runCount = 0
        self.idleCount = 0
        self.jumpCount = 0
        self.shootCount = 0

        self.standing = True
        self.jump = False

        self.shoot = False

        self.right = False
        self.face_right = False
        self.left = False
        self.face_left = False

        self.player_rect = pygame.Rect(self.x, self.y, self.width, self.height)
        #self.hitbox = [self.x + 5, self.y, 50, 84]  # The elements in the hitbox are (top left x, top left y, width, height).
        #self.rect = pygame.Rect(self.x,  self.y, 50, 84)


        # Loading our hero images.
        # Creating running sprites of our hero. (Original Dimension 641 x 542)
        self.runRight = [pygame.transform.scale((pygame.image.load('Images/Hero/Run_R_0.png').convert_alpha()), (self.width, self.height)),
                         pygame.transform.scale((pygame.image.load('Images/Hero/Run_R_1.png').convert_alpha()), (self.width, self.height)),
                         pygame.transform.scale((pygame.image.load('Images/Hero/Run_R_2.png').convert_alpha()), (self.width, self.height)),
                         pygame.transform.scale((pygame.image.load('Images/Hero/Run_R_3.png').convert_alpha()), (self.width, self.height)),
                         pygame.transform.scale((pygame.image.load('Images/Hero/Run_R_4.png').convert_alpha()), (self.width, self.height)),
                         pygame.transform.scale((pygame.image.load('Images/Hero/Run_R_5.png').convert_alpha()), (self.width, self.height)),
                         pygame.transform.scale((pygame.image.load('Images/Hero/Run_R_6.png').convert_alpha()), (self.width, self.height)),
                         pygame.transform.scale((pygame.image.load('Images/Hero/Run_R_7.png').convert_alpha()), (self.width, self.height))]

        self.runLeft = [pygame.transform.scale((pygame.image.load('Images/Hero/Run_L_0.png').convert_alpha()), (self.width, self.height)),
                        pygame.transform.scale((pygame.image.load('Images/Hero/Run_L_1.png').convert_alpha()), (self.width, self.height)),
                        pygame.transform.scale((pygame.image.load('Images/Hero/Run_L_2.png').convert_alpha()), (self.width, self.height)),
                        pygame.transform.scale((pygame.image.load('Images/Hero/Run_L_3.png').convert_alpha()), (self.width, self.height)),
                        pygame.transform.scale((pygame.image.load('Images/Hero/Run_L_4.png').convert_alpha()), (self.width, self.height)),
                        pygame.transform.scale((pygame.image.load('Images/Hero/Run_L_5.png').convert_alpha()), (self.width, self.height)),
                        pygame.transform.scale((pygame.image.load('Images/Hero/Run_L_6.png').convert_alpha()), (self.width, self.height)),
                        pygame.transform.scale((pygame.image.load('Images/Hero/Run_L_7.png').convert_alpha()), (self.width, self.height))]

        # Creating standing sprite while hero is idle.(Original Dimensions 641 x 542)
        self.idle_right = [pygame.transform.scale((pygame.image.load('Images/Hero/Idle_R_0.png').convert_alpha()), (self.width - 10, self.height)),
                           pygame.transform.scale((pygame.image.load('Images/Hero/Idle_R_1.png').convert_alpha()), (self.width - 10, self.height)),
                           pygame.transform.scale((pygame.image.load('Images/Hero/Idle_R_2.png').convert_alpha()), (self.width - 10, self.height)),
                           pygame.transform.scale((pygame.image.load('Images/Hero/Idle_R_3.png').convert_alpha()), (self.width - 10, self.height)),
                           pygame.transform.scale((pygame.image.load('Images/Hero/Idle_R_4.png').convert_alpha()), (self.width - 10, self.height)),
                           pygame.transform.scale((pygame.image.load('Images/Hero/Idle_R_5.png').convert_alpha()), (self.width - 10, self.height)),
                           pygame.transform.scale((pygame.image.load('Images/Hero/Idle_R_6.png').convert_alpha()), (self.width - 10, self.height)),
                           pygame.transform.scale((pygame.image.load('Images/Hero/Idle_R_7.png').convert_alpha()), (self.width - 10, self.height)),
                           pygame.transform.scale((pygame.image.load('Images/Hero/Idle_R_8.png').convert_alpha()), (self.width - 10, self.height)),
                           pygame.transform.scale((pygame.image.load('Images/Hero/Idle_R_9.png').convert_alpha()), (self.width - 10, self.height))]

        self.idle_left = [pygame.transform.scale((pygame.image.load('Images/Hero/Idle_L_0.png').convert_alpha()), (self.width - 10, self.height)),
                          pygame.transform.scale((pygame.image.load('Images/Hero/Idle_L_1.png').convert_alpha()), (self.width - 10, self.height)),
                          pygame.transform.scale((pygame.image.load('Images/Hero/Idle_L_2.png').convert_alpha()), (self.width - 10, self.height)),
                          pygame.transform.scale((pygame.image.load('Images/Hero/Idle_L_3.png').convert_alpha()), (self.width - 10, self.height)),
                          pygame.transform.scale((pygame.image.load('Images/Hero/Idle_L_4.png').convert_alpha()), (self.width - 10, self.height)),
                          pygame.transform.scale((pygame.image.load('Images/Hero/Idle_L_5.png').convert_alpha()), (self.width - 10, self.height)),
                          pygame.transform.scale((pygame.image.load('Images/Hero/Idle_L_6.png').convert_alpha()), (self.width - 10, self.height)),
                          pygame.transform.scale((pygame.image.load('Images/Hero/Idle_L_7.png').convert_alpha()), (self.width - 10, self.height)),
                          pygame.transform.scale((pygame.image.load('Images/Hero/Idle_L_8.png').convert_alpha()), (self.width - 10, self.height)),
                          pygame.transform.scale((pygame.image.load('Images/Hero/Idle_L_9.png').convert_alpha()), (self.width - 10, self.height))]

        # Create jumping sprites of our hero.(Original Dimensions 641 x 542)
        self.jump_right = [pygame.transform.scale((pygame.image.load('Images/Hero/Jump_R_2.png').convert_alpha()), (self.width - 10, self.height)),
                           pygame.transform.scale((pygame.image.load('Images/Hero/Jump_R_3.png').convert_alpha()), (self.width - 10, self.height)),
                           pygame.transform.scale((pygame.image.load('Images/Hero/Jump_R_4.png').convert_alpha()), (self.width - 10, self.height)),
                           pygame.transform.scale((pygame.image.load('Images/Hero/Jump_R_5.png').convert_alpha()), (self.width - 10, self.height)),
                           pygame.transform.scale((pygame.image.load('Images/Hero/Jump_R_6.png').convert_alpha()), (self.width - 10, self.height))]

        self.jump_left = [pygame.transform.scale((pygame.image.load('Images/Hero/Jump_L_2.png').convert_alpha()), (self.width - 10, self.height)),
                          pygame.transform.scale((pygame.image.load('Images/Hero/Jump_L_3.png').convert_alpha()), (self.width - 10, self.height)),
                          pygame.transform.scale((pygame.image.load('Images/Hero/Jump_L_4.png').convert_alpha()), (self.width - 10, self.height)),
                          pygame.transform.scale((pygame.image.load('Images/Hero/Jump_L_5.png').convert_alpha()), (self.width - 10, self.height)),
                          pygame.transform.scale((pygame.image.load('Images/Hero/Jump_L_6.png').convert_alpha()), (self.width - 10, self.height))]

        # Create shoot sprites of our hero.(Original Dimensions 641 x 542)
        self.shoot_right = [pygame.transform.scale((pygame.image.load('Images/Hero/Shoot_R_0.png').convert_alpha()), (self.width - 10, self.height)),
                            pygame.transform.scale((pygame.image.load('Images/Hero/Shoot_R_1.png').convert_alpha()), (self.width - 10, self.height)),
                            pygame.transform.scale((pygame.image.load('Images/Hero/Shoot_R_2.png').convert_alpha()), (self.width - 10, self.height))]

        self.shoot_left= [pygame.transform.scale((pygame.image.load('Images/Hero/Shoot_L_0.png').convert_alpha()), (self.width - 10, self.height)),
                          pygame.transform.scale((pygame.image.load('Images/Hero/Shoot_L_1.png').convert_alpha()), (self.width - 10, self.height)),
                          pygame.transform.scale((pygame.image.load('Images/Hero/Shoot_L_2.png').convert_alpha()), (self.width - 10, self.height))]

    def draw(self, win):
        # We have 10 images for our walking animation, I want to show the same image for 3 frames
        # so I use the number 30 as an upper bound for walkCount because 30 / 3 = 10. 10 images shown
        # 3 times each animation.
        if self.runCount + 1 >= 24:
            self.runCount = 0

        if self.idleCount + 1 >= 30:
            self.idleCount = 0

        if self.jumpCount + 1 >= 12:
            self.jumpCount = 0

        if self.shootCount + 1 >= 9:
            self.shootCount = 0

        if not self.shoot:
            if not (self.standing):
                if self.jump == False:
                    if self.left:  # If we are facing left
                        win.blit(self.runLeft[self.runCount // 3], (self.player_rect.x, self.player_rect.y))  # We integer divide walkCount by 3 to ensure each image is shown 3 times every animation.
                        self.runCount += 1
                    elif self.right:
                        win.blit(self.runRight[self.runCount // 3], (self.player_rect.x, self.player_rect.y))
                        self.runCount += 1
                else:
                    if self.left == True:
                        win.blit(self.jump_left[self.jumpCount // 3], (self.player_rect.x, self.player_rect.y))  # We integer divide walkCount by 3 to ensure each image is shown 3 times every animation.
                        self.jumpCount += 1
                    else:
                        win.blit(self.jump_right[self.jumpCount // 3], (self.player_rect.x, self.player_rect.y))
                        self.jumpCount += 1
            else:  # If the character is idle.
                if self.jump == False:  # If the character is not jumping.
                    if self.face_right:
                        win.blit(self.idle_right[self.idleCount // 3], (self.player_rect.x, self.player_rect.y))
                        self.idleCount += 1
                    else:
                        win.blit(self.idle_left[self.idleCount // 3], (self.player_rect.x, self.player_rect.y))
                        self.idleCount += 1
                else:   # If the character is jumping.
                    if self.face_left == True:
                        win.blit(self.jump_left[self.jumpCount // 3], (self.player_rect.x, self.player_rect.y))  # We integer divide walkCount by 3 to ensure each image is shown 3 times every animation.
                        self.jumpCount += 1
                    else:
                        win.blit(self.jump_right[self.jumpCount // 3], (self.player_rect.x, self.player_rect.y))
                        self.jumpCount += 1
        else:
            if self.face_right:
                if self.shoot == True:
                    win.blit(self.shoot_right[self.shootCount // 3], (self.player_rect.x, self.player_rect.y))
                    self.shootCount += 1
            else:
                if self.shoot == True:
                    win.blit(self.shoot_left[self.shootCount // 3], (self.player_rect.x, self.player_rect.y))
                    self.shootCount += 1
        #self.hitbox = (self.x + 5, self.y, 50, 84)  # The elements in the hitbox are (top left x, top left y, width, height).
        #self.rect = pygame.Rect(self.hitbox)
        #pygame.draw.rect(win, (255, 0, 0), self.hitbox,2) # To draw the hit box around the player

    def hit(self):
        if self.health > 0:
            self.health -= 1
        print("hit")



class Enemy():
    def __init__(self, x, y, width, height, end, health):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.end = end
        self.health = health
        #self.path = [self.x, self.end]  # This will define where our enemy starts and finishes their path.

        self.walkCount = 0
        self.idleCount = 0

        self.vel = 3

        self.visible = True

        self.standing = False
        self.right = False
        #self.face_right = False
        self.left = False
        #self.face_left = False

        self.enemy_rect = pygame.Rect(self.x, self.y, self.width, self.height)
        #self.hitbox = (self.enemy_rect.x + 50, self.enemy_rect.y + 2, 31, 57)

        # Loading our hero images.
        # Creating running sprites of our hero. (Dimension 680 x 472)
        self.walkRight = [pygame.transform.scale((pygame.image.load('Images/Dino/Walk_Right_0.png').convert_alpha()), (self.width, self.height)),
                          pygame.transform.scale((pygame.image.load('Images/Dino/Walk_Right_1.png').convert_alpha()), (self.width, self.height)),
                          pygame.transform.scale((pygame.image.load('Images/Dino/Walk_Right_2.png').convert_alpha()), (self.width, self.height)),
                          pygame.transform.scale((pygame.image.load('Images/Dino/Walk_Right_3.png').convert_alpha()), (self.width, self.height)),
                          pygame.transform.scale((pygame.image.load('Images/Dino/Walk_Right_4.png').convert_alpha()), (self.width, self.height)),
                          pygame.transform.scale((pygame.image.load('Images/Dino/Walk_Right_5.png').convert_alpha()), (self.width, self.height)),
                          pygame.transform.scale((pygame.image.load('Images/Dino/Walk_Right_6.png').convert_alpha()), (self.width, self.height)),
                          pygame.transform.scale((pygame.image.load('Images/Dino/Walk_Right_7.png').convert_alpha()), (self.width, self.height)),
                          pygame.transform.scale((pygame.image.load('Images/Dino/Walk_Right_8.png').convert_alpha()), (self.width, self.height)),
                          pygame.transform.scale((pygame.image.load('Images/Dino/Walk_Right_9.png').convert_alpha()), (self.width, self.height))]

        self.walkLeft = [pygame.transform.scale((pygame.image.load('Images/Dino/Walk_Left_0.png').convert_alpha()), (self.width, self.height)),
                         pygame.transform.scale((pygame.image.load('Images/Dino/Walk_Left_1.png').convert_alpha()), (self.width, self.height)),
                         pygame.transform.scale((pygame.image.load('Images/Dino/Walk_Left_2.png').convert_alpha()), (self.width, self.height)),
                         pygame.transform.scale((pygame.image.load('Images/Dino/Walk_Left_3.png').convert_alpha()), (self.width, self.height)),
                         pygame.transform.scale((pygame.image.load('Images/Dino/Walk_Left_4.png').convert_alpha()), (self.width, self.height)),
                         pygame.transform.scale((pygame.image.load('Images/Dino/Walk_Left_5.png').convert_alpha()), (self.width, self.height)),
                         pygame.transform.scale((pygame.image.load('Images/Dino/Walk_Left_6.png').convert_alpha()), (self.width, self.height)),
                         pygame.transform.scale((pygame.image.load('Images/Dino/Walk_Left_7.png').convert_alpha()), (self.width, self.height)),
                         pygame.transform.scale((pygame.image.load('Images/Dino/Walk_Left_8.png').convert_alpha()), (self.width, self.height)),
                         pygame.transform.scale((pygame.image.load('Images/Dino/Walk_Left_9.png').convert_alpha()), (self.width, self.height))]

        # Creating standing sprite while hero is idle.(Dimensions 319 x 485)
        self.idle_right = [pygame.transform.scale((pygame.image.load('Images/Dino/Idle_R_0.png').convert_alpha()), (self.width - 10, self.height)),
                           pygame.transform.scale((pygame.image.load('Images/Dino/Idle_R_1.png').convert_alpha()), (self.width - 10, self.height)),
                           pygame.transform.scale((pygame.image.load('Images/Dino/Idle_R_2.png').convert_alpha()), (self.width - 10, self.height)),
                           pygame.transform.scale((pygame.image.load('Images/Dino/Idle_R_3.png').convert_alpha()), (self.width - 10, self.height)),
                           pygame.transform.scale((pygame.image.load('Images/Dino/Idle_R_4.png').convert_alpha()), (self.width - 10, self.height)),
                           pygame.transform.scale((pygame.image.load('Images/Dino/Idle_R_5.png').convert_alpha()), (self.width - 10, self.height)),
                           pygame.transform.scale((pygame.image.load('Images/Dino/Idle_R_6.png').convert_alpha()), (self.width - 10, self.height)),
                           pygame.transform.scale((pygame.image.load('Images/Dino/Idle_R_7.png').convert_alpha()), (self.width - 10, self.height)),
                           pygame.transform.scale((pygame.image.load('Images/Dino/Idle_R_8.png').convert_alpha()), (self.width - 10, self.height)),
                           pygame.transform.scale((pygame.image.load('Images/Dino/Idle_R_9.png').convert_alpha()), (self.width - 10, self.height))]

        self.idle_left = [pygame.transform.scale((pygame.image.load('Images/Dino/Idle_L_0.png').convert_alpha()), (self.width - 10, self.height)),
                          pygame.transform.scale((pygame.image.load('Images/Dino/Idle_L_1.png').convert_alpha()), (self.width - 10, self.height)),
                          pygame.transform.scale((pygame.image.load('Images/Dino/Idle_L_2.png').convert_alpha()), (self.width - 10, self.height)),
                          pygame.transform.scale((pygame.image.load('Images/Dino/Idle_L_3.png').convert_alpha()), (self.width - 10, self.height)),
                          pygame.transform.scale((pygame.image.load('Images/Dino/Idle_L_4.png').convert_alpha()), (self.width - 10, self.height)),
                          pygame.transform.scale((pygame.image.load('Images/Dino/Idle_L_5.png').convert_alpha()), (self.width - 10, self.height)),
                          pygame.transform.scale((pygame.image.load('Images/Dino/Idle_L_6.png').convert_alpha()), (self.width - 10, self.height)),
                          pygame.transform.scale((pygame.image.load('Images/Dino/Idle_L_7.png').convert_alpha()), (self.width - 10, self.height)),
                          pygame.transform.scale((pygame.image.load('Images/Dino/Idle_L_8.png').convert_alpha()), (self.width - 10, self.height)),
                          pygame.transform.scale((pygame.image.load('Images/Dino/Idle_L_9.png').convert_alpha()), (self.width - 10, self.height))]

    def draw(self, win):
        #self.move()
        if self.visible:
            if self.walkCount + 1 >= 30:  # Since we have 10 images for each animation our upper bound is 33.We will show each image for 3 frames. 3 x 10 = 30.
                self.walkCount = 0

            if self.idleCount + 1 >= 30:
                self.idleCount = 0

            if not self.standing:
                if self.vel > 0:  # If we are moving to the right we will display our walkRight images.
                    win.blit(self.walkRight[self.walkCount // 3], (self.enemy_rect.x, self.enemy_rect.y))
                    self.walkCount += 1
                else:  # Otherwise we will display the walkLeft images
                    win.blit(self.walkLeft[self.walkCount // 3], (self.enemy_rect.x, self.enemy_rect.y))
                    self.walkCount += 1
            else:
                if self.right:
                    win.blit(self.idle_right[self.idleCount // 3], (self.enemy_rect.x, self.enemy_rect.y))
                    self.idleCount += 1
                #else:
                 #   win.blit(self.idle_left[self.idleCount // 3], (self.enemy_rect.x, self.enemy_rect.y))
                  #  self.idleCount += 1

            #pygame.draw.rect(win, (255, 0, 0), (self.hitbox[0], self.hitbox[1] - 20, 75, 10))
            #pygame.draw.rect(win, (0, 128, 0), (self.hitbox[0], self.hitbox[1] - 20, 75 - ((50 / 10) * (10 - self.health)), 10))
            #self.hitbox = (self.enemy_rect.x + 50, self.enemy_rect.y + 2, 31, 57)
            #pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

    def hit(self):
        if self.health > 0:
            self.health -= 1
        else:
            self.visible = False
        print("hit")

    #  Since we want our enemy to be moving along a path we must figure out how much to move the enemy by and in what direction.
    #  We call this move method from our draw class as every time we draw the enemy we want to move first move it to a new position.
    #def move(self):
        #if self.vel > 0:  # If we are moving right
            #if self.x + self.vel < self.path[1]:  # If we have not reached the furthest right point on our path.
                #self.x += self.vel
            #else:  # Change direction and move back the other way
                #self.vel = self.vel * -1
                #self.walkCount = 0
        #else:  # If we are moving left
            #if self.x - self.vel > self.path[0]:  # If we have not reached the furthest left point on our path
                #self.x += self.vel
            #else:  # Change direction
                #self.vel = self.vel * -1
                #self.walkCount = 0
