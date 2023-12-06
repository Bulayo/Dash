import pygame, sys, gm

def draw_sprites():

    BACKGROUNG.draw_img()
    BACKGROUNG2.draw_img()
    GROUND.draw_img()
    GROUND2.draw_img()
    FLIP_PORTAL.draw_img()
    REVERSE_PORTAL.draw_img()
    UFO_PORTAL.draw_img()
    CUBE_PORTAL.draw_img()

    if START_GAME is False:
        BUTTON.draw_img()
        LOGO.draw_img()

    if CURRENT_GM == "G_CUBE":
        CUBE.change_gamemode("G_CUBE")

    if CURRENT_GM == "F_CUBE":
        F_CUBE.change_gamemode("F_CUBE")

    if CURRENT_GM == "R_CUBE":
        R_CUBE.change_gamemode("R_CUBE")

    if CURRENT_GM == "G_UFO":
        UFO.change_gamemode("G_UFO")



def bg_scroll():

    bg_speed = 5

    if START_GAME:
        
        bg_rect.x -= bg_speed
        bg_rect_2.x -= bg_speed

        if (bg_rect.right <= 0):
            bg_rect.x = 800

        elif (bg_rect_2.right <= 0):
            bg_rect_2.x = 800


def move_objects():
    obj_speed = 5
    
    if START_GAME:
        flip_portal_rect.x -= obj_speed
        reverse_portal_rect.x -= obj_speed
        ufo_portal_rect.x -= obj_speed
        cube_portal_rect.x -= obj_speed


def gamemode_state(state):
    global CURRENT_GM
    global G_CUBE_GRAV
    global F_CUBE_GRAV
    global R_CUBE_GRAV
    global G_UFO_GRAV
    global F_UFO_GRAV
    global R_UFO_GRAV

    if (state == "G_CUBE"):
        G_CUBE_GRAV += 1.3

        if (G_CUBE_GRAV > 8):
            G_CUBE_GRAV = 8

        cube_rect.y += G_CUBE_GRAV

        if (cube_rect.bottom >= 400):
            cube_rect.bottom = 400

    if (state == "F_CUBE"):
        F_CUBE_GRAV += 1.3

        if (F_CUBE_GRAV > 8):
            F_CUBE_GRAV = 8

        cube_rect_180.y -= F_CUBE_GRAV

        if (cube_rect_180.top <= 0):
            cube_rect_180.top = 0

    if (state == "R_CUBE"):
        R_CUBE_GRAV += 1.3

        if (R_CUBE_GRAV > 8):
            R_CUBE_GRAV = 8

        R_cube_rect.y += R_CUBE_GRAV

        if (R_cube_rect.bottom >= 400):
            R_cube_rect.bottom = 400

    if (state == "G_UFO"):
        G_UFO_GRAV += 0.5

        if (G_UFO_GRAV > 5):
            G_UFO_GRAV = 5
        ufo_rect.y += G_UFO_GRAV
        
        if (ufo_rect.bottom >= 400):
            ufo_rect.bottom = 400

        elif (ufo_rect.top <= 0):
            ufo_rect.top = 0




def change_state():
    global CURRENT_GM

    if (cube_portal_rect.colliderect(ufo_rect)):
        CURRENT_GM = "G_CUBE"
        
    if (flip_portal_rect.colliderect(cube_rect)):
        CURRENT_GM = "F_CUBE"

    if (reverse_portal_rect.colliderect(cube_rect_180)):
        CURRENT_GM = "R_CUBE"

    if (ufo_portal_rect.colliderect(R_cube_rect)):
        CURRENT_GM = "G_UFO"
    
pygame.init()

WIDTH, HEIGHT = 800, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
FONT = pygame.font.Font("assets/pusab.otf", 50)
logo_surf = pygame.image.load("assets/logo.png").convert_alpha()
logo_rect = logo_surf.get_rect(topleft= (300, 50))
LOGO = gm.Gamemode(WIN, logo_surf, logo_rect)

MENU_THEME = pygame.mixer.Sound("assets/Menu-theme.mp3")
MENU_THEME.play(loops= 10)
GAME_MUSIC = pygame.mixer.Sound("assets/stereo-madness.mp3")
START_GAME = False
END_GAME = False

CURRENT_GM = "G_CUBE"

#point_surf = FONT.render("Dash", False, "green")
#point_rect = point_surf.get_rect(center= (800/2, 100))

pygame.display.set_caption("Dash")
FPS = 60
clock = pygame.time.Clock()

bg_surf = pygame.image.load("assets/background.png").convert_alpha()
bg_rect = bg_surf.get_rect(topleft= (0, 0))
bg_rect_2 = bg_surf.get_rect(topleft= (800, 0))
BACKGROUNG = gm.Gamemode(WIN, bg_surf, bg_rect)
BACKGROUNG2 = gm.Gamemode(WIN, bg_surf, bg_rect_2)

ground_surf = pygame.image.load("assets/ground2.png").convert_alpha()
ground_rect = ground_surf.get_rect(topleft= (0, 400))
ground_rect_2 = ground_surf.get_rect(topleft= (800, 400))
GROUND = gm.Gamemode(WIN, ground_surf, ground_rect)
GROUND2 = gm.Gamemode(WIN, ground_surf, ground_rect_2)

button_surf = pygame.image.load("assets/play-button.png").convert_alpha()
button_rect = button_surf.get_rect(center= (800/2, 500/2))
BUTTON = gm.Gamemode(WIN, button_surf, button_rect)

cube_surf = pygame.image.load("assets/p-sprite3.png").convert_alpha()
cube_rect = cube_surf.get_rect(topleft= (20, 400))
R_cube_rect = cube_surf.get_rect(topleft= (20, 0))
CUBE = gm.Gamemode(WIN, cube_surf, cube_rect)
R_CUBE = gm.Gamemode(WIN, cube_surf, R_cube_rect)

cube_surf_180 = pygame.transform.rotate(cube_surf, -180)
cube_rect_180 = cube_surf_180.get_rect(bottomleft= (20, 400))
F_CUBE = gm.Gamemode(WIN, cube_surf_180, cube_rect_180)

G_CUBE_GRAV = 0
F_CUBE_GRAV = 0
R_CUBE_GRAV = 0

ufo_surf = pygame.image.load("assets/ufo.png").convert_alpha()
ufo_rect = ufo_surf.get_rect(topleft= (20, 400))
R_ufo_rect = ufo_surf.get_rect(topleft= (20, 0))
UFO = gm.Gamemode(WIN, ufo_surf, ufo_rect)
R_UFO = gm.Gamemode(WIN, ufo_surf, R_ufo_rect)

ufo_surf_180 = pygame.transform.rotate(ufo_surf, -180)
ufo_rect_180 = ufo_surf_180.get_rect(bottomleft= (20, 400))
F_UFO = gm.Gamemode(WIN, ufo_surf_180, ufo_rect_180)

G_UFO_GRAV = 0
F_UFO_GRAV = 0
R_UFO_GRAV = 0

ufo_portal_surf = pygame.image.load("assets/ufo-portal.png").convert_alpha()
ufo_portal_surf = pygame.transform.scale(ufo_portal_surf, (100, 150))
ufo_portal_rect = ufo_portal_surf.get_rect(topleft= (2600, 250))
UFO_PORTAL = gm.Gamemode(WIN, ufo_portal_surf, ufo_portal_rect)

cube_portal_surf = pygame.image.load("assets/cube-portal.png").convert_alpha()
cube_portal_surf = pygame.transform.scale(cube_portal_surf, (100, 150))
cube_portal_rect = cube_portal_surf.get_rect(topleft= (3600, 250))
CUBE_PORTAL = gm.Gamemode(WIN, cube_portal_surf, cube_portal_rect)

flip_portal_surf = pygame.image.load("assets/up.png").convert_alpha()
flip_portal_surf = pygame.transform.scale(flip_portal_surf, (100, 150))
flip_portal_rect = flip_portal_surf.get_rect(topleft= (1200, 250))
FLIP_PORTAL = gm.Gamemode(WIN, flip_portal_surf, flip_portal_rect)

reverse_portal_surf = pygame.image.load("assets/down.png").convert_alpha()
reverse_portal_surf = reverse_portal_surf = pygame.transform.scale(reverse_portal_surf, (100, 150))
reverse_portal_rect = reverse_portal_surf.get_rect(topleft= (1900, 0))
REVERSE_PORTAL = gm.Gamemode(WIN, reverse_portal_surf, reverse_portal_rect)

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

        elif (event.type == pygame.KEYDOWN):
            if (event.key == pygame.K_w or event.key == pygame.K_SPACE or event.key == pygame.K_UP):

                if CURRENT_GM == "G_CUBE" and cube_rect.bottom >= 385:
                    G_CUBE_GRAV = -15

                elif CURRENT_GM == "F_CUBE" and cube_rect_180.top <= 15:
                    F_CUBE_GRAV = -15

                elif CURRENT_GM == "R_CUBE" and R_cube_rect.bottom >= 385:
                    R_CUBE_GRAV = -15

                elif CURRENT_GM == "G_UFO":
                    G_UFO_GRAV = -10


        if (event.type == pygame.MOUSEBUTTONDOWN):

            if CURRENT_GM == "G_CUBE" and cube_rect.bottom >= 385:
                G_CUBE_GRAV = -15

            elif CURRENT_GM == "F_CUBE" and cube_rect_180.top <= 15:
                F_CUBE_GRAV = -15

            elif CURRENT_GM == "R_CUBE" and R_cube_rect.bottom >= 385:
                R_CUBE_GRAV = -15

            elif CURRENT_GM == "G_UFO":
                G_UFO_GRAV = -10

    draw_sprites()
    bg_scroll()
    gamemode_state(CURRENT_GM)
    change_state()
    move_objects()

    pygame.display.update()