import re


def board(fen: str):
    """
    Display the board in a human-readable format.
    """
    lines = fen.split("/")
    for line in lines:
        i = 0
        row = []
        while i < len(line):
            if line[i].isdigit():
                row.extend([''] * int(line[i]))
            elif line[i] == 'b' or line[i] == 'r':
                if i + 1 < len(line) and line[i+1] == '0':
                    row.append(line[i])
                    i += 1
                else:
                    row.append(line[i] + line[i+1])
                    i += 1
            else:
                row.append(line[i] + line[i+1])
                i += 1
            i += 1
        print(row)


if __name__ == "__main__":
    board("r01r0r01r0/1r0rr1r0r0r01/3r04/2b05/4r0b02/8/1b0b0b0b0b0b01/1b0b0b0b01")
