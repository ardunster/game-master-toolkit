# from encounters import encounters


def root_interface():
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
    selection = input("> ")
    parse_selection(selection)
    # print(encounters.sample_encounters())


def parse_selection(selection):
    if (
        selection == "1"
        or selection == 1
        or (isinstance(selection, str) and selection.lower() == "e")
        or (isinstance(selection, str) and "encounters".startswith(selection.lower()))
    ):
        return 1
    else:
        return -1
