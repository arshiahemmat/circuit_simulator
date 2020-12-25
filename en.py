import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import tkinter
from tkinter import *

windows = tkinter.Tk()
voltage = list()
series = list()
parallel = list()


def land_page():
    windows.geometry('500x500')
    windows.configure(bg='gray', cursor='circle')
    windows.title('circuit')
    lbl = Label(master=windows, text='Welcome to the electrical circuit simulator', bg='gray', fg='yellow', font=("bold italic", "24"),
                bd=5).pack()
    btn = Button(master=windows, text='Click to enter', bg='yellow', activebackground='black',
                 activeforeground='white')
    # windows.iconbitmap('pcba-thumb.ico')
    btn.place(width=500, height=200, relx=.5, rely=.5, anchor=CENTER)
    btn.bind('<Button>', next_page)
    windows.mainloop()


def next_page(event):
    def clc():
        def graph(R):
            I = np.linspace(0, 20, 20)
            V = R * I
            plt.plot(I,V,color = 'green')
            plt.show()

        devider = '-------------------\n'
        sum_volt = 0
        # windows2.destroy()
        windows3 = Tk()
        windows3.geometry('500x500')
        windows3.configure(bg='gray', cursor='circle')
        windows3.title('circuit')
        # windows3.iconbitmap('pcba-thumb.ico')
        if voltage[0] == 'c':
            voltage.pop(0)
            v = [int(i) for i in voltage]
            sum_v = sum(v)
            s = [int(i) for i in series]
            p = [int(i) for i in parallel]
            g = [1 / i for i in p]
            sum_g = sum(g)
            r_eq = sum_g + sum(s)
            counter = 0
            intro = Label(master=windows3, text='We first examine the series resistors', bg='gray', fg='yellow').pack()
            for each in s:
                a = 'R' + str(counter)
                res = 'for R{}\nvoltage : {}\ncurrent : {}\nPower : {}\nConductance : {}\n'.format(counter,
                                                                                                   str(sum_v * each),
                                                                                                   sum_v,
                                                                                                   sum_v ** 2 * each,
                                                                                                   1 / each)
                res_btn = Label(master=windows3, text=res, bg='gray', fg='blue', font=('times', 12)).pack()
                g_btn = Button(master=windows3, text='Click to draw a current voltage diagram', bg='yellow', fg='blue',
                               command=graph(each)).pack()
                divider = Label(master=windows3, text=devider, bg='gray', fg='yellow').pack()
                counter += 1
            # windows3.destroy()
            windows4 = Tk()
            windows4.geometry('500x500')
            windows4.configure(bg='gray', cursor='circle')
            windows4.title('circuit')
            # windows4.iconbitmap('pcba-thumb.ico')
            intro = Label(master=windows4, text='We now turn to parallel resistors', bg='gray', fg='yellow').pack()
            for each in p:
                a = 'R' + str(counter)
                res = 'for R{}\nvoltage : {}\ncurrent : {}\nPower : {}\nConductance : {}\n'.format(counter,
                                                                                                   (sum_v * ((
                                                                                                                     1 / each) / sum_g)) * each,
                                                                                                   sum_v * ((
                                                                                                                    1 / each) / sum_g),
                                                                                                   sum_v * ((
                                                                                                                    1 / each) / sum_g) ** 2 * each,
                                                                                                   1 / each)
                res_btn = Label(master=windows4, text=res, bg='gray', fg='blue', font=('times', 12)).pack()
                g_btn = Button(master=windows4,text = 'Click to draw a current voltage diagram',bg = 'yellow',fg = 'blue',command = graph(each)).pack()
                divider = Label(master=windows4, text=devider, bg='gray', fg='yellow').pack()
                counter += 1
        elif voltage[0] == 'v':
            voltage.pop(0)
            v = [int(i) for i in voltage]
            sum_v = sum(v)

            s = [int(i) for i in series]
            p = [int(i) for i in parallel]
            g = [1 / i for i in p]
            sum_g = sum(g)
            r_p = 1 / sum_g
            r_eq = r_p + sum(s)
            i_eq = sum_v / r_eq
            counter = 0
            v_p = r_p / r_eq
            intro = Label(master=windows3, text='We first examine the series resistors', bg='gray', fg='yellow').pack()
            for each in s:
                a = 'R' + str(counter)
                res = 'for R{}\nvoltage : {}\ncurrent : {}\nPower : {}\nConductance : {}\n'.format(counter,
                                                                                                   each / r_eq, i_eq,
                                                                                                   i_eq ** 2 * each,
                                                                                                   1 / each)
                res_btn = Label(master=windows3, text=res, bg='gray', fg='blue', font=('times', 12)).pack()
                g_btn = Button(master=windows3, text='Click to draw a current-voltage diagram', bg='yellow', fg='blue',
                               command=graph(each)).pack()
                divider = Label(master=windows3, text=devider, bg='gray', fg='yellow').pack()
                counter += 1
            # windows3.destroy()
            windows4 = Tk()
            windows4.geometry('500x500')
            windows4.configure(bg='gray', cursor='circle')
            windows4.title('circuit')
            # windows4.iconbitmap('pcba-thumb.ico')
            intro = Label(master=windows4, text='We now turn to parallel resistors', bg='gray', fg='yellow',
                          font=('times', 20)).pack()
            for each in p:
                a = 'R' + str(counter)
                res = 'for R{}\nvoltage : {}\ncurrent : {}\nPower : {}\nConductance : {}\n'.format(counter,
                                                                                                   v_p,
                                                                                                   v_p / each,
                                                                                                   (v_p / each)
                                                                                                   ** 2 * each,
                                                                                                   1 / each)
                res_btn = Label(master=windows4, text=res, bg='gray', fg='blue', font=('times', 12)).pack()
                g_btn = Button(master=windows4, text='Click to draw a current voltage diagram', bg='yellow', fg='blue',
                               command=graph(each)).pack()
                divider = Label(master=windows4, text=devider, bg='gray', fg='yellow').pack()
                counter += 1

    def R_dtc():
        windows1.destroy()
        windows2 = Tk()
        windows2.geometry('500x500')
        windows2.configure(bg='gray', cursor='circle')
        windows2.title('circuit')
        # windows2.iconbitmap('pcba-thumb.ico')
        # next = Label(master=windows2, bg='gray', fg='gray', text='\n\n\n').pack()
        lbl = Label(master=windows2, text='Enter your series resistors in one line to continue', bg='gray',
                    fg='yellow',
                    font='times',
                    bd=5).pack()
        # next = Label(master=windows2,bg = 'gray',fg = 'gray',text = '\n\n\n').pack()
        series_in = Entry(master=windows2, bg='yellow', fg='blue')
        next = Label(master=windows2, bg='gray', fg='gray', text='\n').pack()
        series_in.pack()
        # next = Label(master=windows2, bg='gray', fg='gray', text='\n\n\n').pack()
        parallel_in = Entry(master=windows2, bg='yellow', fg='blue')

        # parallel_in.pack()
        def set_p():
            l = parallel_in.get()
            parallel.extend(l.split())
            windows2.destroy()
            clc()

        def set():
            ll = series_in.get()
            series.extend(ll.split())
            next = Label(master=windows2, bg='gray', fg='gray', text='\n\n').pack()
            get_el = Label(master=windows2, text='Please enter the values of parallel resistors in a line', bg='gray',
                           fg='yellow', font='times',
                           bd=5).pack()
            next = Label(master=windows2, bg='gray', fg='gray', text='\n').pack()
            parallel_in.pack()
            # bt21 = Button(master=windows2, text='\n\n', bg='gray', bd=0).pack()
            next = Label(master=windows2, bg='gray', fg='gray', text='\n').pack()
            bt22 = Button(master=windows2, text='Please click to confirm the Values of parallel resistors',
                          command=set_p).pack()

        next = Label(master=windows2, bg='gray', fg='gray', text='\n').pack()
        bt2 = Button(master=windows2, text='Please click to confirm the series resistors and continue', command=set).pack()
        windows.mainloop()

    def check():
        if var.get() == 1:
            voltage.append('c')
            lbl1 = Label(text="Your choice is the current source ... Please specify the number of current sources", master=windows1,
                         bg='gray', fg='yellow', font=('times', 12)).pack()

            ent = Entry(master=windows1, bg='yellow', fg='blue')
            ent.pack()
            series_ent = Entry(master=windows1, bg='yellow', fg='blue')

            def set_2():
                l = series_ent.get()
                voltage.extend(l.split())
                R_dtc()
                # lav = Label(master=windows1, text=voltage, bg='gray', fg='yellow').pack()

            def set():
                get_el = Label(master=windows1, text='Please enter the values Values of the current sources in one line.', bg='gray',
                               fg='yellow', font='times',
                               bd=5).pack()
                series_ent.pack()
                bt21 = Button(master=windows1, text='\n\n', bg='gray', bd=0).pack()
                bt22 = Button(master=windows1, text='Please click to confirm the Current rate', command=set_2).pack()

            bt = Button(master=windows1, text='\n\n', bg='gray', bd=0).pack()
            bt2 = Button(master=windows1, text='Please click to confirm the Current rate', command=set).pack()
            # bt = Button(master=windows1, text='\n\n').pack()
            # voltage.append()
            # lbl2 = Label(text = ent.get).pack()
        elif var.get() == 2:
            voltage.append('v')
            lbl1 = Label(text="Your choice is the voltage source ... Please specify the number of voltage sources", master=windows1,
                         bg='gray', fg='yellow', font=('times', 12)).pack()

            ent = Entry(master=windows1, bg='yellow', fg='blue')
            ent.pack()
            series_ent = Entry(master=windows1, bg='yellow', fg='blue')

            def set_2():
                l = series_ent.get()
                voltage.extend(l.split())
                R_dtc()
                # lav = Label(master=windows1, text=voltage, bg='gray', fg='yellow').pack()

            def set():
                get_el = Label(master=windows1, text='Please enter the voltage sources in one line...', bg='gray',
                               fg='yellow', font='times',
                               bd=5).pack()
                series_ent.pack()
                bt21 = Button(master=windows1, text='\n\n', bg='gray', bd=0).pack()
                bt22 = Button(master=windows1, text='Please click to confirm the voltage value', command=set_2).pack()

            bt = Button(master=windows1, text='\n\n', bg='gray', bd=0).pack()
            bt2 = Button(master=windows1, text='Please click to confirm the voltage value', command=set).pack()
            # bt = Button(master=windows1, text='\n\n').pack()
            # voltage.append()
            # lbl2 = Label(text = ent.get).pack()

    windows.destroy()
    windows1 = tkinter.Tk()
    windows1.geometry('500x500')
    windows1.configure(bg='gray', cursor='circle')
    windows1.title('current\tvoltage detector')
    lbl = Label(master=windows1, text='Enter your source type to continue', bg='gray', fg='yellow', font='times',
                bd=5).pack()
    var = IntVar()
    rb1 = Radiobutton(master=windows1, bg='gray', fg='blue', text='Current source', font='times', variable=var,
                      value=1).pack()
    rb2 = Radiobutton(master=windows1, bg='gray', fg='blue', text='Voltage source', variable=var, font='times',
                      value=2).pack()
    btn = Button(master=windows1, text='Click to send', bg='yellow', activebackground='black',
                 activeforeground='white', command=check).pack()
    # send = Button(master=windows1, bg='yellow', fg='gray', text='برای ارسال لطفا کلیک نمایید', commmand=set_volt).pack()
    # btn.bind('<Button>', check)
    # windows1.iconbitmap('pcba-thumb.ico')
    # btn.place(width=500, height=200, relx=.5, rely=.5, anchor=CENTER)


land_page()
# print(voltage, series, parallel)


