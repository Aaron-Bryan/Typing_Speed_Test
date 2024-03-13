import pygame
from pygame.locals import *
import sys
import time
import random

#Create class for typing speed test
class typing_speed_test:

    def __init__(self):
        self.width = 750
        self.height = 500
        self.reset = True
        self.active = False
        self.input_text = ""
        self.word = ""
        self.starting_time = 0
        self.end_time = 0
        self.typing_accuracy = "0%"
        self.wpm = 0
        self.results = "Time: 0  Accuracy: 0%  Wpm: 0"
        self.end = False
        self.head_color = (255,213,102)
        self.text_color = (240,240,240)
        self.results_color = (255,70,70)

        #Initialize pygme
        pygame.init()

        #Load the images to draw
        self.startup_img = pygame.image.load(r"resources/startup.jpg")
        self.startup_img = pygame.transform.scale(self.startup_img, (self.width, self.height))

        self.background = pygame.image.load(r"resources/background.jpg")
        self.background = pygame.transform.scale(self.background, (self.width, self.height))

        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Typing Speed test")

    #Methods

    #Method for drawing the text on the screen
    def draw_text(self, screen, message, y_pos, font_size, color):
        font = pygame.font.Font(None, font_size)
        text = font.render(message, 1, color)
        text_rect = text.get_rect(center=(self.width / 2, y_pos))

        screen.blit(text, text_rect)
        pygame.display.update()