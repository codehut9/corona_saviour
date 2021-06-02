import tkinter as tk
from pyzipcode import ZipCodeDatabase

zcdb = ZipCodeDatabase()

root=tk.Tk()

def instruction():
    tk.Label(text="So, if you have an emergency with a patient that is in a certain condition due to covid and you can't find the nearest vacant hospital just use our app. When you press the start button the device will ask you your pin code and the category(low,mild,critical)of effects you have due to covid. Then a map will appear containing all hospitals and info curated from hundreds of websites. Using color code and the grading process you will find the hospital just right for you",font=("Arial",5)).pack()

def start():
    def submit():
        zipcode=zcdb[560103]
        lat=zipcode.latitude
        long=zipcode.longitude



    pin_label=tk.Label(root, text = 'pin code', font=('Arial',10, 'bold')
    pin_entry=tk.Label(root,font=('Arial',10)

    cat_label=tk.Label(root, text = 'category of covid(low,mild,critical)', font=('Arial',10, 'bold')
    cat_entry=tk.Label(root,font=('Arial',10)
    
    sub_btn=tk.Button(root,text = 'Submit', command = submit)
  




name=tk.Label(text="CORONA SAVIOUR",font=("Arial",25))
name.pack()

instruction=tk.Button(root,text="instructions",command=instruction)
instruction.pack(side=tk.RIGHT)

start=tk.Button(root,text="start",command=start)
start.pack(side=tk.LEFT)



root.mainloop()
