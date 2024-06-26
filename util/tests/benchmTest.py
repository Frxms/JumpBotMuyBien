from util.Bitboard.Bitboard import GameBoard
from util.Bitboard.moves import gen_moves
from util.engine import calcMove
from util.generator import createVis
from util.evaluate import evaluate
from util.tests.minmaxTestFunc import (minimax_1_move, minimax_1_move_1, minimax_2_moves,
                                       alphabeta_2_moves, alphabeta1Move, alphabeta_1_move_1)

import time


def move_performance():
    fen = "b01b0b01b0/1b0bb1b0b0b01/3b04/2r05/4b0r02/8/1r0r0r0r0r0r01/1r0r0r0r01 b"
    splitted = fen.split(" ")
    turn = splitted[1]
    start_time = time.time()
    for i in range(1000):
        calcMove(createVis(splitted[0]), turn, True)
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"early Game took: {elapsed_time} seconds")

    fen = "b02b01b0/3b01b02/b02b02b01/b01b05/5r02/1r02r02r0/2rrr02r01/r03r01 b"
    splitted = fen.split(" ")
    turn = splitted[1]
    start_time = time.time()
    for i in range(1000):
        calcMove(createVis(splitted[0]), turn, True)
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"mid Game took: {elapsed_time} seconds")

    fen = "3b02/2b05/1b06/1r0rr2b02/8/5r02/1r0r03b01/3r02 b"
    splitted = fen.split(" ")
    turn = splitted[1]
    start_time = time.time()
    for i in range(1000):
        calcMove(createVis(splitted[0]), turn, True)
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"end Game took: {elapsed_time} seconds")


def eval_performance():
    fen = "b01b0b01b0/1b0bb1b0b0b01/3b04/2r05/4b0r02/8/1r0r0r0r0r0r01/1r0r0r0r01 b"
    splitted = fen.split(" ")
    result = []
    start_time = time.time()
    for i in range(1000):
        res1 = evaluate(createVis(splitted[0]))
        if res1 not in result:
            result.append(res1)
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"early Game took: {elapsed_time} seconds")
    print(f"Array length: {len(result)} with {result[0]}")

    fen = "b02b01b0/3b01b02/b02b02b01/b01b05/5r02/1r02r02r0/2rrr02r01/r03r01 b"
    splitted = fen.split(" ")
    result = []
    start_time = time.time()
    for i in range(1000):
        res1 = evaluate(createVis(splitted[0]))
        if res1 not in result:
            result.append(res1)
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"mid Game took: {elapsed_time} seconds")
    print(f"Array length: {len(result)} with {result[0]}")

    fen = "3b02/2b05/1b06/1r0rr2b02/8/5r02/1r0r03b01/3r02 b"
    splitted = fen.split(" ")
    result = []
    start_time = time.time()
    for i in range(1000):
        res1 = evaluate(createVis(splitted[0]))
        if res1 not in result:
            result.append(res1)
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"end Game took: {elapsed_time} seconds")
    print(f"Array length: {len(result)} with {result[0]}")


def minimax_performance():
    minimax_1_move()
    minimax_1_move_1()
    minimax_2_moves()


def alphabeta_performance():
    alphabeta1Move()
    alphabeta_1_move_1()
    alphabeta_2_moves()


def test_both_performances():
    print("minimax Algorithm")
    minimax_performance()
    print("*****************************************************")
    print("Alpha-Beta Algorithm:")
    alphabeta_performance()

def test_all_performances():
    print("Move generation test:")
    move_performance()
    print("********************************************************")
    print("Evaluation test:")
    eval_performance()
    print("********************************************************")
    print("minimax Algorithm:")
    minimax_performance()
    print("********************************************************")
    print("Alpha-Beta Algorithm:")
    alphabeta_performance()


if __name__ == "__main__":
    move_performance()
