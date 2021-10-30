from collections import namedtuple
from itertools import permutations
import os
import pickle

state_file = ".argb_state"


def generator():
    return permutations(range(0x00, 0xFF), 4)


def yield_one():
    argb_generator = None

    if os.path.exists(state_file):
        with open(state_file, 'rb') as f:
            try:
                argb_generator = pickle.load(f)
            except EOFError:
                pass

    if not argb_generator:
        argb_generator = generator()

    element = next(argb_generator)
    hexai = bytearray(element).hex()

    with open(state_file, 'wb') as f:
        pickle.dump(argb_generator, f)

    return hexai


def print_one():
    print(f"#{yield_one()}")


if __name__ == "__main__":
    print_one()
