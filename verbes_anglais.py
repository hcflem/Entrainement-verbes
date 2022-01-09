# -*- coding: utf-8 -*-
"""
Created on Wed Jan  5 18:51:37 2022

@author: hcflem
"""

from random import randint

# import csv
import time
# mydict = {}

# with open('verbs.csv', mode='r') as inp:
#     reader = csv.reader(inp)
#     verbes = [[rows[1],[rows[2],rows[3],rows[4]]] for rows in reader]
verbes=[['parier', ['to bet', 'bet', 'bet']], ['brÃ»ler', ['to burn', 'burnt', 'burnt']], ['Ã©clater', ['to burst', 'burst', 'burst']], ['se courber, se pencher', ['to bend', 'bent', 'bent']], ['offrir un prix (enchÃ¨re)-ordonner', ['to bid', 'bid', 'bid']], ['jeter, distribuer (rÃ´les)', ['to cast', 'cast', 'cast']], ['coÃ»ter', ['to cost', 'cost', 'cost']], ['couper', ['to cut', 'cut', 'cut']], ['frapper, atteindre', ['to hit', 'hit', 'hit']], ['blesser', ['to hurt', 'hurt', 'hurt']], ['permettre, louer', ['to let', 'let', 'let']], ['mettre', ['to put', 'put', 'put']], ['cesser (de), dÃ©missionner', ['to quit', 'quit', 'quit']], ['lire', ['to read', 'read', 'read']], ['dÃ©barrasser ', ['to rid', 'rid', 'rid']], ['fixer, poser', ['to set', 'set', 'set']], ['verser (larme) muer-rÃ©pandre', ['to shed', 'shed', 'shed']], ['fermer', ['to shut', 'shut', 'shut']], ['(se) fendre, inciser', ['to slit', 'slit', 'slit']], ['fendre, couper en 2', ['to split', 'split', 'split']], ['rÃ©pandre', ['to spread', 'spread', 'spread']], ['enfoncer', ['to thrust', 'thrust', 'thrust']], ['supporter/tolÃ©rer/demeurer', ['to abide', 'abode', 'abode']], ['lier, relier', ['to bind', 'bound', 'bound']], ['saigner', ['to bleed', 'bled', 'bled']], ['Ã©lever des animaux', ['to breed', 'bred', 'bred']], ['apporter', ['to bring', 'brought', 'brought']], ['construire', ['to build', 'built', 'built']], ['acheter', ['to buy', 'bought', 'bought']], ['attraper', ['to catch', 'caught', 'caught']], ["s'accrocher", ['to cling', 'clung', 'clung']], ['ramper', ['to creep', 'crept', 'crept']], ['distribuerÂ\xa0Â\xa0Â\xa0', ['to deal', 'dealt', 'dealt']], ['creuser', ['to dig', 'dug', 'dug']], ['rÃªver', ['to dream', 'dreamt', 'dreamt']], ["habiter / -- on : s'appesantir sur", ['to dwell', 'dwelt', 'dwelt']]]

def aleatoire(verbes):
    return randint(0,len(verbes))


def script(verbes,i_verbe):
    print("\n",verbes[i_verbe][0])
    réponse_infinitif=input("    Écrivez son infinitif : ")
    réponse_preterit=input("    Écrivez son prétérit  : ") 
    réponse_participe_passé=input("    Écrivez son participe passé  : ")
    réponses=[réponse_infinitif,réponse_preterit,réponse_participe_passé]
    compteur=0
    if réponses[0]==verbes[i_verbe][1][0]:
        compteur+=1
    if réponses[1]==verbes[i_verbe][1][1]:
        compteur+=1
    if réponses[2]==verbes[i_verbe][1][2]:
        compteur+=1
    if compteur==3:
        return True
    else:
        return verbes[i_verbe][0]
    

  

    
def main(verbes):
    print("Bienvenue sur mon script d'entrainement aux verbes irréguliers, \n si vous avez des idées de modifications/bugs => @hcflem ")
    time.sleep(3)
    verbes2=verbes
    score=0
    échecs=[]
    invariable=0
    i_verbe=aleatoire(verbes2)
    print("")
    while invariable==0:
        a=script(verbes2,i_verbe)
        if a==True:
            score+=1
        else:
            échecs.append(a)
        del verbes2[i_verbe]
        print("\nVotre score: ",score,"/",36-len(verbes2),"     Erreurs :",échecs)
    return 

main(verbes)
