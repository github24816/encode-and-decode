import tkinter
from tkinter import *
from tkinter.ttk import *
from tkinter import scrolledtext
def encode():
    root=Toplevel()
    root.geometry("600x500")
    l= Label(root,text='What is the text to be encoded?')
    global inputtxt
    inputtxt = scrolledtext.ScrolledText(root,wrap = tkinter.WORD,width = 25, height = 8, font = ("Times New Roman", 15))
    global outputttxt
    outputttxt=scrolledtext.ScrolledText(root,wrap=tkinter.WORD,width=25,height=8,font=("Times New Roman",15))
    butt= Button(root,text='Encode',command=lambda:sus())
    l.pack()
    inputtxt.pack()
    butt.pack()
    outputttxt.pack()
    root.mainloop()
def sus():
    text=inputtxt.get("1.0","end-1c")
    coder= {"A": "Z", "B":"M", "C":"O", "D":"T", "E":"7", "F":"8", "G":"1", "H":"S", "I":"P", "J":"Q", "K":"4", "L":"2", "M":"R", "N":"N", "O":"5", "P":"V","Q":"C","R":"3","S":"6","T":"9","U":"D","V":"G","W":"K","X":"A","Y":"U","Z":"W"," ":"0"
            ,"a":"z","b":"m","c":"o","d":"t","e":"!","f":"@","g":"*","h":"s","i":"p","j":"q","k":"#","l":"$","m":"r","n":"n","o":"%","p":"v","q":"c","r":"^","s":"&","t":"(","u":"d","v":"g","w":"k","x":"a","y":"u","z":"w","1":"[","2":"]","3":"|",
            "4":":","5":";","6":"<","7":".","8":",","9":"?","10":"/","0":"+","!":"』","@":"©","#":"®","$":"™","%":"℠","^":"℡","&":"℗","*":"‱","(":"№",")":"℀","{":"℁","[":"℅","]":"℆","}":"⅍","/":"☊",":":"☎",";":"☏","'":"⌨",",":"✂","<":"✆",">":"✇",".":"✈","?":"✉"
            ,"-":"¢","_":"ƒ","+":"€","=":"௹","~":"฿","\n":"♚"}
    test= ""
    for i in text:
        test+=coder[i] 
    outputttxt.insert(1.0,test)
def decode():
    root=Toplevel()
    root.geometry("600x500")
    l= Label(root,text='What is the text to be decoded?')
    global inputtxt
    inputtxt = scrolledtext.ScrolledText(root,wrap = tkinter.WORD,width = 25, height = 8, font = ("Times New Roman", 15))
    global outputttxt
    outputttxt=scrolledtext.ScrolledText(root,wrap=tkinter.WORD,width=25,height=8,font=("Times New Roman",15))
    butt= Button(root,text='Decode',command=lambda:sussybaka())
    l.pack()
    inputtxt.pack()
    butt.pack()
    outputttxt.pack()
    root.mainloop()
def sussybaka():
    text=inputtxt.get("1.0","end-1c")
    coder2= {"Z": "A", "M":"B", "O":"C", "T":"D", "7":"E", "8":"F", "1":"G", "S":"H", "P":"I", "Q":"J", "4":"K", "2":"L", "R":"M", "N":"N", "5":"O", "V":"P","C":"Q","3":"R","6":"S","9":"T","D":"U","G":"V","K":"W","A":"X","U":"Y","W":"Z","0":" "
             ,"z":"a","m":"b","o":"c","t":"d","!":"e","@":"f","*":"g","s":"h","p":"i","q":"j","#":"k","$":"l","r":"m","n":"n","%":"o","v":"p","c":"q","^":"r","&":"s","(":"t","d":"u","g":"v","k":"w","a":"x","u":"y","w":"z","[":"1","]":"2","|":"3",
             ":":"4",";":"5","<":"6",".":"7",",":"8","?":"9","/":"10","+":"0","』":"!","©":"@","®":"#","™":"$","℠":"%","℡":"^","℗":"&","‱":"*","№":"(","℀":")","℁":"{","℅":"[","℆":"]","⅍":"}","☊":"/","☎":":","☏":";","⌨":"'","✂":",","✆":"<","✇":">","✈":".","✉":"?"
             ,"¢":"-","ƒ":"_","€":"+","௹":"=","฿":"~","♚":"\n"}
    decode_text=""
    for i in text:
        decode_text+= coder2[i]
    outputttxt.insert(1.0,decode_text)
root= Tk()
root.geometry("200x200")
lab=Label(root,text='What do you want to do?')
btn = Button(root, text = 'Encode', command = encode)
btn2= Button(root, text='Decode',command= decode)
lab.pack()
btn.pack()
btn2.pack()
root.mainloop()
