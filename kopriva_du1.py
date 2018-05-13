# Prvni domaci uloha z IB111, 2017
#
# Mate za ukol naprogramovat 5 funkci, za kazdou muzete ziskat az 5 bodu
# Piste co nejprehlednejsi kod, zejmena vhodne pojmenovavejte promenne
#           (za necitelny kod hrozi bodova srazka)
#
# Sve reseni pojmenujte jako "prijmeni_du1.py" a ulozte do prislusne odevzdavarny
#           (bez uvozovek a bez diakritiky)
# --------------------------------------------------------------
# Zde muzete definovat pripadne importy
from turtle import Turtle
from math import ceil
#---------------------------------------------------------------
# 1) Napiste funkci, ktera pro zadane N vypise vsechna cela cisla od jedne do N vcetne
# tak, ze suda jsou vypsana normalne a misto lichych se vypise cislo opacne
#
# napr: pro N = 8 funkce vypise: -1, 2, -3, 4, -5, 6, -7, 8
#       pozn. muzete predpokladat, ze jako N bude zadavano kladne cele cislo
#---------------------------------------------------------------
def numbers_interlaced(n):
    for i in range(1, n+1):
        if i%2==0:
            print(i, end=", ")
        else:
            print(0-i, end=", ")


#---------------------------------------------------------------
# 2) Napiste funkci, ktera pro zadane parametry N, M vypise matici (tabulku) cisel
# o velikosti N krat M, (N radku, M sloupcu) kde kazde cislo je dano jako soucet cisla radku a sloupce.
# Radky i sloupce cislujte od 1, zarovnani nereste (sloupce oddelujte mezerou)
#
# napr: pro N = 4, M = 6 bude vystup:
#
#   2 3 4 5 6 7
#   3 4 5 6 7 8
#   4 5 6 7 8 9
#   5 6 7 8 9 10
#---------------------------------------------------------------
def sum_table(n, m):
    for i in range (1, n+1):
        for j in range (1, m+1):
            print(i+j, end=" ")
        print()


#---------------------------------------------------------------
# 3) Napiste funkci, ktera v textove grafice vykresli pro zadane N prazdnou
# pyramidu o N patrech tvorenou krizky "#" a vyplnenou teckami "."
#
# napr: pro N = 4 funkce vykresli

            #
          # . # 
        # . . . #
      # # # # # # #

# pozn. zde je spravne odsazovani mezi patry stezejni (na velikosti odsazeni cele pyramidy nezalezi)
#---------------------------------------------------------------
def blank_pyramid(n):
    for i in range (-n,0):
        for j in range (-n,n):
            if abs(i) + abs(j) == n or (i==-1 and j>(-n+1)):
                print("#", end=" ")
            elif abs(i) + abs(j) < n:
                print(".", end=" ")
            else:
                print(" ", end=" ")
        print()


#---------------------------------------------------------------
# 4) Napiste funkci, ktera v zelvi grafice vykresli tvar medove plastve. Plastev je slozena z prostredniho 
# sestiuhelniku o strane "side" a sesti dalsich stejne velkych sestiuhelnicich prilehajicich
# k jeho stenam (viz obrazek honeycomb.png)
#---------------------------------------------------------------
def honey_comb(side):
    bob=Turtle()
    for i in range (6):
        for j in range (7):
            bob.left(60)
            bob.forward(side)
        bob.right(120)

