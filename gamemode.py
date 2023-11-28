import pygame

class Gamemode:

    def __init__(self, screen, character, surf, rect):
        self.screen = screen
        self.character = character
        self.surf = surf
        self.rect = rect

    def change_gamemode(self):

        if (self.character == "CUBE"):
            self.screen.blit(self.surf, self.rect)

        elif (self.character == "UFO"):
            self.screen.blit(self.surf, self.rect)

