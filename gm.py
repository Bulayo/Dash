import pygame

class Gamemode:

    def __init__(self, screen, surf, rect):
        self.screen = screen
        self.surf = surf
        self.rect = rect

    def draw_img(self):
        self.screen.blit(self.surf, self.rect)

    def change_gamemode(self, character):
        self.character = character

        if (self.character == "G_CUBE"):
            self.screen.blit(self.surf, self.rect)

        if (self.character == "F_CUBE"):
            self.screen.blit(self.surf, self.rect)

        if (self.character == "R_CUBE"):
            self.screen.blit(self.surf, self.rect)

        if (self.character == "G_UFO"):
            self.screen.blit(self.surf, self.rect)

        if (self.character == "F_UFO"):
            self.screen.blit(self.surf, self.rect)

        if (self.character == "R_UFO"):
            self.screen.blit(self.surf, self.rect)

            

