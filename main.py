# -*- coding: utf-8 -*-
"""
Created on Thu Oct 20 12:09:56 2022

@author: csuser
"""

# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import json
from tkinter import *
from tkinter import ttk
from tkinter.tix import *
import os

#fileN = open("fileNames.txt","a")

window=Tk()
#------------------------------------------------------------------------------------------------
file1=open('passF.txt.txt', 'r')
list1=file1.readlines()
namelistF=[]
passlistF=[]
for i in list1:
    i=i.strip('\n')
    list2=i.split(' ')
    namelistF.append(list2[0])
    passlistF.append(list2[1])

file2=open('passS.txt.txt', 'r')
list1=file2.readlines()
namelistS=[]
passlistS=[]
for i in list1:
    i=i.strip('\n')
    list2=i.split(' ')
    namelistS.append(list2[0])
    passlistS.append(list2[1])


#-------------------------------------------------------------------------------------------------
#AVL

# Create a tree node
class AVLTreeNode(object):
    def __init__(self, name, pss):
        self.name = name
        self.pss=pss
        self.left = None
        self.right = None
        self.height = 1


class AVLTree(object):

    # Function to insert a node
    def insert_node(self, root, name, pss):

        # Find the correct location and insert the node
        if not root:
            return AVLTreeNode(name, pss)
        elif name < root.name:
            root.left = self.insert_node(root.left, name, pss)
        else:
            root.right = self.insert_node(root.right, name,pss)

        root.height = 1 + max(self.getHeight(root.left),
                              self.getHeight(root.right))

        # Update the balance factor and balance the tree
        balanceFactor = self.getBalance(root)
        if balanceFactor > 1:
            if name < root.left.name:
                return self.rightRotate(root)
            else:
                root.left = self.leftRotate(root.left)
                return self.rightRotate(root)

        if balanceFactor < -1:
            if name > root.right.name:
                return self.leftRotate(root)
            else:
                root.right = self.rightRotate(root.right)
                return self.leftRotate(root)

        return root

    # Function to delete a node
    def delete_node(self, root, key):

        # Find the node to be deleted and remove it
        if not root:
            return root
        elif key < root.key:
            root.left = self.delete_node(root.left, key)
        elif key > root.key:
            root.right = self.delete_node(root.right, key)
        else:
            if root.left is None:
                temp = root.right
                root = None
                return temp
            elif root.right is None:
                temp = root.left
                root = None
                return temp
            temp = self.getMinValueNode(root.right)
            root.key = temp.key
            root.right = self.delete_node(root.right,
                                          temp.key)
        if root is None:
            return root

        # Update the balance factor of nodes
        root.height = 1 + max(self.getHeight(root.left),
                              self.getHeight(root.right))

        balanceFactor = self.getBalance(root)

        # Balance the tree
        if balanceFactor > 1:
            if self.getBalance(root.left) >= 0:
                return self.rightRotate(root)
            else:
                root.left = self.leftRotate(root.left)
                return self.rightRotate(root)
        if balanceFactor < -1:
            if self.getBalance(root.right) <= 0:
                return self.leftRotate(root)
            else:
                root.right = self.rightRotate(root.right)
                return self.leftRotate(root)
        return root

    # Function to perform left rotation
    def leftRotate(self, z):
        y = z.right
        T2 = y.left
        y.left = z
        z.right = T2
        z.height = 1 + max(self.getHeight(z.left),
                           self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left),
                           self.getHeight(y.right))
        return y

    # Function to perform right rotation
    def rightRotate(self, z):
        y = z.left
        T3 = y.right
        y.right = z
        z.left = T3
        z.height = 1 + max(self.getHeight(z.left),
                           self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left),
                           self.getHeight(y.right))
        return y

    # Get the height of the node
    def getHeight(self, root):
        if not root:
            return 0
        return root.height

    # Get balance factore of the node
    def getBalance(self, root):
        if not root:
            return 0
        return self.getHeight(root.left) - self.getHeight(root.right)

    def getMinValueNode(self, root):
        if root is None or root.left is None:
            return root
        return self.getMinValueNode(root.left)

    def preOrder(self, root):
        if not root:
            return
        print("{0} {1}".format(root.name, root.pss), end="\n")
        self.preOrder(root.left)
        self.preOrder(root.right)

    # Print the tree
    def printHelper(self, currPtr, indent, last):
        if currPtr != None:
            sys.stdout.write(indent)
            if last:
                sys.stdout.write("R----")
                indent += "     "
            else:
                sys.stdout.write("L----")
                indent += "|    "
            print(currPtr.name, currPtr.pss)
            self.printHelper(currPtr.left, indent, False)
            self.printHelper(currPtr.right, indent, True)
    #Search
    def search(self, root, name):
        if root==None:
            return root
        else:
            if name==root.name:
                return root
            elif name>root.name:
                return self.search(root.right, name)
            else:
                return self.search(root.left, name)


passTreeF = AVLTree()
passTreeF.root = None
for i in range(len(namelistF)):
    passTreeF.root=passTreeF.insert_node(passTreeF.root, namelistF[i], passlistF[i])
#passTree.printHelper(passTree.root, " ", True)
#passTree.preOrder(passTree.root)

passTreeS = AVLTree()
passTreeS.root=None
for i in range(len(namelistS)):
    passTreeS.root=passTreeS.insert_node(passTreeS.root, namelistS[i], passlistS[i])
#passTreeS.printHelper(passTreeS.root, " ", True)
#-------------------------------------------------------------------------------------------------

# BTREE


# Create a node
class BTreeNode:
  def __init__(self, leaf=False):
    self.leaf = leaf
    self.keys = []
    self.child = []


# Tree
class BTree:
  def __init__(self, t):
    self.root = BTreeNode(True)
    self.t = t

    # Insert node
  def insert(self, k):
    root = self.root
    if len(root.keys) == (2 * self.t) - 1:
      temp = BTreeNode()
      self.root = temp
      temp.child.insert(0, root)
      self.split_child(temp, 0)
      self.insert_non_full(temp, k)
    else:
      self.insert_non_full(root, k)

    # Insert nonfull
  def insert_non_full(self, x, k):
    i = len(x.keys) - 1
    if x.leaf:
      x.keys.append((None, None))
      while i >= 0 and k[0] < x.keys[i][0]:
        x.keys[i + 1] = x.keys[i]
        i -= 1
      x.keys[i + 1] = k
    else:
      while i >= 0 and k[0] < x.keys[i][0]:
        i -= 1
      i += 1
      if len(x.child[i].keys) == (2 * self.t) - 1:
        self.split_child(x, i)
        if k[0] > x.keys[i][0]:
          i += 1
      self.insert_non_full(x.child[i], k)

    # Split the child
  def split_child(self, x, i):
    t = self.t
    y = x.child[i]
    z = BTreeNode(y.leaf)
    x.child.insert(i + 1, z)
    x.keys.insert(i, y.keys[t - 1])
    z.keys = y.keys[t: (2 * t) - 1]
    y.keys = y.keys[0: t - 1]
    if not y.leaf:
      z.child = y.child[t: 2 * t]
      y.child = y.child[0: t - 1]

  # Print the tree
  def print_tree(self, x, file, l=0):
    '''
    print("Level ", l, " ", len(x.keys), end=":")
    for i in x.keys:
      print(i, end=" ")
    print()
    l += 1
    if len(x.child) > 0:
      for i in x.child:
        self.print_tree(i, l)
    '''
    for i in x.keys:
        i1=i
        file.write(i1)
    if len(x.child)>0:
        for i in x.child:
            self.print_tree(i, file)

  # Search key in the tree
  def search_key(self, k, x=None):
    if x is not None:
      i = 0
      while i < len(x.keys) and k > x.keys[i][0]:
        i += 1
      if i < len(x.keys) and k == x.keys[i][0]:
        return (x, i)
      elif x.leaf:
        return None
      else:
        return self.search_key(k, x.child[i])

    else:
      return self.search_key(k, self.root)



#-------------------------------------------------------------------------------------------------

class Interval:
	def __init__(self, low, high):
		self.low = low
		self.high = high

	def __str__(self):
		return "[" + str(self.low) + "," + str(self.high) + "]"


class IntNode:
	def __init__(self, range, max):
		self.range = range
		self.max = max
		self.left = None
		self.right = None

	def __str__(self):
		return "[" + str(self.range.low) + ", " + str(self.range.high) + "] "


def insert(root, x):
	if root == None:
		return IntNode(x, x.high)

	if x.low < root.range.low:
		root.left = insert(root.left, x)
	else:
		root.right = insert(root.right, x)

	if root.max < x.high:
		root.max = x.high

	return root


def inOrder(root):
	if root == None:
		return

	inOrder(root.left)
	print(root, end="")
	inOrder(root.right)

def doOverlap(i1, i2):
	if (i1.low <= i2.high and i2.low <= i1.high):
		return True
	return False

def overlapSearch(root, i):
	if root==None:
		return None
	if doOverlap(root.range, i):
		return root.range
	if (root.left !=None and root.left.max >=i.low):
		return overlapSearch(root.left, i)
	return overlapSearch(root.right, i)

#-------------------------------------------------------------------------------------------------
def pssCheckF(n, p):
    #print(type(p))
    searchtest=passTreeF.search(passTreeF.root, n)
    if searchtest.pss==p:
        print("yay")
    else:
        print("no")

def pssCheckS(n, p):
    searchtest=passTreeS.search(passTreeS.root, n)
    if searchtest.pss==p:
        print("yay")
    else:
        print("no")


def hide_widget(widget):
    #okBtn.pack_forget()
    widget.destroy()



def uploadFile(n):
    n=n+".txt"
    print(n)
    def onClick():
        fileName=entry1_tk.get()
        fileName1=fileName+".txt"
        fileN=open(n, "r")
        path='D:/SEM3:/' + fileName1
        #fileA=open(fileName1, "r")
        fileA=1
        if fileA:
            list1=fileN.readlines()
            B=BTree(3)
            for i in list1:
                B.insert(i)
            fileN.close()
            fileN=open(n, "w")
            if B.search_key(fileName) is None:
                B.insert(fileName)
            B.print_tree(B.root, fileN)
            fileN.close()
            tkinter.messagebox.showinfo(" ","File Succesfully uploaded !")
        else:
            tkinter.messagebox.showinfo(" ", "File not Available !")
        w1.destroy()
    w1=Tk()
    w1.geometry("1000x2000+10+20")
    label1_tk = Label(w1, text="File Name", font=('garamond',10,'bold'),fg="black")
    label1_tk.pack()
    entry1_tk = Entry(w1, bd = 9,fg="black")
    entry1_tk.pack()
    label1_tk.place(x=350,y=300)
    entry1_tk.place(x=350,y=330)
    okBtn=Button(w1,text="Ok", fg="Black",font="Garamond", command=onClick)
    okBtn.pack(pady=20)
    okBtn.place(x=400,y=400)
    def forgUp():
        label1_tk.pack_forget()
        entry1_tk.pack_forget()
        okBtn.pack_forget()


def displayFile(fName):
    fName=fName+".txt"
    fileWind=Tk()
    fileWind.title(fName)
    lb=Label(fileWind, text=fName, font="garamond")
    S = tkinter.Scrollbar(fileWind)
    T = tkinter.Text(fileWind, height=40, width=50)
    S.pack(side=tkinter.RIGHT, fill=tkinter.Y)
    T.pack(side=tkinter.LEFT, fill=tkinter.Y)
    S.config(command=T.yview)
    T.config(yscrollcommand=S.set)
    with open(fName) as f:
        quote=(f.read())
        T.insert(tkinter.END, quote)
    fileWind.mainloop()

def readFile(n):
    w2=Tk()
    w2.geometry("1000x2000+10+20")
    def retrieve():

        fileR=cb.get()
        w2.destroy()
        displayFile(fileR)
    n=n+".txt"
    file=open(n, 'r')
    if file:
        lines = file.readlines()
        lines = [line.rstrip() for line in lines]
    var=StringVar()
    var.set("lecture1")
    vList=lines
    cb=ttk.Combobox(w2,values=vList)
    cb.place(x=300,y=350)
    okBtn=Button(w2,text="Ok", fg="Black",font="Garamond", command=retrieve)
    okBtn.pack(pady=20)
    okBtn.place(x=300,y=500)

def genTable(n):
    IntList=[]
    w2=Tk()
    w2.geometry("1000x2000+10+20")
    def retrieve():
        n=entry1_tk.get()
        n=n+'.txt'
        fileN=open(n, "r")
        list1=fileN.readlines()
        for i in list1:
            list2=i.split(' ')
            l4=[]
            for j in list2:
                list3=j.split(':')
                n1=int(list3[0])*60+int(list3[1])
                l4.append(n1)
            IntList.append(l4)
        print(IntList)
        '''
        for i in range(1, n):
            t="Lecture "+str(i)
            label2=Label(w2, text=t, fg="Black", font="Garamond")
            label2.place(x=400, y=200)
            startL=Label(w2, text="Starting time", fg="Black", font="Garamond")
            startL.place(x=200, y=500)
            startE=Entry(w2, bd=7, fg="black")
            startE.place(x=400, y=500)
            endL=Label(w2, text="Ending time", fg="Black", font="Garamond")
            endL.place(x=200, y=600)
            endE=Entry(w2, bd=7, fg="Black")
            endE.place(x=400, y=600)
            okBtn1=Button(w2, text="Ok", fg="Black", font="Garamond", command=retrieve1)
            okBtn1.place(x=900, y=800)
            print(IntList)
        '''
    nlist=range(2, 10)
    label1=Label(w2, text="Enter file with lecture timings", fg="Black", font="Garamond")
    label1.pack()
    label1.place(x=50, y=100)
    entry1_tk = Entry(w2, bd = 10,fg="black")
    entry1_tk.pack()
    entry1_tk.place(x=500, y=100)
    okBtn=Button(w2, text="Ok", fg="Black", font="Garamond", command=retrieve)
    okBtn.pack()
    okBtn.pack(pady=20)
    okBtn.place(x=800, y=100)



def facultyDisplay(n):
    def callUpload():
        uploadFile(n)
    def callRead():
        readFile(n)
    def callGen():
        genTable(n)
    #w1=Tk()
    b1=Button(window,text="Upload Files ",fg="Black",command=callUpload)
    b1.place(x=300,y=200)
    b2=Button(window,text="Read Files ",fg="Black",command=callRead)
    b2.place(x=400,y=200)
    b3=Button(window,text="Generate lecture Timetable",fg="Black", command=callGen)
    b3.place(x=500,y=200)

def studentDisplay():
    #b1=Button(window,text="Upload Files ",fg="Black",command=uploadFile)
    #b1.place(x=300,y=200)
    #b2=Button(window,text="Read Files ",fg="Black",command=readFile)
    #b2.place(x=400,y=200)
    #b3=Button(window,text="Generate lecture Timetable",fg="Black")
    #b3.place(x=500,y=200)
    def retrieve():
        n=cb.get()
        n=n+".txt"
        print(n)
        readFile(w2, n)
    w2=Tk()
    cb=ttk.Combobox(w2, values=namelistF)
    cb.place(x=300, y=350)
    okBtn=Button(w2, text="Ok", fg="Black", font="Garamond", command=retrieve)
    okBtn.pack(pady=20)
    okBtn.place(x=300, y=500)



def loginF():

    def hide_widget():
        okBtn.pack_forget()
    def retrieve():
        name=entry1_tk.get()
        pss=entry2_tk.get()
        pssCheckF(name,pss)
        close_win(name)
    def close_win(name):
       w1.destroy()
       facultyBtn.destroy()
       studentBtn.destroy()
       facultyDisplay(name)

    w1=Tk()
    w1.title("Login")
    w1.geometry("1000x2000+10+20")
    lbF=Label(w1,text="Faculty Login", fg="black", font=("Garamond",20))
    label1_tk = Label(w1, text="Name", font=('garamond',15,'bold'),fg="black",bg="white")
    label1_tk.place(x=350,y=300)
    entry1_tk = Entry(w1, bd = 9,fg="black")
    entry1_tk.place(x=350,y=330)

    label1_tk = Label(w1, text="Password",font=('garamond',15,'bold'),fg="black",bg="white")
    label1_tk.place(x=575,y=300)

    entry2_tk = Entry(w1, bd = 9, show="*")
    entry2_tk.place(x=575,y=330)

    okBtn=Button(w1,text="Ok", fg="Black",font="Garamond", command=retrieve)
    okBtn.pack(pady=20)
    okBtn.place(x=350,y=400)


def loginS():
    def hide_widget():
        okBtn.pack_forget()
    def retrieve():
        name=entry1_tk.get()
        pss=entry2_tk.get()
        pssCheckS(name,pss)
        close_win()
    def close_win():
       w1.destroy()
       facultyBtn.destroy()
       studentBtn.destroy()
       studentDisplay()
    w1=Tk()
    w1.title("Login")
    w1.geometry("1000x2000+10+20")
    lbF=Label(w1,text="Student Login", fg="black", font=("Garamond",20))
    label1_tk = Label(w1, text="Name", font=('garamond',15,'bold'),fg="black",bg="white")
    label1_tk.place(x=350,y=300)

    entry1_tk = Entry(w1, bd = 9,fg="black")
    entry1_tk.place(x=350,y=330)

    label1_tk = Label(w1, text="Password",font=('garamond',15,'bold'),fg="black",bg="white")
    label1_tk.place(x=575,y=300)

    entry2_tk = Entry(w1, bd = 9, show="*")
    entry2_tk.place(x=575,y=330)

    okBtn=Button(w1,text="Ok", fg="Black",font="Garamond", command=retrieve)
    okBtn.pack(pady=20)
    okBtn.place(x=100,y=500)

facultyBtn=Button(window,text="Faculty ",fg="Black",command=loginF)
facultyBtn.place(x=350,y=200)
studentBtn=Button(window,text="Student ",fg="Black",command=loginS)
studentBtn.place(x=500,y=200)


lb0=Label(window,text="ATOM", fg="green", font=("garamond",50))
lb0.place(x=350,y=100)
window.title('Mini Nucleus')
window.geometry("1000x2000+10+20")
window.mainloop()
