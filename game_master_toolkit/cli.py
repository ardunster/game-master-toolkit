from enum import Enum

from game_master_toolkit.encounters import encounters_cli


class LoadInterface(Enum):
    ERROR = -99
    QUIT = -1
    ENCOUNTERS = 1
    SOMETHING_ELSE = 2


def print_intro():
    print("###################################")
    print("##                               ##")
    print("##    Game Master's Toolkit      ##")
    print("##                               ##")
    print("###################################")


def root_interface():
    print_intro()
    while True:
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
        elif selection == LoadInterface.ERROR:
            print(
                f"Sorry, {raw_selection} is not a recognized input. Please try again."
            )
        elif selection == LoadInterface.ENCOUNTERS:
            print("You have selected the ENCOUNTERS tool.")
            encounters_cli.enc_interface()
        elif selection == LoadInterface.SOMETHING_ELSE:
            print("Something else? Like what?  (what did you actually expect here?)")


def parse_selection(selection):
    if (
        selection == "1"
        or selection == 1
        or (isinstance(selection, str) and "encounters".startswith(selection.lower()))
    ):
        return LoadInterface.ENCOUNTERS
    elif (
        selection == "2"
        or selection == 2
        or (
            isinstance(selection, str)
            and "something else".startswith(selection.lower())
        )
    ):
        return LoadInterface.SOMETHING_ELSE
    elif (
        (isinstance(selection, str) and selection.lower() == "x")
        or (isinstance(selection, str) and "exit".startswith(selection.lower()))
        or (isinstance(selection, str) and "quit".startswith(selection.lower()))
    ):
        return LoadInterface.QUIT
    else:
        return LoadInterface.ERROR
