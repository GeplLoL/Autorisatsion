from tkinter import *
from webbrowser import *
import io as io
global passList
global logList
global salaList
passList=[]
logList=[]
salaList=[]
k=0
j=0
m=0
ente=0
create=0
with io.open("TextFile1.txt",'r',encoding="utf-8-sig") as f:
    for rida in f:
        passList.append(rida.strip())
    f.close()
with io.open("TextFile2.txt",'r',encoding="utf-8-sig") as f:
    for rida in f:
        logList.append(rida.strip())
    f.close()
with io.open("TextFile3.txt",'r',encoding="utf-8-sig") as f:
    for rida in f:
        salaList.append(rida.strip())
    f.close()
def Kirjuta_failisse(fail:str,jarjend:list):
    with io.open(fail, 'a', encoding='utf-8') as f:
        for line in jarjend:
            f.write(line+"\n")
        f.close()
def enter(event):
    global ente
    ente+=1
    entGet=ent.get()
    ent1Get=ent1.get()
    if entGet=="":
        ent.configure(bg="red")
    else:
        ent.configure(bg="white")
    if ent1Get=="":
        ent1.configure(bg="red")
    else:
        ent1.configure(bg="white")
    if  entGet in logList and ent1Get in passList:
        open("https://www.google.com/")
        print("You are in")
    else:
        print("Acc invalid")
def reg(event):
    global k
    k+=1
    if k>0:
        reg=Tk()
        reg.geometry("500x500")
        reg.title("Register")
        lblReg=Label(reg, text="Register", font="Arial 30" )
        entN=Entry(reg, width=10, font="Arial 20", text="Name")
        entS=Entry(reg, width=10, font="Arial 20", text="sajalane")
        lblN=Label(reg, text="Login",font="Arial 20")
        lblPass=Label(reg, text="Password",font="Arial 20")
        lblConfirm=Label(reg, text="Password confirm",font="Arial 20")
        lblS=Label(reg, text="Sajalane sõna",font="Arial 15")
        entPass=Entry(reg, width=10, font="Arial 20", text="Password")
        entPassC=Entry(reg,show="*", width=10, font="Arial 20", text="Password confirm")
        btnCreate=Button(reg, text="Create acc",font="Arial 18", bg="lightblue")
        def createACC(event):
            global create
            create+=1
            entPassGet=entPass.get()
            entPassCGet=entPassC.get()
            global entNGet
            entNGet=entN.get()
            entSGet=entS.get()
            if entNGet=="":
                entN.configure(bg="red")
            else:
                entN.configure(bg="white")
                logList.append(entNGet)
                Kirjuta_failisse("TextFile2.txt", logList)
            if entPassGet=="":
                entPass.configure(bg="red")
            else:
                entPass.configure(bg="white")
            if entPassCGet=="":
                entPassC.configure(bg="red")
            else:
                entPass.configure(bg="white")
            if entSGet=="":
                entS.configure(bg="red")
            else:
                entS.configure(bg="white")
                salaList.append(entSGet)
                Kirjuta_failisse("TextFile3.txt", salaList)
            if entPassGet!="" and entPassCGet!="" and (entPassGet==entPassCGet and entPassCGet==entPassGet):
                entPassC.configure(bg="lightgreen")
                entPass.configure(bg="lightgreen")
                entPassGetForList=entPass.get()
                passList.append(entPassGetForList)
                Kirjuta_failisse("TextFile1.txt", passList)
            else:
                entPassC.configure(bg="red")
                entPass.configure(bg="red")
        ob=[lblReg,lblN,entN,lblPass, entPass,lblConfirm,entPassC,lblS,entS,btnCreate]
        for item in ob:
            item.pack()
        btnCreate.bind('<Button-1>',createACC) 
def MutaNime(e):
    print(logList, passList)
    global m
    m+=1
    if m>0:
        mutNune=Tk()
        mutNune.geometry("500x500")
        mutNune.title("Nime või parooli muutmine")
        lblMut=Label(mutNune, text="Nime või parooli muutmine", font="Arial 30" )
        btnMut=Button(mutNune, text="Muuta",font="Arial 18", bg="lightblue")
        entNimi=Entry(mutNune, font="Arial 18", bg="white")
        entPassii=Entry(mutNune, font="Arial 18", bg="white")
        entNimiMut=Entry(mutNune, font="Arial 18", bg="white")
        entSala=Entry(mutNune, font="Arial 18", bg="white")
        entPassiiMut=Entry(mutNune, font="Arial 18", bg="white")
        obje=[lblMut,entNimi,entPassii,btnMut,entNimiMut,entPassiiMut,entSala]
        for item in obje:
            item.pack(pady=2)
        def Mutnimi(e):
            entNimiGet=entNimi.get()
            entNimiMutGet=entNimiMut.get()
            entPassiiMutGet=entPassiiMut.get()
            entSalaGet=entSala.get()
            salaList.append(entSalaGet)
            entSalaInd=salaList.index(entSalaGet)
            entPassiiGet=entPassii.get()
            entNimiGetInd=logList.index(entNimiGet)
            entPassiiGetInd=passList.index(entPassiiGet)
            logList.insert(entNimiGetInd, entNimiMutGet)
            passList.insert(entPassiiGetInd, entPassiiMutGet)
            salaList.insert(entSalaInd,entSalaGet)
    btnMut.bind('<Button-1>', Mutnimi)
def unu(event):
    global j
    j+=1
    if j>0:
        unu=Tk()
        unu.geometry("500x500")
        unu.title("Unustanud parooli taastamine")
        btnUnu=Button(unu, text="tagasta parool",font="Arial 18", bg="lightblue")
        lblUnu=Label(unu, text="Sisse Nimi", font="Arial 30" )
        entNUnu=Entry(unu, font="Arial 18", bg="white")
        lblSUnu=Label(unu, text="Sisse sajala sõna", font="Arial 30" )
        entSalaUnu=Entry(unu, font="Arial 18", bg="white")
        lblPass=Label(unu, text="", font="Arial 30")
        lblUnu.pack()
        entNUnu.pack()
        lblSUnu.pack()
        entSalaUnu.pack()
        btnUnu.pack()
        def unuPass(e):
            entNUnuGetUn=entNUnu.get()
            entSalaUnuGet=entSalaUnu.get()
            entNGetListiInd=salaList.index(entSalaUnuGet)
            if entNUnuGetUn=="":
                entNUnu.configure(bg="red")
            else:
                entNUnu.configure(bg="white")
            if entSalaUnuGet=="":
                entSalaUnu.configure(bg="red")
            else:
                entSalaUnu.configure(bg="white")
            if entNUnuGetUn in logList and entSalaUnuGet in salaList:
                lblPass.configure(text=passList[entNGetListiInd])
        lblPass.pack()
    btnUnu.bind('<Button-1>', unuPass)
def close(e):
    aken.destroy()
aken=Tk()
aken.geometry("800x550");aken.title("Govnoklasniki")
lblName=Label(aken, width=10, text="Govnoklasniki", font="Arial 30")
ent=Entry(aken, width=10, text="Login", font="Arial 20")
lbl=Label(aken, text="Login",font="Arial 20")
ent1=Entry(aken, show="*", width=10, text="Password", font="Arial 20")
lbl1=Label(aken, text="Password",font="Arial 20")
btn=Button(aken, text="Enter",font="Arial 20", bg="lightblue", width=30)
btnReg=Button(aken, text="Register",font="Arial 18", bg="red", width=30)
btnMuuta=Button(aken, text="Nime või parooli muutmine",font="Arial 18", bg="green", width=30)
btnUn=Button(aken, text="Unustanud parooli taastamine",font="Arial 18", bg="purple", width=30)
btnlop=Button(aken, text="Lõpetamine",font="Arial 18", bg="gray", width=30)
btnReg.bind('<Button-1>',reg)
btn.bind('<Button-1>',enter)
btnMuuta.bind('<Button-1>',MutaNime)
btnUn.bind('<Button-1>',unu)
btnlop.bind('<Button-1>',close)
obi=[lblName,lbl,ent,lbl1,ent1,btn,btnReg,btnMuuta,btnUn,btnlop]
for item in obi:
    item.pack(pady=2)
aken.mainloop()