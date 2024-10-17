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
        img.thumbnail((int(spinbox_var_w.get()), int(spinbox_var_h.get())))
        img_tk = ImageTk.PhotoImage(img)
        new_win = Toplevel(window)
        i_o = Label(new_win, image=img_tk)
        i_o.image = img_tk
        i_o.pack()
    progress.stop()


def func_progress():
    progress.config(value=0)
    progress.start(25)
    window.after(3000,image_dog_in_tk)

window = Tk()
window.geometry("500x200")
window.title("Изображения собак")

btn = ttk.Button(window, text="Получить собачку", command=func_progress)
btn.pack(pady=[0,10])

progress = ttk.Progressbar(mode="determinate", length=400)
progress.pack()

spinbox_var_w = StringVar(value=250)
spinbox_var_h = StringVar(value=250)

width_m = Label(window, text="Ширина:")
width_m.pack()
width_img = ttk.Spinbox(window, from_=250, to=500, increment=50, textvariable=spinbox_var_w)
width_img.pack()
height_m = Label(window, text="Высота:")
height_m.pack()
height_img = ttk.Spinbox(window, from_=250, to=500, increment=50, textvariable=spinbox_var_h)
height_img.pack()

window.mainloop()
