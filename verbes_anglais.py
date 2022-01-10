# -*- coding: utf-8 -*-
"""
Created on Mon Jan 10 18:49:11 2022

@author: hcflem
"""
from random import randint

import time 

verbes=[['parier', ['to bet', 'bet', 'bet']], ['bruler', ['to burn', 'burnt', 'burnt']], ['Éclater', ['to burst', 'burst', 'burst']], ['se courber, se pencher', ['to bend', 'bent', 'bent']], ['offrir un prix (enchère)-ordonner', ['to bid', 'bid', 'bid']], ['jeter, distribuer (rôles)', ['to cast', 'cast', 'cast']], ['coûter', ['to cost', 'cost', 'cost']], ['couper', ['to cut', 'cut', 'cut']], ['frapper, atteindre', ['to hit', 'hit', 'hit']], ['blesser', ['to hurt', 'hurt', 'hurt']], ['permettre, louer', ['to let', 'let', 'let']], ['mettre', ['to put', 'put', 'put']], ['cesser (de), démissionner', ['to quit', 'quit', 'quit']], ['lire', ['to read', 'read', 'read']], ['débarrasser ', ['to rid', 'rid', 'rid']], ['fixer, poser', ['to set', 'set', 'set']], ['verser (larme) muer-répandre', ['to shed', 'shed', 'shed']], ['fermer', ['to shut', 'shut', 'shut']], ['(se) fendre, inciser', ['to slit', 'slit', 'slit']], ['fendre, couper en 2', ['to split', 'split', 'split']], ['répandre', ['to spread', 'spread', 'spread']], ['enfoncer', ['to thrust', 'thrust', 'thrust']], ['supporter/tolérer/demeurer', ['to abide', 'abode', 'abode']], ['lier, relier', ['to bind', 'bound', 'bound']], ['saigner', ['to bleed', 'bled', 'bled']], ['Élever des animaux', ['to breed', 'bred', 'bred']], ['apporter', ['to bring', 'brought', 'brought']], ['construire', ['to build', 'built', 'built']], ['acheter', ['to buy', 'bought', 'bought']], ['attraper', ['to catch', 'caught', 'caught']], ["s'accrocher", ['to cling', 'clung', 'clung']], ['ramper', ['to creep', 'crept', 'crept']], ['distribuer', ['to deal', 'dealt', 'dealt']], ['creuser', ['to dig', 'dug', 'dug']], ['rêver', ['to dream', 'dreamt', 'dreamt']], ["habiter / -- on : s'appesantir sur", ['to dwell', 'dwelt', 'dwelt']]]





def script(verbes,i_verbe):
    print("\n     ",verbes[i_verbe][0])
    réponse_infinitif=input("        Écrivez son infinitif : ")
    réponse_preterit=input("        Écrivez son prétérit  : ") 
    réponse_participe_passé=input("        Écrivez son participe passé  : ")
    réponses=[réponse_infinitif,réponse_preterit,réponse_participe_passé]
    compteur=0
    if 'exit()' in réponses:
        return False
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
    verbes2=verbes
    score=0
    échecs=[]
    invariable=0
    print("Bienvenue sur mon script d'entrainement aux verbes irréguliers,\nPour quitter le programme, répondez 'exit()' lors de la conjugaison d'un verbe.\nSi vous avez des idées de modifications/bugs => @hcflem ")
    time.sleep(3)
    while invariable==0:
        i_verbe=randint(0,len(verbes2))
        a=script(verbes2,i_verbe)
        if a==True:
            score+=1
        elif a==False:
            print('\nScore total : ',score,"/",36-len(verbes2),'     Github : https://github.com/hcflem/ \nAu revoir !')
            time.sleep(2)
            return 
        else:
            échecs.append(a)
        del verbes2[i_verbe]
        if len(échecs)==0:
            print("\nVotre score est de ",score,"/",36-len(verbes2),"        Échecs: ")
        else:
            print("\nVotre score est de ",score,"/",36-len(verbes2),"        Échecs:",échecs)
        
    return 

main(verbes)

