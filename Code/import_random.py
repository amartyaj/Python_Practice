import random
from pprint import pprint

# These are all arrays:
suits = ["Clubs", "Spades", "Hearts", "Diamonds"]
faces = ["Jack", "Queen", "King", "Ace"]
numbered = [2, 3, 4, 5, 6, 7, 8, 9, 10]

"""
This is a multi-line
comment
"""
combined_array = faces + numbered
pprint(combined_array)

"""
This is also a multi-line
comment
"""


def draw():
    the_suit = random.choice(suits)
    the_card = random.choice(combined_array)
    return_val = str(the_card) + " of " + the_suit
    return return_val


# for iter in range(1, 3): -> This would run from 1 to 2 so only 2 times
for iter in range(3):
    print(draw())
