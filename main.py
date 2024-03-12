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