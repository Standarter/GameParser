from ast import arg
import os, random, argparse
parser = argparse.ArgumentParser()
parser.add_argument("-r", "--random", help="Print in random order", action="store_const", const=True)
parser.add_argument("-a", "--alphabet", help="Print in alphabet order (Default)", action="store_const", const=True)
parser.add_argument("-p", "--positional", help="Add positional number to DumpList", action="store_const", const=True)
args = parser.parse_args()
Games = os.listdir(os.curdir + "/Games")
if args.random:
    random.shuffle(Games)
for Game in Games:
    if args.positional:
        print(str(Games.index(Game)) + ") ", end="")
    print(Game.replace(".url", "").replace(".lnk", ""))