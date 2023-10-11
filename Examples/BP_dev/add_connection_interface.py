import tkinter
from tkinter import *


class Node:
   def __init__(self, x0, y0, x1, y1, l, R):
      self.x0 = x0
      self.y0 = y0
      self.x1 = x1
      self.y1 = y1
      self.l = l
      self.R = R



class Graph:
   def __init__(self):
      self.nodes = []
      self.arcs = []

   def add_node(self, node):
      self.nodes.append(node)

   def add_arc(self, arc):
      self.arcs.append(arc)


def draw_node(canvas, node):
   canvas.create_oval(node.x0, node.y0, node.x1, node.y1, width=3, outline="black")


def draw_arc(canvas, arc):
   fich = "C:\\Users\\amal\\Desktop\\dossier GD\\Projet Business Process\\project\\R1\\BU_connection.txt"
   if arc.start_node.R != arc.end_node.R:
      if arc.start_node.y0 < arc.end_node.y0:
         x0 = arc.start_node.x0+20
         y0 = arc.start_node.y1
         x1 = arc.end_node.x0+20
         y1 = arc.end_node.y0
         canvas.create_line(x0, y0, x1, y1,dash=(1,1), arrow=tkinter.LAST)
         canvas.create_text((x0 + x1) / 2 - 20, y0+10, text="msg")
         with open(fich, "a") as fichier:
            fichier.write(arc.start_node.R)
            fichier.write(": ")
            fichier.write(arc.start_node.l)
            fichier.write("-->")
            fichier.write(arc.end_node.R)
            fichier.write(": ")
            fichier.write(arc.end_node.l)
            fichier.write("\n")
      else:
         x0 = arc.start_node.x0 + 20
         y0 = arc.start_node.y0
         x1 = arc.end_node.x0 + 20
         y1 = arc.end_node.y1
         canvas.create_line(x0, y0, x1, y1, dash=(1, 1), arrow=tkinter.LAST)
         canvas.create_text((x0 + x1) / 2, y0 - 10, text="msg")
         with open(fich, "a") as fichier:
            fichier.write(arc.start_node.R)
            fichier.write(": ")
            fichier.write(arc.start_node.l)
            fichier.write("-->")
            fichier.write(arc.end_node.R)
            fichier.write(": ")
            fichier.write(arc.end_node.l)
            fichier.write("\n")

def click_to_add():
   # crete new fenetre avec des radio button pour choisir
   print("111111111")
   dessin.bind("<Button-1>", record_position)

x1, y1, x2, y2 = None, None, None, None
global oldx, oldy

start_node = None
end_node = None
def record_position(event):
   global graph, start_node
   x, y = event.x, event.y

   for node in graph.nodes:
      if (x >= node.x0 - 50 and x <= node.x1 + 50
              and y >= node.y0 - 50 and y <= node.y1 + 50):
         if start_node is None:
            start_node = node
         else:
            end_node = node
            arc = Arc(start_node, end_node)
            graph.add_arc(arc)
            draw_arc(dessin, arc)
            print(start_node.l, "+", end_node.l)
            start_node = None
            end_node = None

         break


class Arc:
   def __init__(self, start_node, end_node):
      self.start_node = start_node
      self.end_node = end_node







fen = Tk()
fen.title('BUs engaged in a data-centric interaction')

bouton_quitter = Button(fen, text='Exit', command=fen.destroy)
bouton_quitter.grid(row=2, column=1, padx=3, pady=3, sticky=S+W+E)

bouton_addc = Button(fen, text='Add a connection', command=click_to_add)
bouton_addc.grid(row=2, column=0, padx=3, pady=3)

#bouton_addc = Button(fen, text='Add a connection', command=click_to_add)
#bouton_addc.grid(row=2, column=0, padx=3, pady=3)

dessin = Canvas(fen, width =1200, height =400, bg ="ivory")
dessin.grid(row = 1, column = 0, columnspan = 2, padx=5, pady=5)

graph = Graph()
with open("C:\\Users\\amal\\Desktop\\dossier GD\\Projet Business Process\\project\\R1\\CF_lifecycles.txt", 'r') as filin:
   lignes = filin.readlines()
   LI= len(lignes)
   i=-1

   j= 1
   for ligne in lignes:
      i = i + 1
      x = ligne.split("-->")
      exec(f'node{j} = Node(30+100*i, 50, 80+100*i, 100, x[0], "Customer_file")')
      graph.add_node(eval(f"node{j}"))
      draw_node(dessin, eval(f"node{j}"))
      dessin.create_text(55 + 100 * i, 70, text=x[0])
      j = j + 1
      if '-->' in ligne:
         exec(f'node{j} = Node(130+100*i, 50, 180+100*i, 100, x[1], "Customer_file")')
         graph.add_node(eval(f"node{j}"))
         draw_node(dessin, eval(f"node{j}"))
         dessin.create_text(155+100*i, 80, text=x[1])

         dessin.create_line(80+100*i, 70, 130+100*i, 70, arrow='last')
         i = i + 1
         j = j + 1









with open("C:\\Users\\amal\\Desktop\\dossier GD\\Projet Business Process\\project\\R1\\CA_lifecycles.txt", 'r') as filin:
   lignes = filin.readlines()
   LI= len(lignes)
   i=-1


   for ligne in lignes:
      i = i + 1
      x = ligne.split("-->")
      exec(f'node{j} = Node(30+100*i, 130, 80+100*i, 180, x[0], "Credit_application")')
      graph.add_node(eval(f"node{j}"))
      draw_node(dessin, eval(f"node{j}"))
      dessin.create_text(55 + 100 * i, 160, text=x[0])
      print("ahayyya", x[0])
      j = j + 1
      if '-->' in ligne:
         exec(f'node{j} = Node(130+100*i, 130, 180+100*i, 180, x[1], "Credit_application")')
         graph.add_node(eval(f"node{j}"))
         draw_node(dessin, eval(f"node{j}"))
         dessin.create_text(155+100*i, 160, text=x[1])
         dessin.create_line(80 + 100 * i, 150, 130 + 100 * i, 150, arrow='last')
         j = j + 1
         i = i + 1






for node in graph.nodes:
   print(node.R)

fen.mainloop()

f_BU_connect = "C:\\Users\\amal\\Desktop\\dossier GD\\Projet Business Process\\project\\R1\\BU_connection.txt"
with open(f_BU_connect, "r") as file:
   file.readlines()
