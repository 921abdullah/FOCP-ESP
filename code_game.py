import pygame
import pygame_menu
from random import random
import random

#initialising 
pygame.init()
pygame.font.init()
pygame.mixer.init()

#game window
WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Star Wars 22")

#background dimensions
bg_width,bg_height=900,500
bg_image=pygame.image.load("planet.png")
bg=pygame.transform.scale(bg_image,(bg_width, bg_height))

VADER_HIT=pygame.USEREVENT+1
XFIGHTER_HIT=pygame.USEREVENT+2
FALCON_HIT=pygame.USEREVENT+3

def begin():
    
    #sound effects
    bulletfire_sound = pygame.mixer.Sound("Bullet.mp3")
    bulletfire_sound.play()
    bulletfire_sound.set_volume(0.9)
    xfighter_sound = pygame.mixer.Sound("XWing-Proton.mp3")
    xfighter_sound.play()
    xfighter_sound.set_volume(0.1)
    ship_explosion = pygame.mixer.Sound("XWing explode.mp3")
    ship_explosion.play()
    ship_explosion.set_volume(0.5)
    #tie_hit = pygame.mixer.Sound("darthVader.mp3")
    bg_sound= pygame.mixer.Sound("music.mp3")
    bg_music = pygame.mixer.music.load("music.mp3")
    pygame.mixer.music.play(-1)
    
    # Colours
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    RED=(255,0,0)
    GREEN=(0,255,0)
    BLUE=(0,0,255)

    #number of levels
    VICTORY_LEVEL = 4
    #number of kills for level up
    LEVEL_UP_KILLS = 5

    # Velocity of ship
    VEL=4
    
    # Velocity of bullets
    BULLET_VEL=7
    
    # Max no. of our bullets on screen at a time
    MAX_BULLETS_VADER=5
   
    MAX_BULLETS_XFIGHTER=4

    # Enemy velocity
    XFIGHTER_VEL=1
    
    # Max frame rate for game to run
    FPS=60

    #loading images 
    bg_width,bg_height=900,500
    bg_image=pygame.image.load("planet.png")
    bg=pygame.transform.scale(bg_image,(bg_width, bg_height))

    frigate1_width, frigate1_height=300,140
    frigate2_width, frigate2_height=150,60
    frigate3_width, frigate3_height=205,85

    empirefrigate1_image=pygame.image.load("empirefrigate.png")
    empirefrigate1=pygame.transform.scale(empirefrigate1_image,(frigate1_width,frigate1_height))

    empirefrigate2_image=pygame.image.load("empirefrigate.png")
    empirefrigate2=pygame.transform.scale(empirefrigate2_image,(frigate2_width,frigate2_height))

    empirefrigate3_image=pygame.image.load("empirefrigate.png")
    empirefrigate3=pygame.transform.scale(empirefrigate3_image,(frigate3_width,frigate3_height))

    spaceship_width, spaceship_height = 40, 50
    tie_bg_width, tie_bg_height=20,20

    tie_bg_image=pygame.image.load("tie fighter pixel.png")
    tie_bg = pygame.transform.scale(tie_bg_image, (tie_bg_width, tie_bg_height))

    spaceship_image = pygame.image.load("darth.png")
    spaceship = pygame.transform.scale(spaceship_image, (spaceship_width,spaceship_height))

    frigate1_width, frigate1_height=300,140
    frigate2_width, frigate2_height=170,65

    rebelfrigate1_image=pygame.image.load("rebelfrigate.png")
    rebelfrigate1=pygame.transform.scale(rebelfrigate1_image,(frigate1_width,frigate1_height))
    
    rebelfrigate2_image=pygame.image.load("rebelfrigate.png")
    rebelfrigate2=pygame.transform.scale(rebelfrigate2_image,(frigate2_width,frigate2_height))
    
    xfighter1_width, xfighter1_height = 40, 50
    xfighter_bg1_width, xfighter_bg1_height = 20,20
    xfighter_bg2_width, xfighter_bg2_height = 20,20
    xfighter_bg3_width, xfighter_bg3_height = 20,20
    xfighter_bg4_width, xfighter_bg4_height = 20,20

    xfighter_image=pygame.image.load("xfighter pixel.png")
    xfighter=pygame.transform.rotate(pygame.transform.scale(xfighter_image, (xfighter1_width, xfighter1_height)),270)
    xfighter_image=pygame.image.load("xfighter pixel.png")
    xfighter=pygame.transform.rotate(pygame.transform.scale(xfighter_image, (xfighter1_width, xfighter1_height)),270)

    xfighter_bg1_image=pygame.image.load("xfighter pixel.png")
    xfighter_bg1 = pygame.transform.rotate(pygame.transform.scale(xfighter_bg1_image, (xfighter_bg1_width,xfighter_bg1_height)),270)
    
    xfighter_bg2_image=pygame.image.load("xfighter pixel.png")
    xfighter_bg2 = pygame.transform.rotate(pygame.transform.scale(xfighter_bg2_image, (xfighter_bg2_width,xfighter_bg2_height)),270)
   
    xfighter_bg3_image=pygame.image.load("xfighter pixel.png")
    xfighter_bg3 = pygame.transform.rotate(pygame.transform.scale(xfighter_bg3_image, (xfighter_bg3_width,xfighter_bg3_height)),270)
    
    xfighter_bg4_image=pygame.image.load("xfighter pixel.png")
    xfighter_bg4 = pygame.transform.rotate(pygame.transform.scale(xfighter_bg4_image, (xfighter_bg4_width,xfighter_bg4_height)),270)
 
    def draw_text (lives, level, target):
        #drawing text
        main_font=pygame.font.SysFont("comicsans", 20)
        main_font_1=pygame.font.SysFont("comicsans", 80)
        label_lives = main_font.render(f"Lives:{lives}",1,(WHITE))
        label_level = main_font_1.render(f"Level: {level}",1,(WHITE))
        label_target = main_font.render(f"Enemies Remaining: {target}",1,(WHITE))
        if lives<=2:
            label_lives = main_font.render(f"Lives:{lives}",1,(RED))

        WIN.blit(label_lives, (10,5))
        WIN.blit(label_level, (325,270))
        WIN.blit(label_target, (670,5))

    def draw_window (vader_bullets, xfighter1_bullets, xfighter2_bullets, xfighter3_bullets, xfighter4_bullets, spaceship_location, spaceship_bg_location, xfighter1_location, xfighter2_location, xfighter3_location, xfighter4_location):

        #placing images on screen
        WIN.blit(rebelfrigate1,(650,100))
        WIN.blit(rebelfrigate2,(550,60))
        
        WIN.blit(empirefrigate1,(50,200))
        WIN.blit(empirefrigate2,(170,100))
        WIN.blit(empirefrigate3,(30,30))
        
        WIN.blit(tie_bg,(spaceship_bg_location.x,spaceship_bg_location.y))
        WIN.blit(tie_bg,(190,150))
        WIN.blit(tie_bg,(155,300))
        WIN.blit(tie_bg,(215,220))
        WIN.blit(tie_bg,(315,50))

        WIN.blit(xfighter_bg1,(450,180))
        WIN.blit(xfighter_bg2,(500,220))
        WIN.blit(xfighter_bg3,(750,200))
        WIN.blit(xfighter_bg4,(650,150))

        WIN.blit(xfighter,(xfighter1_location.x, xfighter1_location.y))
        WIN.blit(xfighter,(xfighter2_location.x, xfighter2_location.y))
        WIN.blit(xfighter,(xfighter3_location.x, xfighter3_location.y))
        WIN.blit(xfighter,(xfighter4_location.x, xfighter4_location.y))
        WIN.blit(spaceship,(spaceship_location.x,spaceship_location.y))

        #draws bullets on screen
        for bullet in vader_bullets:
            pygame.draw.rect(WIN, RED, bullet)
        
        for bullet in xfighter1_bullets:
            pygame.draw.rect(WIN, GREEN, bullet)

        for bullet in xfighter2_bullets:
            pygame.draw.rect(WIN, GREEN, bullet)
        
        for bullet in xfighter3_bullets:
            pygame.draw.rect(WIN, GREEN, bullet)

        for bullet in xfighter4_bullets:
            pygame.draw.rect(WIN, GREEN, bullet)

    def spaceship_icon_movement(keys_pressed, spaceship_location):
            
            # Movement Keys
            keys_pressed = pygame.key.get_pressed()
            if keys_pressed[pygame.K_a] and spaceship_location.x-20 - VEL > 0 : #Move Left 
                spaceship_location.x -= VEL 
            if keys_pressed[pygame.K_d] and spaceship_location.x + VEL + spaceship_location.width < WIDTH-300  : #Move Right
                spaceship_location.x += VEL
            if keys_pressed[pygame.K_w] and spaceship_location.y-20 - VEL > 0 : #Move Up
                spaceship_location.y -= VEL
            if keys_pressed[pygame.K_s] and spaceship_location.y + VEL + spaceship_location.height + 20 < 500 : #Move Down
                spaceship_location.y += VEL   
                

    #bullets for our ship
    def vader_handle_bullets(vader_bullets, xfighter1_location, xfighter2_location, xfighter3_location, xfighter4_location, xfighter_count, target):
        for bullet in vader_bullets:
            bullet.x += BULLET_VEL
            #detects collision
            if bullet.colliderect(xfighter1_location):
                xfighter1_location = pygame.Rect(950, random.randint(50, 450), xfighter1_width, xfighter1_height)
                vader_bullets.remove(bullet)
                xfighter_count+=1
                target-=1
                #ship_explosion.play()
              
            if bullet.colliderect(xfighter2_location):
                xfighter2_location=pygame.Rect(950, random.randint(50, 450), xfighter1_width, xfighter1_height)
                vader_bullets.remove(bullet)
                xfighter_count+=1
                target-=1
                #ship_explosion.play()
             
            if bullet.colliderect(xfighter3_location):
                xfighter3_location=pygame.Rect(950, random.randint(50, 450), xfighter1_width, xfighter1_height)
                vader_bullets.remove(bullet)
                xfighter_count+=1
                target-=1
                ship_explosion.play()
               
            if bullet.colliderect(xfighter4_location):
                xfighter4_location=pygame.Rect(950, random.randint(50, 450), xfighter1_width, xfighter1_height)
                vader_bullets.remove(bullet)
                xfighter_count+=1
                target-=1
                ship_explosion.play()
                            
                ship_explosion.play()
         
            if vader_bullets!=[] and bullet.x > WIDTH:
                vader_bullets.remove(bullet)

        return xfighter1_location, xfighter2_location, xfighter3_location, xfighter4_location, xfighter_count, target

    #bullets for enemy ships
    def xfighter_handle_bullets(xfighter_bullets, spaceship_location, lives):
        for bullet in reversed(xfighter_bullets):
            bullet.x -= BULLET_VEL
            if bullet.colliderect(spaceship_location):
                xfighter_bullets.remove(bullet)
                lives = lives - 1
                #tie_hit.play()
            if bullet.x < -200:
                xfighter_bullets.remove(bullet)
            return lives
       
    #background movements
    def spaceship_bg_icon_movement(spaceship_bg_location, spaceship_vel):
        if spaceship_bg_location.x==450:
            spaceship_bg_location.x+=spaceship_vel
            spaceship_vel = -1
        elif spaceship_bg_location.x == 150:
            spaceship_bg_location.x+=spaceship_vel
            spaceship_vel = 1
        else:
            spaceship_bg_location.x+=spaceship_vel
            spaceship_bg_location.y-=spaceship_vel
        return spaceship_vel

    #movement for enemy
    #increase in speed for movement of wnwmy
    def xfighter_icon_movement(xfighter_location, level):
        xfight_vel = XFIGHTER_VEL
        if xfighter_location.x>-50:
            xfight_vel*=level
            xfighter_location.x-=xfight_vel
        elif xfighter_location.x==-50:
            xfighter_location.x+=900
            xfighter_location.y=random.randint(100,400)
            
    #Implement     
    # When game end    
    def gameover(WIN):
        pygame.mixer.music.stop()
        
        gameoverfont1=pygame.font.SysFont('comicsans',50)
        gameoverfont2=pygame.font.SysFont('comicsans',30)
        text1=gameoverfont1.render('Defeat!', 1 ,RED)
        text2=gameoverfont2.render('Play again? Press y or n', 1 ,RED)
       
        WIN.blit(text1,(350,140))
        WIN.blit(text2,(275,200))

    def main():
        
        lives = 5
        level = 1
        target = 15

        spaceship_location=pygame.Rect(100,200, spaceship_width, spaceship_height)
        spaceship_bg_location=pygame.Rect(170,330, tie_bg_width, tie_bg_height)

        xfighter1_location=pygame.Rect(940,random.randint(50, 450), xfighter1_width, xfighter1_height)
        xfighter2_location=pygame.Rect(1150,random.randint(50, 450), xfighter1_width, xfighter1_height)
        xfighter3_location=pygame.Rect(1000,random.randint(50, 450), xfighter1_width, xfighter1_height)
        xfighter4_location=pygame.Rect(1050,random.randint(50, 450), xfighter1_width, xfighter1_height)

        vader_bullets=[]
        xfighter1_bullets=[]
        xfighter2_bullets=[]
        xfighter3_bullets=[]
        xfighter4_bullets=[]
        
        xfighter_count = 0
        spaceship_velocity = 1 

        clock = pygame.time.Clock()
        run = True
        while run:
            clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False 
                  
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE and len(vader_bullets) <= MAX_BULLETS_VADER:
                        bullet_tie=pygame.Rect(spaceship_location.x-10 + spaceship_location.width, spaceship_location.y-4 + spaceship_location.height//2 - 2, 8, 5)
                        vader_bullets.append(bullet_tie)
                        bulletfire_sound.play()

                    # To restart the game (Press r)
                    if event.key == pygame.K_r or event.key == pygame.K_y:
                        begin()

                    # Quits game (Press q)
                    if event.key == pygame.K_q:
                        pygame.quit()

                    # Go to menu (Press m)
                    if event.key == pygame.K_m or event.key == pygame.K_n:
                        menu.mainloop(WIN)

            if len(xfighter1_bullets) <= MAX_BULLETS_XFIGHTER:
                bullet1 = pygame.Rect(xfighter1_location.x-10, xfighter1_location.y-4 + xfighter1_location.height//2 - 2, 8, 5)
                xfighter1_bullets.append(bullet1)
                xfighter_sound.play()
            if len(xfighter2_bullets) <= MAX_BULLETS_XFIGHTER:
                bullet2 = pygame.Rect(xfighter2_location.x-10, xfighter2_location.y-4 + xfighter2_location.height//2 - 2, 8, 5)
                xfighter2_bullets.append(bullet2)
                #xfighter_sound.play()
            if len(xfighter3_bullets) <= MAX_BULLETS_XFIGHTER:
                bullet3 = pygame.Rect(xfighter3_location.x-10, xfighter3_location.y-4 + xfighter3_location.height//2 - 2, 8, 5)
                xfighter3_bullets.append(bullet3)
                #xfighter_sound.play()
            if len(xfighter4_bullets) <= MAX_BULLETS_XFIGHTER:
                bullet4 = pygame.Rect(xfighter4_location.x-10, xfighter4_location.y-4 + xfighter4_location.height//2 - 2, 8, 5)
                xfighter4_bullets.append(bullet4)
                xfighter_sound.play()

            keys_pressed = pygame.key.get_pressed()
            #calling
            spaceship_icon_movement(keys_pressed, spaceship_location)
            spaceship_velocity = spaceship_bg_icon_movement(spaceship_bg_location, spaceship_velocity)
            
            xfighter1_location, xfighter2_location, xfighter3_location, xfighter4_location, xfighter_count, target = vader_handle_bullets(vader_bullets, xfighter1_location, xfighter2_location, xfighter3_location, xfighter4_location, xfighter_count, target)
            
            xfighter_icon_movement(xfighter1_location, level)
            xfighter_icon_movement(xfighter2_location, level)
            xfighter_icon_movement(xfighter3_location, level)
            xfighter_icon_movement(xfighter4_location, level)
            
            lives = xfighter_handle_bullets(xfighter1_bullets, spaceship_location, lives)
            lives = xfighter_handle_bullets(xfighter2_bullets, spaceship_location, lives)
            lives = xfighter_handle_bullets(xfighter3_bullets, spaceship_location, lives)
            lives = xfighter_handle_bullets(xfighter4_bullets, spaceship_location, lives)
            
            #check_bullet_collision(vader_bullets, xfighter1_bullets, xfighter2_bullets, xfighter3_bullets, xfighter4_bullets)
            
            # Display
            WIN.blit(bg,(0,0))

            if(lives == 0):
                gameover(WIN)
                pygame.display.update()
                pygame.time.delay(4000)
                #run = False
                #menu.mainloop(WIN)
            
            if (xfighter_count >= LEVEL_UP_KILLS and level <= VICTORY_LEVEL):
                
                level += 1
            
                if(level == VICTORY_LEVEL and xfighter_count >= LEVEL_UP_KILLS):
                    spaceship_location.x + VEL > 930
                    
                    gameoverfont1=pygame.font.SysFont('comicsans',50)
                    gameoverfont2=pygame.font.SysFont('comicsans',30)
                    text1=gameoverfont1.render('Victory!', 1 ,RED)
                    text2=gameoverfont2.render('Play again? Press y or n', 1 ,RED)

                    WIN.blit(text1,(340,140))
                    WIN.blit(text2,(275,200))
                    pygame.display.update()
                    pygame.time.delay(8000)
                    lives = 5
                    level = 1
                    target=15
                    
                xfighter_count = 0
                
            else:
                draw_text(lives, level, target)
                draw_window(vader_bullets,  xfighter1_bullets, xfighter2_bullets, xfighter3_bullets, xfighter4_bullets, spaceship_location,  spaceship_bg_location, xfighter1_location, xfighter2_location, xfighter3_location, xfighter4_location)
            
            

            pygame.display.update()

        pygame.quit()

    if __name__=="__main__":
        main()

#controls screen
def controls():
    run = True
    while run:
        #clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False 
              
            if event.type == pygame.KEYDOWN:
                # Go to menu (Press m)
                if event.key == pygame.K_m:
                    menu.mainloop(WIN)
        WIN.blit(bg,(0,0))

        main_font=pygame.font.SysFont("comicsans", 40)
        label_instructions1 = main_font.render("W = Go Up", 15, (255, 255, 255))
        label_instructions2 = main_font.render("A = Go Left", 15, (255, 255, 255))
        label_instructions3 = main_font.render("D = Go Right", 15, (255, 255, 255))
        label_instructions4 = main_font.render("S = Go Down", 15, (255, 255, 255))
        label_instructions5 = main_font.render("Press m to go to Menu", 15, (255, 255, 255))
        label_instructions6 = main_font.render("Press r to restart (in game)", 15, (255, 255, 255))

        WIN.blit(label_instructions1, (300,60))
        WIN.blit(label_instructions2, (300,120))
        WIN.blit(label_instructions3, (300,180))
        WIN.blit(label_instructions4, (300,240))
        WIN.blit(label_instructions5, (220,300))
        WIN.blit(label_instructions6, (170,360))

        pygame.display.update()

#objectives screen
def objective():
    run = True
    while run:
        #clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False 
              
            if event.type == pygame.KEYDOWN:
                # Go to menu (Press m)
                if event.key == pygame.K_m:
                    menu.mainloop(WIN)
        WIN.blit(bg,(0,0))

        main_font=pygame.font.SysFont("comicsans", 30)
        label_instructions1 = main_font.render("There are a maximum of 3 levels.", 15, (255, 255, 255))
        label_instructions2 = main_font.render("In each level you have to take out ", 15, (255, 255, 255))
        label_instructions3 = main_font.render("atleast 5 xwings to progress ", 15, (255, 255, 255))
        label_instructions4 = main_font.render("GOOD LUCK!", 15, (255, 255, 255))
        
        WIN.blit(label_instructions1, (100,60))
        WIN.blit(label_instructions2, (100,120))
        WIN.blit(label_instructions3, (100,180))
        WIN.blit(label_instructions4, (100,240))
        
        pygame.display.update()

#for making menu
def mainmenu():
    global menu
    
    menu=pygame_menu.Menu("WELCOME TROOPER", 900, 500, theme=pygame_menu.themes.THEME_DARK)
    menu.add.button("PLAY", begin)
    menu.add.button("CONTROLS", controls)
    menu.add.button("OBJECTIVE", objective)
    menu.add.button("QUIT", pygame_menu.events.EXIT)
    
mainmenu()

menu.mainloop(WIN)
    
    
    
