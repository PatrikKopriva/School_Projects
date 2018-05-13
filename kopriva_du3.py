# Treti domaci uloha z IB111, 2017
#
# Piste co nejprehlednejsi kod, zejmena vhodne pojmenovavejte promenne
#           (za necitelny kod hrozi bodova srazka)
#
# Sve reseni pojmenujte jako "prijmeni_du3.py" a ulozte do prislusne odevzdavarny
#           (bez uvozovek a bez diakritiky)
# --------------------------------------------------------------
# zde muzete definovat pripadne importy
import random
"""
[az 30 bodu]
Vytvorte program hrajici hru "Padajici piskvorky" na plánu zadané velikosti. Tato varianta se hraje na 2D plánu
a je podobná klasickym piskvorkams tím rozdilem, ze hrac na tahu nevolí ctverecek, ale sloupec. Ve zvolenem sloupci
se symbol spadne co nejniz, co to jde (na drive vlozene symboly). Vyhrava ten, kdo jako prvni posklada 4 sve 
symboly v rade, sloupci nebo diagonale.

Hru hraji 2 hraci a kazdy z nich odehraje v danem kole svuj tah. Prvni "hrac" bude primo soucasti vaseho 
algoritmu. Druhym hracem muze byt clovek nebo opet pocitac. Jak toho elegantne dostahnout je naznaceno v kostre dale.
Pro jednoduchost uvazujte napevno dane symboly: kolecko (pismeno "o") pro prvniho "hrace" realizovaneho hrou samotnou
a krizek (pismeno "x") pro druheho hrace (tj. cloveka nebo pocitac).

Nasleduje kostra prgramu, ktera vam pomuze problem rozumne dekomponovat a nasledne vyresit. Rozhrani funkci by melo
byt dostatecne. Pokud jim pridate dalsi parametry, neni to chyba, ale nemelo by to byt potreba. Kazdopadne takovou 
zmenu dokumentujte pomoci komentaru. 
"""

#0=_ 1=O 2=X
# Tato funkce pro zadany stav hry vrati nejaky validni tah hrace se symbolem. V zakladu staci nahodny tah
# ktery se vejde do hraciho planu.
#
# @state	aktualni stav hry reprezentovany vhodnou strukturou (asi v tom budou nejak figurovat seznamy :) )
# @symbol	symbol hrace,pro ktereho se strategie pocita (je potreba poznat, jake posloupnosti dokoncovat 
# 		a jake naopak blokovat)
# @return	cislo sloupce v hernim planu (nemelo by ukazovat mimo herni plan)
def strategy(state, symbol,a,b,version):
        return(random.randint(0,len(state)-3))


# Tato funkce vypise pro dany stav hry herni plan pomoci textove grafiky. Nevraci nic. Ukazku vypisu najdete na konci  
# tohoto souboru. Zajistete, aby pripadna dvouciferna cisla sloupcu nerozhodila vypis.
#
# @state	aktualni stav hry reprezentovany vhodnou strukturou
def showState(state):
    length=len(state)
    for i in range (length):
        for j in range (length):
            if state[j][i]==0:
                print(" ",end=" ")
            elif state[j][i]==1:
                print("O",end=" ")
            elif state[j][i]==3:
                print("-",end=" ")
            else:
                print("X",end=" ")
        print()
    print(" ",end=" ")
    for j in range (length-2):
        print(j, end=" ")
    print()

##Tato funkce je mnou přidaná a detekuje konec hry. Vyžívá k tomu: @state- herní pole, @symbol- hráč který je na
##tahu, @a,b jsou souřadnice přidaného znaku, @xdir,ydir jsou směr ve kterém se bude detekovat

def result(state,symbol,a,b,xdir,ydir):
    temp=1
    for i in range (-1,1,2):
        x=a
        y=b
        end=False
        while end==False:
            end=True
            if state[x+xdir*i][y+ydir*i]==symbol:
                end=False
                temp+=1
                x=x+xdir*i
                y=y+ydir*i
            if temp==4:
                if symbol==2:
                    print("Game over, player 2 wins")
                else:
                    print("Game over, player 1 wins")
                return(True)
    return()
##Tato funkce slouží k rozvržení směrů, kterými se detekuje funkce "result"
def directions(state,symbol,a,b,version):
    if version==0:
        if result(state,symbol,a,b,1,0)==True:
            return(True)
        elif result(state,symbol,a,b,0,-1)==True:
            return(True)
        elif result(state,symbol,a,b,1,1)==True:
            return(True)
        elif result(state,symbol,a,b,-1,1)==True:
            return(True)
        else:
            return(False)

# Toto je zakladni funkce ukolu. Jeji parametry ani nazev v idealnim pripade nemente. V jejim prubehu se voli tahy
# prvnho a druheho hrace a vykresluje se po kazdem tahu stav hry. Funkce musi detekovat konec hry a vypsat na konci 
# vitezneho hrace
#
# @size			udava pocet policek na planu. Pocitejte s rozumnymi hodnotami (rekneme od 3 do 30)
# @secondPlayerHuman	udava, zda je druhy hrac realizovan clovekem nebo pocitacem. V pripade cloveka nactete vstup
#			vhodnym zpusobem z klavesnice. V pripade pocitace na stejnem miste znovu zavolejte funkci 				strategy(...)
# @secondPlayerStarts	znaci, ze zacina druhy hrac (tj. nezacina ten hrac realizovany hrou samotnou)
def tictactoe(size, secondPlayerHuman=True, secondPlayerStarts=True):
    a=1
    b=1
    if secondPlayerStarts==True:
        symbol=2
    else:
        symbol=1
    state=[]
    for i in range (size+2):
        state.append([])
        for j in range (size+2):
            if i==0 or j==0:
                state[i].append(3)
            elif i==(size+1) or j==(size+1):
                state[i].append(3)
            else:
                state[i].append(0)
    win=False
    while win==False:           
        if secondPlayerHuman==False or symbol%2==1:
            print("Computer turn")
            column=strategy(state, symbol,a,b,1)+1
            for i in range (size,-1,-1):
                if state[column][i]==0:
                    state[column][i]=symbol
                    a=column
                    b=i
                    break
        else:
            print("Player turn")
            print("Select column (from 0 to ",size,"): ",end="")
            column=int(input())+1
            for i in range (size,-1,-1):
                if state[column][i]==0:
                    state[column][i]=symbol
                    a=column
                    b=i
                    break
        showState(state)
        if directions(state,symbol,a,b,0)==True:
            break
        if symbol==2:
            symbol-=1
        else:
            symbol+=1
        

"""
Ukazka vypisu hry:

Player 2 turn
Select column (from 0 to 9): 5









          X
- - - - - - - - - -
0 1 2 3 4 5 6 7 8 9

Player 1 turn
Player 1 chose column 9









          X       O
- - - - - - - - - -
0 1 2 3 4 5 6 7 8 9

Player 2 turn
Select column (from 0 to 9): 6









          X X     O
- - - - - - - - - -
0 1 2 3 4 5 6 7 8 9

Player 1 turn
Player 1 chose column 5








          O
          X X     O
- - - - - - - - - -
0 1 2 3 4 5 6 7 8 9

Player 2 turn
Select column (from 0 to 9): 4








          O
        X X X     O
- - - - - - - - - -
0 1 2 3 4 5 6 7 8 9

Player 1 turn
Player 1 chose column 7








          O
        X X X O   O
- - - - - - - - - -
0 1 2 3 4 5 6 7 8 9

Player 2 turn
Select column (from 0 to 9): 3








          O
      X X X X O   O
- - - - - - - - - -
0 1 2 3 4 5 6 7 8 9
Player 2 won!
"""

