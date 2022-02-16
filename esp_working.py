import pygame
import pygame_menu
from random import random, randrange

pygame.init()
pygame.font.init()
pygame.mixer.init()

WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Star Wars 22")

bg_width,bg_height=900,500
bg_image=pygame.image.load("planet.png")
bg=pygame.transform.scale(bg_image,(bg_width, bg_height))

def begin():
    
    bulletfire_sound = pygame.mixer.Sound("Bullet.mp3")
    bg_sound= pygame.mixer.Sound("music.mp3")
    bg_music = pygame.mixer.music.load("music.mp3")
    pygame.mixer.music.play(-1)
    
    # Colours
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    RED=(255,0,0)
    GREEN=(0,255,0)
    BLUE=(0,0,255)

    xfighter1_hit = pygame.USEREVENT + 1
    spaceship_hit = pygame.USEREVENT + 2

    # Velocity of ship
    VEL=4
    # Velocity of bullets
    BULLET_VEL=7
    # Max no. of our bullets on screen at a time
    MAX_BULLETS=2
    # Enemy velocity
    XFIGHTER_VEL=6

    level=1
    lives=5

    # Max frame rate for game to run
    FPS=60

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
    
    xfighter1_width, xfighter1_height= 40, 50
    xfighter_bg1_width, xfighter_bg1_height=20,20
    xfighter_bg2_width, xfighter_bg2_height=20,20
    xfighter_bg3_width, xfighter_bg3_height=20,20
    xfighter_bg4_width, xfighter_bg4_height=20,20
    
    xfighter1_image=pygame.image.load("xfighter pixel.png")
    xfighter1=pygame.transform.rotate(pygame.transform.scale(xfighter1_image, (xfighter1_width, xfighter1_height)),270)
    xfighter1_image=pygame.image.load("xfighter pixel.png")
    xfighter1=pygame.transform.rotate(pygame.transform.scale(xfighter1_image, (xfighter1_width, xfighter1_height)),270)

    xfighter_bg1_image=pygame.image.load("xfighter pixel.png")
    xfighter_bg1 = pygame.transform.rotate(pygame.transform.scale(xfighter_bg1_image, (xfighter_bg1_width,xfighter_bg1_height)),270)
    
    xfighter_bg2_image=pygame.image.load("xfighter pixel.png")
    xfighter_bg2 = pygame.transform.rotate(pygame.transform.scale(xfighter_bg2_image, (xfighter_bg2_width,xfighter_bg2_height)),270)
   
    xfighter_bg3_image=pygame.image.load("xfighter pixel.png")
    xfighter_bg3 = pygame.transform.rotate(pygame.transform.scale(xfighter_bg3_image, (xfighter_bg3_width,xfighter_bg3_height)),270)
    
    xfighter_bg4_image=pygame.image.load("xfighter pixel.png")
    xfighter_bg4 = pygame.transform.rotate(pygame.transform.scale(xfighter_bg4_image, (xfighter_bg4_width,xfighter_bg4_height)),270)

    def draw_window (vader_bullets, spaceship_location, spaceship_bg_location):
        WIN.blit(bg,(0,0))
        
        WIN.blit(rebelfrigate1,(650,100))
        WIN.blit(rebelfrigate2,(550,60))
        
        WIN.blit(empirefrigate1,(50,200))
        WIN.blit(empirefrigate2,(170,100))
        WIN.blit(empirefrigate3,(30,30))
        
        WIN.blit(tie_bg,(spaceship_bg_location.x,spaceship_bg_location.y))
        WIN.blit(tie_bg,(310,505))
        WIN.blit(tie_bg,(155,300))
        WIN.blit(tie_bg,(215,220))
        WIN.blit(tie_bg,(315,50))

        WIN.blit(xfighter_bg1,(450,180))
        WIN.blit(xfighter_bg2,(500,220))
        WIN.blit(xfighter_bg3,(750,200))
        WIN.blit(xfighter_bg4,(650,150))

        #drawing text
        main_font=pygame.font.SysFont("comicsans", 20)
        label_lives = main_font.render(f"Lives:{lives}",1,(255,255,255))
        label_level = main_font.render(f"Level: {level}",1,(255,255,255))

        WIN.blit(label_lives, (10,10))
        WIN.blit(label_level, (800,10))
        
        WIN.blit(xfighter1,(700,400))
        WIN.blit(xfighter1,(700,150))
        WIN.blit(spaceship,(spaceship_location.x-300,spaceship_location.y-50))

        for bullet in vader_bullets:
            pygame.draw.rect(WIN, GREEN, bullet)
                
        
        pygame.display.update()

    def spaceship_icon_movement(keys_pressed, spaceship_location):
            
            # Movement Keys
            keys_pressed = pygame.key.get_pressed()
            if keys_pressed[pygame.K_a] and spaceship_location.x-300 - VEL > 0 : #Move Left 
                spaceship_location.x -= VEL 
            if keys_pressed[pygame.K_d] and spaceship_location.x + VEL + spaceship_location.width < WIDTH-300  : #Move Right
                spaceship_location.x += VEL
            if keys_pressed[pygame.K_w] and spaceship_location.y-50 - VEL > 0 : #Move Up
                spaceship_location.y -= VEL
            if keys_pressed[pygame.K_s] and spaceship_location.y + VEL + spaceship_location.height - 50 < HEIGHT : #Move Down
                spaceship_location.y += VEL   
                

    def handle_bullets(vader_bullets):
        for bullet in vader_bullets:
            bullet.x += BULLET_VEL
            if  bullet.x > WIDTH:
                vader_bullets.remove(bullet)
        
       
    def spaceship_bg_icon_movement(spaceship_bg_location):
    
        if spaceship_bg_location.x<450:
            spaceship_bg_location.x+=1
        elif spaceship_bg_location.x==450:
            spaceship_bg_location.x-=100

  
    def main():
        tie_bg_width, tie_bg_height=20,20
        spaceship_location=pygame.Rect(425,300, spaceship_width, spaceship_height)
        spaceship_bg_location=pygame.Rect(170,330, tie_bg_width, tie_bg_height)
        xfighter1_location=pygame.Rect(700,400, xfighter1_width, xfighter1_height)
        

        vader_bullets=[]
        xfighter1_bullets=[]
        
        clock = pygame.time.Clock()
        run = True
        while run:
            clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False 
                  
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE and len(vader_bullets) < MAX_BULLETS:
                        bullet=pygame.Rect(spaceship_location.x-300 + spaceship_location.width, spaceship_location.y-50 + spaceship_location.height//2 - 2, 8, 5)
                        vader_bullets.append(bullet)
                        bulletfire_sound.play()

                    if event.key == pygame.K_p and len(xfighter1_bullets) < MAX_BULLETS:
                        bullet = pygame.Rect(xfighter1_location.x+300, xfighter1_location.y+5 + xfighter1_location.height//2 - 2, 10, 5)
                        xfighter1_bullets.append(bullet)
            
            keys_pressed = pygame.key.get_pressed()
            spaceship_icon_movement(keys_pressed, spaceship_location)
            spaceship_bg_icon_movement(spaceship_bg_location)
            handle_bullets(vader_bullets)
            draw_window(vader_bullets, spaceship_location, spaceship_bg_location)
            
        pygame.quit()

    if __name__=="__main__":
        main()

def mainmenu():
    global menu

    menu=pygame_menu.Menu("WELCOME TROOPER", 900, 500, theme=pygame_menu.themes.THEME_DARK)
    menu.add.text_input("Identity Number:")
    menu.add.button("PLAY", begin)
    menu.add.button("QUIT", pygame_menu.events.EXIT)
mainmenu()

menu.mainloop(WIN)
    
