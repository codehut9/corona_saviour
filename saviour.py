import tkinter as tk
from pyzipcode import ZipCodeDatabase
import gmplot

zcdb = ZipCodeDatabase()

root=tk.Tk()

def instruction():
    tk.Label(text="So, if you have an emergency with a patient that is in a certain condition due to covid and you can't find the nearest vacant hospital just use our app. When you press the start button the device will ask you your pin code and the category(low,mild,critical)of effects you have due to covid. Then a map will appear containing all hospitals and info curated from hundreds of websites. Using color code and the grading process you will find the hospital just right for you",font=("Arial",5)).pack()

def start():
    def submit():
        zipcode=zcdb[560103]
        latitude=zipcode.latitude
        longitude=zipcode.longitude

        gmap=gmplot.GoogleMapPlotter(latitude,longitude)
        SIHM =gmplot.GoogleMapPlotter(14.15201,77.77684)
       # Sai Institute of Higher Medical Sciences=(14.15201,77.77684)
       # Sri Venkateswara Institute of Medical Sciences=(13.63805,79.40389)
       # Siddhartha Medical College, NTR University of Health Sciences=(16.51723,80.67144)
       # Rainbow Hospital headquarters=(17.41386,78.44608)
       # Apollo Hospitals Ramnagar Vizag=(17.71725,83.30918)
       # CARE Hospitals - Ram Nagar=(17.72027,83.31262)
       # Government ENT Hospital, Visakhapatnam=(17.73022,83.33074)
       # Government Victoria Hospital=(17.69883,83.29810)
       # King George Hospital=(17.70872,83.30603)
       # Rani Chandramani Devi Government Hospital=(17.72889,83.33686)
       # SevenHills Hospital=(17.71730,83.30957)
        
        gmap.draw( "C:\\Users\\apple\\code\\corona_saviour\\map1.html" )



    pin_label=tk.Label(root, text = 'pin code', font=('Arial',10, 'bold'))
    pin_entry=tk.Label(root,font=('Arial',10))

    cat_label=tk.Label(root, text = 'category of covid(low,mild,critical)', font=('Arial',10, 'bold'))
    cat_entry=tk.Label(root,font=('Arial',10))
    
    sub_btn=tk.Button(root,text = 'Submit', command = submit)
  




name=tk.Label(text="CORONA SAVIOUR",font=("Arial",25))
name.pack()

instruction=tk.Button(root,text="instructions",command=instruction)
instruction.pack(side=tk.RIGHT)

start=tk.Button(root,text="start",command=start)
start.pack(side=tk.LEFT)



root.mainloop()
