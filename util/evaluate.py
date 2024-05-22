def evaluate(fen):
    redEval = countMaterial(fen.split(" ")[0], "r")
    blueEval = countMaterial(fen.split(" ")[0], "b")

    evaluation = blueEval + redEval

    return evaluation


def countMaterial(fen: str, color: str) -> float:
    counted_towers = fen.count(color+color) * 3
    counted = fen.count(color) - fen.count(color + color) * 2 + counted_towers
    if color == "b":
        return counted * -1
    return counted


if __name__ == "__main__":
    print(evaluate("r0r0rrb0b0bbbb b"))
