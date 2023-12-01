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

fileN = open("fileNames.txt","a")
fileN.write("lecture1 \n")
fileN.write("lecture2 \n")

window=Tk()
#------------------------------------------------------------------------------------------------
file1=open('pass.txt.txt', 'r')
list1=file1.readlines()
namelist=[]
passlist=[]
for i in list1:
    i=i.strip('\n')
    list2=i.split(' ')
    namelist.append(list2[0])
    passlist.append(list2[1])


#-------------------------------------------------------------------------------------------------
#AVL

# Create a tree node
class TreeNode(object):
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
            return TreeNode(name, pss)
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
                self.search(root.right, name)
            else:
                self.search(root.left, name)


passTree = AVLTree()
passTree.root = None
for i in range(len(namelist)):
    passTree.root=passTree.insert_node(passTree.root, namelist[i], passlist[i])
#passTree.printHelper(passTree.root, " ", True)
#passTree.preOrder(passTree.root)

#-------------------------------------------------------------------------------------------------    

def pssCheck(n, p):
    #print(type(p))
    searchtest=passTree.search(passTree.root, n)
    if searchtest.pss==p:
        print("yay")
    else:
        print("no")
        
def uploadFile():
    label1_tk = Label(window, text="File Name", font=('garamond',10,'bold'),fg="black")
    label1_tk.place(x=350,y=300)
    entry1_tk = Entry(window, bd = 9,fg="black")
    entry1_tk.place(x=350,y=330)
    fileName=entry1_tk.get()
    fileN.write(fileName)
    okBtn=Button(window,text="Ok", fg="Black",font="Garamond", command=done)
    okBtn.pack(pady=20)
    okBtn.place(x=100,y=500)
    def done():
        doneLab=Label(window, text="File sucesfully uploaded!",font=('garamond',10,'bold'),fg="black")
        doneLab.place(x=350,y=300)
def readFile():
    f=open("fileNames.txt","r")
    print(f.read())
    
def facultyDisplay():
    b1=Button(window,text="Upload Files ",fg="Black",command=uploadFile)
    b1.place(x=300,y=200)
    b2=Button(window,text="Read Files ",fg="Black",command=readFile)
    b2.place(x=400,y=200)
    b3=Button(window,text="Generate lecture Timetable",fg="Black")
    b3.place(x=500,y=200)
    
    
def loginF():
    def hide_widget():
        okBtn.pack_forget()
    def retrieve():
        name=entry1_tk.get()
        pss=entry2_tk.get()
        pssCheck(name,pss)
        close_win()
    def close_win():
       w1.destroy()
       facultyBtn.destroy()
       studentBtn.destroy()
       facultyDisplay()
   
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
    okBtn.place(x=100,y=500)


def loginS():
    def hide_widget():
        okBtn.pack_forget()
    def retrieve():
        name=entry1_tk.get()
        pss=entry2_tk.get()
        pssCheck(name,pss)
    w1=Tk()
    w1.title("Login")
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
    okBtn.place(x=100,y=500)
    
facultyBtn=Button(window,text="Faculty ",fg="Black",command=loginF)
facultyBtn.place(x=350,y=200)
studentBtn=Button(window,text="Student ",fg="Black",command=loginS)
studentBtn.place(x=500,y=200)

print("hi")
lb0=Label(window,text="ATOM", fg="green", font=("garamond",50))
lb0.place(x=350,y=100)
window.title('Mini Nucleus')
window.geometry("1000x2000+10+20")
window.mainloop()