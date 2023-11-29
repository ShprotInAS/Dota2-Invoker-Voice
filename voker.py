import tkinter as tk
from PIL import ImageTk, Image
from threading import Thread
import speech_recognition as sr
import keyboard
import time

def open_second_menu(root, background_image="tehnical.png"):
    second_window = tk.Toplevel(root)
    second_window.geometry("300x120")

    # Создание фона с изображением
    image = Image.open(background_image)
    image.thumbnail((300, 200))
    photo = ImageTk.PhotoImage(image)
    bg_label = tk.Label(second_window, image=photo)
    bg_label.image = photo
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)

    # Добавьте элементы и функционал для второго меню

    # Добавьте элементы и функционал для второго меню

    second_window.mainloop()


def run_code():
    button.config(state="disabled")  # Делаем кнопку неактивной
    def process_speech():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            while True:
                print("Говорите...")
                audio = r.listen(source)

                try:
                    text = r.recognize_google(audio, language='ru-RU')
                    print("Вы сказали: " + text)

                    text = text.lower()
                    if 'cold snap' in text or 'холод' in text:
                        keyboard.press('q')
                        keyboard.release('q')
                        keyboard.press('q')
                        keyboard.release('q')
                        keyboard.press('q')
                        keyboard.release('q')

                    if 'ghost' in text or 'гост' in text:
                        keyboard.press('q')
                        keyboard.release('q')
                        keyboard.press('q')
                        keyboard.release('q')
                        keyboard.press('w')
                        keyboard.release('w')

                    if 'ice' in text or 'айс' in text:
                        keyboard.press('q')
                        keyboard.release('q')
                        keyboard.press('q')
                        keyboard.release('q')
                        keyboard.press('e')
                        keyboard.release('e')

                    if 'emp' in text or 'емп' in text:
                        keyboard.press('w')
                        keyboard.release('w')
                        keyboard.press('w')
                        keyboard.release('w')
                        keyboard.press('w')
                        keyboard.release('w')

                    if 'торнадо' in text:
                        keyboard.press('w')
                        keyboard.release('w')
                        keyboard.press('w')
                        keyboard.release('w')
                        keyboard.press('q')
                        keyboard.release('q')

                    if 'alacritty' in text:
                        keyboard.press('w')
                        keyboard.release('w')
                        keyboard.press('w')
                        keyboard.release('w')
                        keyboard.press('e')
                        keyboard.release('e')

                    if 'qwe' in text:
                        keyboard.press('q')
                        keyboard.release('q')
                        keyboard.press('w')
                        keyboard.release('w')
                        keyboard.press('e')
                        keyboard.release('e')

                    if 'санстрайк' in text or 'sun strike' in text:
                        keyboard.press('e')
                        keyboard.release('e')
                        keyboard.press('e')
                        keyboard.release('e')
                        keyboard.press('e')
                        keyboard.release('e')

                    if 'spirits' in text:
                        keyboard.press('e')
                        keyboard.release('e')
                        keyboard.press('e')
                        keyboard.release('e')
                        keyboard.press('q')
                        keyboard.release('q')

                    if 'метеор' in text:
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

                time.sleep(1)  # Приостановка записи голоса на 4 секунды



    thread = Thread(target=process_speech)
    thread.start()

root = tk.Tk()

image = Image.open("Menu.png")
image = image.resize((500, 300), Image.BICUBIC)
background_image = ImageTk.PhotoImage(image)

canvas = tk.Canvas(root, width=500, height=300)
canvas.pack(fill="both", expand=True)
canvas.create_image(0, 0, image=background_image, anchor="nw")

button_image = Image.open("VoiceManage.png")
button_image = button_image.resize((100, 30), Image.BICUBIC)
button_image = ImageTk.PhotoImage(button_image)

button = tk.Button(root, image=button_image, width=100, height=30, bg="white", bd=0, highlightthickness=0, relief='flat', command=run_code)

button.place(relx=0.12, rely=0.35, anchor="center")

setting_image = Image.open("Setting.png")
setting_image = setting_image.resize((85, 20), Image.BICUBIC)
setting_image = ImageTk.PhotoImage(setting_image)

setting_button = tk.Button(root, image=setting_image, width=85, height=20, bg="white", bd=0, highlightthickness=0, relief='flat', command=lambda: open_second_menu(root))
setting_button.place(relx=0.12, rely=0.45, anchor="center")

contact_image = Image.open("contacts.png")
contact_image = contact_image.resize((85, 20), Image.BICUBIC)
contact_image = ImageTk.PhotoImage(contact_image)

contact_button = tk.Button(root, image=contact_image, width=85, height=20, bg="white", bd=0, highlightthickness=0, relief='flat', command=lambda: open_second_menu(root))

contact_button.place(relx=0.12, rely=0.55, anchor="center")

root.mainloop()