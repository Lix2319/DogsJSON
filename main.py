import requests as r
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from io import BytesIO

def get_json_dog():
    answer_api = r.get("https://dog.ceo/api/breeds/image/random")
    json_dog = answer_api.json()
    return json_dog["message"]


def image_dog_in_tk():
    url_image = get_json_dog()
    if url_image:
        answer_img = r.get(url_image)
        image = BytesIO(answer_img.content)
        img = Image.open(image)
        img.thumbnail((500,350))
        img_tk = ImageTk.PhotoImage(img)
        i_m.config(image=img_tk)
        i_m.image = img_tk


window = Tk()
window.geometry("500x400")
window.title("Изображения собак")

i_m = Label(window)
i_m.pack(pady=[0,10])

btn = Button(window, text="Получить собачку", command=image_dog_in_tk)
btn.pack()

window.mainloop()
