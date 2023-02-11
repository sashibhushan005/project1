from tkinter import *


root = Tk()
root.title("project")
root.config(bg="light blue")
root.geometry("550x550")
new=root




class getval:

    def twoval():
        global n1
        global n2

        a =DoubleVar()
        b = DoubleVar()
        l = Label(root, text="ENTER THE VALUES",font="italic",foreground="black")
        l.grid(row=6, column=0,pady=5)
        l1 = Label(root, text="ENTER THE VALUE OF A   ", background="light blue",foreground="black")
        lab2 = Label(root, text="ENTER THE VALUE OF B", background="light blue",foreground="black")
        n1 = Entry(root,textvariable=a)
        n2 = Entry(root,textvariable=b)
        n1.insert(END, '')
        n2.insert(END, '')
        l1.grid(row=7, column=0,pady=5)
        n1.grid(row=7, column=1,pady=5)
        lab2.grid(row=8, column=0,pady=10)
        n2.grid(row=8, column=1,pady=5)
        l.config(background="light blue")


    def threeval():
        a = DoubleVar()
        b = DoubleVar()
        l = Label(root, text="ENTER THE VALUES")
        l.grid(row=6, column=0, pady=5)
        l1 = Label(root, text="enter the value of a   ",background="light blue",foreground="black")
        lab2 = Label(root, text="enter the value of b   ",background="light blue",foreground="black")
        n1 = Entry(root, textvariable=a)
        n2 = Entry(root, textvariable=b)
        l1.grid(row=7, column=0, pady=5)
        n1.grid(row=7, column=1, pady=5)
        lab2.grid(row=8, column=0, pady=5)
        n2.grid(row=8, column=1, pady=5)
        l3 = Label(root, text="enter the value of a   ")
        lab3 = Label(root, text="enter the value of b   ")
        n3 = Entry(root, textvariable=a)
        n3 = Entry(root, textvariable=b)
        lab3.grid(row=9, column=0)
        lab3.grid(row=9, column=0)
        n3.grid(row=9, column=1)

        l.config(background="light blue")



twov=Button(new,text="For a,b",command=getval.twoval,background="cyan")
twov.grid(row=1,column=0,pady=10)
twov1=Button(new,text="For a,b,c",command=getval.threeval,background="cyan")
twov1.grid(row=1,column=1,pady=10)

"""
########################################################################################################################
                                    FORMULA

########################################################################################################################
"""

class ans:
    def f1():
        new = root
        step1 = Label(new, text="(a+b)^2 = (a * a) + (b * b) + (2 * a * b)")
        step1.grid(row=14, column=0,columnspan=20,pady=15)

        step2 = Label(new, text="a*a = " + str(float(n1.get()) ** 2))

        step2.grid(row=15, column=0)

        step4 = Label(new, text="b*b = " + str(float(n2.get()) * float(n2.get())))

        step4.grid(row=16, column=0)

        step6 = Label(new, text="2*a*b =" + str(2 * float(n1.get()) * float(n2.get())))

        step6.grid(row=17, column=0)

        step7 = Label(new, text="Total = " + str(
            (float(n1.get()) * float(n1.get())) + (float(n2.get()) * float(n2.get())) + (
                        2 * float(n1.get()) * float(n2.get()))))

        step7.grid(row=18, column=0)

        step1.config(background="light blue")
        step2.config(background="light blue")

        step4.config(background="light blue")

        step6.config(background="light blue")
        step7.config(background="light blue")



    def f2():
        new = root
        step1 = Label(new, text="(a+b)^2 = (a * a) + (b * b) - (2 * a * b)")
        step1.grid(row=14, column=0)

        step2 = Label(new, text="a*a = " + str(float(n1.get()) ** 2))

        step2.grid(row=15, column=0)

        step4 = Label(new, text="b*b = " + str(float(n2.get()) **2 ))

        step4.grid(row=16, column=0)

        step6 = Label(new, text="2*a*b =" + str(2 * float(n1.get()) * float(n2.get())))

        step6.grid(row=17, column=0)

        step7 = Label(new, text="Total = " + str(
            (float(n1.get()) * float(n1.get())) + (float(n2.get()) * float(n2.get())) - (
                    2 * float(n1.get()) * float(n2.get()))))

        step7.grid(row=18, column=0)

        step1.config(background="light blue")
        step2.config(background="light blue")

        step4.config(background="light blue")

        step6.config(background="light blue")
        step7.config(background="light blue")

    def f3():
        new = root
        step1 = Label(new, text="(a+b)^3 = (a)^3+(b)^3+[3*(a)^2*b]+[3*a*(b)^2]")
        step1.grid(row=14, column=0)

        step2 = Label(new, text="(a)^3 = " + str(float(n1.get()) **3))

        step2.grid(row=15, column=0)

        step4 = Label(new, text="3*(a)^2*b= " + str(3 * (float(n1.get()) ** 2) * (float(n2.get()))))


        step4.grid(row=16, column=0)

        step6 = Label(new, text="3*a*(b)^2=" + str(3 * (float(n1.get())) * (float(n2.get())) ** 2))

        step6.grid(row=17, column=0)

        step7 = Label(new, text="(b)^3 = " + str(float(n2.get()) ** 3))

        step7.grid(row=18, column=0)

        step8 = Label(new,
                      text="Total = " + str((float(n1.get()) ** 3) + (3 * (float(n1.get()) ** 2) * (float(n2.get())))
                                            + (3 * (float(n1.get())) * (float(n2.get())) ** 2) + (
                                                        float(n2.get()) ** 3)))


        step8.grid(row=19, column=0)


        step1.config(background="light blue")
        step2.config(background="light blue")

        step4.config(background="light blue")

        step6.config(background="light blue")
        step7.config(background="light blue")
        step8.config(background="light blue")

    def f4():
        new = root
        step1 = Label(new, text="(a-b)^3 = (a)^3-(b)^3+[3*(a)^2*b]+[3*a*(b)^2]")
        step1.grid(row=14, column=0)

        step2 = Label(new, text="(a)^3 = " + str(float(n1.get()) **3))

        step2.grid(row=15, column=0)

        step4 = Label(new, text="3*(a)^2*b= " + str(3 * (float(n1.get()) ** 2) * (float(n2.get()))))


        step4.grid(row=16, column=0)

        step6 = Label(new, text="3*a*(b)^2=" + str(3 * (float(n1.get())) * (float(n2.get())) ** 2))

        step6.grid(row=17, column=0)

        step7 = Label(new, text="(b)^3 = " + str(float(n2.get()) ** 3))

        step7.grid(row=18, column=0)

        step8 = Label(new,
                      text="Total = " + str((float(n1.get()) ** 3) + (3 * (float(n1.get()) ** 2) * (float(n2.get())))
                                            + (3 * (float(n1.get())) * (float(n2.get())) ** 2) - (
                                                        float(n2.get()) ** 3)))
        step8.grid(row=19, column=0)


        step1.config(background="light blue")
        step2.config(background="light blue")

        step4.config(background="light blue")

        step6.config(background="light blue")
        step7.config(background="light blue")
        step8.config(background="light blue")

    def f5():
        new = root
        step1 = Label(new, text="(a)^3+(b)^3 = (a + a) ((a * a) + (b * b) - (2 * a * b)")
        step1.grid(row=14, column=0)

        step2 = Label(new, text="(a * a) - (b * b) = " + str(float(n1.get()) * (float(n1.get()))))

        step2.grid(row=15, column=0)

        step4 = Label(new, text="(2 * a * b) = " + str((2*(float(n1.get()) * (float(n1.get()))))))

        step4.grid(row=16, column=0)


        step8 = Label(new,
                      text="Total = " + str(
                          (float(n1.get()) * (float(n1.get()))) - (2 * (float(n1.get()) * (float(n1.get()))))))
        step8.grid(row=17, column=0)


    def f6():
        new = root
        step1 = Label(new, text="(a)^3-(b)^3 = (a + a) ((a * a) + (b * b) + (2 * a * b)")
        step1.grid(row=14, column=0)

        step2 = Label(new, text="(a * a) - (b * b) = " + str(float(n1.get()) * (float(n1.get()))))

        step2.grid(row=15, column=0)

        step4 = Label(new, text="(2 * a * b) = " + str((2*(float(n1.get()) * (float(n1.get()))))))

        step4.grid(row=16, column=0)


        step8 = Label(new,
                      text="Total = " + str(
                          (float(n1.get()) * (float(n1.get()))) + (2 * (float(n1.get()) * (float(n1.get()))))))
        step8.grid(row=17, column=0)















opt = ["(a+b)^2", "(a-b)^2", "(a+b)^3", "(a-b)^3", "(a)^3+(b)^3", "(a)^3+(b)^3", "(a+b+c)^2", "(a-b-c)^2"]
mylab = Label(root, text="SRI RAMAKRISHNA MISSION VIDYALAYA \n POLYTECHNIC COLLEGE",
              anchor="center",font="italic",background="light blue",
              foreground="black")

mylab.grid(row=0, column=0,columnspan=20)

b1 = Button(root, text=opt[0], width=15, command=ans.f1,background="cyan")
b2 = Button(root, text=opt[1], width=15, command=ans.f2,background="cyan")
b3 = Button(root, text=opt[2], width=15, command=ans.f3,background="cyan")
b4 = Button(root, text=opt[3], width=15, command=ans.f4,background="cyan")
b5 = Button(root, text=opt[4], width=15, command=ans.f1,background="cyan")
b6 = Button(root, text=opt[5], width=15, command=ans.f1,background="cyan")
b7 = Button(root, text=opt[6], width=15, command=ans.f1,background="cyan")
b8 = Button(root, text=opt[7], width=15, command=ans.f1,background="cyan")


b1.grid(row=10, column=0)
b2.grid(row=10, column=1)

b3.grid(row=11, column=0)
b4.grid(row=11, column=1)

b5.grid(row=12, column=0)
b6.grid(row=12, column=1)

b7.grid(row=13, column=0)
b8.grid(row=13, column=1)



new.mainloop()