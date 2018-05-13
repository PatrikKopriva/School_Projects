# Druha domaci uloha z IB111, 2017
#
# Piste co nejprehlednejsi kod, zejmena vhodne pojmenovavejte promenne
# Pritom se snazte pouzivat anglictinu alespon ve jmenech, idealne i v komentarich
#           (za necitelny kod hrozi bodova srazka)
#
# Sve reseni pojmenujte jako "prijmeni_du2.py" a ulozte do prislusne odevzdavarny
#           (bez uvozovek a bez diakritiky)
# Celkem můžete získat až 25 bodů (16 za algoritmus souboje, 6 za analytickou funkci a 2 za drobnou modifikaci vypisu algoritmu)
# --------------------------------------------------------------
# zde muzete definovat pripadne importy
from random import randint, random
"""
1) [az 16 bodu]Predstavte si zjednoduseny sobojovy system podobny systemu z RPG her
pravidla jsou nasledujici:
 - boj probiha jako sekvence kol, v kazdem kole utoci hrac (player) na nestvuru (monster)
        (nestvura na hrace nijak neutoci)
 - sila hracova utoku je vypoctena jako hod 6stennou kostkou + zakladni utok (predavany 1. parametrem)
 - sila obrany nestvury se vypocita pouze jako samotny hod 6stennou kostkou (zadnou zakladni obranu nepricitame)
          	!! padne-li (na utok nebo na obranu) sestka, hazi se znovu a hodnoty se pricitaji!! (ukazka: round 13)
 - nestvura ma zadany pocet zivotu (2. parametrem). Klesne-li na/pod nulu, simulace konci 
		!! u nestvury v tom pripade vypiste 0 hitpoints, ne zapornou hodnotu
 - pokud je sila utoku vyssi, nez sila obrany, nestvura ztraci tolik zivotu, kolik je rozdil techto hodnot

 - definujte jeste 3. parametr "output", ktery pokud je roven True, zajisti vypisovani stavu hry:
 - v kazdem kole vypisujte hozene hodnoty hracem (pred pricitanim) a nestvurou
 - pokud byla zranena nestvura, vypiste o kolik a kolik zivotu z kolika ji zbyva
 - na konci vypiste, po kolika kolech simulace skoncila

(moznost "vypnout" vypisovani je nutne pro nasledujici ukol)
------------------------------------------------------------------
ukazka: simple_fight(4, 42)
------------------------------------------------------------------
round 1: player throws 3, monster throws 5.
	Monster was hit for 2, remaining 40/42 hitpoints.

round 2: player throws 5, monster throws 3.
	Monster was hit for 6, remaining 34/42 hitpoints.

round 3: player throws 3, monster throws 4.
	Monster was hit for 3, remaining 31/42 hitpoints.

round 4: player throws 3, monster throws 2.
	Monster was hit for 5, remaining 26/42 hitpoints.

round 5: player throws 4, monster throws 5.
	Monster was hit for 3, remaining 23/42 hitpoints.

round 6: player throws 1, monster throws 5.

round 7: player throws 1, monster throws 5.

round 8: player throws 4, monster throws 2.
	Monster was hit for 6, remaining 17/42 hitpoints.

round 9: player throws 3, monster throws 5.
	Monster was hit for 2, remaining 15/42 hitpoints.

round 10: player throws 2, monster throws 1.
	Monster was hit for 5, remaining 10/42 hitpoints.

round 11: player throws 1, monster throws 2.
	Monster was hit for 3, remaining 7/42 hitpoints.

round 12: player throws 2, monster throws 1.
	Monster was hit for 5, remaining 2/42 hitpoints.

round 13: player throws 4, monster throws 8.

round 14: player throws 1, monster throws 2.
	Monster was hit for 3, remaining 0/42 hitpoints.

Game ended in 14 rounds
----------------------------------------------------------------- 
Napiste funkci simulujici tento soubojovy system
"""
def simple_fight(attack, max_hp, output):
    rounds=0
    hp=max_hp
    while hp>0:
        off=attack
        deff=0
        rounds+=1
        throwoff=dice()
        throwdeff=dice()
        for i in range (len(throwoff)):
            off+=throwoff[i]
        for j in range (len(throwdeff)):
            deff+=throwdeff[j]
        dmg=off-deff
        if dmg>0:
            hp-=dmg
        if output==True:
            printing(throwoff, throwdeff, dmg, hp, max_hp, attack, rounds)
    return(rounds)

def dice():
    x=6
    throw=[]
    while x==6:
        x=randint(1,6)
        throw.append(x)
    return(throw)

def printing(throwoff, throwdeff, dmg, hp, max_hp, attack, rounds):    
    print("round: ",rounds,", player throws: ",throws_print(throwoff),
          ", monster throws: ",throws_print(throwdeff))
    if dmg>0:
        print("Monster was hit for: ",dmg,", remaining",
              hp,"/",max_hp," hitpoints.")
    print()
    if hp<=0:
        print("Game over on round: ",rounds)

def throws_print(throws):
    x=""
    for i in range(len(throws)):
        if i!=(len(throws)-1):
            x+=(str(throws[i])+"+")
        else:
            x+=str(throws[i])
    return(x)


"""
2) [az 7 bodů] Napiste funkci, ktera pro zadany opakovani simulaci (3. parametr) z bodu 1) s parametry attack, max_hp
vypocte prumerny pocet kol.
------------------------------------------------------------------
ukazka: simple_fight_stats(4, 42)
------------------------------------------------------------------
For attack 4 and 42 hitpoints, average simulation length is 9.925 rounds.
"""
def simple_fight_stats(attack, max_hp, iterations):
    x=0
    for i in range (iterations):
        x+=simple_fight(attack, max_hp, False)
    avg=x/iterations
    print("For attack",attack,"and",max_hp,
          "hitpoints, average simulation lenght is:",avg,"rounds.")
"""
3) [az 2 body] upravte program z bodu 1 tak, aby se v pripade opakovani hodu po padnuti sestky
vypisovaly hodnoty jednotlivych hodu oddelenych pluskem. Priklad:

....
13. round: player throws 4, monster throws 6+2.
...
"""

