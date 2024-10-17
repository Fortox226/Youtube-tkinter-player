import tkinter as tk
# global next
next = False
def startWindow():
    
    def nextStep():
        global next
        next = True
        
    root = tk.Tk()
    root.geometry('400x400')
    button = tk.Button(root, text='Rozpocznij pobieranie', command=nextStep)
    button.pack()

    root.mainloop()
startWindow()