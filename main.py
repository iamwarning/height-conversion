from tkinter import Tk, Button, Label, DoubleVar, Entry, DISABLED, OUTSIDE

window = Tk()
window.title('Height Conversion')
window.configure(background="#f4f4f4")
window.geometry("430x400")
window.resizable(width=False, height=False)


def convert():
    value = float(ft_entry.get())
    meter = value / 3.281
    inches = value * 12
    centimeters = value * 30.48
    kilometers = value / 3281
    mt_value.set("%.3f" % meter)
    in_value.set("%.3f" % inches)
    cm_value.set("%.3f " % centimeters)
    km_value.set("%.8f" % kilometers)


def reset():
    ft_value.set("")
    mt_value.set("")
    in_value.set("")
    cm_value.set("")


def valida(number):
    if number.isdigit():
        return True
    else:
        return False


ft_lbl = Label(window, text="Feet", bg="#f4f4f4", fg="#212121", width=14)
ft_lbl.config(font=("Courier", 12))
ft_lbl.grid(column=0, row=0, padx=15, pady=15)

ft_value = DoubleVar()
ft_entry = Entry(window, textvariable=ft_value, width=14, relief="flat", bd=0, highlightthickness=0)
ft_entry.config(font=("Courier", 12))
ft_entry.grid(column=1, row=0)
ft_entry.delete(0, 'end')

mt_lbl = Label(window, text="Meter", bg="#f4f4f4", fg="#212121", width=14)
mt_lbl.config(font=("Courier", 12))
mt_lbl.grid(column=0, row=1)

mt_value = DoubleVar()
mt_entry = Entry(window, textvariable=mt_value, width=14, relief="flat", bd=0, highlightthickness=0, state=DISABLED)
mt_entry.config(font=("Courier", 12))
mt_entry.grid(column=1, row=1, padx=15, pady=15)
mt_entry.delete(0, 'end')

in_lbl = Label(window, text="Inches", bg="#f4f4f4", fg="#212121", width=14)
in_lbl.config(font=("Courier", 12))
in_lbl.grid(column=0, row=2, padx=15, pady=15)

in_value = DoubleVar()
in_entry = Entry(window, textvariable=in_value, width=14, relief="flat", bd=0, highlightthickness=0, state=DISABLED)
in_entry.config(font=("Courier", 12))
in_entry.grid(column=1, row=2, padx=15, pady=13)
in_entry.delete(0, 'end')

cm_lbl = Label(window, text="Centimeters", bg="#f4f4f4", fg="#212121", width=14)
cm_lbl.config(font=("Courier", 12))
cm_lbl.grid(column=0, row=3, padx=15, pady=15)

cm_value = DoubleVar()
cm_entry = Entry(window, textvariable=cm_value, width=14, relief="flat", bd=0, highlightthickness=0, state=DISABLED)
cm_entry.config(font=("Courier", 12))
cm_entry.grid(column=1, row=3, padx=15, pady=13)
cm_entry.delete(0, 'end')

km_lbl = Label(window, text="Kilometers", bg="#f4f4f4", fg="#212121", width=20)
km_lbl.config(font=("Courier", 12))
km_lbl.grid(column=0, row=4, padx=14, pady=15)

km_value = DoubleVar()
km_entry = Entry(window, textvariable=km_value, width=14, relief="flat", bd=0, highlightthickness=0, state=DISABLED)
km_entry.config(font=("Courier", 12))
km_entry.grid(column=1, row=4, padx=15, pady=13)
km_entry.delete(0, 'end')

convert_btn = Button(window, text="Convert", bg="#15d798", fg="white", width=14, height=2, relief='flat',
                     highlightthickness=0, bd=0, cursor="hand2", command=convert)
convert_btn.config(font=("Courier", 12))
convert_btn.grid(column=0, row=6, padx=14, pady=14)

reset_btn = Button(window, text="Reset", bg="#607D8B", fg="white", width=14, height=2,
                   relief="flat", highlightthickness=0, bd=0, cursor="hand2", command=reset)
reset_btn.config(font=("Courier", 12))
reset_btn.place(bordermode=OUTSIDE, height=134, width=107, x=40, y=200)
reset_btn.grid(column=1, row=6, padx=15)

window.mainloop()
