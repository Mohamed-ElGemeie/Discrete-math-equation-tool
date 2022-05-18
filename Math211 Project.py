import turtle
import tkinter as tk
from collections import OrderedDict

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
#--------------------------------------------------------------------------------------------------
class calc():
    def bit_not(l1):
        l2=[]
        for i in l1:
            if i=='True':
                l2.append('False')
            else:
                l2.append('True')
        return(l2)
    def bit_and(l1,l2):
        l3=[]
        for (i,g) in zip(l1,l2):
            if i=='True' and g=='True':
                l3.append('True')
            else:
                l3.append('False')
        return(l3)
    def bit_or(l1,l2):
        l3=[]
        for(i,g)in zip(l1,l2):
            if i=='False' and g=="False":
                l3.append('False')
            else:
                l3.append('True')
        return(l3)
    def bit_imply(l1,l2):
        l3=[]
        for(i,g)in zip(l1,l2):
            if i=='True' and g=="False":
                l3.append('False')
            else:
                l3.append('True')
        return(l3)
    def bit_bicond(l1,l2,same):
        l3=[]
        if same:
            for (i,g) in zip(l1,l2):
                if i ==g:
                    l3.append('True')
                else:
                    l3.append('False')
        else:
            for (i,g) in zip(l1,l2):
                if i !=g:
                    l3.append('True')
                else:
                    l3.append('False')
        return(l3)
#--------------------------------------------------------------------------------------------------

#groups by sections to calcuate correclty
def sectioner(cont,table_dic,size):
    in_l=cont[:]
    sections={}
    order = OrderedDict()
    i=0
    while i<len(in_l):
        if in_l[i]=='~':
            name=f'~{in_l[i+1]}'
            sections[name]=[True,calc.bit_not(table_dic[in_l[i+1]])]
            table_dic[name]=calc.bit_not(table_dic[in_l[i+1]])
            order[name]=calc.bit_not(table_dic[in_l[i+1]])
            in_l.pop(i+1)
            in_l.pop(i)
            in_l.insert(i,name)
            i-=1
        i+=1
    #master loop on all operators
    i=0 
    while i< len(in_l):
        #------------------ and
        if in_l[i]=='^':
            name=f'{in_l[i-1]}^{in_l[i+1]}'
            sections[name]=[True,calc.bit_and(table_dic[in_l[i-1]],table_dic[in_l[i+1]])]
            table_dic[name]=calc.bit_and(table_dic[in_l[i-1]],table_dic[in_l[i+1]])
            order[name]=calc.bit_and(table_dic[in_l[i-1]],table_dic[in_l[i+1]])
            in_l.pop(i+1)
            in_l.pop(i)
            in_l.pop(i-1)
            in_l.insert(i-1,name)
            i-=1
        #------------------ or
        if in_l[i]=='v':
            name=f'{in_l[i-1]}v{in_l[i+1]}'
            sections[name]=[True,calc.bit_or(table_dic[in_l[i-1]],table_dic[in_l[i+1]])]
            table_dic[name]=calc.bit_or(table_dic[in_l[i-1]],table_dic[in_l[i+1]])
            order[name]=calc.bit_or(table_dic[in_l[i-1]],table_dic[in_l[i+1]])
            in_l.pop(i+1)
            in_l.pop(i)
            in_l.pop(i-1)
            in_l.insert(i-1,name)
            i-=1
        i+=1
    #implies
    i=0
    while i<len(in_l):
        if in_l[i]=='>':
            name=f'{in_l[i-1]}>{in_l[i+1]}'
            sections[name]=[True,calc.bit_imply(table_dic[in_l[i-1]],table_dic[in_l[i+1]])]
            table_dic[name]=calc.bit_imply(table_dic[in_l[i-1]],table_dic[in_l[i+1]])
            order[name]=calc.bit_imply(table_dic[in_l[i-1]],table_dic[in_l[i+1]])
            in_l.pop(i+1)
            in_l.pop(i)
            in_l.pop(i-1)
            in_l.insert(i-1,name)
            i-=1
        i+=1      
    #bi condictional
    i=0    
    while i<len(in_l):
        if in_l[i]=='$':
            name=f'{in_l[i-1]}${in_l[i+1]}'
            sections[name]=[True,calc.bit_bicond(table_dic[in_l[i-1]],table_dic[in_l[i+1]],1)]
            table_dic[name]=calc.bit_bicond(table_dic[in_l[i-1]],table_dic[in_l[i+1]],0)
            order[name]=calc.bit_bicond(table_dic[in_l[i-1]],table_dic[in_l[i+1]],0)
            in_l.pop(i+1)
            in_l.pop(i)
            in_l.pop(i-1)
            in_l.insert(i-1,name)
            i-=1
        i+=1          
    #xor
    i=0
    while i<len(in_l):
        if in_l[i]=='o':
            name=f'{in_l[i-1]}o{in_l[i+1]}'
            sections[name]=[True,calc.bit_bicond(table_dic[in_l[i-1]],table_dic[in_l[i+1]],0)]
            table_dic[name]=calc.bit_bicond(table_dic[in_l[i-1]],table_dic[in_l[i+1]],0)
            order[name]=calc.bit_bicond(table_dic[in_l[i-1]],table_dic[in_l[i+1]],0)
            in_l.pop(i+1)
            in_l.pop(i)
            in_l.pop(i-1)
            in_l.insert(i-1,name)
            i-=1
        i+=1          
    return(sections,order)

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
        for i in (startpage,truth):
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
        go_truth.place(x=150,y=170)  
   
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
        self.turt_equ=    turtle.RawTurtle(self.canvas)
         
        #draw line
        draw_btn=tk.Button(self,font=15,text="Draw",command= lambda:truth.draw(self))
        draw_btn.pack(side='top',pady=5)   
        #error visor
        self.error_visor=tk.Label(self ,width=80,height=5,text=(""),font=('Helvetica',12,'bold'),bg="#02002b",fg="white")
        self.error_visor.pack(side='top',pady=5)    
        self.error_visor.config(text="Insert in only one box for drawing the Truth table\nInsert in both for equivalence checking")
        #go back button
        go_back=tk.Button(self,height = 1 ,text=('Back'),font=('Helvetica',16,'bold'),
                              command=lambda: stacker.show_frame('startpage'),bg="#050045",fg="white",activeforeground="#050069")
        go_back.place(x=1700,y=650,anchor='w')
        #equation entry button
        self.eqt_entry_box1=tk.Entry(self,font=("Times",20),width=50)
        self.eqt_entry_box1.pack(side='top',pady=5)
        self.eqt_entry_box2=tk.Entry(self,font=("Times",20),width=50)
        self.eqt_entry_box2.pack(side='top',pady=5)
    
        #info label
        info_entry=tk.Label(self ,text=("Accepted Opertaions:\nv (OR)\n^ (AND)\n~ (NOT)\no (XOR)\n> (Implies)\n$ (Biconditional)\n\nNo Brackets ()"),font=('Helvetica',12,'bold'),bg="#02002b",fg="white")
        info_entry.place(x=15,y=0)
    
        info_entry=tk.Label(self ,text=("Accepted letter variables:\np , q , r , s"),font=('Helvetica',12,'bold'),bg="#02002b",fg="white")
        info_entry.place(x=200,y=0)
        #bind the entry box with enter key press
        self.eqt_entry_box1.bind('<Return>',lambda x:truth.draw(self))
        self.eqt_entry_box2.bind('<Return>',lambda x:truth.draw(self))
        
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
    def equivalence(self):
        x1=self.eqt_entry_box1.get()
        x2=self.eqt_entry_box2.get()
        package1,stat1= grombat(x1)
        package2,stat2= grombat(x2)
        # used to call the wrong input handler with the specific message
        if stat1 or stat2:
            truth.error_visor(self,f"EQU1:{stat1}\nEQU2:{stat2}")
            return()
        # -----
        self.eqt_entry_box1.delete(0,tk.END)
        self.eqt_entry_box2.delete(0,tk.END)
        self.varis1=[]
        self.varis2=[]
        for i in ['p','q','r','s']:
            if i in x1:
                self.varis1.append(i)
            if i in x2:
                self.varis2.append(i)
        self.turt_truth.penup()
        self.turt_equ.penup()

        self.turt_truth.setpos(0,0)
        self.turt_equ.setpos(0,0)    
        table_dic1=truth.create_table(self.varis1)
        table_dic2=truth.create_table(self.varis2)
        start_pos1=[-530,190]
        start_pos2=[530,190]
        for i,g in table_dic1.items():
            change_draw(turt=self.turt_truth,name=i,cont=g,pos=start_pos1,heading=-90)
            start_pos1[0]=start_pos1[0]+65
        for i,g in table_dic2.items():
            change_draw(turt=self.turt_equ,name=i,cont=g,pos=start_pos2,heading=-90)
            start_pos2[0]=start_pos2[0]-65
        sections1,last1=sectioner(cont=package1,table_dic=table_dic1,size=pow(2,len(self.varis1)))
        sections2,last2=sectioner(cont=package2,table_dic=table_dic2,size=pow(2,len(self.varis2)))
        last_l1= list(last1.items())
        last_l2= list(last2.items())

        for i,g in sections1.items():
            if g[0]:
                change_draw(turt=self.turt_truth,name=i,cont=g[1],pos=start_pos1,heading=-90)
                start_pos1[0]=start_pos1[0]+30+(len(i)*19)
        for i,g in sections2.items():
            if g[0]:
                change_draw(turt=self.turt_equ,name=i,cont=g[1],pos=start_pos2,heading=-90)
                start_pos2[0]=start_pos2[0]-(30+(len(i)*19))        
        self.turt_truth.setpos(0,0)
        self.turt_equ.setpos(0,0)
        for i,g in zip(last_l1[-1][1],last_l2[-1][1]):
            if i !=g:
                truth.error_visor(self,"These two Equations are Unequivalent")
                return()
        truth.error_visor(self,"These two Equations are Equivalent")
        
    def draw(self): 
        self.turt_truth.clear()
        self.turt_equ.clear()
        truth.error_visor(self,'')
        x=self.eqt_entry_box1.get()
        y=self.eqt_entry_box2.get()
        if x=='' and y=='':
            truth.error_visor(self,"Please fill any of the entry boxes")
            return()
        elif x!='' and y!='':
            truth.equivalence(self)
        else:
            if x=='':
                this_entry=y
            else:
                this_entry=x
            package,stat= grombat(this_entry)
            # used to call the wrong input handler with the specific message
            if stat:
                truth.error_visor(self,stat)
                return()
            # -----
            self.eqt_entry_box1.delete(0,tk.END)
            self.varis=[]
            if 'p' in this_entry:
                self.varis.append('p')
            if 'q' in this_entry:
                self.varis.append('q')
            if 'r' in this_entry:
                self.varis.append('r')
            if 's' in this_entry:
                self.varis.append('s')
            self.turt_truth.penup()
            self.turt_truth.setpos(0,0)    
            table_dic=truth.create_table(self.varis)
            start_pos=[-530,190]
            for i,g in table_dic.items():
                change_draw(turt=self.turt_truth,name=i,cont=g,pos=start_pos,heading=-90)
                start_pos[0]=start_pos[0]+65
            
            sections,last=sectioner(cont=package,table_dic=table_dic,size=pow(2,len(self.varis)))

            for i,g in sections.items():
                if g[0]:
                    change_draw(turt=self.turt_truth,name=i,cont=g[1],pos=start_pos,heading=-90)
                    start_pos[0]=start_pos[0]+20+(len(i)*18)
            self.turt_truth.setpos(0,0)
 
if __name__ == "__main__":
  #driver
    app = SampleApp()  
    app.mainloop()
# This project was made by Mohamed Galal ElGemeie 202000206
# All rights reserved to the user https://github.com/Mohamed-ElGemeie
