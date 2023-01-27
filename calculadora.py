import tkinter as tk
import operator
import re


class button(tk.Button):
    def __init__(self, master=None, **kw):
        tk.Button.__init__(self, master, **kw)
        self.config(font=("Arial", 20), width=4,
                    height=1, relief='groove', bd=1)


def num_function_button(x, num):
    x = str(x)
    if len(num) < 17:
        if num == '0':
            shown_lower_number.set(value=x)
        else:
            shown_lower_number.set(value=(num+x))
    else:
        show_error()


def erase_function_button(num):
    index = len(num)
    new_shown_lower_number = num[:index-1]
    if len(new_shown_lower_number) == 0:
        shown_lower_number.set(value='0')
    else:
        shown_lower_number.set(value=new_shown_lower_number)


def clear_function_button():
    shown_lower_number.set(value='0')
    shown_upper_number.set(value='')


def operation_function_button(simbol, lowerNumber):
    simbol = str(simbol)
    shown_upper_number.set(value=(lowerNumber+simbol))
    shown_lower_number.set(value='0')


def result_function_button(upp, low, oper):
    operador = upp[len(upp)-1]
    upper_num_str = upp[:(len(upp)-1)]
    if re.search(r'\.', upper_num_str) == None:
        upper_num = int(upper_num_str)
    else:
        upper_list = re.split(r'\.', upper_num_str)
        if len(upper_list[1]) == 1:
            decimal_number = int(upper_list[1])/10
        else:
            decimal_number = int(upper_list[1])/100
        upper_num = int(upper_list[0])+decimal_number
    if re.search(r'\.', low) == None:
        lower_num = int(low)
    else:
        lower_list = re.split(r'\.', low)
        if len(lower_list[1]) == 1:
            decimal_number = int(lower_list[1])/10
        else:
            decimal_number = int(lower_list[1])/100
        lower_num = int(lower_list[0])+decimal_number

    result = oper[operador](upper_num, lower_num)
    shown_upper_number.set(value=upp+low)
    shown_lower_number.set(value=str(result))


def show_alert():
    alert = tk.Toplevel()
    alert.config(width=350, height=500, border=3)
    label = tk.Label(
        alert, text='TOLD YOU NOT TO PRESS THE BUTTON\nMOTHERF***ER', justify='center')
    label.grid(column=0, row=1, sticky='we')
    image = tk.PhotoImage(file='./images/jackson_small.png')
    image_label = tk.Label(alert, image=image, state='active')
    image_label.grid(column=0, row=0, sticky='new')
    image_label.image = image
    boton = tk.Button(alert, text='I\'m a pussy', command=alert.destroy)
    boton.grid(column=0, row=2)


def show_error():
    error = tk.Toplevel()
    error.config(width=100, height=100, border=3)
    label = tk.Label(error, text='Max Digits Reached', justify='center')
    label.grid(sticky='we', row=0)
    boton = tk.Button(error, text='OK', command=error.destroy)
    boton.grid(row=1)


operadores = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.truediv
}

ventana = tk.Tk()  # Objeto ventana
ventana.config(width=350, height=500, border=5,
               bg='#397cbe')  # tamaño de la ventana

ventana.title('No soy Casio')

shown_lower_number = tk.StringVar(value='0')
shown_upper_number = tk.StringVar()  # String que contiene numero y simbolo

display_frame = tk.Frame(ventana)
display_frame.config(bg='#3b5998', relief="sunken",
                     bd=10)
display_frame.columnconfigure(0, weight=1)
display_frame.grid(row=0, column=0, sticky='new',
                   columnspan=5, rowspan=2, padx=1, pady=10)

display_lower_row = tk.Label(display_frame)
# la row 0 del frame es la de arriba
display_lower_row.config(textvariable=shown_lower_number,
                         anchor='e', bg='#c2c2c2', font=('Arial', 20))
display_lower_row.grid(column=0, row=1, sticky='we')


display_upper_row = tk.Label(display_frame)
display_upper_row.config(textvariable=shown_upper_number,
                         anchor='e', bg='#adadad', font=('Arial', 12))
display_upper_row.grid(column=0, row=0, columnspan=5, sticky='we')


buttons_frame = tk.Frame(ventana, bg='#397cbe')
buttons_frame.grid(rowspan=4, columnspan=5, row=3,
                   padx=1, pady=10, sticky='sew')

button_1 = button(buttons_frame, text='1', bg='light grey',
                  command=lambda: num_function_button('1', shown_lower_number.get()))
button_1.grid(column=1, row=1, padx=1, pady=1)

button_2 = button(buttons_frame, text='2', bg='light grey',
                  command=lambda: num_function_button('2', shown_lower_number.get()))
button_2.grid(column=2, row=1, padx=1, pady=1)

button_3 = button(buttons_frame, text='3', bg='light grey',
                  command=lambda: num_function_button('3', shown_lower_number.get()))
button_3.grid(column=3, row=1, padx=1, pady=1)

button_4 = button(buttons_frame, text='4', bg='light grey',
                  command=lambda: num_function_button('4', shown_lower_number.get()))
button_4.grid(column=1, row=2, padx=1, pady=1)

button_5 = button(buttons_frame, text='5', bg='light grey',
                  command=lambda: num_function_button('5', shown_lower_number.get()))
button_5.grid(column=2, row=2, padx=1, pady=1)

button_6 = button(buttons_frame, text='6', bg='light grey',
                  command=lambda: num_function_button('6', shown_lower_number.get()))
button_6.grid(column=3, row=2, padx=1, pady=1)

button_7 = button(buttons_frame, text='7', bg='light grey',
                  command=lambda: num_function_button('7', shown_lower_number.get()))
button_7.grid(column=1, row=3, padx=1, pady=1)

button_8 = button(buttons_frame, text='8', bg='light grey',
                  command=lambda: num_function_button('8', shown_lower_number.get()))
button_8.grid(column=2, row=3, padx=1, pady=1)

button_9 = button(buttons_frame, text='9', bg='light grey',
                  command=lambda: num_function_button('9', shown_lower_number.get()))
button_9.grid(column=3, row=3, padx=1, pady=1)

button_0 = button(buttons_frame, text='0', bg='light grey',
                  command=lambda: num_function_button('0', shown_lower_number.get()))
button_0.grid(column=2, row=4, padx=1, pady=1)

button_punto_decimal = button(buttons_frame, text='.', command=lambda: shown_lower_number.set(
    value=shown_lower_number.get()+'.'))
button_punto_decimal.grid(column=1, row=4, padx=1, pady=1)

button_suma = button(buttons_frame, text='+',
                     command=lambda: operation_function_button('+', shown_lower_number.get()))
button_suma.grid(column=5, row=1, padx=1, pady=1)

button_resta = button(buttons_frame, text='-',
                      command=lambda: operation_function_button('-', shown_lower_number.get()))
button_resta.grid(column=5, row=2, padx=1, pady=1)

button_multiplicacion = button(
    buttons_frame, text='x', command=lambda: operation_function_button('*', shown_lower_number.get()))
button_multiplicacion.grid(column=5, row=3, padx=1, pady=1)

button_division = button(buttons_frame, text='÷', command=lambda: operation_function_button(
    '/', shown_lower_number.get()))
button_division.grid(column=5, row=4, padx=1, pady=1)

button_erase = button(buttons_frame, text='<<',
                      command=lambda: erase_function_button(shown_lower_number.get()))
button_erase.grid(column=5, row=0, padx=1, pady=1)

button_clear = button(buttons_frame, text='C',
                      command=lambda: clear_function_button())
button_clear.grid(column=1, row=0, padx=1, pady=1)

button_result = button(buttons_frame, text='=', command=lambda: result_function_button(
    shown_upper_number.get(), shown_lower_number.get(), operadores), bg='light blue')
button_result.grid(column=3, row=4, padx=1, pady=1)

button_fake = tk.Button(
    buttons_frame, text='DO NOT PRESS\nOUT OF SERVICE', justify='center', command=lambda: show_alert())
button_fake.config(font=("Arial", 10),
                   height=1, relief='groove', bd=1)
button_fake.grid(column=2, row=0, padx=1, pady=1, columnspan=2, sticky='wens')

ventana.mainloop()  # para que se ejecute constantemente
