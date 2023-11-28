import tkinter as tk
from PIL import ImageTk, Image
from threading import Thread
import speech_recognition as sr
import keyboard
import time

def run_code():
    def process_speech():
        r = sr.Recognizer()

        while True:
            with sr.Microphone() as source:
                print("Говорите...")
                audio = r.listen(source)

            try:
                text = r.recognize_google(audio, language='ru-RU')
                print("Вы сказали: " + text)

                if 'cold snap' in text.lower(): #Колдснеп
                        keyboard.press('q')
                        keyboard.release('q')
                        keyboard.press('q')
                        keyboard.release('q')
                        keyboard.press('q')
                        keyboard.release('q')

                if 'ghost' in text.lower(): #гоуст
                        keyboard.press('q')
                        keyboard.release('q')
                        keyboard.press('q')
                        keyboard.release('q')
                        keyboard.press('w')
                        keyboard.release('w')

                if 'ice' in text.lower(): #айц
                        keyboard.press('q')
                        keyboard.release('q')
                        keyboard.press('q')
                        keyboard.release('q')
                        keyboard.press('e')
                        keyboard.release('e')

                if 'emp' in text.lower(): #емпи
                        keyboard.press('w')
                        keyboard.release('w')
                        keyboard.press('w')
                        keyboard.release('w')
                        keyboard.press('w')
                        keyboard.release('w')

                if 'торнадо' in text.lower():  #торнадо
                        keyboard.press('w')
                        keyboard.release('w')
                        keyboard.press('w')
                        keyboard.release('w')
                        keyboard.press('q')
                        keyboard.release('q')

                if 'alacritty' in text.lower():  #алакрити
                        keyboard.press('w')
                        keyboard.release('w')
                        keyboard.press('w')
                        keyboard.release('w')
                        keyboard.press('e')
                        keyboard.release('e')

                if 'qwe' in text.lower():  #кью в е
                        keyboard.press('q')
                        keyboard.release('q')
                        keyboard.press('w')
                        keyboard.release('w')
                        keyboard.press('e')
                        keyboard.release('e')

                if 'санстрайк' in text.lower():  #сен страйк
                        keyboard.press('e')
                        keyboard.release('e')
                        keyboard.press('e')
                        keyboard.release('e')
                        keyboard.press('e')
                        keyboard.release('e')

                if 'spirits' in text.lower():  #фордж
                        keyboard.press('e')
                        keyboard.release('e')
                        keyboard.press('e')
                        keyboard.release('e')
                        keyboard.press('q')
                        keyboard.release('q')

                if 'метеор' in text.lower():  #метеор
                        keyboard.press('e')
                        keyboard.release('e')
                        keyboard.press('e')
                        keyboard.release('e')
                        keyboard.press('w')
                        keyboard.release('w')

            except sr.UnknownValueError:
                print("Упс! Не удалось распознать речь")
            except sr.RequestError as e:
                print("Ошибка сервиса распознавания речи: {0}".format(e))

    thread = Thread(target=process_speech)
    thread.start()

root = tk.Tk()

# Создание объекта класса ImageTk.PhotoImage из выбранного изображения
image = Image.open("voker.png")
image = image.resize((300, 300), Image.BICUBIC)
background_image = ImageTk.PhotoImage(image)

# Создание виджета Canvas с установленным фоновым изображением
canvas = tk.Canvas(root, width=300, height=300)
canvas.pack(fill="both", expand=True)
canvas.create_image(0, 0, image=background_image, anchor="nw")

# Создание изображения для кнопки
button_image = Image.open("button.png")
button_image = button_image.resize((100, 30), Image.BICUBIC)
button_image = ImageTk.PhotoImage(button_image)

# Создание кастомной кнопки с установленным изображением
button = tk.Button(root, image=button_image, width=100, height=30, bg=None, bd=0, highlightthickness=0, command=run_code)

# Размещение кнопки ниже изображения
button.place(relx=0.5, rely=0.9, anchor="center")

root.mainloop()