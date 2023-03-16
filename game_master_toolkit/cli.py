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
    print(" 2. Do something else")
    print(" 3. [Q]uit")
    selection = input("> ")
    parse_selection(selection)
    # print(encounters.sample_encounters())


def parse_selection(selection):
    if selection == "1" or selection == "E":
        print("1")
