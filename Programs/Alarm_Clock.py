from tkinter import *
import time
import datetime
from playsound import playsound


def alarm(set_alarm_timer):
    while True:
        time.sleep(1)
        current_time = datetime.datetime.now()
        now = current_time.strftime("%H:%M:%S")
        date = current_time.strftime("%d:%m:%Y")
        print("Текущая дата: ", date)
        print("Текущее время: ", now)
        print()

        if now == set_alarm_timer:
            print("Пора вставать")

            play = 0
            while play != 10:  # Повторение 10 раз
                playsound(
                    "sound1.wav")
                play += 1
            print("Поставь будильник еще раз!")
            return


def actual_time():
    set_alarm_timer = f"{hour.get()}:{min.get()}:{sec.get()}"
    print(set_alarm_timer)
    alarm(set_alarm_timer)


clock = Tk()
clock.title("TryCatch Alarm Clock")
clock.geometry("550x250")
clock.resizable(False, False)

Label(clock, text="На какое время вы хотите поставить будильник",
      fg="Blue", bg="black", font=("Arial", 15, 'bold')).place(x=30, y=10)

Label(clock, text="Выберите время в 24-м формате",
      fg="Blue", bg="black", font=("Arial", 15, 'bold')).place(x=105, y=200)

Label(clock, text="Часы      Минуты    Секунды", font=60).place(x=135, y=90)

hour = StringVar()
min = StringVar()
sec = StringVar()

Entry(clock, textvariable=hour, bg="powderblue",
      width=15).place(x=110, y=120)
Entry(clock, textvariable=min, bg="powderblue",
      width=15).place(x=210, y=120)
Entry(clock, textvariable=sec, bg="powderblue",
      width=15).place(x=310, y=120)

Button(clock, text="Поставить", fg="green", activebackground="grey", activeforeground="darkgreen", width=10, font=(
    "Arial", 15, 'bold'), command=actual_time).place(x=190, y=150)

photo = PhotoImage(file="D:/Python project/alarm.png")
clock.iconphoto(False, photo)

clock.mainloop()
