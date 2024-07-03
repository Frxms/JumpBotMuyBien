import time

import pygame
import json

from main import clientRun
from gameServer.network import Network
from util.Bitboard.Bitboard import GameBoard
from util.Bitboard.bb_helper import get_index
from util.Tree import Node, Tree
from util.search import bb_alpha_beta

pygame.font.init()


def clientRun(fen, depth=3):
    board = GameBoard(fen)
    # print(board.__str__())
    node = Node(board, False)
    if board.is_endgame():
        print("Game already ended")

        return
    tree = Tree(node)

    tree.create_bb_tree(node, depth)
    # print(tree.root)

    search_value = bb_alpha_beta(tree.root, depth, -100000, 100000, False)
    child: Node = tree.get_root_children(search_value)
    return f"{get_index(child.move[0], True)}-{get_index(child.move[1], True)}"


def main():
    run = True
    clock = pygame.time.Clock()
    n = Network()
    player = int(n.getP())
    print("You are player", player)

    while run:
        clock.tick(60)
        try:
            #try to send get as a json to server over network, rest is error handling
            game = n.send(json.dumps("get"))
            if game is None:
                raise ValueError("Game data is None")
        except:
            run = False
            print("Couldn't get game")
            break

        #response is also a json, json.loads transforms into a python dictionary
        #dictionary consists of board string, a variable player1 which is true, when player 1 (or better 0),
        #variable player2 with the same concept and bothConnected, also a boolean
        try:
            game = json.loads(game)
        except:
            print(game)

        #allow input just when both players are in
        if game["bothConnected"]:

            #allow to only give input, when it is your turn
            if player == 0 and game["player1"]:
                #printing not necessary, game["board"] is the way to get the board string
                print("New Board: " + game["board"])
                print("New Time: " + str(game["time"]))

                #change to any input you like. This one is just console input. Change it here to respond with your Ai's answer.
                #Answer must have format: start-end like E7-F7
                i = clientRun(game["board"], 3)

                # json.dumps(i) transforms the input into a json. You can print it, if you want to see the difference
                data = json.dumps(i)

                #send data via network
                n.send(data)

            elif player == 1 and game["player2"]:
                print("New Board: " + game["board"])
                print("New Time: " + str(game["time"]))
                i = clientRun(game["board"], 3)
                data = json.dumps(i)
                n.send(data)

while True:
    main()

