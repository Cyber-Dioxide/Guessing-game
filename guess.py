import random
import pyfiglet
import MyColors
import os

lbiu = MyColors.lightColorsBIU()
nbiu = MyColors.NormalBIUColors()

lbold = MyColors.lightColorsBold()

def game():
    os.system("clear")
    name = input(lbold.LIGHT_greenBold("\n\n\nYour name: "))
    print("\nWelcome")
    print(pyfiglet.figlet_format(name))
    l = random.randint(1,100)
    c = random.randrange(2,100,4)
    m = l +l
    print("\nThink a number")
    input(lbold.LIGHT_cyanBold("\nHit enter to continue! :"))
    k = m+c
    print(f"Add the number you've thought! ")
    input(lbold.LIGHT_megantaBold("Hit enter to continue! :"))
    print(f"Add {c} to the total! ")
    input(lbold.LIGHT_megantaBold("Hit enter to continue! :"))
    j = k/2
    print(f"Divide the total by 2! :")
    input(lbold.LIGHT_cyanBold("\nHit enter to continue! :"))

    s = j-l
    print("Sub the number you've thought from the remaining amount! ")
    input(lbold.LIGHT_cyanBold("\nHit enter to continue! :"))

    print(f"You are left with {s}")

no = ["n", "no"]
cont = ""

while cont not in no:
    game()

    cont = input(lbold.LIGHT_cyanBold("Do you want to play again!"))







