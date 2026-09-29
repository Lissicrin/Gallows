import tkinter as t
import random as r
import tkinter.messagebox as m
from PIL import Image, ImageTk

with open("words.txt", encoding="utf-8") as file:
    data = file.read()
    words = data.split()


word = r.choice(words)
letters = []


def check_letter():
    letter = entry_letter.get()
    if letter not in word:
        image1 = Image.open("medali_2.jpg")
        foto1 = ImageTk.PhotoImage(image1)
        label = t.Label(window, image=foto1, )
        label.place(x=180, y=0)
    letters.append(letter)
    show_word = ""
    for char in word:
        if char in letters:
            show_word += char
        else:
            show_word += "*"
    label_word["text"] = show_word
    entry_letter.delete(0,"end")
    if show_word == word:
        m.showinfo("Победа", "Ты угадал славека")


def new_production():
    global word
    global letters
    word = r.choice(words)
    letters = []
    check_letter()


window = t.Tk()
window.title("Славикус спаситус!!!!")
window.geometry("900x500")

label_word = t.Label(window, text="", font=("Arial", 15))
label_word.place(x=170, y=20)

entry_letter = t.Entry(window, width=20, font=("Arial", 10))
entry_letter.place(x=130, y=80)

new_word_production = t.Button(window, text="Новое слово", font=("Arial",10), command=new_production)
new_word_production.place(x=130, y=160)

check_button = t.Button(window, text="Проверить Славека", font=("Arial",10), command=check_letter)
check_button.place(x=130, y=120)

image = Image.open("фоторопо.jpg")
foto = ImageTk.PhotoImage(image)
label = t.Label(window, image=foto, )
label.place(x=180, y=0)



check_letter()



window.mainloop()











