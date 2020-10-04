import tkinter as tk

def eg():
    window = tk.Tk()
    text=tk.Text(window)
    text.pack()
    text.insert(tk.END, "https://pastebin.com/G4XjWmfb" )
    window.mainloop()

root = tk.Tk()

def destroy(event):
    root.destroy()


root.bind("<Control_L>"+"q", destroy)
root.title('Calculator')
ans = tk.Entry(root, borderwidth=4, width=40)
ans.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

data = []
tmpnum = None

def typeNum(number):
    global tmpnum
    current = ans.get()
    ans.delete(0, tk.END)
    ans.insert(0, str(current) + str(number))
    tmpnum = int(str(current) + str(number))

def eq():
    global tmpnum
    global data
    if tmpnum:
        data.append(tmpnum)
    print("DEBUG")
    print(data)

    # Evaluate
    if len(data) < 3:
        print("ERROR: incomplete equation")
        data.clear()
        return

    firstnum = data.pop(0)
    operator = data.pop(0)
    secondnum = data.pop(0)
    data.clear()

    if operator == "+":
        answer = firstnum + secondnum
    elif operator == "-":
        answer = firstnum - secondnum
    elif operator == "*":
        answer = firstnum * secondnum
    elif operator == "/":
        answer = firstnum / secondnum

    ans.delete(0, tk.END)
    ans.insert(0, str(answer))
    if answer==666:
        eg()
    tmpnum = answer # Store result in case you want to use it for next operation

def operation(op):
    global tmpnum
    global data
    ans.delete(0, tk.END)
    if tmpnum:
        data.append(tmpnum)
        tmpnum = None
        data.append(op)

def clearAll():
    global data
    ans.delete(0, tk.END)
    data.clear()



button1 = tk.Button(root, text='1', padx=40, pady=20, command=lambda: typeNum(1))
button2 = tk.Button(root, text='2', padx=40, pady=20, command=lambda: typeNum(2))
button3 = tk.Button(root, text='3', padx=40, pady=20, command=lambda: typeNum(3))
button4 = tk.Button(root, text='4', padx=40, pady=20, command=lambda: typeNum(4))
button5 = tk.Button(root, text='5', padx=40, pady=20, command=lambda: typeNum(5))
button6 = tk.Button(root, text='6', padx=40, pady=20, command=lambda: typeNum(6))
button7 = tk.Button(root, text='7', padx=40, pady=20, command=lambda: typeNum(7))
button8 = tk.Button(root, text='8', padx=40, pady=20, command=lambda: typeNum(8))
button9 = tk.Button(root, text='9', padx=40, pady=20, command=lambda: typeNum(9))

button0 = tk.Button(root, text='0', padx=40, pady=20, command=lambda: typeNum(0))
equals = tk.Button(root, text='=', padx=40, pady=20, command=eq)
clear = tk.Button(root, text='CLEAR', padx=23, pady=20, command=clearAll)

add = tk.Button(root, text='+', padx=30, pady=20, command=lambda: operation('+'))
sub = tk.Button(root, text='-', padx=30, pady=20, command=lambda: operation('-'))
mult = tk.Button(root, text='x', padx=30, pady=20, command=lambda: operation('*'))
div = tk.Button(root, text='÷', padx=30, pady=20, command=lambda: operation('/'))

button1.grid(row=1, column=0)
button2.grid(row=1, column=1)
button3.grid(row=1, column=2)

button4.grid(row=2, column=0)
button5.grid(row=2, column=1)
button6.grid(row=2, column=2)

button7.grid(row=3, column=0)
button8.grid(row=3, column=1)
button9.grid(row=3, column=2)

button0.grid(row=4, column=0)
equals.grid(row=4, column=1)
clear.grid(row=4, column=2)

add.grid(row=1, column=3)
sub.grid(row=2, column=3)
mult.grid(row=3, column=3)
div.grid(row=4, column=3)

file = open('./settings/sombre','r')
sombre = file.read()
file.close()
if sombre == 'oui':
    root.config(bg='black')



root.mainloop()