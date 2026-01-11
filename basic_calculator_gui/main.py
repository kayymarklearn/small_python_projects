from tkinter import *
from calculate import *
digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
operators = ['x', '+', '-', '/', '=']
digit_buttons = []

window = Tk()
window.title("Basic Calculator")
window.minsize(400, 300)
window.config(padx=20, pady=20)

def get_user_input():
    pass

def display_user_input(dig):
    user_input.insert('end-1c', dig)


# User Input
user_input = Text(height=2, width=15)
user_input.grid(row=0, column=0, columnspan=5)

row_x = 1
col_y = 0

# Create digits
for digit in digits:
    digit_button = Button(text=digit)
    digit_button.grid(row=row_x, column=col_y)
    digit_button.config(padx=5, pady=5)
    col_y += 1
    if col_y % 5 == 0:
        row_x += 1
        col_y = 0
    digit_buttons.append(digit_button)

# Show buttons for the math operators
for operator in operators:
    operator_button = Button(text=operator)
    operator_button.grid(row=row_x, column=col_y)
    operator_button.config(padx=5, pady=5)
    col_y += 1

print(col_y)
print(row_x)
window.mainloop()