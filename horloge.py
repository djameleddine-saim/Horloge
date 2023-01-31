from tkinter import *
from tkinter.ttk import *
from time import strftime

root = Tk()
root.title("Clock")

format = StringVar()
format.set("AM/PM")
alarm_set = False
alarm_time = ""


def time():
    if format.get() == "AM/PM":
        string = strftime('%I:%M:%S %P')
    else:
        string = strftime('%H:%M:%S')
    if alarm_set and string == alarm_time:
        alarm()
    label.config(text=string)
    label.after(1000, time)


def toggle_format():
    if format.get() == "AM/PM":
        format.set("24-hour")
    else:
        format.set("AM/PM")


def alarm():
    alarm_window = Toplevel(root)
    alarm_window.title("Alarm")
    Label(alarm_window, text="c'est L'heure de se réveiller!", font=("ds-digital", 50)).pack()
    Button(alarm_window, text="MERCI", command=alarm_window.destroy).pack()


def set_alarm():
    global alarm_set, alarm_time
    alarm_time = alarm_entry.get()
    if format.get() == "AM/PM":
        alarm_time = alarm_time   # régler l'heure au niveaux des 24H
    alarm_set = True


def clear_alarm():
    global alarm_set
    alarm_set = False
    alarm_entry.delete(0, END)


def set_time():
    global current_time
    current_time = set_time_entry.get()
    label.config(text=current_time)

set_time_frame = Frame(root)
set_time_frame.grid(row=3, columnspan=2)

set_time_entry = Entry(set_time_frame)
set_time_entry.pack(side=LEFT)



set_time_button = Button(set_time_frame, text="Modifier l'heure", command=set_time)
set_time_button.pack(side=LEFT)



label = Label(root, font=("ds-digital", 60), background="black", foreground="cyan")
label.grid(row=0, columnspan=4)

toggle_format_button = Button(root, text="12H/24H", command=toggle_format)
toggle_format_button.grid(row=1, columnspan=4)

alarm_frame = Frame(root)
alarm_frame.grid(row=2, columnspan=2)

alarm_entry = Entry(alarm_frame)
alarm_entry.pack(side=LEFT)


set_alarm_button = Button(alarm_frame, text="Régler L'alarme", command=set_alarm)
set_alarm_button.pack(side=LEFT)

clear_alarm_button = Button(alarm_frame, text="Effacer L'alarme", command=clear_alarm)
clear_alarm_button.pack(side=LEFT)

time()
mainloop()

