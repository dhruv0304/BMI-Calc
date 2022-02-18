import tkinter

root = tkinter.Tk()
root.title("Dhruv's BMI Calculator")
root.geometry('600x500')
root.resizable(False, False)

background_photo = tkinter.PhotoImage(file="BMI Calc.png")
tkinter.Label(root, image=background_photo).place(x=-2, y=-2)


height = tkinter.StringVar()
weight = tkinter.StringVar()
answer = tkinter.StringVar()

entry_box = tkinter.Entry(root, textvariable = height, width = 15).place(x = 325, y = 100)
entry_box = tkinter.Entry(root, textvariable = weight, width = 15).place(x = 325, y = 135)

tkinter.Label(root, textvariable = answer, font=('Segoe UI Black', 10), fg='#75e3fd', bg='black').place(x=120, y=180)

def BMI():
    y = float(weight.get())
    x = float(height.get())
    BMI = y / (x ** 2)
    
    if BMI < 1:
        answer.set('Double check if your measurements are inputed correctly.')
    elif BMI < 18.5:
        answer.set("You are underweight, a caloric surplus is recommended.")
    elif BMI < 25:
        answer.set("You are at a healthy weight, keep it up!")
    elif BMI < 30:
        answer.set("You are overweight, a caloric deficit is recommended.")
    else:
        answer.set("You are obese, a caloric deficit is recommended.")

def clear():
    answer.set("")
    height.set("")
    weight.set("")

tkinter.Button(text = " Calculate BMI! ", command = BMI).place(x=220, y=225)
tkinter.Button(text = " Reset ", command = clear).place(x=320, y=225)

root.mainloop()