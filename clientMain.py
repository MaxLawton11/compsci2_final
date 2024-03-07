# start up the "Client" computer

import lib.Client as Client
if __name__ == "__main__" :
    beta = Client.Client()

    while True :
        beta.tick()