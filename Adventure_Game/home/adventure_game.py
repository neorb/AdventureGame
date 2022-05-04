import random
from var_string_list import *
from print_pause import *
from valid_input import valid_input


def contacting():
    response = valid_input(str(prompt), str(option1), str(option2))
    if "yes" == response:
        intro()
    elif "no" == response:
        print_wrong_person()
        contacting()
    else:
        print("Wrong input, please try to concetrate")
        contacting()


def intro():
    print_introduction()
    get_tools()


def get_tools():
    response = valid_input(str(text_tool), str(option_1), str(option_2))
    if "1" == response:
        print("That's up to you. Here we go.\n")
        start_mission(tools)
    elif "2" == response:
        tools.append(tools)
        start_mission(tools)
    else:
        print("Wrong input, please try to concetrate")
        get_tools()


def start_mission(tools):
    response = valid_input(str(text_button), str(option_red), str(option_blue))

    if "red" == response:
        wrong_choice()
    elif "blue" == response:
        end_of_mission(tools)
    else:
        print("Wrong input, please try to concetrate")
        start_mission(tools)


def end_of_mission(tools):
    items = random.choice(random_complexity)
    if "laser" in items:
        if "shopsticks" in tools:
            print_laser()
            play_again()
        else:
            print_failed_mission()
            play_again()
    elif "wires" in items:
        if "pliers" in tools:
            print_wires()
            play_again()
        else:
            print_failed_mission()
            play_again()


def wrong_choice():
    print_wrong_choice()
    play_again()


def play_again():
    response = valid_input(str(text_yes_not), str(option_yes), str(option_no))
    if "yes" == response:
        play_game()
    elif "no" == response:
        print("Ok, good bye")
    else:
        print("Wrong input, please try to concetrate")
        play_again()


def play_game():
    contacting()


play_game()
