from tkinter import *
from orders import *
from PIL import ImageTk, Image
root = Tk()
def send():
    send = "You:"+ e.get()
    text.insert(END,"\n" + send)
    if(e.get()=='hi'):
        text.insert(END, "\n" + """Bot: hello how can i help you today
                                        """)
    elif (e.get() == 'Is there any particular opening and closing hours for police stations?'):
        text.insert(END, "\n" + """The basic functional unit of police is police station, which is open for 24 X 7 hour for hearing your voice. """)   
    elif (e.get() == 'What is an FIR?'):
        text.insert(END, "\n" + """FIR stands for First Information Report which is defined U/S 154 Cr.PC. Whenever
anybody reports about any crime which discloses cognizable offence then information is
entered into the general or station diary according to Rule 53 of Assam Police Manual
Part V in Form No. 135 of Schedule XL(A), Part I is prescribed in Section 44 of the
Police Act (Act V of 1861). It is the right of complainant to get an FIR registered if his
complaint discloses any cognizable offence. It is the right of the complainant to get one
copy of FIR free of cost, immediately from concerned police station. FIR can be
registered either on written statement or verbal statement of complainant which is later
reduced in writing by Police Officer and is signed by the complainant. """)   
    
    elif (e.get() == """What are cognizable and non-cognizable offences? """):
        text.insert(END, "\n" + """Cognizable offence :- An offence for which a police officer has the powers to arrest
without a warrant is defined as a cognizable offence. Offences like murder, rape,
kidnapping, theft, robbery, fraud etc. are classified as cognizable. To get detailed list of
cognizable offence kindly refer to first schedule of Criminal Procedure Code. Non
cognizable offence :- An offence for which a police officer does not have the power to
arrest the accused without warrant. To get detailed list of non-cognizable offences please
refer to first schedule of Criminal Procedure Code. 
""")  
    
        a=e.get()
        a=None
        text.insert(END, "\n" + "enter choice")
        choice=e.get()
        print(choice)
        e.delete(0,END)
        text.insert(END, "\n" + "enter quantity")
        quantity=e.get() 
        print(quantity)
        menu(choice,quantity)     
        
text = Text(root,bg='white')
text.grid(row=0,column=0,columnspan=2)
e = Entry(root,width=80)
send = Button(root,text='Send',bg='turquoise',width=20,command=send).grid(row=1,column=1)
e.grid(row=1,column=0)
root.title('Say Hi!')
root.geometry("650x400")
root.mainloop()



        
        
        
        
    
