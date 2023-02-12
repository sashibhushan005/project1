from tkinter import *


"""
########################################################################################################################
                                   OPENING A WINDOW
########################################################################################################################
"""
root = Tk()
root.title("project")
root.config(bg="light blue")
root.geometry("600x800")
#root.resizable(width=False,height=False)
new=root
bg=PhotoImage(file="rootbg (1)-overlay.png")
my_lab=Label(root,image=bg)
my_lab.place(x=0,y=0,relwidth=1,relheight=1)
root.iconbitmap("logo2.ico")





"""
########################################################################################################################
                                  GETTING VALUES
########################################################################################################################
"""


class getval:

    """def twoval():
        global n1
        global n2

        a =DoubleVar()
        b = DoubleVar()
        l1 = Label(root, text="ENTER THE VALUE OF A   ", background="light blue",foreground="black")
        lab2 = Label(root, text="ENTER THE VALUE OF B", background="light blue",foreground="black")
        n1 = Entry(root,textvariable=a)
        n2 = Entry(root,textvariable=b)
        n1.insert(END, '')
        n2.insert(END, '')
        l1.grid(row=7, column=0,pady=5)
        n1.grid(row=7, column=1,pady=5)
        lab2.grid(row=8, column=0,pady=10)
        n2.grid(row=8, column=1,pady=5)"""



    def threeval():
        global n1
        global n2
        global n3
        a = DoubleVar()
        b = DoubleVar()
        c = DoubleVar()

        l1 = Label(root, text="ENTER THE VALUE OF A   ",background="light blue",foreground="black")
        lab2 = Label(root, text="ENTER THE VALUE OF B    ",background="light blue",foreground="black")
        n1 = Entry(root, textvariable=a)
        n2 = Entry(root, textvariable=b)
        l1.grid(row=7, column=0, pady=5)
        n1.grid(row=7, column=1, pady=5)
        lab2.grid(row=8, column=0, pady=5)
        n2.grid(row=8, column=1, pady=5)

        lab3 = Label(root, text="ENTER THE VALUE OF C   ",background="light blue",foreground="black")
        n3 = Entry(root, textvariable=c)
        lab3.grid(row=9, column=0)
        n3.grid(row=9, column=1)




"""twov=Button(new,text="For a,b",command=getval.twoval,background="cyan")
twov.grid(row=1,column=0,pady=10)"""
twov1=Button(new,width=40,text=" TO ENTER THE VALUES CLICK!",command=getval.threeval,background="cyan")
twov1.grid(row=1,column=0,columnspan=5)

"""
########################################################################################################################
                                    FORMULA
########################################################################################################################
"""

class ans:
    def f1():
        global step1
        global step2
        global step4
        global step6
        global step7
        global step8



        new = root
        step1 = Label(new, text="(A+B)^2 = (A * A) + (B * B) - (2 * A * B)")
        step1.grid(row=14, column=0,columnspan=20,pady=15)

        step2 = Label(new, text="A * A = " + str(float(n1.get()) ** 2))

        step2.grid(row=15, column=0)

        step4 = Label(new, text="B * B = " + str(float(n2.get()) * float(n2.get())))

        step4.grid(row=16, column=0)

        step6 = Label(new, text="2 * A * B =" + str(2 * float(n1.get()) * float(n2.get())))

        step6.grid(row=17, column=0)

        step7 = Label(new, text="TOTAL = " + str(
            (float(n1.get()) * float(n1.get())) + (float(n2.get()) * float(n2.get())) + (
                        2 * float(n1.get()) * float(n2.get()))))

        step7.grid(row=18, column=0)





    def f2():
        global step1
        global step2
        global step4
        global step6
        global step7
        global step8
        new = root
        step1 = Label(new, text="(A+B)^2 = (A * A) + (B * B) - (2 * A * B)")
        step1.grid(row=14, column=0)

        step2 = Label(new, text="A * A = " + str(float(n1.get()) ** 2))

        step2.grid(row=15, column=0)

        step4 = Label(new, text="B * B = " + str(float(n2.get()) **2 ))

        step4.grid(row=16, column=0)

        step6 = Label(new, text="2 * A * B =" + str(2 * float(n1.get()) * float(n2.get())))

        step6.grid(row=17, column=0)

        step7 = Label(new, text="Total = " + str(
            (float(n1.get()) * float(n1.get())) + (float(n2.get()) * float(n2.get())) - (
                    2 * float(n1.get()) * float(n2.get()))))

        step7.grid(row=18, column=0)


    def f3():
        global step1
        global step2
        global step4
        global step6
        global step7
        global step8
        new = root
        step1 = Label(new, text="(A+B)^3 = (A)^3+(B)^3+[3*(A)^2*B]+[3*A*(B)^2]")
        step1.grid(row=14, column=0)

        step2 = Label(new, text="(A)^3 = " + str(float(n1.get()) **3))

        step2.grid(row=15, column=0)

        step4 = Label(new, text="3*(A)^2*B= " + str(3 * (float(n1.get()) ** 2) * (float(n2.get()))))


        step4.grid(row=16, column=0)

        step6 = Label(new, text="3*A*(B)^2=" + str(3 * (float(n1.get())) * (float(n2.get())) ** 2))

        step6.grid(row=17, column=0)

        step7 = Label(new, text="(B)^3 = " + str(float(n2.get()) ** 3))

        step7.grid(row=18, column=0)

        step8 = Label(new,
                      text="TOTAL= " + str((float(n1.get()) ** 3) + (3 * (float(n1.get()) ** 2) * (float(n2.get())))
                                            + (3 * (float(n1.get())) * (float(n2.get())) ** 2) + (
                                                        float(n2.get()) ** 3)))


        step8.grid(row=19, column=0)




    def f4():
        global step1
        global step2
        global step4
        global step6
        global step7
        global step8
        new = root
        step1 = Label(new, text="(A-B)^3 = (A)^3-(B)^3+[3*(A)^2*B]+[3*A*(B)^2]")
        step1.grid(row=14, column=0)

        step2 = Label(new, text="(A)^3 = " + str(float(n1.get()) **3))

        step2.grid(row=15, column=0)

        step4 = Label(new, text="3*(A)^2*B= " + str(3 * (float(n1.get()) ** 2) * (float(n2.get()))))


        step4.grid(row=16, column=0)

        step6 = Label(new, text="3*A*(B)^2=" + str(3 * (float(n1.get())) * (float(n2.get())) ** 2))

        step6.grid(row=17, column=0)

        step7 = Label(new, text="(B)^3 = " + str(float(n2.get()) ** 3))

        step7.grid(row=18, column=0)

        step8 = Label(new,
                      text="TOTAL   = " + str((float(n1.get()) ** 3) + (3 * (float(n1.get()) ** 2) * (float(n2.get())))
                                            + (3 * (float(n1.get())) * (float(n2.get())) ** 2) - (
                                                        float(n2.get()) ** 3)))
        step8.grid(row=19, column=0)




    def f5():
        global step1
        global step2
        global step4
        global step6
        global step7
        global step8
        new = root
        step1 = Label(new, text="(A)^3+(B)^3 = (A + A) ((A * A) + (B * B) - (2 * A * B)")
        step1.grid(row=14, column=0)

        step2 = Label(new, text="(A * A) - (B * B) = " + str(float(n1.get()) * (float(n1.get()))))

        step2.grid(row=15, column=0)

        step4 = Label(new, text="(2 * A * B) = " + str((2*(float(n1.get()) * (float(n1.get()))))))

        step4.grid(row=16, column=0)


        step8 = Label(new,
                      text="TOTAL = " + str(
                          (float(n1.get()) * (float(n1.get()))) - (2 * (float(n1.get()) * (float(n1.get()))))))
        step8.grid(row=17, column=0)


    def f6():
        global step1
        global step2
        global step4
        global step6
        global step7
        global step8
        new = root
        step1 = Label(new, text="(A)^3-(B)^3 = (A + A) ((A * A) + (B * B) + (2 * A * B)")
        step1.grid(row=14, column=0)

        step2 = Label(new, text="(A * A) - (B * B) = " + str(float(n1.get()) * (float(n1.get()))))

        step2.grid(row=15, column=0)

        step4 = Label(new, text="(2 * A * B) = " + str((2*(float(n1.get()) * (float(n1.get()))))))

        step4.grid(row=16, column=0)


        step8 = Label(new,
                      text="TOTAL= " + str(
                          (float(n1.get()) * (float(n1.get()))) - (2 * (float(n1.get()) * (float(n1.get()))))))
        step8.grid(row=17, column=0)

    def f7():

        global stepx
        global stepy
        global stepz
        global stepv
        new = root
        stepx = Label(new, text="(A+B+C)^2 = (A)^2+(B)^2+(C)^2+2AB+2BC+2CA")
        stepx.grid(row=14, column=0)

        stepy = Label(new, text="(A * A) + (B * B) + (C * C) = " + str(float(n1.get()) * (float(n1.get())) + (float(n2.get())) * (float(n2.get())) + (float(n3.get())) * (float(n3.get()))))

        stepy.grid(row=15, column=0)

        stepz = Label(new, text="(2 * A * B) + (2 * B * C) + (2 * C * A)= " + str((2*(float(n1.get())) * (float(n2.get()))) + (2*(float(n2.get())) * (float(n3.get()))) + (2*(float(n3.get())) * (float(n1.get())))))

        stepz.grid(row=16, column=0)

        stepv = Label(new,
                      text="TOTAL= " + str((float(n1.get())) * (float(n1.get())) + (float(n2.get())) * (float(n2.get())) + (float(n3.get())) * (float(n3.get())) + (2*(float(n1.get()) * (float(n2.get())))) + (2*(float(n2.get()) * (float(n3.get())))) + (2*(float(n3.get())) * (float(n1.get())))))
        stepv.grid(row=17, column=0)

    def f8():
        global stepx
        global stepy
        global stepz
        global stepv
        new = root
        stepx = Label(new, text="(A-B-C)^2 = (A)^2+(B)^2+(C)^2-2AB+2BC-2CA")
        stepx.grid(row=14, column=0)

        stepy = Label(new, text="(A * A) + (B * B) + (C * C) = " + str(float(n1.get()) * (float(n1.get())) + (float(n2.get())) * (float(n2.get())) + (float(n3.get())) * (float(n3.get()))))

        stepy.grid(row=15, column=0)
        stepz = Label(new, text="(2 * A * B) + (2 * B * C) + (2 * C * A)= " + str((2 * (float(n1.get())) * (float(n2.get()))) + (2 * (float(n2.get())) * (float(n3.get()))) - (2 * (float(n3.get())) * (float(n1.get())))))

        stepz.grid(row=16, column=0)


        stepv = Label(new,
                      text="TOTAL= " + str((float(n1.get())) * (float(n1.get())) + (float(n2.get())) * (float(n2.get())) + (float(n3.get())) * (float(n3.get())) - (2 * (float(n1.get())) * (float(n2.get()))) + (2 * (float(n2.get())) * (float(n3.get()))) - (2 * (float(n3.get())) * (float(n1.get())))))
        stepv.grid(row=17, column=0)


    def clear():
        step1.destroy()
        step2.destroy()
        step4.destroy()
        step6.destroy()
        step7.destroy()
        step8.destroy()

    def clear2():
        stepx.destroy()
        stepy.destroy()
        stepz.destroy()
        stepv.destroy()

"""
########################################################################################################################
                               BUTTON
########################################################################################################################
"""

opt = ["(A+B)^2", "(A-B)^2", "(A+B)^3", "(A-B)^3", "(A)^3+(B)^3", "(A)^3-(B)^3", "(A+B+C)^2", "(A-B-C)^2"]
mylab = Label(root, text="SRI RAMAKRISHNA MISSION VIDYALAYA \n POLYTECHNIC COLLEGE",
              anchor="center",font="bold",
              foreground="black")


mylab.grid(row=0, column=0,columnspan=20)


b1 = Button(root, text=opt[0], width=20, command=ans.f1,background="cyan")

b2 = Button(root, text=opt[1], width=20, command=ans.f2,background="cyan")

b3 = Button(root, text=opt[2], width=20, command=ans.f3,background="cyan")

b4 = Button(root, text=opt[3], width=20, command=ans.f4,background="cyan")

b5 = Button(root, text=opt[4], width=20, command=ans.f5,background="cyan")

b6 = Button(root, text=opt[5], width=20, command=ans.f6,background="cyan")

b7 = Button(root, text=opt[6], width=20, command=ans.f7,background="cyan")

b8 = Button(root, text=opt[7], width=20, command=ans.f8,background="cyan")

b9= Button(root,text="CLEAR",width=20,background="cyan",command=ans.clear)

b10= Button(root,text="CLEAR",width=20,background="cyan",command=ans.clear2)



"""
########################################################################################################################
                    GRID OF THE BUTTON
########################################################################################################################
"""
b1.grid(row=10, column=0)

b2.grid(row=10, column=1)

b3.grid(row=11, column=0)

b4.grid(row=11, column=1)

b5.grid(row=12, column=0)

b6.grid(row=12, column=1)

b7.grid(row=13, column=0)

b8.grid(row=13, column=1)

b9.grid(row=25,column=0)

b10.grid(row=25,column=1)




new.mainloop()
