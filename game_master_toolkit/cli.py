# from encounters import encounters
from enum import Enum


class LoadInterface(Enum):
    ERROR = -99
    QUIT = -1
    ENCOUNTERS = 1


def root_interface():
    while True:
        print("###################################")
        print("##                               ##")
        print("##    Game Master's Toolkit      ##")
        print("##                               ##")
        print("###################################")
        print("")
        print("Welcome to Game Master's Toolkit. Would you like to:")
        print(" 1. Run the [E]ncounter tool")
        print(" 2. Do [S]omething else")
        print("    [Q]uit")
        raw_selection = input("> ")
        selection = parse_selection(raw_selection)
        if selection == LoadInterface.QUIT:
            print("Thanks for using Game Master's Toolkit!")
            break

    # print(encounters.sample_encounters())


def parse_selection(selection):
    if (
        selection == "1"
        or selection == 1
        or (isinstance(selection, str) and "encounters".startswith(selection.lower()))
    ):
        return LoadInterface.ENCOUNTERS
    elif (
        (isinstance(selection, str) and selection.lower() == "x")
        or (isinstance(selection, str) and "exit".startswith(selection.lower()))
        or (isinstance(selection, str) and "quit".startswith(selection.lower()))
    ):
        return LoadInterface.QUIT
    else:
        return LoadInterface.ERROR
