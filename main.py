from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showinfo
import random

# Создание окна

mainWindow = Tk()
mainWindow.geometry("1280x720+600+100")
mainWindow.title("Оконное приложение")
mainWindow.resizable(width = False, height = False)

def outPutName():

    value = entryFieldLab1.get()

    showinfo(title = "Приветствие", message = f"Привет, {value}!")

def calculate():

    value1 = int(entryField1Lab2.get())
    value2 = int(entryField2Lab2.get())
    res = "на ноль делить нельзя!"
    if value2 != 0:
        res = value1 / value2

    showinfo(title = "Действия на числами", 
            message = f"Сумма = {value1 + value2}\nРазность = {value1 - value2}\nПроизведение = {value1 * value2}\nЧастное = {res}")

def listManipulate():

    list = []
    for i in range(10):
        list.append(int(random.random() * 50))

    originalList = list.copy()
    list.sort()

    sum = 0
    for i in range(10):
        sum += list[i]

    showinfo(title = "Список", 
        message = f"Список: {originalList}\nОтсортированный список: {list}\nМаксимальное значение: {max(list)}\nМинимальное значение: {min(list)}\nСумма чисел в списке: {sum}")

def makeFiles():

    number = 0
    for i in range(5):
        file_name = "file" + str(i + 1) + ".txt"
        file = open(file_name, "w")
        for i in range(10):
            n = (int(random.random() * 50))
            file.write(str(n) + " ")
        file.close()

    showinfo(title = "Успех!", message = "5 файлов успешно созданы")

def readFile():

    value = int(entryFieldNumberOfFileLab4.get())
    file = open("file" + str(value) + ".txt")
    fileContentString = file.read()
    fileContentNumber = [int(i) for i in fileContentString.split()]

    file.close()

    showinfo(title = "Содержимое файла", 
            message = f"Содержимое файла: {fileContentString}\nСреднее арифметическое значение чисел в файле: {sum(fileContentNumber) / len(fileContentNumber)}")

def calculator():

    action = int(entryFieldForActionLab5.get())
    value1 = int(entryFieldFirstNumberLab5.get())
    value2 = int(entryFieldSecondNumberLab5.get())

    res = 0
    if action == 1:
        res = value1 + value2
    elif action == 2:
        res = value1 - value2
    elif action == 3:
        res = value1 * value2
    elif action == 4:
        if value2 == 0:
            res = "Не существует. На ноль делить нельзя!"
        else:
            res = value1 / value2

    showinfo(title = "Калькулятор", message = f"Ответ = {res}")

# Лаба №1

textLab1 = ttk.Label(text = "Введите имя", background = "#1864de", foreground = "#ffffff", padding = "10")
textLab1.place(x = 20, y = 20, height = "40")

entryFieldLab1 = ttk.Entry(background = "#1864de", font = "Fixedsys 16")
entryFieldLab1.place(x = 140, y = 20, height = "40")

enterBtnLab1 = ttk.Button(text = "Ввести", command = outPutName)
enterBtnLab1.place(x = 330, y = 20, height = "40")

# Лаба №2
textLab2 = ttk.Label(text = "Введите числа", background = "#1864de", foreground = "#ffffff", padding = "10")
textLab2.place(x = 20, y = 100, height = "40")

entryField1Lab2 = ttk.Entry(background = "#1864de", font = "Fixedsys 16")
entryField1Lab2.place(x = 170, y = 100, width = "50", height = "40")

entryField2Lab2 = ttk.Entry(background = "#1864de", font = "Fixedsys 16")
entryField2Lab2.place(x = 230, y = 100, width = "50", height = "40")

enterBtnLab2 = ttk.Button(text = "Ввести", command = calculate)
enterBtnLab2.place(x = 330, y = 100, height = "40")

# Лаба №3
textLab3 = ttk.Label(text = "Генерация списка", background = "#1864de", foreground = "#ffffff", padding = "10")
textLab3.place(x = 20, y = 180, height = "40")

enterBtnLab3 = ttk.Button(text = "Сгенерировать", command = listManipulate)
enterBtnLab3.place(x = 330, y = 180, height = "40")

# Лаба №4

textLab4 = ttk.Label(text = "Сгенерировать файлы", background = "#1864de", foreground = "#ffffff", padding = "10")
textLab4.place(x = 20, y = 260, height = "40")

enterBtnLab4 = ttk.Button(text = "Сгенерировать", command = makeFiles)
enterBtnLab4.place(x = 330, y = 260, height = "40")

textNumberOfFileLab4 = ttk.Label(text = "Выберете номер файла", background = "#1864de", foreground = "#ffffff", padding = "10")
textNumberOfFileLab4.place(x = 20, y = 340, height = "40")

entryFieldNumberOfFileLab4 = ttk.Entry(background = "#1864de", font = "Fixedsys 16")
entryFieldNumberOfFileLab4.place(x = 210, y = 340, width = "40", height = "40")

enterBtn = ttk.Button(text = "Выбрать", command = readFile)
enterBtn.place(x = 330, y = 340, height = "40")

# Лаба №5-1
textForNumbersLab5 = ttk.Label(text = "Введите числа", background = "#1864de", foreground = "#ffffff", padding = "10")
textForNumbersLab5.place(x = 20, y = 420, height = "40")

entryFieldFirstNumberLab5 = ttk.Entry(background = "#1864de", font = "Fixedsys 16")
entryFieldFirstNumberLab5.place(x = 140, y = 420, width = "50", height = "40")

entryFieldSecondNumberLab5 = ttk.Entry(background = "#1864de", font = "Fixedsys 16")
entryFieldSecondNumberLab5.place(x = 210, y = 420, width = "50", height = "40")

textForActionLab5 = ttk.Label(text = "Введите действие: 1 - сумма; 2 - разность; 3 - произведение; 4 - частное", background = "#1864de", foreground = "#ffffff", padding = "10")
textForActionLab5.place(x = 280, y = 420)

entryFieldForActionLab5 = ttk.Entry(background = "#1864de", font = "Fixedsys 16")
entryFieldForActionLab5.place(x = 710, y = 420, width = "50", height = "40")

enterBtnLab5 = ttk.Button(text = "Ввод", command = calculator)
enterBtnLab5.place(x = 770, y = 420, height = "40")

# Лаба №5-2



mainWindow.mainloop()