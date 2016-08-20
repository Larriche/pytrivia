import sys
import pygame
from pygame.locals import *

class Trivia(object):
    def __init__(self,filename,screen):
        # the pygame screen
        self.screen = screen
        
        # the lines read from the questions text file
        self.data = []

        # index of current question
        self.current = 0

        # questions answered so far
        self.played = 0

        # total number of lines in the question text file
        self.total = 0

        # the numeric value of the correct answer for a question
        self.correct = 0

        # score of the player so far
        self.score = 0

        # determine whether answer is correct
        self.scored = False

        # determines whether answer is incorrect
        self.failed = False

        # the numeric value of a wrong answer given by a player
        self.wronganswer = 0

        # colors to use for displaying the answer options
        self.colors = [white,white,white,white]

        # reading data from questions file
        f = open(filename,"r")
        trivia_data = f.readlines()
        f.close()

        # removing whitespaces from data
        self.data = [ i.strip() for i in trivia_data ]

        self.total = len(self.data)

        # an offset to add to position of text to make the credits be in
        # motion
        self.credits_offset = 200
        
        
    def display(self):
        print_text(font1,300,5,"PYTHON TRIVIA GAME")
        print_text(font2,730,5,"SCORE",purple)
        print_text(font2,750,25,str(self.score),purple)

        # end game when we've shown all questions
        if self.current >= self.total:
           self.show_credits()

        else:
            self.show_question()


    def show_question(self):
        #get correct answer out of data
        self.correct = int(self.data[self.current + 5])

        #display question
        question = self.current
        print_text(font1,5,80,"QUESTION " + str(self.played + 1))
        print_text(font1,20,120,self.data[self.current],yellow)
        self.attempted = False

        #update display upon answer choice
        if self.scored:
            self.colors = [white,white,white,white]
            self.colors[self.correct - 1] = green

            print_text(font1,280,380,"CORRECT!",green)
            
        elif self.failed:
            self.colors = [white,white,white,white]

            # we colour the incorrect answer red 
            self.colors[self.wronganswer - 1] = red              

            # we always colour the correct answer green to provide feedback
            self.colors[self.correct - 1] = green
            print_text(font1,280,380,"INCORRECT!",red)


        print_text(font2,270,420,"Press Enter For Next Question",yellow)
        print_text(font2,290,500-20,"Press keys(1-4) to answer",yellow)

        #display answers
        print_text(font1,5,170,"ANSWERS")
        print_text(font2,20,210,"1 - " + self.data[self.current+1],self.colors[0])
        print_text(font2,20,240,"2 - " + self.data[self.current+2],self.colors[1])
        print_text(font2,20,270,"3 - " + self.data[self.current+3],self.colors[2])
        print_text(font2,20,300,"4 - " + self.data[self.current+4],self.colors[3])

    def handle_input(self,number):
        if not self.scored and not self.failed:
            if number == self.correct:
                self.scored = True
                self.score += 10
            else:
                self.failed = True
                self.wronganswer = number
        

    def next_question(self):
        self.scored = False
        self.failed = False
        self.colors = [white,white,white,white]

        # locating the next question based on structure of the questions file
        self.current += 6
        self.played += 1
        

    def show_credits(self):
        self.screen.fill((255,255,255))
        scoreStr = "Your final score: " + str(self.score)
        print_text(font1,300, 230 + self.credits_offset,scoreStr,purple)
        print_text(font1,300 ,250 + self.credits_offset,"Thanks for Playing",purple)
        print_text(font1,280 ,280 + self.credits_offset,"Created By Richman Larry Clifford",purple)

        pygame.time.wait(500)
        self.credits_offset -= 20

        if self.credits_offset < -250:
            self.credits_offset = 250
            

def print_text(font,x,y,text,color=(255,255,255),shadow = False):
    if shadow:
        imgText = font.render(text,True,(0,0,0))
        screen.blit(imgText,(x-2,y-2))
    imgText = font.render(text,True,color)
    screen.blit(imgText,(x,y))


    
    
#main program begins

# initialise pygame and the screen
pygame.init()
screen = pygame.display.set_mode((800,500))
pygame.display.set_caption("Python Trivia Game")

# fonts to use
font1 = pygame.font.Font(None,22)
font2 = pygame.font.Font(None,20)

# named constants for RGB values
white = 255,255,255
yellow = 255,255,0
purple = 255,0,255
green = 0,255,0
red = 255,0,0


trivia = Trivia("questions.txt",screen)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
        elif event.type == KEYUP:
            if event.key == pygame.K_ESCAPE:
                sys.exit
                
            elif event.key == pygame.K_1:
                trivia.handle_input(1)
                
            elif event.key == pygame.K_2:
                trivia.handle_input(2)
                
            elif event.key == pygame.K_3:
                trivia.handle_input(3)
                
            elif event.key == pygame.K_4:
                trivia.handle_input(4)
                
            elif event.key == pygame.K_RETURN:
                trivia.next_question()

    #clear the screen
    screen.fill((72,61,139))

    #display trivia data
    trivia.display()

    #update the display
    pygame.display.update()
            
        

            

        
