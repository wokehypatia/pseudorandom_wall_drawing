#walldrawing.py
#Randomly generates the schematic for an iterative wall drawing, with options to change color, overlay a grid (for ease of copying on a wall), and save the image.
#I affirm that I have adhered to the Honor Code in this assignment.
#Asie Mussard-Afcari
#December 2014

import os
import sys
import math
import random
import picture2

class Drawing():
    def __init__(self):
        self.canvas = picture2.Picture(1000,1000) #create canvas
        self.canvas.setPenColor(255,255,255) #picture2 uses PenColor as fill color
        self.canvas.drawRectFill(0,0,1000,1000) #makes the canvas background white
        self.canvas.setPenWidth(4)
        self.x = 0
        self.y = 0
        self.deltax = 0
        self.angle = 0
        self.angleList = [] #create an empty list to save the angles for repetition
    
    def getPosition(self): #returns the position of the pen
        self.x = self.canvas.pen_position[0] 
        self.y = self.canvas.pen_position[1]
        return self.x, self.y
    
    def nextPoint(self,angle):
        self.angleList.append(angle) #add it to list for future use
        x = self.getPosition()[0] #pull out x and y values so that we can have a while loop that makes sure we don't run off the edge
        y = self.getPosition()[1]
        x1 = x + (math.sin(angle)/20) #calculate new x
        y1 = y * (math.cos(angle)/20) #calculate new y
        return x1,y1
        
    def drawnLine(self):
        self.canvas.setPenColor(0,0,0) #change pen color back to black for drawing 
        angle = random.randrange(0,180) #generate a random angle
        x,y = self.nextPoint(angle) #use nextPoint to find the next point
        self.canvas.setDirection(angle) #change pen direction to randomly generated angle
        self.canvas.drawForward(20) 
        x,y = self.getPosition() #reset x and y to the new pen position
        done = False
        if y >= 1000: #loop stops drawing the line when it gets to the bottom of the page
            return True
        else:
            return self.drawnLine()

    
    def repeatLinePositive(self): #draws lines from left to right when first line ends on the right side of its beginning
        lastx = (self.getPosition()[0]) 
        self.canvas.setPosition(lastx,0) #moves pen back up to the top of the page offset from the beginning of the first line by the x value of the last point on the previous line
        for i in range(len(self.angleList)): #repeats the line by pulling the proper angles from our list
            self.canvas.setDirection(self.angleList[i])
            self.canvas.drawForward(20)
        repeatdone = False
        if lastx >= 1000: #stops repeating the line when we reach the opposite end of the page
            repeatdone = True
        else:
            return self.repeatLinePositive()
        return repeatdone
    
    def repeatLineNegative(self): #draws lines from right to left when first line ends on the left side of its beginning
        lastx = (self.getPosition()[0]) 
        self.canvas.setPosition(lastx,0) #moves pen back up to the top of the page offset from the beginning of the first line by the x value of the last point on the previous line
        for i in range(len(self.angleList)): #repeats the line by pulling the proper angles from our list
            self.canvas.setDirection(self.angleList[i])
            self.canvas.drawForward(20)
        repeatdone = False
        if lastx <= 0: #stops repeating the line when we reach the opposite end of the page
            repeatdone = True
        else:
            return self.repeatLinePositive()
        return repeatdone
    
    def repeatLine(self): #determines which direction the line runs in and decides if the negative or positive version of repeatLine should be called
        if self.deltax > 0:
            return self.repeatLinePositive()
        else:
            return self.repeatLineNegative()
    
    
    def gridOverlay(self): #overlays a grey grid on top of the canvas
        self.canvas.setPenColor(220,220,220)
        self.canvas.setPenWidth(1)
        for i in range(44):
            self.canvas.drawLine(25*i,0,25*i,1000)
            self.canvas.drawLine(0,25*i,1000,25*i)
    

def main():
    userWelcome()
    while True:
        try:
            image = generateDrawing()
            break
        except RuntimeError: #Because drawnLine is called recursively a random number of times, this protects from hitting maximum recursion depth.
            continue
    while True:   
        try:
            nextstep = raw_input("What would you like to do next? (grid, save, close): ")
            if nextstep == 'grid':
                grid(image)
                nextstep = raw_input("What would you like to do next? (save, close): ")
                if nextstep == 'save':
                    filename = raw_input("What would you like to name this picture? ")
                    image.canvas.writeFile(filename + ".jpg")
                    print "Your image has been saved in your current directory."
                elif nextstep == 'close':
                    return False
            elif nextstep == 'save':
                filename = raw_input("What would you like to name this picture? ")
                image.canvas.writeFile(filename + ".jpg")
                print "Your image has been saved in your current directory."
            elif nextstep == 'close':
                return False
            else:
                print "Your input is weird, please try again."
        except Exception:
            print("I'm sorry, something went wrong! Let's try again.")

def userWelcome(): #Introduces the user to the program
    print "Welcome to the wall drawing generator!"
    background = raw_input("Would you like some information on wall drawings? Y/N: ")
    if background == 'Y':
        print "A wall drawing is a work made directly on the wall in the space it is displayed in.",
        print "Many artists have experimented with wall drawings that are created iteratively, by repeating the same figure over and over.",
        print "This program creates a schematic for one of these drawings by randomly generating a line and then repeating it."
        print " "
        print "Let's start drawing now!"
    else:
        print "Then let's start drawing!"
    
def generateDrawing():    
    image = Drawing() #creates a new object in the Drawing class
    image.canvas.setPosition(0,0) #starts drawing off inside of the canvas
    image.drawnLine()
    image.deltax = image.getPosition()[0]
    if image.deltax < 0: #prevents lines that run left from being repeated only off the page
        image.canvas.setPosition(1000,0)
    repeatdone = False
    while repeatdone == False: #loops until the reapeated lines cover the whole page, works bc repeatline returns True when it hits opposite side of page
        repeatdone = image.repeatLine()
    image.canvas.display()
    return image

def grid(image): #adds a grid to the image
    image.gridOverlay()
    image.canvas.display()
    
main()

