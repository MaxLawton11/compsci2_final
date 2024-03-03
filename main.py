import pygame
import Client

def master() :
    alpha = Client.Master()

    while True :
        pass

def Client() :
    beta = Client.Client()

    while True :
        #alpha.tick()
        beta.tick()


if __name__ == "__main__" :
    alpha = Client.Master()
    beta = Client.Client()

    while True :
        #alpha.tick()
        beta.tick()