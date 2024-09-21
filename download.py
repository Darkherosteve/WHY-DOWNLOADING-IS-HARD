import tkinter  as tk
import ttkbootstrap as ttk
import os
import yt_dlp
from tkinter import filedialog


def Download():
    url = linkget.get()
    path = linkset.get()
    
    #Path should not be empty
    if not url or not path:
        print("plese Provide Both Url and Path")
        msg.set("plese Provide Both Url and Path")
        return
    
    download = {
        'format': 'best',
         'outtmpl': os.path.join(path,'%(title)s.%(ext)s')
        
    }
    try:
        #downloading
        with yt_dlp.YoutubeDL(download) as ydl:
            ydl.download([url])
            print('Download Complete')
            msg.set("Download Complete")      
        
    except Exception as e:
        print(f"Somthing Went Wrong!: {e}")
        msg.set("Something Went Wrong! \n plz Check Your Internet \n Report @ 'Minionsknowledge10@gmail.com' ")
    
 

#save Path From User
def choose_path():
    dir = filedialog.askdirectory(title="Choose Path To Save")
    linkset.set(dir)
    
    

#main Window 
window = tk.Tk()

#window Title
window.title("Why Downloading Is Hard")

#icon
# window.iconbitmap('download.ico')

#Fix The Size  of window
window.maxsize(400, 400)
window.minsize(400, 400)

msg = tk.StringVar()
msgbox = ttk.Label(master=window, text="", textvariable=msg, font=("Ariel", 10, "bold"))
msgbox.pack(padx=10, pady=10)

#container 
MainFrame = tk.Frame(master=window)

#text labekl for link
linklabel = ttk.Label(master=MainFrame, text="Paste Your Link Bellow", font=("Ariel", 10, "bold"))
linklabel.pack(padx=5, pady=5)

#link Entry from Ussr
linkget = tk.StringVar()
linkEntry = ttk.Entry(master=MainFrame, textvariable=linkget)
linkEntry.pack(padx=5, pady=5, fill="x")


#Download path label
linkpath = tk.Label(master=MainFrame, text="Download Path", font=("Ariel", 10, "bold"))
linkpath.pack(padx=5, pady=5)

#Entry of Download path
linkset = tk.StringVar()
loctaion = ttk.Entry(master=MainFrame, textvariable=linkset)
loctaion.pack(padx=5, pady=5, fill="x")


#buuton For File path
choose_button = ttk.Button(master=MainFrame, text="Choose Path", command=choose_path)
choose_button.pack(padx=10, pady=10, fill="x")

#Download button
Download_button = ttk.Button(master=MainFrame, text="Download", command=Download)
Download_button.pack(padx=10, pady=10, fill="x")


MainFrame.pack(padx=10, pady=10, fill="x")


window.mainloop()