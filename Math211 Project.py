import turtle
import tkinter as tk
import numpy as np
import operator
import re
from time import sleep
# NO more nested brackets, soo be happy man. you seem to lose alot of fatih when facced with calamty, but i want you to know 

# that you are the srtongest currently in your entier life,
#and that as much as it seems impossible, you can do it.
#Note: 1-create sectonier that sorts the equations by nesting in a list that could be passed to the turtles that would pass it
#        calculator calss.
# You got this, i know you scared, but you pulled alot before. i AM WITH  YOU and GOD IS too. Dont worry
#      2-create turtle for each column, and use the bits class to return the turtle's next drawing depending on the equation given
#      3-create bits class where we craete bitwise operations that take bits and returns output  

#Accepted Opertaions: 
# v (OR)
# ^ (AND)
# ~ (NOT)
# o (XOR)
# > (Implies)
# $ (Biconditional)
#--------------------------------------------------------------------------------------------------
def change_draw(turt,cont,name,pos,heading):
    turt.setpos(pos)
    turt.write(name,font=("Helvetica", 20, "bold"), align="center")
    turt.setheading(heading)        
    turt.forward(25)
    for i in cont:
        if i=='True':
            turt.color('green')
            turt.write(1,font=("Helvetica", 16, "normal"), align="center")
        else:
            turt.color('red')
            turt.write(0,font=("Helvetica", 16, "normal"), align="center")
        turt.forward(25)
    turt.color('black')
   # self.turt_truth,i,pow(2*len(self.varis)),1      
#--------------------------------------------------------------------------------------------------
class calc():
    def bit_not(l1):
        l2=[]
        for i in l1:
            l2.append(not i)
        return(l2)
#--------------------------------------------------------------------------------------------------
# pvpvpv(pvp)
# (pv(pvp))v((pvp)v(pvp))

#groups by sections to calcuate correclty
def sectioner(cont,table_dic,size):
 
    in_l=cont[:]
    print(in_l)
    sections={'':[bool(),[]]}
    for i in range(len(in_l)):
        if in_l[i]=='~':
            sections[f'~{in_l[i+1]}']=[0,[]]
            for g in range(size):
                sections[f'~{in_l[i+1]}'][1].append(calc.bit_not(table_dic[f'{in_l[g+1]}']))
    
    print(sections)
    return(sections)
#--------------------------------------------------------------------------------------------------

def grombat(equ_raw):
    # Check for Correct entry-----------
    equ_raw=equ_raw.lower()
    equ_l=list(equ_raw)
    #basic vars to check for validity
    correct_entries=['v','^','~','o','>','$','p','q','r','s']
    letters=['p','q','r','s']
    operands=['v','^','o','>','$']
    try:
        while equ_l.count(' '):
            equ_l.remove(' ')
    except:
        pass
    
    if len(equ_l)==1:
        pass
    #check if all entries are correct chars, test 1
    for i in equ_l:
        if i not in correct_entries:
            return(False,"Only type the showen Chars!")
        
    #check if the first and the last indices are not operands, test 3
    if (equ_l[0] in operands) or (equ_l[-1] in operands):
        return(False,"You can't end or begin an equation with an operator\nStart and end with a variable")
  
    #check if the input is written correclety, test 4
    if len(equ_l)>1:
        bitmap=[]
        for i in equ_l:
            if i in letters:
                bitmap.append(1)
            else:
                bitmap.append(0)
        for i in range(len(bitmap)-1):
            if bitmap[i]+bitmap[i+1]>1:
                return(False,"You can't have two consecutive variables or operators\nEX: PQ or ^>")
    #check if every Not symbol ~ is placed correctly, test 6
    for i in range(len(equ_l)):
        if (equ_l[i]=='~') and (equ_l[i+1] in operands):
            return(False,"You have incorreclty used the 'not'(~) operator\nMake sure each ~ has its corresponding variable")    
    # Sort the list into sections-----------
    return(equ_l,'')
#--------------------------------------------------------------------------------------------------
class SampleApp(tk.Tk):
    global truth_ref
    def __init__(self,*args,**kwargs):
        tk.Tk.__init__(self,*args,**kwargs)
        self.geometry(f'{1200}x{900}+10+10')
        #stacker of pages
        stacker=tk.Frame(self)
        stacker.pack(side="top",fill='both',expand=True)
        #change stacker row and column sizes
        stacker.grid_rowconfigure(0,weight=1)
        stacker.grid_columnconfigure(0,weight=1)
        self.frames={}
        for i in (startpage,truth,inference):
            page_name=i.__name__
            frame= i(stacker,self,bg='#050045')
            self.frames[page_name]= frame
            frame.grid(row=0,column=0,sticky='nsew')
          #put all the pages in the same location
        self.show_frame("startpage")
      
    def show_frame(self,page_name):
        frame=self.frames[page_name]
        frame.tkraise()
    
class startpage(tk.Frame):
    def __init__(self, parent, stacker,bg=None,fg=None):
        tk.Frame.__init__(self, parent,bg=bg,fg=fg)
    
        self.stacker = stacker 
        go_truth=tk.Button(self,height = 2,text=('Truth Table Drawer + Equivlence Check'),font=('Helvetica',20,'bold'),
                           command=lambda: stacker.show_frame('truth'),bg="#050045",fg="white",activeforeground="#050069")
        go_infrence=tk.Button(self,height = 2 ,text=('Infrence Ruels Vizuilizer'),font=('Helvetica',20,'bold'),
                              command=lambda: stacker.show_frame('inference'),bg="#050045",fg="white",activeforeground="#050069")
        go_truth.place(x=150,y=170)
        go_infrence.place(x=150,y=50)
   
class truth(tk.Frame):
    def __init__(self, parent, stacker,bg=None,fg=None):
        tk.Frame.__init__(self, parent,bg=bg,fg=fg)
        self.stacker = stacker 
        self.parent=parent
        #Turtle initilize
        self.canvas = tk.Canvas(self)
        self.canvas.config(width=1160, height=450)
        self.canvas.place(x=20,y=250)
        self.screen = turtle.TurtleScreen(self.canvas)    
        self.screen.colormode('#ebebeb')
        self.turt_truth = turtle.RawTurtle(self.canvas)
        #the equations vars
         
        #draw line
        draw_btn=tk.Button(self,text="draw",command= lambda:truth.draw(self))
        draw_btn.pack(side='top',pady=20)   
        #error visor
        self.error_visor=tk.Label(self ,width=60,height=4,text=(""),font=('Helvetica',12,'bold'),bg="#02002b",fg="white")
        self.error_visor.pack(side='top',pady=20)    
        #go back button
        go_back=tk.Button(self,height = 1 ,text=('Back'),font=('Helvetica',16,'bold'),
                              command=lambda: stacker.show_frame('startpage'),bg="#050045",fg="white",activeforeground="#050069")
        go_back.place(x=1700,y=650,anchor='w')
        #equation entry button
        self.eqt_entry_box=tk.Entry(self,font=("Times",20),width=50)
        self.eqt_entry_box.pack(side='top',pady=20)
        #place(x=250,y=160)
        #info label
        info_entry=tk.Label(self ,text=("Accepted Opertaions:\nv (OR)\n^ (AND)\n~ (NOT)\no (XOR)\n> (Implies)\n$ (Biconditional)"),font=('Helvetica',12,'bold'),bg="#02002b",fg="white")
        info_entry.place(x=15,y=15)
    
        info_entry=tk.Label(self ,text=("Accepted letter variables:\np , q , r , s"),font=('Helvetica',12,'bold'),bg="#02002b",fg="white")
        info_entry.place(x=200,y=15)
        
    
        #enter button
      #  enter_btn=tk.Button(self,text="Press",command= lambda: truth.enter(self))
      #  enter_btn.pack()
    
        
    def error_visor(self,display):
        self.error_visor.config(text=display)
    def create_table(varis):
        table_library={}
        count=1
        start=1         
        for i in varis:
            alter=True           
            table_library[f'{i}']=[]            
            for g in range(pow(2,len(varis))):
                if alter: 
                    table_library[f'{i}'].append('False')
                else:
                    table_library[f'{i}'].append('True')
                count-=1
                if count==0:
                    alter= not alter
                    count=start
            count=start*2
            start=count
        return(table_library)
    def draw(self): 
        x=self.eqt_entry_box.get()
        if self.eqt_entry_box.get()=='':
            truth.error_visor(self,"The entry box is empty")
            return()
        package,stat= grombat(self.eqt_entry_box.get())
        # used to call the wrong input handler with the specific message
        truth.error_visor(self,stat)
        if stat:
            return()
        # -----
        self.eqt_entry_box.delete(0,tk.END)
        self.varis=[]
        if 'p' in x:
            self.varis.append('p')
        if 'q' in x:
            self.varis.append('q')
        if 'r' in x:
            self.varis.append('r')
        if 's' in x:
            self.varis.append('s')
        self.turt_truth.penup()
        #self.turt_truth.hideturtle()
        self.turt_truth.setpos(0,0)    
        table_dic=truth.create_table(self.varis)
        start_pos=[-530,200]
        for i,g in table_dic.items():
            change_draw(turt=self.turt_truth,name=i,cont=g,pos=start_pos,heading=-90)
            start_pos[0]=start_pos[0]+65
        
        sections=sectioner(cont=package,table_dic=table_dic,size=pow(2,len(self.varis)))
         
        self.turt_truth.setpos(0,0)
        self.turt_truth.write(package, True,font=("Helvetica", 20, "normal"), align="center")
        
class inference(tk.Frame):
    def __init__(self, parent, stacker,bg=None,fg=None):
        tk.Frame.__init__(self, parent,bg=bg,fg=fg)
        self.stacker = stacker 
    
        go_back=tk.Button(self,height = 1 ,text=('Back'),font=('Helvetica',16,'bold'),
                          command=lambda: stacker.show_frame('startpage'),bg="#050045",fg="white",activeforeground="#050069")
        go_back.place(x=900,y=600)

    
#main = turtle.Turtle()
##main.write("P", True,font=("Helvetica", 24, "normal"), align="center")
#main.penup()
#main.setpos((-100,50))
##main.pendown()
##main.forward(100)
#turtle.done()
if __name__ == "__main__":
  #driver
    app = SampleApp()  
    app.mainloop()