import random

from firebase import add_highscore






if(__name__ == "__main__"):
    add_highscore(str(random.randrange(0, 2000)), random.randrange(0,100), "default", "annon");