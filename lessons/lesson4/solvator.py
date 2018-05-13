from tkinter import *
from solve import get_roots
window = Tk()
window.title("Решить уравнение!")
#label = Label(text="1")
#label.pack()

def click():
    counter = int(label["text"])
    counter += 1
    print("CLICK!")
    label["text"] = str(counter)

def copy():
    label["text"] = text_field.get()


#button = Button(text="press me", command=copy)
#button.pack()

#text_field = Entry()
#text_field.pack()

tf1 = Entry()
tf2 = Entry()
tf3 = Entry()

label1 = Label(text="x^2 + ")
label2 = Label(text="x + ")
label3 = Label(text=" = 0")

tf1.grid(row=1, column=1)
label1.grid(row=1, column=2)

tf2.grid(row=1, column=3)
label2.grid(row=1, column=4)

tf3.grid(row=1, column=5)
label3.grid(row=1, column=6)

def solve():
    try:
        a = int(tf1.get())
        b = int(tf2.get())
        c = int(tf3.get())
        roots = get_roots(a, b, c)
        result_label["text"] = str(roots)
    except:
        result_label["text"] = "Произошла ошибка!"

button = Button(text="Решить!", command=solve)
button.grid(row=2, column = 3)

result_label = Label(text="")
result_label.grid(row=3, column = 3)

window.mainloop()







