"""This is a program which plays a music track (object) after a fixed interval of time (adjustable, as per the needs).
    One can use this program as a reminder to drink water, care for his eye, and do streching at stipulated time intervals.
    """

import os
import pygame as p
import time

WATER = 30 * 60
EYE = 1 * 60 * 60
LEG = 2 * 60 * 60

def getdate():
    """This module returns current value of date and time in integers."""
    return time.ctime(int(time.time()))


def play():
    """This module plays the loaded music track (object), infinitely."""
    p.mixer.music.play(loops = -1)


def stop():
    """This module stops the playing music track (object) and unloads it from the mixer."""
    p.mixer.music.stop()
    p.mixer.music.unload()


def gettime():
    """This module returns amount of seconds passed from epoch in integers."""
    return int(time.time())


def ifevent(t1):
    """This module checks if an event is supposed to occur and decides accordingly."""
    t2 = gettime()

    if (t2-t1) % WATER == 0:
        p.mixer.music.load("Water.ogg")
        play()
        while True:
            ch = input()
            if ch == "Drank" or ch == "drank" or ch == "DRANK":
                stop()
                GUI()
                time.sleep(1)
                break

    if (t2-t1) % EYE == 0:
        p.mixer.music.load("Eye.ogg")
        play()
        while True:
            ch = input()
            if ch == "Closed" or ch == "closed" or ch == "CLOSED":
                stop()
                GUI()
                time.sleep(1)
                break

    if (t2-t1) % LEG == 0:
        p.mixer.music.load("Exercise.ogg")
        play()
        while True:
            ch = input()
            if ch == "Walked" or ch == "walked" or ch == "WALKED":
                stop()
                GUI()
                time.sleep(1)
                break


def GUI():
    """This module prints the GUI."""
    d = getdate()

    os.system('cls')
    print(F"Date: {d}\n")
    print("\nNote: To stop drink, eye or leg event, type 'drank', 'closed', or 'walked' respectively")
    print("\n\nTime for drink/eye/leg event. Type your response: ", end = '')


def main():
    """This is the 'main' module."""
    time1 = gettime()

    GUI()
    time.sleep(1)

    while True:
        ifevent(time1)
        time2 = gettime()
        if time2-time1 in range(8 * 60 * 60, 12 * 60 * 60):
            break


if __name__ == "__main__":
    os.system('cls')
    p.mixer.init()
    main()
    os.system('cls')
    print("\n\n\n\n\n\n\n\n\t\t\t\t\t\tPress Enter to exit", end=' ')
    input()

