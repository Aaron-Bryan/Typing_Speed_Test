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
        self.reset_state = True
        self.active = False
        self.input_text = ""
        self.word = ""
        self.starting_time = 0
        self.end_time = 0
        self.typing_accuracy = "0%"
        self.wpm = 0
        self.results = 'Time:0 Accuracy:0 % Wpm:0 '
        self.end = False
        self.head_color = (255, 213, 102)
        self.text_color = (240, 240, 240)
        self.results_color = (255, 70, 70)

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

    #Method for retreiving a random sentence from the txt file (dictionary.txt)
    def get_sentence(self):
        file = open(r"resources/dictionary.txt").read()
        sentence = file.split("\n")
        random_sentence = random.choice(sentence)
        return random_sentence

    #Method for showing the results of the test
    def show_results(self, screen):

        if(self.end == False):

            #Calculate the time of the user
            self.end_time = time.time() - self.starting_time

            #Calculate the accuracy of the user
            count = 0
            for i, c in enumerate(self.word):
                try:
                    if self.input_text[i] == c:
                        count = count + 1
                except:
                    pass
            self.typing_accuracy = count / len(self.word) * 100

            #Calculate the wpm of the user
            #self.wpm = len(self.input_text) * 60 / (5 * self.end_time)

            word_count = len(self.input_text) / 5
            self.wpm = word_count / (self.end_time / 6)

            self.end = True
            print(self.end_time)

            #Placeholder text for the results
            self.results = 'Time:' + str(round(self.end_time)) + " secs Accuracy:" + str(round(self.typing_accuracy)) + "%" + '   WPM: ' + str(round(self.wpm))

            #Draw the image that will serve as a reset button
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
            # update the text of user input
            self.draw_text(self.screen, self.input_text, 274, 26, (250, 250, 250))
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.running = False
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONUP:
                    x, y = pygame.mouse.get_pos()
                    # position of input box
                    if (x >= 50 and x <= 650 and y >= 250 and y <= 300):
                        self.active = True
                        self.input_text = ''
                        self.time_start = time.time()
                        # position of reset box
                    if (x >= 310 and x <= 510 and y >= 390 and self.end):
                        self.reset()
                        x, y = pygame.mouse.get_pos()


                elif event.type == pygame.KEYDOWN:
                    if self.active and not self.end:
                        if event.key == pygame.K_RETURN:
                            print(self.input_text)
                            self.show_results(self.screen)
                            print(self.results)
                            self.draw_text(self.screen, self.results, 350, 28, self.results_color)
                            self.end = True

                        elif event.key == pygame.K_BACKSPACE:
                            self.input_text = self.input_text[:-1]
                        else:
                            try:
                                self.input_text += event.unicode
                            except:
                                pass

            pygame.display.update()
        clock.tick(60)


    def reset(self):
        self.screen.blit(self.startup_img, (0,0))

        pygame.display.update()
        time.sleep(1)

        #Refresh the variables to initial state
        self.reset_state = False
        self.end = False

        self.input_text = ""
        self.word = ""
        self.starting_time = 0
        self.end_time = 0
        self.wpm = 0

        #Get Random sentence again
        self.word = self.get_sentence()
        if (self.word == False):
            self.reset_state()

        #Heading
        self.screen.fill((0, 0, 0))
        self.screen.blit(self.background, (0, 0))

        head_text = "Typing Speed Test"

        self.draw_text(self.screen, head_text, 80, 80, self.head_color)

        #Draw the text area
        pygame.draw.rect(self.screen, (255, 192, 25), (50, 250, 650, 50), 2)

        #Draw the head_text
        self.draw_text(self.screen, self.word, 200, 28, self.text_color)

        pygame.display.update()


typing_speed_test().run()