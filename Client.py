import threading
import pygame
import asyncio

import Shapes
import Socket
import Screen

class Client :
    def __init__(self):
        self.screen = Screen.Screen()
        self.user_input = ClientUserInput()

        self.socket = threading.Thread(target=Socket.ClientSocket, args=(self,))
        self.socket.start()

    def _addObject(self) :
        if self.user_input.getMouseClicked() :
            self.screen.addObject(Shapes.Circle(self.user_input.getMousePos()[0],self.user_input.getMousePos()[1],20,'red'))
        else :
            return

    def tick(self) :
        self.user_input.testEvents()
        self._addObject()
        self.screen.frame()
    
class ClientUserInput :
    def __init__(self) :
        self.mouse_click_last = False

    def testEvents(self) :
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

            if event.type == pygame.MOUSEBUTTONDOWN :
                self.mouse_click_last = True
            else :
                self.mouse_click_last = False

    def getMousePos(self) :
        return pygame.mouse.get_pos()
    
    def getMouseClicked(self) :
        return self.mouse_click_last

class Master :
    def __init__(self):
        self.screen = Screen.Screen()
        self.user_input = ClientUserInput()

        self.socket = threading.Thread(target=Socket.MasterSocket, args=(self,))
        self.socket.start()

    def _addObject(self) :
        if self.user_input.getMouseClicked() :
            self.screen.addObject(Shapes.Circle(self.user_input.getMousePos()[0],self.user_input.getMousePos()[1],20,'blue'))
        else :
            return

    def tick(self) :
        self.user_input.testEvents()
        self._addObject()
        self.screen.frame()

    