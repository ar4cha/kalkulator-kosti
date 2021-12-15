import random
from pygame import mixer
import time

def playRound():

    trials = int(input("write (1) if you want to start:"))
    for i in range(trials):
        die1 = random.randint(1,6)
        die2 = random.randint(1,6)
        die3 = random.randint(1,6)
        die4 = random.randint(1,6)
        die5 = random.randint(1,6)
        sum = die1 + die2 + die3 + die4 +die5
        mixer.init()
        mixer.music.load("kosti.mp3")
        mixer.music.play()
        print("first throw:", die1)
        time.sleep(1)
        print("second throw:", die2)
        time.sleep(1)
        print("third throw", die3)
        time.sleep(1)
        print("fourth throw" ,die4)
        print("tutututu......")
        time.sleep(3)
        print("fifth throw ",die5)

        if sum in (7,11):

            print("You rolled a", sum)
            print("You Win: Natural!")

        if sum in (2,3,12):
            print("You rolled a", sum)
            print("You Lose: Crap-Out!")

        print("You Rolled a", sum)


def paraSkaitli():
    p = 3*skaists
    print("coming soon")


def neparskaitli():
    print("coming soon")


def vienadiskaitli():
    print("coming soon")


def divivienadi():
    print("coming soon")



def main():
    if __name__ == '__main__':
        print("sis i...")
        playRound()

while True:
       main()
       restart = input('\033[97mdo you want again?').lower()
       if restart == "yes":
           main()
       else:
           print("\033[91mGoodbye")
           exit(0)