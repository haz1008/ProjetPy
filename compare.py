import sys
import re
import sys
import re 
#Version 1:
def lect_VCF(file): 
    dico={}
    print("Processing file: "+file)
    
    with open(file, 'r') as fichier:
        for line in fichier :
            if not line.startswith('#'):
                info=line.strip().split("\t")  #transforme chaque ligne du fichier VCF en une liste
                #puisque les infos d'une ligne sont séparés par des tabulations 
                position= info[1]  #la position est le 2eme element de la ligne
                sequence=info[4]   #la sequence est le 5eme element de la ligne
                colonne_8=info[7].strip().split(";") #la colonne 8 est separée par des ; 
                svlen=colonne_8[2].strip().split("=") [1]  #svlen est le 2eme element de la colonne8, et sous forme de clef=valeur
                
                #Pour fusionner les doublouns de variants sur une meme position en fct de svlen:
                valeur=[sequence, svlen] #stockage temporaire des seq avec leurs svlen ds une liste
                if position in dico:  #Si position (clef de dico) existe deja dans dico 
                    #print("La position: "+position + " existe déjà")
                    if dico[position][1] < svlen:  # Si svlen de la sequence actuelle (svlen) est sup à celle déjà stocké ds dico sur cette meme position
                        dico[position]=valeur
                        #print("valeur")
                        
                else:
                    #print("La position "+position +  " doit etre ajoutée")
                    dico[position]=valeur #Si on a pas une clef pour cette position, on la cree et on lui affecte la valeur

    for position in dico: #pour enlever svlen du dico
        dico[position]=dico[position][0] #on ecrase [seq,svlen] par la valeur à la position 0: seq
    return dico

def dupl_v1(dico_ech):
    liste_1=[]
    liste_rep=list(dico_ech.keys()) #crée une liste des clefs du dico externe (=> P15-1, P15-2, P15-3)
    pdb=0
    for i in range(len(liste_rep)):
        for j in range(i+1, len(liste_rep)):
            dico1=dico_ech[liste_rep[i]]
            dico2=dico_ech[liste_rep[j]]
            for pos1,seq1 in dico1.items():
                for pos2,seq2 in dico2.items(): #del et dup comparer que la position
                    if seq1==seq2 and (int(pos1)-pdb <= int(pos2) <= int(pos1) +pdb):
                        if (seq1=="<DEL>" or seq1=="<INS>" or seq1=="<DUP>") and (seq2=="<DEL>" or seq2=="<INS>" or seq2=="<DUP>"): #J'ai pas les séquences des ins et des del donc je eux pas les comparer
                            print("Impossible de comparer.")
                        else:
                            liste_1.append(seq1)
    return liste_1


def dupl_var(dico_echan): #prend le nom du dico externe comme argument (P15 ou P30)
    pdb=10
    liste_var=dupl_v1(dico_ech)
    return liste_var