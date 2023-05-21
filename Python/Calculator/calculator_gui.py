from tkinter import *

root = Tk()

root.geometry('280x330')  # program WidthxHeight
root.title('Calculator | Nisheet')

# input field
entry_input = Entry(root)
entry_input.pack(fill=X, pady=10)

# Display number on input field
def NUMBERS_INPUT(num):
    current_num = entry_input.get()
    entry_input.delete(0, END)
    entry_input.insert(0, current_num + num)

# clear input field
def clear():
    entry_input.delete(0, END)

# Remove last number from the input field
def cut_num():
    Num_index = len(entry_input.get())
    entry_input.delete(Num_index-1, END)

# show_error funtion for impossible calculations
def show_error():
    entry_input.delete(0, END)
    entry_input.insert(0, 'Error')

# Calculation function
def Equalto():
    Num = entry_input.get()

    # Error Checker
    error_list = ['/*', '*/', '-*', '+*', '-/', '+/']
    for er in error_list:
        if er in Num: show_error()

    try:
        cul = eval(Num) # Evaluate given string
        entry_input.delete(0, END)
        entry_input.insert(0, cul)
    except:
        pass

# number keys Frame
number_frame = Frame(root, width=220)

button_7 = Button(number_frame, text='7', height=3, width=8, command=lambda: NUMBERS_INPUT('7'))
button_7.grid(column=0, row=0)
button_8 = Button(number_frame, text='8', height=3, width=8, command=lambda: NUMBERS_INPUT('8'))
button_8.grid(column=1, row=0)
button_9 = Button(number_frame, text='9', height=3, width=8, command=lambda: NUMBERS_INPUT('9'))
button_9.grid(column=2, row=0)
button_div = Button(number_frame, text='/', height=3, width=8, command=lambda: NUMBERS_INPUT('/'))
button_div.grid(column=3, row=0)

button_4 = Button(number_frame, text='4', height=3, width=8, command=lambda: NUMBERS_INPUT('4'))
button_4.grid(column=0, row=1)
button_5 = Button(number_frame, text='5', height=3, width=8, command=lambda: NUMBERS_INPUT('5'))
button_5.grid(column=1, row=1)
button_6 = Button(number_frame, text='6', height=3, width=8, command=lambda: NUMBERS_INPUT('6'))
button_6.grid(column=2, row=1)
button_mul = Button(number_frame, text='*', height=3, width=8, command=lambda: NUMBERS_INPUT('*'))
button_mul.grid(column=3, row=1)

button_1 = Button(number_frame, text='1', height=3, width=8, command=lambda: NUMBERS_INPUT('1'))
button_1.grid(column=0, row=3)
button_2 = Button(number_frame, text='2', height=3, width=8, command=lambda: NUMBERS_INPUT('2'))
button_2.grid(column=1, row=3)
button_3 = Button(number_frame, text='3', height=3, width=8, command=lambda: NUMBERS_INPUT('3'))
button_3.grid(column=2, row=3)
button_sub = Button(number_frame, text='-', height=3, width=8, command=lambda: NUMBERS_INPUT('-'))
button_sub.grid(column=3, row=3)

button_0 = Button(number_frame, text='0', height=3, width=8, command=lambda: NUMBERS_INPUT('0'))
button_0.grid(column=0, row=4)
button_clear = Button(number_frame, text='Clear', height=3, width=8, command=clear)
button_clear.grid(column=1, row=4)
button_clear = Button(number_frame, text='<--', height=3, width=8, command=cut_num)
button_clear.grid(column=2, row=4)
button_add = Button(number_frame, text='+', height=7, width=8, command=lambda: NUMBERS_INPUT('+'))
button_add.grid(column=3, row=4, rowspan=2)

button_point = Button(number_frame, text='.', height=3, width=8, command=lambda: NUMBERS_INPUT('.'))
button_point.grid(column=0, row=5)
button_equl = Button(number_frame, text='=', height=3, width=18, command=Equalto)
button_equl.grid(column=1, columnspan=2, row=5)

number_frame.pack(fill=Y)

root.mainloop()