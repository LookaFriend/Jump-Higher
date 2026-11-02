from tracemalloc import start

import pygame , time , random, sys
pygame.init

WIDTH, HEIGHT = 1000, 700
pygame.display.set_caption("Jump Higher")
BG =  pygame.display.set_mode((WIDTH, HEIGHT))
timer = pygame.time.Clock()

# game variables
PLAYER_WIDTH, PLAYER_HEIGHT = 50, 50
fps = 60
player_x = 475
player_y = HEIGHT - PLAYER_HEIGHT - 50
player_speed_y = 0
player_speed_x = 0
y_change = 0
max_plat = 10
scroll_thresh = 200
scroll = 0

class Platform():
    def __init__(self,x,y,width,height):
        self.rect = pygame.Rect(x,y,width,height)
        self.rect.x = x
        self.rect.y = y

    def update(self,scroll):
        self.rect.y += scroll
        #check if plat off screen
        if self.rect.top > HEIGHT:
            self.kill()


platform = Platform(WIDTH/2 - 40, 650, 80, 10)

def animate_player():
    global player_speed_x, player_x, player_y, event, player_speed_y, platform, start_platform, scroll,scroll_thresh
    player.x += player_speed_x
    player.y += player_speed_y

    #collision with platforms
    for platform in platform_list:
        if player.colliderect(platform):
            if player.bottom <= platform.top + 10:  
                player_speed_y = 0  
                player.bottom = platform.top 
                player.y -= 200
    if player.colliderect(start_platform):
        if player.bottom <= start_platform.top + 10:  
            player_speed_y = 0  
            player.bottom = start_platform.top 
            player.y -= 200
    if player.top <= scroll_thresh:
        scroll = player.y
    

#make list
platform_list = [pygame.Rect(100, 300, 80, 10)]

start_platform = pygame.Rect(WIDTH/2 -40, 650, 80, 10)

for p in range(max_plat):
    plat_width = random.randint(50, 100)
    plat_x = random.randint(0, WIDTH - plat_width)
    plat_y = p * random.randint(80, 100)
    platform = Platform(plat_x, plat_y, plat_width, 10)
    platform_list.append(pygame.Rect(plat_x, plat_y, plat_width, 10))

def able_jump():
    global player, platform
    if player.colliderect(platform):
        player.y = -150
    
def reset_player():
    if player.bottom >= HEIGHT:
        player.y = 600
        player.x = WIDTH/2 - 15

pygame.font.init()
score_font = pygame.font.Font(None, 100)

player = pygame.Rect(WIDTH/2,670,30,30)
player.center = (player.width/2, player.height/2)

plat_x = random.choice(range(0, 501))
plat_y = 40

points = 0
player_points = points 
height_gained = player.y 

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                able_jump()
            if event.key == pygame.K_a:
                player_speed_x = -6
            if event.key == pygame.K_d:
                player_speed_x = 6
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                player_speed_x = 0
            if event.key == pygame.K_d:
                player_speed_x = 0
            
    BG.fill('Light blue')
    #defs
    animate_player()
    reset_player()
    scroll = animate_player

    pygame.draw.rect(BG, 'dark gray', start_platform, 0 )

   

    #draw
    for platform in platform_list:
        pygame.draw.rect(BG, 'dark gray', platform, 0 )
    pygame.draw.rect(BG, 'blue', player, 0 )
   
    player_score_suface = score_font.render(str(player_points),True, "blue")
    BG.blit(player_score_suface, (10, 10))
    
    player_speed_y = 3
    
    pygame.display.update()
    pygame.display.flip()
    timer.tick(fps)
pygame.quit()