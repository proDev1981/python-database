
import tkinter

body ={
    "bg":"black",
    "width":200,
    "height":200,
    }


def button( 
    parent,
    value="button",
    bghover="gray",
    bg ="white",
    color="black",
    colorhover="black",
    width=10,
    height=2,
    widthhover=11,
    heighthover=3):

    
    
    def send(str):
        print(str)

    def enter(e):
        button.config(
            width=widthhover,
            height=heighthover,
        )
    

    def leave(e):
        button.config(
            width=width,
            height=height,
        )
    button = tkinter.Button(
        parent,
        command=lambda:send(value),
        text=value,
        activebackground=bghover,
        activeforeground=colorhover,
        background=bg,
        foreground=color,
        bd=0,
        relief="flat",
        width=width,
        height=height,
        )
    button.bind("<Enter>",enter)
    button.bind("<Leave>",leave)
    button.pack(padx=0,pady=0)

win = tkinter.Tk()
win.configure()
Body = tkinter.Frame(win)
Body.config(
    **body,
)
Body.pack()
button(
    Body,
    value="entrar",
    bg=body['bg'],
    bghover="blue"
)
button(
    Body,
    value="salir",
    bg=body['bg'],
    bghover="red"
)

win.mainloop()
