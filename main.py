import pygame
from pygame.locals import *
import sys
import time
import random

#Create class for the typing speed test
class typing_speed_test:

    def __init__(self):
        self.width = 750
        self.height = 500
        self.reset_state = True
        self.active = False
        self.input_text = ""
        self.word = ""
        self.starting_time = 0
        self.end_time = 0
        self.typing_accuracy = "0%"
        self.results = "Time:0 Accuracy:0 % Wpm:0 "
        self.wpm = 0
        self.end = False
        self.head_color = (255, 213, 102)
        self.text_color = (240, 240, 240)
        self.result_color = (255, 70, 70)

        pygame.init()
        self.startup = pygame.image.load(r"resources/startup.jpg")
        self.startup = pygame.transform.scale(self.startup, (self.width, self.height))

        self.background = pygame.image.load(r"resources/background.jpg")
        self.background = pygame.transform.scale(self.background, (self.width, self.height))

        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Typing Speed test")


    #Methods
    #Method to draw the text
    def draw_text(self, screen, msg, y, font_size, color):
        font = pygame.font.Font(None, font_size)
        text = font.render(msg, 1, color)
        text_rect = text.get_rect(center=(self.width / 2, y))

        screen.blit(text, text_rect)
        pygame.display.update()

    #Method to get the sentence from the txt file (Dictionary.txt)
    def get_sentence(self):
        file = open(r"resources/dictionary.txt").read()

        sentence = file.split("\n")
        random_sentence = random.choice(sentence)
        return random_sentence

    #Method to show the results
    def show_results(self, screen):
        if(self.end == False):

            #Calculate the time of the user
            self.end_time = time.time() - self.starting_time

            #Calculate the accuracy of the user
            count = 0
            for i, c in enumerate(self.word):
                try:
                    if(self.input_text[i] == c):
                        count += 1
                except:
                    pass

            self.typing_accuracy = count / len(self.word) * 100

            #Calculate the wpm of the user
            word_count = len(self.input_text) / 5
            self.wpm = word_count / (self.end_time / 60)

            self.end = True
            print(self.end_time)

            self.results = "Time:" + str(round(self.end_time)) + " secs   Accuracy:" + str(round(self.typing_accuracy)) + "%" + "   Wpm: " + str(round(self.wpm))

            #Draw the image that will serve as a button for resetting the state of the program.
            self.reset_img = pygame.image.load(r"resources/icon.png")
            self.reset_img = pygame.transform.scale(self.reset_img, (150, 150))

            screen.blit(self.reset_img, (self.width / 2 - 75, self.height - 140))
            self.draw_text(screen, "Reset", self.height - 70, 26, (100, 100, 100))

            print(self.results)
            pygame.display.update()

    #Main Methods
    def run(self):
        self.reset()

        self.running = True
        while (self.running):
            clock = pygame.time.Clock()
            self.screen.fill((0, 0, 0), (50, 250, 650, 50))
            pygame.draw.rect(self.screen, self.head_color, (50, 250, 650, 50), 2)

            #Updates the text area in respect to user input
            self.draw_text(self.screen, self.input_text, 274, 26, (250, 250, 250))
            pygame.display.update()

            for event in pygame.event.get():
                if(event.type == QUIT):
                    self.running = False
                    sys.exit()

                elif(event.type == pygame.MOUSEBUTTONUP):
                    mouse_pos_x, mouse_pos_y = pygame.mouse.get_pos()

                    #Text area position
                    if(mouse_pos_x >= 50 and mouse_pos_x <= 650 and mouse_pos_y >= 250 and mouse_pos_y <= 300):
                        self.active = True
                        self.input_text = ""
                        self.starting_time = time.time()

                    #Reset button position
                    if(mouse_pos_x >= 310 and mouse_pos_x <= 510 and mouse_pos_y >= 390 and self.end):
                        self.reset()
                        mouse_pos_x, mouse_pos_y = pygame.mouse.get_pos()


                elif(event.type == pygame.KEYDOWN):
                    if((self.active == True) and (self.end == False)):
                        if(event.key == pygame.K_RETURN):
                            print(self.input_text)
                            self.show_results(self.screen)

                            self.draw_text(self.screen, self.results, 350, 28, self.result_color)
                            self.end = True

                        elif(event.key == pygame.K_BACKSPACE):
                            self.input_text = self.input_text[:-1]
                        else:
                            try:
                                self.input_text += event.unicode
                            except:
                                pass

            pygame.display.update()

        clock.tick(60)

    def reset(self):
        self.screen.blit(self.startup, (0, 0))

        pygame.display.update()
        time.sleep(1)

        #Reset the variables to initial state
        self.reset_state = False
        self.end = False

        self.input_text = ""
        self.word = ""
        self.starting_time = 0
        self.end_time = 0
        self.wpm = 0

        #Get random sentence again
        self.word = self.get_sentence()
        if(self.word == False):
            self.reset()

        #Draw the header again
        self.screen.fill((0, 0, 0))
        self.screen.blit(self.background, (0, 0))

        msg = "Typing Speed Test"
        self.draw_text(self.screen, msg, 80, 80, self.head_color)

        #Draw the text area again
        pygame.draw.rect(self.screen, (255, 192, 25), (50, 250, 650, 50), 2)

        #Draw the sentence string again.
        self.draw_text(self.screen, self.word, 200, 28, self.text_color)

        pygame.display.update()


typing_speed_test().run()

