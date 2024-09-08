from tkinter import *
from tkinter import messagebox
import os
from PIL import Image,ImageTk
from tkinter import filedialog

def CreateNewFile():
    with open(filedialog.asksaveasfilename(),'w') as f:
        f.close()
        name=f.name
        messagebox.showinfo("info",f"The File {name} Has Been Created")
def DeleteFile():
    file=filedialog.askopenfilename()
    with open(file,'r') as f:
        pass
    ask=messagebox.askquestion("Confirm","Are You Sure You Want Delete This File ?")
    if ask=='yes':
        os.remove(file)
        messagebox.showinfo("info",f"The File {f.name} Has Been Deleted")
    else:
        messagebox.showinfo("info","Ok")

def WriteOnFile():
    file=filedialog.askopenfilename()
    app2=Tk()
    app2.title("Files Manager")
    app2.geometry("700x500+300+150")
    app2.resizable(False,False)
    app2.config(background='white')
    app2.iconbitmap("accessories_text_editor_16842.ico")
    text_area = Text(app2, wrap='word', height=15, width=50,bd=7)
    with open(file,'r') as f:
        data=f.read()
        def SaveFile():
            All_Data=text_area.get("1.0",END)
            with open(f.name,"w") as fw:
                fw.write(All_Data)
                fw.close()
                messagebox.showinfo("info",f"Done Writing on {f.name}")
    text_area.insert(END,data)
    text_area.pack(side=LEFT, expand=True)
    btn=Button(app2,text="Save To File",bg='green',fg='white',width=60,font=(14,14),command=SaveFile)
    btn.place(x=10,y=450)
    app2.mainloop()

def ReadFile():
    file=filedialog.askopenfilename()
    app3=Tk()
    app3.title("Files Manager")
    app3.geometry("700x500+300+150")
    app3.resizable(False,False)
    app3.config(background='white')
    app3.iconbitmap("accessories_text_editor_16842.ico")
    text_area = Text(app3, wrap='word', height=15, width=50,bd=7)
    with open(file,'r') as fr:
        txt=fr.read()
        text_area.insert(END,txt)
        text_area.pack(side=LEFT, expand=True)
    app3.mainloop()
    


        

    





app=Tk()
app.title("Files Manager")
app.geometry("700x500+300+150")
app.resizable(False,False)
app.config(background='white')
app.iconbitmap("accessories_text_editor_16842.ico")


logo_Image=ImageTk.PhotoImage(Image.open("accessories_text_editor_16842.png"))

lb1=Label(image=logo_Image,bg='white',pady=40,)
lb1.pack()

bt1=Button(text="Create New File +",bg='green',command=CreateNewFile,justify='center',width=45,bd=3,font=(14,14),fg='white')
bt1.place(x=100,y=150)

bt2=Button(text="Write On File ",command=WriteOnFile,justify='center',width=45,bd=3,font=(14,14),activebackground='blue',activeforeground='white')
bt2.place(x=100,y=220)

bt3=Button(text="Read File ",justify='center',command=ReadFile,width=45,bd=3,font=(14,14),activebackground='orangered',activeforeground='white')
bt3.place(x=100,y=290)

bt3=Button(text="Delete File x ",bg="red",command=DeleteFile,justify='center',width=45,bd=3,font=(14,14),fg='white')
bt3.place(x=100,y=360)

app.mainloop()


