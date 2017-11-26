from Tkinter import *

import rockpaperscissors
import hangman


root = Tk()
root.title("Linux Sruji Xenial Developer Mega Microgames Collection")

mainframe = Frame(root, height = 200, width = 500)
mainframe.pack_propagate(0)
mainframe.pack(padx = 5, pady = 5)

intro = Label(mainframe, text= """Welcome to Linux Sruji Xenial Developer Mega Microgames Collection.
                                Please Select one of the following games to play:
                                """)
intro.pack(side = TOP)

rps_button = Button(mainframe, text = "Rock, Paper, Scissors",command = rockpaperscissors.gui)
rps_button.pack()

hm_button = Button(mainframe, text = "Hangman",command = hangman.gui)
hm_button.pack()

exit_button = Button(mainframe, text = "Quit", command = root.destroy)
exit_button.pack(side = BOTTOM)

root.mainloop()

