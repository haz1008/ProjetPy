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
                    if dico[position][1] < svlen:  # et Si svlen de la sequence actuelle (svlen) est inf à celle déjà stocké ds dico sur cette meme position
                        print("Le variant le plus long de la position "+position + " est de " +dico[position][1]+  " et sa séquence est: "+dico[position][0]) #On laisse la seq la plus longue
                        #print("TEST 1")
                        
                else:
                    #print("La position "+position +  " doit etre ajoutée")
                    dico[position]=valeur #Si on a pas une clef pour cette position, on la cree et on lui affecte la valeur

    for position in dico: #pour enlever svlen du dico
        dico[position]=dico[position][0] #on ecrase [seq,svlen] par la valeur à la position 0: seq
        #dico[position].pop([1])?
    #print(dico) ?
    return dico

def dupl_v1(dico_ech):
    liste_1=[]
    liste_rep=list(dico_ech.keys())
    for i in range(len(liste_rep)):
        for j in range(i+1, len(liste_rep)):
            dico1=dico_ech[liste_rep[i]]
            dico2=dico_ech[liste_rep[j]]
            for pos1,seq1 in dico1.items():
                for pos2,seq2 in dico2.items():
                    if seq1==seq2 and pos1==pos2:
                        liste_1.append(seq1)
    return liste_1


def dupl_var(dico_echan): #prend le nom du dico externe comme argument (P15 ou P30)
    liste_var=[]
    liste_replicats=list(dico_echan.keys()) #crée une liste des clefs du dico externe (=> P15-1, P15-2, P15-3)
    #print(liste_replicats)

    #Pour comparer les dico 2 à 2:
    for i in range(len(liste_replicats)): #iteration sur tous les indices des réplicats dans la liste
    #i représente l'indice du premier réplicat de la paire à comparer (ex:i=0 => P15-1)
        for j in range(i+1, len(liste_replicats)): #iteration sur tous les indices des rép suivants (i+1)
    #sans cette boucle, chaque paire de rép va etre répetée 2 fois.
            dico_rep1=dico_echan[liste_replicats[i]]
            #print(dico_rep1)
            dico_rep2=dico_echan[liste_replicats[j]] #extraction et stockage temporaire des données de chacun des sous_dicos de la paire actuelle, pour pouvoir les comparer
    #dico_echan est la source de ces données et la liste_replicats fournit les clefs (sous_dico) pour acceder à ces données
            #print(dico_rep2)
            for pos1, seq1 in dico_rep1.items():
                for pos2, seq2 in dico_rep2.items(): #iterations sur les clefs et valeurs de chacun des sous-dico
                    if seq1==seq2 and (int(pos1)-10 <= int(pos2) <= int(pos1) +10):
                        liste_var.append(seq1)
    #print("TEST3")
    return liste_var
