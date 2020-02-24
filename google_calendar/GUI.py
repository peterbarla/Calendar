from google_calendar import google_calendar_exercise as calendar
from tkinter import *

#Given data
person1_calendar = [["9:00", "10:30"], ["12:00", "13:00"], ["16:00", "18:00"]]
person1_limits = ["9:00", "20:00"]

person2_calendar = [["10:00", "11:30"], ["12:30", "14:30"], ["15:00", "15:30"], ["16:00", "17:00"]]
person2_limits = ["10:00", "18:30"]

meeting_length = 30

#calculating times
merged_list1 = calendar.merge_lists(person1_calendar, person2_calendar)
limits = calendar.limit_parser(person1_limits, person2_limits)
merged_list2 = calendar.merge_lists(merged_list1, limits)
result = calendar.eliminating(merged_list2)
#####################################################################################################

persons_available_intervall = None
persons_busy_list = []


def add_busy_intervall(string):
    global persons_busy_list
    global busy_intervall_entry
    global persons_available_intervall
    global help_label
    #format validity check
    if calendar.check_format(string) == -1:
        help_label = Label(root, width=30, pady=5, text="Wrong format entered!")
        help_label.grid(row=0, column=0, columnspan=4)
        return

    intervall = calendar.pair_splitter(string)
    if calendar.check_validity(persons_busy_list, intervall, persons_available_intervall) == 1:
        persons_busy_list.append(intervall)
        help_label = Label(root, width=30, pady=5, text="Intervall added!!")
        help_label.grid(row=0, column=0, columnspan=4)
    elif calendar.check_validity(persons_busy_list, intervall, persons_available_intervall) == -1:
        help_label = Label(root, width=30, pady=5, text="Intervall out of bounds!!")
        help_label.grid(row=0, column=0, columnspan=4)
    elif calendar.check_validity(persons_busy_list, intervall, persons_available_intervall) == -2:
        help_label = Label(root, width=30, pady=5, text="Intervall already busy!!")
        help_label.grid(row=0, column=0, columnspan=4)
    busy_intervall_entry = Entry(root, width=17)
    busy_intervall_entry.grid(row=1, column=0, padx=10)
    pass


def add_available_intervall(string):
    global persons_available_intervall
    global person_available_entry
    global busy_button
    global busy_intervall_entry
    global persons_available_intervall
    global available_button

    if calendar.check_format(string) == -1:
        help_label = Label(root, width=30, pady=5, text="Wrong format entered!")
        help_label.grid(row=0, column=0, columnspan=4)
        return

    persons_available_intervall = calendar.pair_splitter(string)

    busy_button = Button(root, width=10, text="add", command=lambda: add_busy_intervall(busy_intervall_entry.get()))
    busy_button.grid(row=1, column=1, padx=10)
    busy_intervall_entry = Entry(root, width=17)
    busy_intervall_entry.insert(END, "Busy intervall")
    busy_intervall_entry.grid(row=1, column=0, padx=10)
    person_available_entry = Entry(root, width=17, state=DISABLED)
    person_available_entry.grid(row=1, column=2, padx=10)
    available_button = Button(root, width=10, text="add",
                              command=lambda: add_available_intervall(person_available_entry.get()), state=DISABLED)
    available_button.grid(row=1, column=3, padx=10)
    help_label = Label(root, width=30, pady=5, text="Add busy intervalls!!")
    help_label.grid(row=0, column=0, columnspan=4)

    pass


def get_busy_intervalls(busy_list):
    if busy_list == []:
        help_label = Label(root, width=30, pady=5, text="Add a busy intervall!!")
        help_label.grid(row=0, column=0, columnspan=4)
        return
    list = calendar.sort_list(busy_list)
    temp = ""
    for i in range(len(list)):
        temp += str(list[i]) + "\n"
    busy_labal = Label(root, width=20, height=20, text=temp)
    busy_labal.grid(row=3, column=0, pady=10, columnspan=2)
    pass

def show_free_intervalls(busy_list, available_intervall):
    if available_intervall == None:
        help_label = Label(root, width=30, pady=5, text="Add an available intervall!!")
        help_label.grid(row=0, column=0, columnspan=4)
        return
    else:
        if busy_list == []:
            temp = available_intervall
        else:
            free_list = calendar.get_free_intervalls(busy_list, available_intervall)
            temp = ""
            for i in range(len(free_list)):
                temp += str(free_list[i]) + "\n"
        busy_labal = Label(root, width=20,height=20, text=temp)
        busy_labal.grid(row=3, column=2, pady=10, columnspan=2)
    pass
root = Tk()

root.title("Calendar administrator")

format_label = Label(root, text="Time format example: 18:00-20:00", width=30, pady=5)
format_label.grid(row=0, column=0, columnspan=2)

help_label = Label(root, width= 30, pady=5, text="Add available intervall!")
help_label.grid(row=0, column=2, columnspan=2)

busy_intervall_entry = Entry(root, width=17, state=DISABLED)
busy_intervall_entry.insert(END, "Busy intervall")
busy_intervall_entry.grid(row=1, column=0, padx=10)

busy_button = Button(root, width=10, text="add", command=lambda: add_busy_intervall(busy_intervall_entry.get()), state=DISABLED)
busy_button.grid(row=1, column=1, padx=10)

person_available_entry = Entry(root, width=17)
person_available_entry.insert(END, "Available intervall")
person_available_entry.grid(row=1, column=2, padx=10)

available_button = Button(root, width=10, text="add", command=lambda: add_available_intervall(person_available_entry.get()))
available_button.grid(row=1, column=3, padx=10)

get_busy_button = Button(root, width=15, text="Get busy intervalls!", command=lambda: get_busy_intervalls(persons_busy_list))
get_busy_button.grid(row=2, column=0, columnspan=2, pady=10, padx=10)

show_free_button = Button(root, width=15, text="Show free intervalls!", command=lambda: show_free_intervalls(persons_busy_list, persons_available_intervall))
show_free_button.grid(row=2, column=2, columnspan=2, pady=10, padx=10)

root.mainloop()
