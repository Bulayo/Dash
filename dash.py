import pygame, sys

def draw_img():

    WIN.blit(bg_surf, bg_rect)
    WIN.blit(bg_surf, bg_rect_2)
    WIN.blit(ground_surf, ground_rect)
    WIN.blit(ground_surf, ground_rect_2)
    if (START_GAME is False):
        WIN.blit(logo_surf, logo_rect)
        WIN.blit(button_surf, button_rect)
    WIN.blit(player_surf, player_rect)
    

def bg_scroll():

    if (START_GAME is True):
        bg_speed = 5
        bg_rect.x -= bg_speed
        bg_rect_2.x -= bg_speed
        ground_rect.x -= bg_speed
        ground_rect_2.x -= bg_speed

        if (bg_rect.right <= 0):
            bg_rect.x = 800

        elif (bg_rect_2.right <= 0):
            bg_rect_2.x = 800

        if (ground_rect.right <= 0):
            ground_rect.x = 800
        
        elif (ground_rect_2.right <= 0):
            ground_rect_2.x = 800

  

def obj_movement():
    pass
  
def player_movement():
    global player_gravity

    player_gravity += 0.7
    if (player_gravity > 5):
        player_gravity = 5
    player_rect.y += int(player_gravity)

    if (player_rect.bottom >= 400):
        player_rect.bottom = 400

pygame.init()

WIDTH, HEIGHT = 800, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
FONT = pygame.font.Font("assets/pusab.otf", 50)
logo_surf = pygame.image.load("assets/logo.png").convert_alpha()
logo_rect = logo_surf.get_rect(topleft= (300, 50))

MENU_THEME = pygame.mixer.Sound("assets/Menu-theme.mp3")
MENU_THEME.play(loops= 10)
GAME_MUSIC = pygame.mixer.Sound("assets/stereo-madness.mp3")
START_GAME = False
END_GAME = False

#point_surf = FONT.render("Dash", False, "green")
#point_rect = point_surf.get_rect(center= (800/2, 100))

pygame.display.set_caption("Dash")
FPS = 60
clock = pygame.time.Clock()


bg_surf = pygame.image.load("assets/background.png").convert_alpha()
bg_rect = bg_surf.get_rect(topleft= (0, 0))
bg_rect_2 = bg_surf.get_rect(topleft= (800, 0))

ground_surf = pygame.image.load("assets/ground2.png").convert_alpha()
ground_rect = ground_surf.get_rect(topleft= (0, 400))
ground_rect_2 = ground_surf.get_rect(topleft= (800, 400))

button_surf = pygame.image.load("assets/play-button.png").convert_alpha()
button_rect = button_surf.get_rect(center= (800/2, 500/2))

player_surf = pygame.image.load("assets/p-sprite3.png").convert_alpha()
player_rect = player_surf.get_rect(topleft= (20, 400))
player_gravity = 0


while True:

    clock.tick(FPS)
    mouse_pos = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if (event.type == pygame.QUIT):
            pygame.quit()
            sys.exit()
        
        elif (event.type == pygame.MOUSEBUTTONDOWN):
            if (button_rect.collidepoint(mouse_pos) and START_GAME is False):
                START_GAME = True
                MENU_THEME.fadeout(1000)
                GAME_MUSIC.play()

        elif (event.type == pygame.KEYDOWN and player_rect.bottom >= 380):
            if (event.key == pygame.K_w or event.key == pygame.K_SPACE or event.key == pygame.K_UP):
                player_gravity = -15
        
        if (event.type == pygame.MOUSEBUTTONDOWN and player_rect.bottom >= 380):
            player_gravity = -15


    draw_img()
    bg_scroll()
    player_movement()

    pygame.display.update()