from tkinter import Tk, Entry, Button, END

root = Tk()
root.title("Marciaus Skaiciuokle")

entry = Entry(root, width=35, borderwidth=5)
entry.grid(row=0, column=0, columnspan=3, padx=10, pady=10)


class Calculator:
    FIRST_NUMBER = 0
    SECOND_NUMBER = 0
    SUM = False

    def reset(self):
        self.SECOND_NUMBER = 0
        self.FIRST_NUMBER = 0

    def insert_text(self, number):
        if self.SUM:
            entry.delete(0, END)
            self.SUM = False
        entry.insert(END, number)

    def remove_text(self):
        entry.delete(0, END)
        self.reset()

    def add_text(self):
        self.FIRST_NUMBER += int(entry.get())
        entry.delete(0, END)

    def equal_text(self):
        self.SECOND_NUMBER = int(entry.get())
        entry.delete(0, END)
        entry.insert(0, str(sum([self.FIRST_NUMBER, self.SECOND_NUMBER])))
        self.SUM = True
        self.reset()


calculator = Calculator()

button_0 = Button(root, text="0", command=lambda: calculator.insert_text(0), padx=40, pady=20)
button_1 = Button(root, text="1", command=lambda: calculator.insert_text(1), padx=40, pady=20)
button_2 = Button(root, text="2", command=lambda: calculator.insert_text(2), padx=40, pady=20)
button_3 = Button(root, text="3", command=lambda: calculator.insert_text(3), padx=40, pady=20)

button_4 = Button(root, text="4", command=lambda: calculator.insert_text(4), padx=40, pady=20)
button_5 = Button(root, text="5", command=lambda: calculator.insert_text(5), padx=40, pady=20)
button_6 = Button(root, text="6", command=lambda: calculator.insert_text(6), padx=40, pady=20)

button_7 = Button(root, text="7", command=lambda: calculator.insert_text(7), padx=40, pady=20)
button_8 = Button(root, text="8", command=lambda: calculator.insert_text(8), padx=40, pady=20)
button_9 = Button(root, text="9", command=lambda: calculator.insert_text(9), padx=40, pady=20)

button_add = Button(root, text="+", command=lambda: calculator.add_text(), padx=39, pady=20)
button_equal = Button(root, text="=", command=lambda: calculator.equal_text(), padx=90, pady=20)
button_clear = Button(root, text="Clear", command=lambda: calculator.remove_text(), padx=79, pady=20)

button_1.grid(row=4, column=0)
button_2.grid(row=4, column=1)
button_3.grid(row=4, column=2)
button_4.grid(row=3, column=0)
button_5.grid(row=3, column=1)
button_6.grid(row=3, column=2)
button_clear.grid(row=5, column=1, columnspan=2)
button_0.grid(row=5, column=0)
button_7.grid(row=2, column=0)
button_8.grid(row=2, column=1)
button_9.grid(row=2, column=2)
button_equal.grid(row=6, column=1, columnspan=2)
button_add.grid(row=6, column=0)

root.mainloop()
