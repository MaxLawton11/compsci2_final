# start up the "Master" computer

import Client
if __name__ == "__main__" :
    alpha = Client.Master()

    while True :
        alpha.tick()