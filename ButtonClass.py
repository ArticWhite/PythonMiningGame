import PlayerClass
import numpy as np
import pygame
import random
import time
class Button():
                        def __init__(self, x, y, width, height, screen, buttonText='Button', onclickFunction=None, onePress=False):
                            fontInv = pygame.font.SysFont('Arial', 40)
                            self.x = x
                            self.y = y
                            self.width = width
                            self.height = height
                            self.onclickFunction = onclickFunction
                            self.onePress = onePress
                            self.alreadyPressed = False
                            self.screen=screen
                            self.fillColors = {
                                'normal': '#ffffff',
                                'hover': '#666666',
                                'pressed': '#333333',
                            }
                            self.buttonSurface = pygame.Surface((self.width, self.height))
                            self.buttonRect = pygame.Rect(self.x, self.y, self.width, self.height)

                            self.buttonSurf = fontInv.render(buttonText, True, (20, 20, 20))
                            #objects.append(self) legacy code
                        def process(self):
                            mousePos = pygame.mouse.get_pos()
                            self.buttonSurface.fill(self.fillColors['normal'])
                            if self.buttonRect.collidepoint(mousePos):
                                self.buttonSurface.fill(self.fillColors['hover'])
                                if pygame.mouse.get_pressed(num_buttons=3)[0]:
                                    self.buttonSurface.fill(self.fillColors['pressed'])
                                    if self.onePress:
                                        self.onclickFunction()
                                        
                                    elif not self.alreadyPressed:
                                        self.onclickFunction()
                                        time.sleep(0.1)
                                        self.alreadyPressed = True
                                else:
                                    self.alreadyPressed = False
                            self.buttonSurface.blit(self.buttonSurf, [
                                self.buttonRect.width/2 - self.buttonSurf.get_rect().width/2,
                                self.buttonRect.height/2 - self.buttonSurf.get_rect().height/2
                            ])
                            self.screen.blit(self.buttonSurface, self.buttonRect)
                                