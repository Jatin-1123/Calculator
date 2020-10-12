from tkinter import *

root = Tk()
root.title('Calculator')
root.geometry("320x420")
root.configure(bg='#515151')

list_numbers, list_operators = [None], []


# ||||||||||||||||||||||||||||||||||| #
# ||||||||||||||||||||||||||||||||||| #
# |||                             ||| #
# |||          FUNCTIONS          ||| #
# |||                             ||| #
# ||||||||||||||||||||||||||||||||||| #
# ||||||||||||||||||||||||||||||||||| #
def equal():
    global list_numbers
    global list_operators
    while (len(list_numbers) >= 2) and len(list_operators):
        if list_operators[0] == '+':
            list_numbers[1] = float(list_numbers[0] + list_numbers[1])
        elif list_operators[0] == '-':
            list_numbers[1] = float(list_numbers[0]-list_numbers[1])
        elif list_operators[0] == '*':
            list_numbers[1] = list_numbers[0]*list_numbers[1]
        elif list_operators[0] == '/':
            list_numbers[1] = list_numbers[0]/list_numbers[1]
        list_numbers.pop(0)
        list_operators.pop(0)
    output.delete(0, END)
    print(list_numbers)
    val = str(list_numbers[0])
    clear()
    output.insert(0, val)
    

def number(number):
    output.insert(END, str(number))


def clearEn():
    output.delete(0, END)


def delete():
    output.delete(len(output.get()) - 1, END)


def clear():
    global list_numbers
    global list_operators
    output.delete(0, END)
    list_numbers, list_operators = [None], []


def perc():
    global list_numbers
    global list_operators
    input = output.get()
    if input == '':
        input = '0'
    num = float(input)
    if len(list_operators):
        if list_operators[-1] in '+-':
            val = list_numbers[-1] * round(num/100, 2)
    else:
        val = round(num/100, 2)
    list_numbers.append(val)
    if list_numbers[0] is None:
        list_numbers.pop(0)
    print(list_numbers)
    equal()

            
def eqal():
    global list_numbers
    global list_operators
    inp = output.get()
    if inp == '':
        inp = '0'
    num = float(inp)
    list_numbers.append(num)
    if list_numbers[0] is None:
        list_numbers.pop(0)
    equal()


def reciprocal():
    inp = output.get()
    clear()
    output.insert(0, str(1/float(inp)))


def square():
    inp = output.get()
    clear()
    output.insert(0, str(float(inp)**2))


def squareroot():
    inp = output.get()
    clear()
    output.insert(0, str(float(inp)**0.5))


def negate():
    global list_numbers
    inp = output.get()
    if inp == '' and list_numbers[0] is not None:
        list_numbers[-1] = -(list_numbers[-1])
        return
    clearEn()
    num = float(inp)
    list_numbers.append(num)
    if list_numbers[0] is None:
        list_numbers.pop(0)
    output.insert(0, str(-(float(inp))))


def division():
    global list_numbers
    global list_operators
    inp = output.get()
    if inp == '':
        inp = '0'
    num = float(inp)
    list_numbers.append(num)
    if list_numbers[0] is None:
        list_numbers.pop(0)
    list_operators.append('/')
    output.delete(0, END)


def addition():
    global list_numbers
    global list_operators
    inp = output.get()
    if inp == '':
        inp = '0'
    num = float(inp)
    list_numbers.append(num)
    if list_numbers[0] is None:
        list_numbers.pop(0)
    list_operators.append('+')
    output.delete(0, END)


def subtraction():
    global list_numbers
    global list_operators
    inp = output.get()
    if inp == '':
        inp = '0'
    num = float(inp)
    list_numbers.append(num)
    if list_numbers[0] is None:
        list_numbers.pop(0)
    list_operators.append('-')
    output.delete(0, END)


def mult():
    global list_numbers
    global list_operators
    inp = output.get()
    if inp == '':
        inp = '0'
    num = float(inp)
    list_numbers.append(num)
    if list_numbers[0] is None:
        list_numbers.pop(0)
    list_operators.append('*')
    output.delete(0, END)






# Main Text Box I guess
output = Entry( root,
                width = 13,
                borderwidth = 1,
                bg = '#515151',
                fg = '#fff',
                justify = 'right',
                font = ("Calibri 36 bold")
            )
output.grid(row = 0,
            column = 0,
            columnspan = 4,
            padx = 3,
            pady = 10,
        )


# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||| #
# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||| #
# |||||||                                                                             ||||||||| #
# |||||||                                   BUTTONS                                   ||||||||| #
# |||||||                                                                             ||||||||| #
# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||| #
# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||| #

# |||||||||||||||||||||||||||||||||||||||||||||||||||| #
# |||           CONSTRUCTING THE BUTTONS           ||| #
# |||||||||||||||||||||||||||||||||||||||||||||||||||| #
button_perc = Button(root, text = "% " , padx = 23, pady = 8, font = ("Calibri 15 bold"), bg = '#323232', fg = '#fff', borderwidth = 0, command = perc)
button_ClEn = Button(root, text = "CE ", padx = 20, pady = 8, font = ("Calibri 15 bold"), bg = '#323232', fg = '#fff', borderwidth = 0, command = clearEn)
button_Clea = Button(root, text = "C " , padx = 25, pady = 8, font = ("Calibri 15 bold"), bg = '#323232', fg = '#fff', borderwidth = 0, command = clear)
button_back = Button(root, text = "Del", padx = 19, pady = 8, font = ("Calibri 15 bold"), bg = '#323232', fg = '#fff', borderwidth = 0, command = delete)

button_repr = Button(root, text = "¹/𝑥", padx = 23, pady = 8, font = ("Calibri 15 bold"), bg = '#323232', fg = '#fff', borderwidth = 0, command = reciprocal)
button_sqre = Button(root, text = "𝑥²" , padx = 25, pady = 8, font = ("Calibri 15 bold"), bg = '#323232', fg = '#fff', borderwidth = 0, command = square)
button_sqrt = Button(root, text = "√𝑥 ", padx = 21, pady = 8, font = ("Calibri 15 bold"), bg = '#323232', fg = '#fff', borderwidth = 0, command = squareroot)
button_divi = Button(root, text = "÷"  , padx = 28, pady = 8, font = ("Calibri 15 bold"), bg = '#323232', fg = '#fff', borderwidth = 0, command = division)

button_sevn = Button(root, text = "7"  , padx = 28, pady = 8, font = ('Calibri 15 bold'), bg = '#111111', fg = '#fff', borderwidth = 0, command = lambda: number(7))
button_eigt = Button(root, text = "8"  , padx = 28, pady = 8, font = ('Calibri 15 bold'), bg = '#111111', fg = '#fff', borderwidth = 0, command = lambda: number(8))
button_nine = Button(root, text = "9"  , padx = 28, pady = 8, font = ('Calibri 15 bold'), bg = '#111111', fg = '#fff', borderwidth = 0, command = lambda: number(9))
button_mult = Button(root, text = "×"  , padx = 28, pady = 8, font = ("Calibri 15 bold"), bg = '#323232', fg = '#fff', borderwidth = 0, command = mult)

button_four = Button(root, text = "4"  , padx = 28, pady = 8, font = ('Calibri 15 bold'), bg = '#111111', fg = '#fff', borderwidth = 0, command = lambda: number(4))
button_five = Button(root, text = "5"  , padx = 28, pady = 8, font = ('Calibri 15 bold'), bg = '#111111', fg = '#fff', borderwidth = 0, command = lambda: number(5))
button_seex = Button(root, text = "6"  , padx = 28, pady = 8, font = ('Calibri 15 bold'), bg = '#111111', fg = '#fff', borderwidth = 0, command = lambda: number(6))
button_subt = Button(root, text = "−"  , padx = 28, pady = 8, font = ("Calibri 15 bold"), bg = '#323232', fg = '#fff', borderwidth = 0, command = subtraction)

button_ones = Button(root, text = "1"  , padx = 28, pady = 8, font = ('Calibri 15 bold'), bg = '#111111', fg = '#fff', borderwidth = 0, command = lambda: number(1))
button_twos = Button(root, text = "2"  , padx = 28, pady = 8, font = ('Calibri 15 bold'), bg = '#111111', fg = '#fff', borderwidth = 0, command = lambda: number(2))
button_tree = Button(root, text = "3"  , padx = 28, pady = 8, font = ('Calibri 15 bold'), bg = '#111111', fg = '#fff', borderwidth = 0, command = lambda: number(3))
button_addn = Button(root, text = "+"  , padx = 28, pady = 8, font = ("Calibri 15 bold"), bg = '#323232', fg = '#fff', borderwidth = 0, command = addition)

button_nega = Button(root, text = "⁺∕₋", padx = 22, pady = 8, font = ("Calibri 15 bold"), bg = '#111111', fg = '#fff', borderwidth = 0, command = negate)
button_zero = Button(root, text = "0"  , padx = 28, pady = 8, font = ('Calibri 15 bold'), bg = '#111111', fg = '#fff', borderwidth = 0, command = lambda: number(0))
button_adot = Button(root, text = ". " , padx = 28, pady = 8, font = ("Calibri 15 bold"), bg = '#111111', fg = '#fff', borderwidth = 0, command = lambda: number('.'))
button_eqal = Button(root, text = "="  , padx = 28, pady = 8, font = ("Calibri 15 bold"), bg = '#996b33', fg = '#fff', borderwidth = 0, command = eqal)

# |||||||||||||||||||||||||||||||||||||||||||||||||||| #
# |||         PLACING THE BUTTONS ON SCREEN        ||| #
# |||||||||||||||||||||||||||||||||||||||||||||||||||| #
button_perc.grid(row = 1,column = 0, padx = 2, pady = 1)
button_ClEn.grid(row = 1,column = 1, padx = 2, pady = 1)
button_Clea.grid(row = 1,column = 2, padx = 2, pady = 1)
button_back.grid(row = 1,column = 3, padx = 2, pady = 1)

button_repr.grid(row = 2,column = 0, padx = 2, pady = 1)
button_sqre.grid(row = 2,column = 1, padx = 2, pady = 1)
button_sqrt.grid(row = 2,column = 2, padx = 2, pady = 1)
button_divi.grid(row = 2,column = 3, padx = 2, pady = 1)

button_sevn.grid(row = 3,column = 0, padx = 2, pady = 1)
button_eigt.grid(row = 3,column = 1, padx = 2, pady = 1)
button_nine.grid(row = 3,column = 2, padx = 2, pady = 1)
button_mult.grid(row = 3,column = 3, padx = 2, pady = 1)

button_four.grid(row = 4,column = 0, padx = 2, pady = 1)
button_five.grid(row = 4,column = 1, padx = 2, pady = 1)
button_seex.grid(row = 4,column = 2, padx = 2, pady = 1)
button_subt.grid(row = 4,column = 3, padx = 2, pady = 1)

button_ones.grid(row = 5,column = 0, padx = 2, pady = 1)
button_twos.grid(row = 5,column = 1, padx = 2, pady = 1)
button_tree.grid(row = 5,column = 2, padx = 2, pady = 1)
button_addn.grid(row = 5,column = 3, padx = 2, pady = 1)

button_nega.grid(row = 6,column = 0, padx = 2, pady = 1)
button_zero.grid(row = 6,column = 1, padx = 2, pady = 1)
button_adot.grid(row = 6,column = 2, padx = 2, pady = 1)
button_eqal.grid(row = 6,column = 3, padx = 2, pady = 1)
# |||||||||||||||||||||||||||||||||||||||||||||||||||| #
# |||||||||||||||||||||||||||||||||||||||||||||||||||| #
# |||||||||||||||||||||||||||||||||||||||||||||||||||| #
# |||||||||||||||||||||||||||||||||||||||||||||||||||| #
# |||||||||||||||||||||||||||||||||||||||||||||||||||| #
# |||||||||||||||||||||||||||||||||||||||||||||||||||| #
# |||||||||||||||||||||||||||||||||||||||||||||||||||| #


root.mainloop()
