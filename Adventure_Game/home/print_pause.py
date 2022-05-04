import time
import random
from var_string_list import *


def print_pause_2_second(message_to_print):
    print(message_to_print)
    time.sleep(2)


def print_pause_4_second(message_to_print):
    print(message_to_print)
    time.sleep(4)


def print_pause_5_second(message_to_print):
    print(message_to_print)
    time.sleep(5)


def print_wrong_person():
    print_pause_2_second("Oh, excuse me, " +
                         random.choice(connection_list))  # Random list.
    print_pause_2_second("Let's try again.\n")


def print_introduction():
    print_pause_2_second("Geat!. We have an emergency situation here at " +
                         random.choice(location_list))  # Random list.
    print_pause_4_second("There is a Bomb inside the Building." +
                         " and it has a clock that we need to stop.")
    print_pause_5_second("We are going to give you fully remote access" +
                         " in order to stop and desactivate the Bomb.\n")
    print_pause_2_second("To get you start, accept a Tools in order to" +
                         " complete this mission")
    print_pause_4_second("These are some items that you may need like:" +
                         " talcum, shopsticks, pliers etc.\n")


def print_laser():
    print_pause_2_second("The Box get opened, Great!")
    print_pause_2_second("Hummm.... I can see there is some kind" +
                         " of mechanism inside.")
    print_pause_4_second("A dectector movement. It use laser, there" +
                         " is a Bottom, that should stop the clock.")
    print_pause_4_second("We need to make  Laser Beam visible.")
    print_pause_5_second("Talcum is a good way to make it visible and" +
                         " with the shopsticks you can reach" +
                         " and hit the Bottom")
    print_pause_5_second("Great!...... the laser show up, now try to" +
                         " hit the Bottom. Be carefull")
    print_pause_2_second("Here you go.....")
    print_pause_4_second("Keep going.......")
    print_pause_4_second("Keep going.......")
    print_pause_4_second("Keep going.......")
    print_pause_2_second("Click!. Yeeeees. You dit it. Good job Agent")
    print_pause_2_second("everybody saved!!!\n")


def print_wires():
    print_pause_2_second("Great. Good Choice!.")
    print_pause_2_second("The Box got open.")
    print_pause_4_second("Hummm.... I see there is some" +
                         " kind of mechanism inside.")
    print_pause_5_second("There are a wires connected to" +
                         " the main board, You need to be carefull.")
    print_pause_5_second("You are going to use a plier," +
                         " to cut the wires. Great!.")
    print_pause_2_second("Here you go.....")
    print_pause_4_second("Keep going.......")
    print_pause_4_second("Keep going.......")
    print_pause_4_second("Keep going.......")
    print_pause_2_second("Click!. Yeeeees. You dit it." +
                         " Good job Agent.")
    print_pause_2_second("everybody saved!!!.\n")


def print_wrong_choice():
    print_pause_2_second("Oh, oh, I think that was bad shoice.")
    print_pause_5_second("The Box has a shortcut..... But wait," +
                         " does the Clock get stoped?...." +
                         " I think so... is the Bomb desactivated?.")
    print_pause_2_second("Oooooh, no..... Boooooooooooom!.\n")
    print_pause_2_second("Mission failed. Game over!!!.\n")


def print_failed_mission():
    print_pause_2_second("Oh... The Box got open.")
    print_pause_4_second("Unfortunatly, you do not have" +
                         " the right Tools to finish this mission.")
    print_pause_2_second("Mission failed!.\n")
