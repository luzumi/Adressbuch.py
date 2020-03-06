from tkinter import *    # Python 2.7 "from Tkinter import *"
from Telefonbuch import *




class Test(Telefonbuch,mainWin):

    label_1 = Label(mainWin, text='Type your password: ')
    label_1.grid()
    entry_1 = Entry(mainWin, textvariable=password, width=6, show='*')
    entry_1.grid()
    entry_1.focus()
    label_2 = Label(mainWin, text='Your password is: ')
    label_2.grid()
    label_3 = Label(mainWin, textvariable=passwordClear)
    label_3.grid()
    button_1 = Button(mainWin, text='show', command=showPass, width=6)
    button_1.grid()
    

    





mainWin = Test()














mainWin.mainloop()