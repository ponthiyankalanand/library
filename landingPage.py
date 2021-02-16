from tkinter import *
import tkinter as tk
#getting Screen Size
root = tk.Tk()
scree_size =  str(root.winfo_screenwidth())+'x'+str(root.winfo_screenheight())

def listofBooks():
	top=Toplevel()	 
	backButton=Button(top,text="Back",command=top.destroy)
	top.geometry(scree_size)
	backButton.pack() 
	rightFrame=Frame(root)
	leftFrame=Frame(root)
	header=Frame(root)
	footer=Frame(root)

	#rightFrame.pack(side=RIGHT)
	#leftFrame.pack(side=LEFT)
	header.pack(side=TOP)
	headerName=['Book ID','Book Name','Author','Publisher','Total Copies','Available Copies']
	for i in range(5):
		h1 = Label(top,text=headerName[i])
		h1.pack()

	footer.pack(side=BOTTOM)

	

def listofBooksBorrow():
	top=Toplevel()
	 
	backButton=Button(top,text="Back",command=top.destroy)
	top.geometry(scree_size)
	backButton.pack() 
def listofUsers():
	top=Toplevel()
	 
	backButton=Button(top,text="Back",command=top.destroy)
	top.geometry(scree_size)
	backButton.pack() 
def CR():
	top=Toplevel()
	 
	backButton=Button(top,text="Back",command=top.destroy)
	top.geometry(scree_size)
	backButton.pack() 
def manage():
	top=Toplevel()
	 
	backButton=Button(top,text="Back",command=top.destroy)
	top.geometry(scree_size)
	backButton.pack() 
def EUI():
	top=Toplevel()
	 
	backButton=Button(top,text="Back",command=top.destroy)
	top.geometry(scree_size)
	backButton.pack() 
def backup():
	top=Toplevel()
	 
	backButton=Button(top,text="Back",command=top.destroy)
	top.geometry(scree_size)
	backButton.pack() 

#getting Screen Size
root.geometry(scree_size)
rightFrame=Frame(root)
leftFrame=Frame(root)
header=Frame(root)
footer=Frame(root)

rightFrame.pack(side=RIGHT)
leftFrame.pack(side=LEFT)
header.pack(side=TOP)
footer.pack(side=BOTTOM)

appName = Label(header,text="appName")
button1=Button(rightFrame,text='List Books',command=listofBooks,height = 2, width = 30)
button2=Button(rightFrame,text='List of Borrowed Books',command=listofBooksBorrow,height = 2, width = 30)
button3=Button(rightFrame,text='List of Users',command=listofUsers,height = 2, width = 30)
button4=Button(rightFrame,text='CheckOut / Return',command=CR,height = 2, width = 30)
button5=Button(leftFrame,text='Manage',height = 2,command=manage, width = 30)
button6=Button(leftFrame,text='Edit User info',command=EUI,height = 2, width = 30)
button7=Button(leftFrame,text='Backup',height = 2,command=backup, width = 30)


appName.pack()
button1.pack()
button2.pack()
button3.pack()
button4.pack()
button5.pack()
button6.pack()
button7.pack()


root.mainloop()
