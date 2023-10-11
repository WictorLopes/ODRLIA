#Python3 implementation of the approach
#The line below is to run in Brazil
# -*- coding: utf-8 -*-

import glob
import os
from os import listdir
from os.path import isfile, join
from pathlib import Path


class Graph:
    adj = []
    fich = "C:\\Users\\wicto\\Downloads\\Nova pasta\\BP_dev\\Customer file\\BU_lifecycle\\lifecycle.txt"
    # Function to fill empty adjacency matrix
    def __init__(self, v, e,adj):

        self.v = v
        self.e = e
        Graph.adj = adj


    # Function to add an edge to the graph

    # Function to perform DFS on the graph
    def DFS(self, start, visited, FirstBUVisit,fich):
        # Set current node as visited
        visited[start] = True

        # For every node of the graph
        for i in range(self.v):

            # If some node is adjacent to the current node and it has not already been visited
            if (Graph.adj[start][i] != 0 and
                    (not visited[i])):
                # Pour conna�tre le nom de la tra
                tr = Graph.adj[start][i]

                # Mod�lisation du graphe d'�tat
                print(start, end=' ')
                if (start == 0):
                    op_start = "begin"
                if (start == 1):
                    op_start = "created"
                if (start == 2):
                    op_start = "opened"
                if (start == 3):
                    op_start = "verified"
                if (start == 4):
                    op_start = "rejected"
                if (start == 7):
                    op_start = "accepted"
                if (start == 8):
                    op_start = "updated"
                if (start == 5):
                    op_start = "archived"
                if (start == 6):
                    op_start = "closed"
                #Pour conna�tre le nom de l'�tat pour le mettre dans le lifecycle
                #Mod�lisation du graphe d'�tat
                if (i == 0):
                    op = "begin"
                if (i == 1):
                    op = "created"
                          # l'op�ration qui m�ne � cette transition (�tat) created par exemple
                if (i == 2):
                    op = "opened"
                if (i == 3):
                    op = "verified"
                if (i == 4):
                    op = "rejected"
                if (i == 7):
                    op = "accepted"
                if (i == 8):
                    op = "updated"
                if (i == 5):
                    op = "archived"
                if (i == 6):
                    op = "closed"

                with open(Graph.fich, "a+") as fichier:

                   if FirstBUVisit == False: # si on est dans le lifecycle deja cr�er
                      if (tr == 3): # operatio interne
                         with open(Graph.fich, "r") as f:
                            for ligne in f.readlines()[-1:]:
                               print(ligne)
                         print( ligne)
                         last_line = ligne
                         if (last_line == op_start): #si la ligne actuelle contient deja l'op�ration pr�c�dente de op
                            print(op)
                            fichier.write("-->")
                            fichier.write(op)

                         else:
                            fichier.write("\n")
                            fichier.write(op_start)
                            fichier.write("-->")
                            fichier.write(op)

                      else:
                         FirstBUVisit = True
                         #fichier.write(" \n")

                   if FirstBUVisit == True: # cr�er un nouveau  lifecycle
                      FirstBUVisit = False
                      if (os.path.getsize(fich) == 0) :# si le fichier est vide on ne retourne pas � la ligne
                          fichier.write(op)
                      else: # sinon retourner � la ligne pour un nouveau lifecycle

                         fichier.write("\n")
                         fichier.write(op)

                with open(Graph.fich, "r") as f:
                    for li in f.readlines()[-1:]:
                        print(li)
                print("appel recursif")
                self.DFS(i, visited, FirstBUVisit, fich)


# Driver code
v, e = 9, 9    # v nbre de noeuds e nbre de lien

# Create the graph
G = Graph(v, e, [[0,2,0,0,0,0,0,0,0],
                 [0,0,3,0,0,0,0,0,0],
                 [0,0,0,2,0,0,0,0,0],
                 [0,0,0,0,3,0,0,3,0],
                 [0,0,0,0,0,2,0,0,0],
                 [0,0,0,0,0,0,3,0,0],
                 [0,0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0,2],
                 [0,0,0,0,0,2,0,0,0]])

state_transition = [["created", "creation"],["opened", "opening"],
                    ["verified", "verification"],
                    ["rejected", "rejection"],
                    ["accepted", "acceptance"],
                    ["updated", "update"],
                    ["archived", "archive"],
                    ["closed", "closure"]]



visited = [False] * v
FirstBUVisit = True

G.DFS(0, visited, FirstBUVisit, Graph.fich)
maliste = []
# Ces lifeycles cr�es correspondet � quels BUs???
files_bnf = [file for file in glob.glob("C:\\Users\\wicto\\Downloads\\Nova pasta\\BP_dev\\Customer file\\BU generated\\*.bnf")]
with open("C:\\Users\\wicto\\Downloads\\Nova pasta\\BP_dev\\Customer file\\BU_lifecycle\\lifecycle.txt", "r+") as f_lif:
   for l in f_lif.readlines():
      if "-->" in l:
          maliste.append(l)
          op = l.split("-->")
          for list_op in state_transition:
              if list_op[0] == op[0]:
                  op_O = list_op[1]

              if list_op[0] == op[1].rstrip():
                  op_1 = list_op[1]

          for file_bnf in files_bnf:
             with open(file_bnf, "r") as f_bnf:
                 op_0_exist = False
                 op_1_exist = False
                 for ligne in f_bnf.readlines():
                     if op_O in ligne:
                         op_0_exist = True
                     if op_1 in ligne:
                         op_1_exist = True
                 if  op_0_exist and op_1_exist:
                     print("BU�s lifecycle: ", l.rstrip(), end="")
                     print("  BU: project/R1/BU generated/", Path(file_bnf).stem, ".bnf")


      else:

          for list_op in state_transition:
              if list_op[0] == l.rstrip():
                  op = list_op[1]
          for file_bnf in files_bnf:
             with open(file_bnf, "r") as f_bnf:
                 op_exist = False
                 for ligne in f_bnf.readlines():
                     str = " \" name \": " + op
                     if  str in ligne:
                         op_exist = True
                 if op_exist:
                     print("BU�s lifecycle: ", l.rstrip(), end="")
                     print("  BU: project/R1/BU generated/", Path(file_bnf).stem,".bnf" )

          #for file_bnf in files_bnf:
              #with open(file_bnf, "r") as f_bnf:

          # for ligne in f_bnf.readlines():
       #if op_bu in ligne:
          #  fichier.write(Path(file_bnf).stem)
           #print("ahouaaa", Path(file_bnf).stem)


#with open(file_lifecyc, "r") as f_lif:
    #for ligne in f_lif.readlines():
# if "-->" in ligne:



#l'algorithme prend comme input une matrice qui mod�lise le diagramme d'�tat
#les transitions (op�ration) entre les �tats sont repr�sent�es par 3 si op inetrne et 2 si op�ration externe
#Match(BUSuccessorInternalOperation, t) je l'ai traduit comme si la transition correspond � une op�ration interne
#so Include sNeighbor in current BUcycle else le lifecycle actuel est termin� et on passe � un nouveau lifecycle