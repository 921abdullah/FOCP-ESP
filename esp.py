import pygame
import os
pygame.font.init()
pygame.mixer.init()

WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("First Game!")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
# Velocity of rocket
VEL=4

# Max frame rate for game to run
FPS=60

spaceship_width, spaceship_height = 40, 50

spaceship_image = pygame.image.load(os.path.join("Assets", "lightside2.png"))

spaceship = pygame.transform.scale(spaceship_image, (spaceship_width,spaceship_height))

def draw_window(spaceship_location):
    WIN.fill(WHITE)
    WIN.blit(spaceship,(spaceship_location.x,spaceship_location.y))
    pygame.display.update()

def spaceship_icon_movement(keys_pressed, spaceship_location):
        
        # Movement Keys
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_a] and spaceship_location.x - VEL > 0 : #Move Left 
            spaceship_location.x -= VEL 
        if keys_pressed[pygame.K_d] and spaceship_location.x + VEL + spaceship_location.width < WIDTH  : #Move Right
            spaceship_location.x += VEL
        if keys_pressed[pygame.K_w] and spaceship_location.y - VEL > 0 : #Move Up
            spaceship_location.y -= VEL
        if keys_pressed[pygame.K_s] and spaceship_location.y + VEL + spaceship_location.height < HEIGHT : #Move Down
            spaceship_location.y += VEL   

def main():
    spaceship_location=pygame.Rect(425,300, spaceship_width, spaceship_height)
    
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False 

        keys_pressed = pygame.key.get_pressed()
        spaceship_icon_movement(keys_pressed, spaceship_location)
        draw_window(spaceship_location)

    pygame.quit()

if __name__=="__main__":
    main()
    
