# from encounters import encounters
from enum import Enum


class LoadInterface(Enum):
    ERROR = -99
    QUIT = -1
    ENCOUNTERS = 1


def root_interface():
    running = True
    while running:
        print("###################################")
        print("##                               ##")
        print("##    Game Master's Toolkit      ##")
        print("##                               ##")
        print("###################################")
        print("")
        print("Welcome to Game Master's Toolkit. Would you like to:")
        print(" 1. Run the [E]ncounter tool")
        print(" 2. Do [S]omething else")
        print(" 3. [Q]uit")
        raw_selection = input("> ")
        selection = parse_selection(raw_selection)
        if selection == -1:
            running = False

    # print(encounters.sample_encounters())


def parse_selection(selection):
    if (
        selection == "1"
        or selection == 1
        or (isinstance(selection, str) and selection.lower() == "e")
        or (isinstance(selection, str) and "encounters".startswith(selection.lower()))
    ):
        return LoadInterface.ENCOUNTERS
    else:
        return LoadInterface.ERROR
