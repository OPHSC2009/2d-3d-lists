from tkinter import*
root=Tk()
root.geometry("1000x1000")
root.title("2d & 3d lists")

fruits=["apple","banana","mango","pear"]
print(fruits)
print(fruits[0])
print(fruits[1])
print("\n")
lbl_1=Label(root,text=fruits[0])
lbl_1.place(relx=0.5,rely=0.2, anchor=CENTER)

subjects=[["maths","54"],["english","59"],["science","48"],["spanish","56"]]
print(subjects)
print(subjects[0])
print(subjects[0][1])
print("\n")
lbl_2=Label(root,text=subjects[0][1])
lbl_2.place(relx=0.5,rely=0.4, anchor=CENTER)

students=[[["harnoor","maths","59"],["Farzan","maths","32"],["riya","maths","61"],["priyansh","maths","44"]]]
print(students)
print(students[0][1][2])
lbl_3=Label(root,text=students[0][1][2])
lbl_3.place(relx=0.5,rely=0.5, anchor=CENTER)

root.mainloop()