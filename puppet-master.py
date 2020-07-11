#! /usr/bin/env python3

from init import *
from operation import *
from db import *
import argparse

parser = argparse.ArgumentParser(description='Specify an optional argument with the index corresponding to a puppet to interact with it')
# I. Init
parser.add_argument(
    "-i", "--init", help="Set up new puppet", action="store_true")
parser.add_argument("-r","--random", help = "Generate a random puppet", action="store_true")

# II. DB
parser.add_argument("--db", help="List the puppets and their corresponding index", action="store_true")
parser.add_argument("-m", metavar='index', help="Modify infomation of a puppet", type=int)
parser.add_argument("-v", metavar='index',
                    help="View infomation of a puppet", type=int)
parser.add_argument("--remove", metavar='index',
                    help="Remove a puppet", type=int)
# III. Op
parser.add_argument("-l", metavar='index', help="Load a puppet", type=int)
args = parser.parse_args()



if __name__ == "__main__":
    index_db()
    if args.init:
        puppet = init_puppet()
        save_puppet(puppet)
    elif args.random:
        puppet = vars(random_puppet())
        save_puppet(puppet)
    elif args.db:
        list_db()
    elif args.m:
        puppet = load(profiles[args.m])
        edit_info(puppet)
    elif args.v:
        puppet = load(profiles[args.v])
        display_puppet(puppet)
    elif args.l:
        puppet = load(profiles[args.l])
        driver = init_webdriver(puppet)
        load_cookies(driver,puppet)
        edit_info(puppet)
    elif args.remove:
        try:
            name = profiles[args.d]
            remove(name)
        except KeyError:
            print(f'[!] Index {args.d} not found!')
    else:
        list_db()
        parser.print_help()
