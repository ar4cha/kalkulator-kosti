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


def paraSkaitli(skaits):
    print("Varbutiba para skaitli ir:" + str(1 * skaits) + "/" + str(2 * skaits))


def neparskaitli(skaits):
    print("Varbutiba nepars skaitli ir: " + str(1 * skaits) + "/" + str(2 * skaits))


def vienadiskaitli(skaits):
    print("Varbutiba vienad skaitli ir: " + str(1 * skaits) + "/" + str(6 * skaits))


def divivienadi(skaits):
    kaulins = 1 * 2
    print("Varbutiba divi vienadi skaitli ir: " + str(kaulins) + "/" + str(6 * skaits))



def main():
    if __name__ == '__main__':
        print("sis i...")
        print("what do you want? \n1-is a varbutiba para skaitli\n2-varbutiba neparaskaitli\n3-varbutiba vienadiskaitli\n4-varbutiba divivienadi\n5-playRound")
        metode = int(input("type 1-5:"))
        skaits = int(input("how much dice"))
        if metode == 1:
            paraSkaitli(skaits)
        if metode == 2:
            neparskaitli(skaits)
        if metode == 3:
            vienadiskaitli(skaits)
        if metode == 4:
            divivienadi(skaits)
        if metode == 5:
            playRound()


while True:
       main()
       restart = input('\033[97mdo you want again?').lower()
       if restart == "yes":
           main()
       else:
           print("\033[91mGoodbye")
           exit(0)