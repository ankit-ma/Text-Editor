from tkinter import *
from tkinter import filedialog
from tkinter import font

root = Tk()
root.title("Text editor")
root.geometry("1001x500")
root.maxsize(1001,500)
root.minsize(1001,500)
#global variable for open file status
global openfile_status
openfile_status = False

#global selected variable
global selected 
selected=False
global fontSize
fontSize = 16

#crete new file function
def new_file():
    
    mytext.delete("1.0",END) #dlelete text editor
    root.title("New file - Text editor")
    status_bar.config(text="New file")
    # when we work on new file then the openfile satus should be changed to false for save feature otherwise save feature remmenber it as old open file
    global openfile_status
    openfile_status = False


#Open file funtion
def open_file():
    mytext.delete("1.0",END)
    #open file dialoge
    text_file = filedialog.askopenfilename(initialdir="/Users/ankitsharma/Desktop/java code/python code/voice assistant/text editor",title="Open file",filetypes=(("Text Files","*.txt"),("HTML file","*.html"),("Python file","*.py"),("All file","*.*")))
    #check to see if there is any file name "It will be used in save_file function"
    if text_file:
        #make file name global to avil in other functions
        global openfile_status
        openfile_status = text_file
    
    #update status bar
    name = text_file
    status_bar.config(text= f'{name}          ')
    name=name.replace("/Users/ankitsharma/Desktop/java code/python code/voice assistant/text editor","")
    root.title(f'{name}       - TextPad!')

    #open file
    text_file=open(text_file,'r')
    temp = text_file.read()
    mytext.insert(END,temp)
    text_file.close()

#save as file function
def save_as_file():
    text_file = filedialog.asksaveasfilename(defaultextension=".*", initialdir="/Users/ankitsharma/Desktop/java code/python code/voice assistant/text editor",title="Save file",filetypes=(("Text Files","*.txt"),("HTML file","*.html"),("Python file","*.py"),("All file","*.*")))
    #if we cancel then it dows not work so let give condition here
    if text_file:
        #update status bar
        name = text_file
        status_bar.config(text= f'Saved : {name}          ')
        name=name.replace("/Users/ankitsharma/Desktop/java code/python code/voice assistant/text editor","")
        root.title(f'{name}    - TextPad!')
        #save file
        text_file = open(text_file,'w')
        text_file.write(mytext.get(1.0,END))
        #close file
        text_file.close()

#save file function
def save_file():
    global openfile_status
    #if the file is already existing file then just overwrite the changes made in the file using fie wirte technique
    if openfile_status:
        #save file
        text_file = open(openfile_status,'w') #open file in wrie mode
        text_file.write(mytext.get(1.0,END))# write the mytext content in opend file
        #close file
        text_file.close() #close the file
        #updates the status bar for user and popup
        status_bar.config(text= f'Saved : {openfile_status}          ') 

    #else use 'save as' because it is like first time savig any file 
    else:
        save_as_file()

#cut function
def cut_function(e):
    global selected
    #check to see if keyboard shirtcut is slected
    if e:
        selected = root.clipboard_get()
    else:
        if mytext.selection_get():
            #grab selected text from text box
            selected = mytext.selection_get()
            #delete selected text
            mytext.delete("sel.first","sel.last")
            root.clipboard_clear()
            root.clipboard_append(selected)

#copy function
def copy_function(e):
    global selected
    if e:
        selected = root.clipboard_get()
    
    if mytext.selection_get():
    #grab selected text from text box
        selected = mytext.selection_get()
        root.clipboard_clear()
        root.clipboard_append(selected)

#paste function
def paste_function(e):
    global selected
    #if there is keybord event
    if e:
        #selected = root.clipboard_get()
        mytext.insert(selected)
    else:    
        if selected:
            position_cursor = mytext.index(INSERT)
            mytext.insert(position_cursor,selected)
# font menu functions   
def american_typewrite():
    global fontSize
    mytext.config(font=("American Typewriter",fontSize))
def helvic():
    global fontSize
    mytext.config(font=("Helvitica",fontSize))
def arial():
    global fontSize
    mytext.config(font=("Arial Black",fontSize))
def baskerville():
    global fontSize
    mytext.config(font=("Baskerville Old Face",fontSize))


# background change menu function
def oldyellow():
    mytext.config(background="#FBF2AD")
def mintblue():
    mytext.config(background="#70E4EC")  
def coolgreen():
    mytext.config(background="#DAF7A6")    
def brillentviolet():
    mytext.config(background="#D586F1")    


#create main frame
myframe = Frame(root)
myframe.pack(pady=5)

#create scroll bar for text box
text_scroll = Scrollbar(myframe)
text_scroll.pack(side=RIGHT,fill=Y)

#create x scroll bar
horizontal_scroll = Scrollbar(myframe,orient="horizontal")
horizontal_scroll.pack(side=BOTTOM,fill=X)
#create text box
mytext = Text(myframe,width=97,height =25,background="#FBF2AD",font=("Helvitica",fontSize),border=1,selectbackground="#E3F990",selectforeground="#A11305",undo = True,yscrollcommand=text_scroll,wrap="none",xscrollcommand=horizontal_scroll.set)
mytext.pack()

#Configure our scroll bar
text_scroll.config(command = mytext.yview)
#configure our horizontal scroll
horizontal_scroll.config(command=mytext.xview)
#Create menu
menu_bar = Menu(root)
root.config(menu=menu_bar)

#add file menu
file_menu =Menu(menu_bar)
menu_bar.add_cascade(label="File",menu=file_menu)
file_menu.add_command(label="New",command=new_file)
file_menu.add_command(label="Open",command=open_file)
file_menu.add_command(label="Save",command = save_file)
file_menu.add_command(label="Save As",command=save_as_file)

file_menu.add_separator()
file_menu.add_command(label="Exit",command=root.quit)

#add edit menu
edit_menu =Menu(menu_bar)
menu_bar.add_cascade(label="Edit",menu=edit_menu)
edit_menu.add_command(label="cut   (cmd+x)",command=lambda:cut_function(False))
edit_menu.add_command(label="copy  (cmd+c)",command=lambda:copy_function(False))
edit_menu.add_command(label="paste (cmd+v)",command=lambda:paste_function(False))
edit_menu.add_separator()
edit_menu.add_command(label="Undo",command= mytext.edit_undo,accelerator='(Meta_L + z)')
edit_menu.add_command(label="Redo",command=mytext.edit_redo,accelerator="(Meta_L + y)")

#view menu
view_menu = Menu(menu_bar)
menu_bar.add_cascade(label="View",menu=view_menu)
#cascade menu for font
fontmenu = Menu(view_menu)
view_menu.add_cascade(label="Font",menu=fontmenu)
fontmenu.add_command(label="American Typewriter",command= american_typewrite)
fontmenu.add_command(label="Helvitica",command= helvic)
fontmenu.add_command(label="Arial Black",command= arial)
fontmenu.add_command(label="Baskerville Old Face",command= baskerville)
#cascade menu for background color
bgmenu = Menu(view_menu)
view_menu.add_cascade(label="Background Color",menu=bgmenu)
bgmenu.add_command(label="Old Yellow",command=oldyellow)
bgmenu.add_command(label="Mint Blue",command=mintblue)
bgmenu.add_command(label="cool Green",command=coolgreen)
bgmenu.add_command(label="Brillient Violet",command=brillentviolet)



#status bar
status_bar = Label(root,text="Ready          ",anchor=E)
status_bar.pack(fill=X,side=BOTTOM,ipady=5)

#Edit bindings 
root.bind('<Meta_L><x>',cut_function)
root.bind('<Meta_L><c>',copy_function)
root.bind('<Meta_L><v>',paste_function)
root.mainloop()