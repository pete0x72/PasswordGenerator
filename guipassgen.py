import random
from tkinter import *
import tkinter.font as tkFont

root = Tk()
root.title("PasswordGenerator v0.1")

app_width = 750
app_height = 500

fontStyle = tkFont.Font(family = "CaskaydiaCove Nerd Font", size = "18")
darkFontStyle = tkFont.Font(family = "CaskaydiaCove Nerd Font", size = "12")

lowerCase = "abcdefghijklmnopqrstuvwxyz"
upperCase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "1234567890"
symbols = "`~!@#$%^&*()-_=+[{]}\|;:,<.>/?"

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight() 
x = (screen_width/2) - (app_width/2)
y = (screen_height/2) - (app_height/2)

root.geometry(f"{app_width}x{app_height}+{int(x)}+{int(y)}")
root.maxsize(750,500)
root.minsize(750,500)
root.config(bg = "#161B22")

def main(use_for, length_of_passwd=0):
    password = "".join(random.sample(use_for, int(length_of_passwd)))
    generatedEntry.delete(0, END)
    generatedEntry.insert(0, password)

def choice(passLength):
    use_for = ""
    if a.get() == 1:
        use_for = use_for + lowerCase
    if b.get() == 1:
        use_for = use_for + upperCase
    if c.get() == 1:
        use_for = use_for + numbers
    if d.get() == 1:
        use_for = use_for + symbols
    main(use_for, passLength)

def genButtonFunc():
    passLength = lenEntry.get()
    choice(passLength)


a = IntVar()
b = IntVar()
c = IntVar()
d = IntVar()


lenLabel = Label(root,  text="Password Length:",
                        font=fontStyle,
                        fg = "#C6CFD7",
                        bg = "#161B22")
lenLabel.place(relx = 0.2, rely = 0.10)

lenEntry = Entry(root,  font=fontStyle,
                        width = 5,
                        bg = "#DFDFDE",
                        bd = 3,
                        justify =CENTER,
                        relief = SUNKEN)
lenEntry.place(relx=0.53, rely = 0.10)

lCase = Checkbutton(text = "Include lowercase",
                    font = fontStyle,
                    bg = "#228637",
                    activebackground="#2FA143",
                    fg='white',
                    activeforeground='white',
                    selectcolor="black",
                    relief = SUNKEN,
                    cursor = "hand2",
                    variable = a)
lCase.place(relx = 0.1, rely = 0.23)

uCase = Checkbutton(text = "Include uppercase",
                    font = fontStyle,
                    bg = "#228637",
                    activebackground="#2FA143", 
                    fg='white',
                    activeforeground='white',
                    selectcolor="black",
                    relief = SUNKEN,
                    cursor = "hand2",
                    variable = b)
uCase.place(relx = 0.1, rely = 0.33)

nums = Checkbutton( text = "Include numbers",
                    font = fontStyle,
                    bg = "#228637",
                    activebackground="#2FA143", 
                    fg='white',
                    activeforeground='white',
                    selectcolor="black",
                    relief = SUNKEN,
                    cursor = "hand2",
                    variable = c)
nums.place(relx = 0.1, rely = 0.43)

syms = Checkbutton( text = "Include symbols",
                    font = fontStyle,
                    bg = "#228637",
                    activebackground="#2FA143", 
                    fg='white',
                    activeforeground='white',
                    selectcolor="black",
                    relief = SUNKEN,
                    cursor = "hand2",
                    variable = d)
syms.place(relx = 0.1, rely = 0.53)

generatedLabel = Label(root,text= "Your password:",
                            font=fontStyle,
                            fg = "#C6CFD7",
                            bg = "#161B22")
generatedLabel.place(relx = 0.10, rely = 0.82)

generatedEntry = Entry(root,font=fontStyle,
                            width = 20,
                            bg = "#DFDFDE",
                            bd = 3,
                            justify =CENTER,
                            relief = SUNKEN)
generatedEntry.place(relx=0.40, rely = 0.82)

genButton = Button( text = "Generate",
                    font = fontStyle,
                    bg = "#0A81AB",
                    activebackground="#035397",
                    fg = "white",
                    activeforeground="white",
                    cursor = "hand2",
                    command = genButtonFunc)
genButton.place(relx = 0.40, rely = 0.67)

darkLabel = Label(root, text="Dark Theme",
                        font=darkFontStyle,
                        fg = "#58A7FE",
                        bg = "#161B22")
darkLabel.place(relx = 0.77, rely = 0.045)

is_on = True
def switch():
    global is_on
    
    lowerCase = "abcdefghijklmnopqrstuvwxyz"
    upperCase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numbers = "1234567890"
    symbols = "`~!@#$%^&*()-_=+[{]}\|;:,<.>/?"

    def main(use_for, length_of_passwd=0):
        password = "".join(random.sample(use_for, int(length_of_passwd)))
        generatedEntry.delete(0, END)
        generatedEntry.insert(0, password)

    def choice(passLength):
        use_for = ""
        if a.get() == 1:
            use_for = use_for + lowerCase
        if b.get() == 1:
            use_for = use_for + upperCase
        if c.get() == 1:
            use_for = use_for + numbers
        if d.get() == 1:
            use_for = use_for + symbols
        main(use_for, passLength)

    def genButtonFunc():
        passLength = lenEntry.get()
        choice(passLength)


    a = IntVar()
    b = IntVar()
    c = IntVar()
    d = IntVar()

    if is_on:
        root.config(bg = "#FFF7BC")

        lenLabel = Label(root,  text="Password Length:",
                                font=fontStyle,
                                fg = "black",
                                bg = "#FFF7BC")
        lenLabel.place(relx = 0.2, rely = 0.10)

        lenEntry = Entry(root,  font=fontStyle,
                                width = 5,
                                bg = "#DFDFDE",
                                bd = 3,
                                justify =CENTER,
                                relief = SUNKEN)
        lenEntry.place(relx=0.53, rely = 0.10)

        lCase = Checkbutton(text = "Include lowercase",
                            font = fontStyle,
                            bg = "#FFA8A8",
                            activebackground="#FFCDDD",
                            fg='black',
                            activeforeground='black',
                            selectcolor="white",
                            relief = SUNKEN,
                            cursor = "hand2",
                            variable = a)
        lCase.place(relx = 0.1, rely = 0.23)

        uCase = Checkbutton(text = "Include uppercase",
                            font = fontStyle,
                            bg = "#FFA8A8",
                            activebackground="#FFCDDD",
                            fg='black',
                            activeforeground='black',
                            selectcolor="white",
                            relief = SUNKEN,
                            cursor = "hand2",
                            variable = b)
        uCase.place(relx = 0.1, rely = 0.33)

        nums = Checkbutton( text = "Include numbers",
                            font = fontStyle,
                            bg = "#FFA8A8",
                            activebackground="#FFCDDD",
                            fg='black',
                            activeforeground='black',
                            selectcolor="white",
                            relief = SUNKEN,
                            cursor = "hand2",
                            variable = c)
        nums.place(relx = 0.1, rely = 0.43)

        syms = Checkbutton( text = "Include symbols",
                            font = fontStyle,
                            bg = "#FFA8A8",
                            activebackground="#FFCDDD",
                            fg='black',
                            activeforeground='black',
                            selectcolor="white",
                            relief = SUNKEN,
                            cursor = "hand2",
                            variable = d)
        syms.place(relx = 0.1, rely = 0.53)

        generatedLabel = Label(root,text= "Your password:",
                                    font=fontStyle,
                                    fg = "black",
                                    bg = "#FFF7BC")
        generatedLabel.place(relx = 0.10, rely = 0.82)

        generatedEntry = Entry(root,font=fontStyle,
                                    width = 20,
                                    bg = "#DFDFDE",
                                    bd = 3,
                                    justify =CENTER,
                                    relief = SUNKEN)
        generatedEntry.place(relx=0.40, rely = 0.82)

        genButton = Button( text = "Generate",
                            font = fontStyle,
                            bg = "#001E6C",
                            activebackground="#396EB0",
                            fg = "white",
                            activeforeground="white",
                            cursor = "hand2",
                            command = genButtonFunc)
        genButton.place(relx = 0.40, rely = 0.67)

        darkLabel = Label(root, text="Dark Theme",
                                font=darkFontStyle,
                                fg = "black",
                                bg = "#FFF7BC")
        darkLabel.place(relx = 0.77, rely = 0.045)

        on_button.config(   image = off,
                            bg = "#FFF7BC",
                            activebackground = "#FFF7BC")
        is_on = False
    else:

        root.config(bg = "#161B22")
        lenLabel = Label(root,  text="Password Length:",
                                font=fontStyle,
                                fg = "#C6CFD7",
                                bg = "#161B22")
        lenLabel.place(relx = 0.2, rely = 0.10)

        lenEntry = Entry(root,  font=fontStyle,
                                width = 5,
                                bg = "#DFDFDE",
                                bd = 3,
                                justify =CENTER,
                                relief = SUNKEN)
        lenEntry.place(relx=0.53, rely = 0.10)

        lCase = Checkbutton(text = "Include lowercase",
                            font = fontStyle,
                            bg = "#228637",
                            activebackground="#2FA143",
                            fg='white',
                            activeforeground='white',
                            selectcolor="black",
                            relief = SUNKEN,
                            cursor = "hand2",
                            variable = a)
        lCase.place(relx = 0.1, rely = 0.23)

        uCase = Checkbutton(text = "Include uppercase",
                            font = fontStyle,
                            bg = "#228637",
                            activebackground="#2FA143",
                            fg='white',
                            activeforeground='white',
                            selectcolor="black",
                            relief = SUNKEN,
                            cursor = "hand2",
                            variable = b)
        uCase.place(relx = 0.1, rely = 0.33)

        nums = Checkbutton( text = "Include numbers",
                            font = fontStyle,
                            bg = "#228637",
                            activebackground="#2FA143",
                            fg='white',
                            activeforeground='white',
                            selectcolor="black",
                            relief = SUNKEN,
                            cursor = "hand2",
                            variable = c)
        nums.place(relx = 0.1, rely = 0.43)

        syms = Checkbutton( text = "Include symbols",
                            font = fontStyle,
                            bg = "#228637",
                            activebackground="#2FA143",
                            fg='white',
                            activeforeground='white',
                            selectcolor="black",
                            relief = SUNKEN,
                            cursor = "hand2",
                            variable = d)
        syms.place(relx = 0.1, rely = 0.53)

        generatedLabel = Label(root,text= "Your password:",
                                    font=fontStyle,
                                    fg = "#C6CFD7",
                                    bg = "#161B22")
        generatedLabel.place(relx = 0.10, rely = 0.82)

        generatedEntry = Entry(root,font=fontStyle,
                                    width = 20,
                                    bg = "#DFDFDE",
                                    bd = 3,
                                    justify =CENTER,
                                    relief = SUNKEN)
        generatedEntry.place(relx=0.40, rely = 0.82)

        genButton = Button( text = "Generate",
                            font = fontStyle,
                            bg = "#0A81AB",
                            activebackground="#035397",
                            fg = "white",
                            activeforeground="white",
                            cursor = "hand2",
                            command = genButtonFunc)
        genButton.place(relx = 0.40, rely = 0.67)

        darkLabel = Label(root, text="Dark Theme",
                                font=darkFontStyle,
                                fg = "#58A7FE",
                                bg = "#161B22")
        darkLabel.place(relx = 0.77, rely = 0.045)

        on_button.config(   image = on,
                            bg = "#161B22",
                            activebackground = "#161B22")
        is_on = True



on = PhotoImage(file = "assets/on.png")
off = PhotoImage(file = "assets/off.png")
 
on_button = Button(root,bg = "#161B22",
                        activebackground="#161B22",
                        image = on,
                        bd = 0,
                        command = switch)
on_button.config(width = 50, height = 20)
on_button.place(relx = 0.9, rely = 0.05)




root.mainloop()



