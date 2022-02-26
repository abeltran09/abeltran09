###################
#Name:Angel Beltran
#Date:1/25/2022
#Descriptions: The Reckoner - Calculator
###################
from tkinter import *

class MainGUI(Frame):
    def __init__(self, parent):
        # the constructor
        Frame.__init__(self, parent, bg="white")
        #parent.attributes("-fullscreen", True)
        self.setupGUI()

    # set up the GUI
    def setupGUI(self):
        # the display
        # right-align text in the display; and set its
        # background to white, its height to 2 characters and times new roman font at 50
        self.display = Label(self, text="", anchor=E, bg="white", height=2, font=("Times", 50))
        # put it in the top row, spanning across all four
        # columns; and expand it on all four sides
        self.display.grid(row=0, column=0, columnspan=4, sticky=E+W+N+S)

        # the button layout
        # ( ) AC **
        # 7 8 9 /
        # 4 5 6 *
        # 1 2 3 -
        # 0 . = +

        # configure the rows and columns of the Frame to adjust
        # to the window
        # there are 6 rows (0 through 5)

        for row in range(6):
            Grid.rowconfigure(self, row, weight=1)
        # there are 4 columns (0 through 3)
        for col in range(4):
            Grid.columnconfigure(self, col, weight=1)
        # the first row
        # (
        # first, fetch and store the image
        # to work best on the RPi, images should be 115x115
        # pixels
        # otherwise, may need to add .subsample(n)
        img = PhotoImage(file="images-gif/lpr.gif")
        # next, create the button (white background, no border,
        # no highlighting, no color when clicked)
        button = Button(self, bg="white", image=img, borderwidth=0, highlightthickness=0, activebackground="white", command=lambda:self.process("("))
        #set the button's image
        button.image = img
        # put the button in its proper row and column
        button.grid(row=1, column=0, sticky=N+S+E+W)

        #)
        img = PhotoImage(file="images-gif/rpr.gif")
        button = Button(self, bg="white", image=img, borderwidth=0, highlightthickness=0, activebackground="white", command=lambda:self.process(")"))
        button.image = img
        button.grid(row=1, column=1, sticky=N + S + E + W)

        #AC
        img = PhotoImage(file="images-gif/clr.gif")
        button = Button(self, bg="white", image=img, borderwidth=0, highlightthickness=0, activebackground="white", command=lambda: self.process("AC"))
        button.image = img
        button.grid(row=1, column=2, sticky=N + S + E + W)

        # **
        img = PhotoImage(file="images-gif/pow.gif")
        button = Button(self, bg="white", image=img, borderwidth=0, highlightthickness=0, activebackground="white", command=lambda: self.process("**"))
        button.image = img
        button.grid(row=1, column=3, sticky=N + S + E + W)

        # row 2
        # 7
        img = PhotoImage(file="images-gif/7.gif")
        button = Button(self, bg="white", image=img, borderwidth=0, highlightthickness=0, activebackground="white", command=lambda: self.process("7"))
        button.image = img
        button.grid(row=2, column=0, sticky=N + S + E + W)

        #8
        img = PhotoImage(file="images-gif/8.gif")
        button = Button(self, bg="white", image=img, borderwidth=0, highlightthickness=0, activebackground="white", command=lambda: self.process("8"))
        button.image = img
        button.grid(row=2, column=1, sticky=N + S + E + W)

        #9
        img = PhotoImage(file="images-gif/9.gif")
        button = Button(self, bg="white", image=img, borderwidth=0, highlightthickness=0, activebackground="white", command=lambda:self.process("9"))
        button.image = img
        button.grid(row=2, column=2, sticky=N + S + E + W)

        #/
        img = PhotoImage(file="images-gif/div.gif")
        button = Button(self, bg="white", image=img, borderwidth=0, highlightthickness=0, activebackground="white", command=lambda:self.process("/"))
        button.image = img
        button.grid(row=2, column=3, sticky=N + S + E + W)

        #row 3
        # 4
        img = PhotoImage(file="images-gif/4.gif")
        button = Button(self, bg="white", image=img, borderwidth=0, highlightthickness=0, activebackground="white", command=lambda: self.process("4"))
        button.image = img
        button.grid(row=3, column=0, sticky=N + S + E + W)

        # 5
        img = PhotoImage(file="images-gif/5.gif")
        button = Button(self, bg="white", image=img, borderwidth=0, highlightthickness=0, activebackground="white", command=lambda: self.process("5"))
        button.image = img
        button.grid(row=3, column=1, sticky=N + S + E + W)

        # 6
        img = PhotoImage(file="images-gif/6.gif")
        button = Button(self, bg="white", image=img, borderwidth=0, highlightthickness=0, activebackground="white", command=lambda: self.process("6"))
        button.image = img
        button.grid(row=3, column=2, sticky=N + S + E + W)

        # *
        img = PhotoImage(file="images-gif/mul.gif")
        button = Button(self, bg="white", image=img, borderwidth=0, highlightthickness=0, activebackground="white", command=lambda: self.process("*"))
        button.image = img
        button.grid(row=3, column=3, sticky=N + S + E + W)

        # row 4
        #1
        img = PhotoImage(file="images-gif/1.gif")
        button = Button(self, bg="white", image=img, borderwidth=0, highlightthickness=0, activebackground="white", command=lambda: self.process("1"))
        button.image = img
        button.grid(row=4, column=0, sticky=N + S + E + W)

        #2
        img = PhotoImage(file="images-gif/2.gif")
        button = Button(self, bg="white", image=img, borderwidth=0, highlightthickness=0, activebackground="white", command=lambda: self.process("2"))
        button.image = img
        button.grid(row=4, column=1, sticky=N + S + E + W)

        #3
        img = PhotoImage(file="images-gif/3.gif")
        button = Button(self, bg="white", image=img, borderwidth=0, highlightthickness=0, activebackground="white", command=lambda: self.process("3"))
        button.image = img
        button.grid(row=4, column=2, sticky=N + S + E + W)

        # -
        img = PhotoImage(file="images-gif/sub.gif")
        button = Button(self, bg="white", image=img, borderwidth=0, highlightthickness=0, activebackground="white", command=lambda: self.process("-"))
        button.image = img
        button.grid(row=4, column=3, sticky=N + S + E + W)

        # row 5
        # 0
        img = PhotoImage(file="images-gif/0.gif")
        button = Button(self, bg="white", image=img, borderwidth=0, highlightthickness=0, activebackground="white", command=lambda: self.process("0"))
        button.image = img
        button.grid(row=5, column=0, sticky=N + S + E + W)

        # .
        img = PhotoImage(file="images-gif/dot.gif")
        button = Button(self, bg="white", image=img, borderwidth=0, highlightthickness=0, activebackground="white", command=lambda: self.process("."))
        button.image = img
        button.grid(row=5, column=1, sticky=N + S + E + W)

        # =
        img = PhotoImage(file="images-gif/eql.gif")
        button = Button(self, bg="white", image=img, borderwidth=0, highlightthickness=0, activebackground="white", command=lambda: self.process("="))
        button.image = img
        button.grid(row=5, column=2, sticky=N + S + E + W)

        # add
        img = PhotoImage(file="images-gif/add.gif")
        button = Button(self, bg="white", image=img, borderwidth=0, highlightthickness=0, activebackground="white", command=lambda: self.process("+"))
        button.image = img
        button.grid(row=5, column=3, sticky=N + S + E + W)

        # pack the GUI
        self.pack(fill = BOTH, expand=1)

    # processes button presses
    def process(self, button):
        # AC clears the display
        if button == "AC":
            #clear the display
            self.display["text"] = ""
        # = starts an evaluation of whatever is on display
        elif button == "=":
            # get the expression in display
            expr = self.display["text"]
            # evaluation may return error
            try:
                # evaluate the expression
                result = eval(expr)
                # store the result to the display
                self.display["text"] = str(result)
            # handle if an error occurs during evaluation
            except:
                # note the error in the display
                self.display["text"] = "ERROR"
        else:
            self.display["text"] += button
#Main part of code


#create window
window = Tk()
# set the window title
window.title("The Reckoner")
# generate the GUI
p = MainGUI(window)
# display the GUI and wait for user interaction
window.mainloop()