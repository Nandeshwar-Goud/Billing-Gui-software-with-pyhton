from tkinter import * 
import getpass
from tkinter import ttk
from tkinter import messagebox
from tkinter import Tk
import os
import sys

import calendar
import datetime as dt

import math, random



def loo():
    font_all = "times new romen"
    bg_color="RoyalBlue1"







    def clear_btn_fun():
        custname.set("")
        blackp.set(0)
        twoside.set(0)
        colourp.set(0)
        mahap.set(0)
        TGbp.set(0)
        photos4p.set(0)
        groupp.set(0)
        CheckVar1.set(0)
        CheckVar2.set(0)
        totalp4.set("")
        totalpg.set("")
        totalblackp.set("")
        totalcolourp.set("")
        totalmahabankp.set("")
        totaltgbp.set("")
        grandtotal.set("")
        totaltwo.set("")
        grandtotal.set("")
        otherprv.set(0)
        other_inpuhh.set("")



    def bill_rescipy():
    
        text1.delete('1.0',END)
        text1.insert(END,"\t!Thank you for visiting! \n \tcyber world xerox center")
        text1.insert(END,f"\n\nBill__Number:{billname.get()}" )
        text1.insert(END,f"\nCustomer_Name:{custname.get()}" )
        text1.insert(END,f"\nDATE:{datename.get()}" )
        text1.insert(END,"\n\n***************************************")
        
        text1.insert(END,"\nProducts\t\t   QTY\t\t  Price")
        text1.insert(END,"\n***************************************")


    def bill__savefunpaid():

        
        
        
        
        
        if custname.get() !="":

           

                if CheckVar1.get() == 1:

                    ask=messagebox.askyesno("Bill Notice","Do You Want To Save The Bill?")
                    if ask>0:
                        billd=text1.get('1.0',END)
                        bi=open("Bills/paid/"+str(custname.get())+str(f"{date:%d.%b.%Y}")+".txt","w")
                        bi.write(billd)
                        bi.close()
                    else:
                        return

                if CheckVar2.get() == 1:
                    ask=messagebox.askyesno("Bill Notice","Do You Want To Save The Bill?")
                    if ask>0:
                        billd=text1.get('1.0',END)
                        bi=open("Bills/not paid/"+str(custname.get())+str(f"{date:%d.%b.%Y}")+".txt","w")
                        bi.write(billd)
                        bi.close()
                    else:
                        return
        

    
        
        

            

        
    
    def nandu_toallaall():
        #input 
        photostotal= photos4p.get() * 40
        groupu=groupp.get() * 60
        blackpaper=blackp.get() *3
        colourpaper=colourp.get() * 10
        mahabankpaper=mahap.get()*50
        tgbpaper=TGbp.get()*40
        twopaper= twoside.get()*4
        otherpap= otherprv.get()
        #total print
        totalp4.set(str(photostotal))
        totalpg.set(str(groupu))
        totalblackp.set(str(blackpaper))
        totalcolourp.set(str(colourpaper))
        totalmahabankp.set(str(mahabankpaper))
        totaltgbp.set(str(tgbpaper))
        
        totaltwo.set(str(twopaper))
        grandtotal.set("Rs. "+str(
            (photostotal) +
            (groupu)+
            (blackpaper)+
            (colourpaper)+
            (mahabankpaper)+
            (tgbpaper)+
            (twopaper)+
            (otherpap)
            )
            
        
        
        
        )
    
    
    
    def all_fun():
        bill_rescipy()
        if blackp.get() !=0:

            text1.insert(END,f"\n.Black &\n White Xerox\t\t  {blackp.get()}\t\t  {totalblackp.get()}")

        if twoside.get()!=0:
            text1.insert(END,f"\nTwo side \n xeroxs\t\t  {twoside.get()}\t\t  {totaltwo.get()}")




        if colourp.get() !=0:
            text1.insert(END,f"\n.Colour Xeroxs\t\t  {colourp.get()}\t\t  {totalcolourp.get()}")

        if mahap.get() !=0:
            text1.insert(END,f"\n.mahabank Doc\t\t  {mahap.get()}\t\t  {totalmahabankp.get()}")
        
        if TGbp.get() !=0:
            text1.insert(END,f"\n.TGB Doc\t\t  {TGbp.get()}\t\t  {totaltgbp.get()}")
    
        if photos4p.get() !=0:
            text1.insert(END,f"\n.passport size \n   photos\t\t  {photos4p.get()}\t\t  {totalp4.get()}")
    
        if groupp.get() !=0:
            text1.insert(END,f"\n.Group photos \t\t  {groupp.get()}\t\t  {totalpg.get()}")


        if otherprv.get() !=0:
            text1.insert(END,f"\n.{other_inpuhh.get()}\t\t                 {other_pr.get()}          ")

        if grandtotal.get() !=0:
            text1.insert(END,f"\n=======================================\nTOTAL BILL :\t\t\t       {grandtotal.get()}")
    
        if CheckVar1.get() !=0 and CheckVar2.get()==0:

            text1.insert(END,"\n Paid")
            bill__savefunpaid()
            
        if CheckVar2.get() ==1 and CheckVar1.get() !=1:
            text1.insert(END,"\n Not Paid")
            bill__savefunpaid()


        if custname.get() == "":
            messagebox.showinfo("emply filles","Please fill customer name\n Thankyou")    



        if CheckVar1.get() ==1 and CheckVar2.get() ==1:
            messagebox.showwarning("warn","Only select paid or not paid\n In payment section")

        if CheckVar1.get() == 0 and CheckVar2.get() ==0:
            messagebox.showwarning("check filleds","please select payment status \n If Customer paid check the paid column\nIf customer not paid check not paid column ")
        

        billname.set("")
        r=random.randint(10000,77777)
        billname.set(str(r))
            
    
    
    
    
    
    window.title("Indus Hackerz Billing software")
    
    title=Label(window,text="Indus Hackerz Billing software ",bd=5 ,relief=GROOVE, bg=bg_color,fg="green2",font=(font_all,25,"bold"),pady=3)
    title.place(x=0,y=65,relwidth=1)

     #customer name

    
    custname=StringVar()


    date = dt.datetime.now()

    format_date = f"{date:%d/%b/%Y}" 


    datename=StringVar()
    datename.set(str(format_date))
    billname=StringVar()
    r=random.randint(10000,77777)
    billname.set(str(r))
    
    
 

   




    #******************************frame customer and date***********************************
    frame1 = LabelFrame(window,text="Customer Details",font=(font_all,10,"bold"),fg="gold",bg=bg_color,relief=GROOVE,bd=5)
    frame1.place(x=0,y=120,relwidth=1)
    #customer name label
    cgold=Label(frame1,text="Customer Name :-",font=("times new romen",15,"bold"),fg="green2",bg=bg_color).grid(row=0,column=0)
    
    #custmer name input box
    cgold_in=Entry(frame1,width=20,textvariable=custname,font="arial",bd=2).grid(row=0,column=1,pady=5,padx=10)

    #date label
    
    #date = dt.datetime.now()

    #format_date = f"{date: %d/%b/%Y}"

    




    d_lbl= Label(frame1,text="Date :-",font=(font_all,16,"bold"),fg="green2",bg=bg_color)
    d_lbl.grid(row=0,column=2,pady=5,padx=10)
    
    #date input box
    d_btn=Entry(frame1,width=20,textvariable=datename,font="arial",bd=2,)
    d_btn.grid(row=0,column=3,pady=5,padx=10)
    #Bill nunber
    bil_n= Label(frame1,text="Bill NO.:-",font=(font_all,16,"bold"),fg="green2",bg=bg_color)
    bil_n.grid(row=0,column=4,pady=5,padx=10)

    bil_i=Entry(frame1,width=20,textvariable=billname,font="arial",bd=2,)
    bil_i.grid(row=0,column=5,pady=5,padx=10)
    #search button


    

    #***************************************xerox frame****************************************
    xeroxframe= LabelFrame(window,text="Xerox papers",font=(font_all,10,"bold"),fg="gold",bg=bg_color,relief=GROOVE,bd=5)
    xeroxframe.place(x=0,y=200,width=300,height=200)
    
    #black paper 
    blk_lbl=Label(xeroxframe,text="Black & White xerox :-",font=("arial",12,"bold"),fg="green2",bg=bg_color)
    blk_lbl.grid(row=0,column=0,pady=5,padx=5)

    blackp=IntVar()

    

    #black paper input
    blk_inp=Entry(xeroxframe,width=8,textvariable=blackp,font=("arial",12,"bold"))
    blk_inp.grid(row=0,column=1,pady=2,padx=4)
    #two side xerox

    
    twoside2_lbl=Label(xeroxframe,text="Two side xeroxs :-",font=("arial",12,"bold"),fg="green2",bg=bg_color)
    twoside2_lbl.grid(row=1,column=0,pady=2,padx=4)
    twoside=IntVar()

    twoide2_ety=Entry(xeroxframe,width=8,textvariable=twoside,font=("arial",12,"bold"))
    twoide2_ety.grid(row=1,column=1,pady=5,padx=5)
    #colour xerox 
    clr_lbl = Label(xeroxframe,bd=0,text="colour xeroxs :-",font=("arial",12,"bold"),fg="green2",bg=bg_color)
    clr_lbl.grid(row=2,column=0,pady=5,padx=5)
    
    #colour xerox input
    colourp=IntVar()

    clr_inp=Entry(xeroxframe,textvariable=colourp,width=8,font=("arial",12,"bold"))
    clr_inp.grid(row=2,column=1,pady=5,padx=5)
    
    #maha bank doc
    maha_lbl=Label(xeroxframe,text="Maha Bank Doc :-",font=("arial",12,"bold"),fg="green2",bg=bg_color)
    maha_lbl.grid(row=4,column=0,pady=5,padx=5)

    mahap=IntVar()

    maha_inp=Entry(xeroxframe,textvariable=mahap,width=8,font=("arial",12,"bold"))
    maha_inp.grid(row=4,column=1,pady=5,padx=5)

    #Tgb bank doc
    tgb_lbl=Label(xeroxframe,text="TGB Bank Doc :-",font=("arial",12,"bold"),fg="green2",bg=bg_color)
    tgb_lbl.grid(row=5,column=0,pady=5,padx=5)

    TGbp=IntVar()

    tgb_inp=Entry(xeroxframe,textvariable=TGbp,width=8,font=("arial",12,"bold"))
    tgb_inp.grid(row=5,column=1,pady=5,padx=5)

    #******************photos frame*******************
    pt_frame = LabelFrame(window,text="Photos",font=(font_all,10,"bold"),fg="gold",bg=bg_color,relief=GROOVE,bd=5)
    pt_frame.place(x=300,y=200,width=250,height=200)

    #4phots
    pt_4= Label(pt_frame,text="4 Photos :-",font=("arial",12,"bold"),fg="green2",bg=bg_color)
    pt_4.grid(row=0,column=0,pady=5,padx=5)

    #4phots input 
    photos4p=IntVar()

    pt4_inp=Entry(pt_frame,textvariable=photos4p,width=8,font=("arial",12,"bold"))
    pt4_inp.grid(row=0,column=1,pady=4,padx=5)
    
    otherlbl=Label(pt_frame,text="OTHERS:-",font=("arial",12,"bold"),fg="green2",bg=bg_color).grid(row=3,column=0,pady=1,padx=1)


    other_inpuhh=StringVar()

    other_inpu=Entry(pt_frame,textvariable=other_inpuhh,width=10,font=("arial",12,"bold"))
    other_inpu.grid(row=5,column=0,pady=4,padx=1)

    otherprv=IntVar()

    other_pr=Entry(pt_frame,textvariable=otherprv,width=10,font=("arial",12,"bold"))
    other_pr.grid(row=5,column=1,pady=4,padx=1)

    #group photo

    groupp=IntVar()


    gr_lbl= Label(pt_frame,text="Group photo :-",font=("arial",12,"bold"),fg="green2",bg=bg_color)
    gr_lbl.grid(row=1,column=0,pady=5,padx=5)

    gr_inp=Entry(pt_frame,textvariable=groupp,width=8,font=("arial",12,"bold"))
    gr_inp.grid(row=1,column=1,pady=4,padx=5)

    #***************payment status frame*******************

    pay_frame = LabelFrame(window,bg=bg_color,relief=GROOVE,bd=5)
    pay_frame.place(x=550,y=200,width=250,height=200)

    pay_s=Label(pay_frame,text="  Payment Status ",font=("arial",18,"bold"),fg="green2",bg=bg_color,)
    pay_s.grid(row=0,column=0,pady=5,padx=5)
    
    CheckVar1 = IntVar()
    CheckVar2 = IntVar()
    line_p=Label(pay_frame,text="------------------------------------",font=("arial",14,"bold"),fg="green2",bg=bg_color,).grid(row=1,column=0,pady=0,padx=5)
    
    
    warn_pp=Checkbutton(pay_frame, text = "    Paid", variable = CheckVar1, \
                 onvalue = 1, offvalue = 0,  \
                 bg=bg_color,font=("arial",14,"bold")
                 ).grid(row=2,column=0,pady=1,padx=1)

    warnp2=Checkbutton(pay_frame, text = "Not Paid", variable = CheckVar2, \
                 onvalue = 1, offvalue = 0,  \
                 bg=bg_color,font=("arial",14,"bold")).grid(row=3,column=0,pady=1,padx=1)
    #warn_p=Label(pay_frame,text="paid",font=("arial",14,"bold"),fg="green2",bg=bg_color,).grid(row=2,column=0,pady=5,padx=0)
    #warn_p2=Label(pay_frame,text="Not paid",font=("arial",14,"bold"),fg="green2",bg=bg_color,).grid(row=3,column=0,pady=5,padx=0)
    #warn_inp=Checkbutton(pay_frame,font=("arial",14,"bold"),).grid(row=2,column=1,pady=0,padx=0)

    #**************************Other columns information*********************

    ottt_frame = LabelFrame(window,bg=bg_color,relief=GROOVE,bd=5)
    ottt_frame.place(x=800,y=200,width=200,height=200)

    ott_s=Label(ottt_frame,text="  Others column \ninformation ",font=("arial",16,"bold"),fg="green2",bg=bg_color,)
    ott_s.grid(row=0,column=0,pady=1,padx=1)


    ott_info=Label(ottt_frame,text="please use others column \nfor recharges and etc\nfirst column enter product\n name and in second\n fill the price ",font=("arial",10,"bold"),fg="green2",bg=bg_color,)
    ott_info.grid(row=1,column=0,pady=1,padx=1)

    #***********************Bill Recipt******************************

    bil_rs=Frame(window,bg="white",relief=GROOVE,bd=5)
    bil_rs.place(x=1005,y=200,width=350,height=405)
    
    bill_tt=Label(bil_rs,text="Bill Receipt",font="arial 15 bold",bd=4,relief=GROOVE).pack(fill=X)
    scroll_bar=Scrollbar(bil_rs,orient=VERTICAL)
    text1=Text(bil_rs,yscrollcommand=scroll_bar.set)
    scroll_bar.pack(side=RIGHT,fill=Y)
    scroll_bar.config(command=text1.yview)
    text1.pack()
    #**********************total*************
    totall_rs=LabelFrame(window,text="Total",font=("arial",12,"bold"),fg="gold",bg="RoyalBlue1",relief=GROOVE,bd=5)
    totall_rs.place(x=0,y=405,width=1000,height=200)
    


    #total
    totalp4=StringVar()
    totalpg=StringVar()
    totalblackp=StringVar()
    totalcolourp=StringVar()
    totalmahabankp=StringVar()
    totaltgbp=StringVar()
    grandtotal=StringVar()
    totaltwo=StringVar()

    #total photos 
    pht_tt4=Label(totall_rs,text="TOTAL PHOTOS BILL :-",font=("arial", 12, "bold"),fg="green2",bg=bg_color)
    pht_tt4.grid(row=0,column=2,pady=5,padx=5)

    pht4_inn=Entry(totall_rs,textvariable=totalp4,width=8,font=("arial",12,"bold"))
    pht4_inn.grid(row=0,column=3,pady=4,padx=5)

    pht_ttggg=Label(totall_rs,text="TOTAL GROUP PHOTO BILL :-",font=("arial", 12, "bold"),fg="green2",bg="RoyalBlue1")
    pht_ttggg.grid(row=1,column=2,pady=5,padx=5)

    phtggg_inn=Entry(totall_rs,textvariable=totalpg,width=8,font=("arial",12,"bold"))
    phtggg_inn.grid(row=1,column=3,pady=4,padx=5)

    xerox_lbloo=Label(totall_rs,text="TOTAL BLACK &\n WHITE XEROX :-",font=("arial",12,"bold"),fg="green2",bg="RoyalBlue1")
    xerox_lbloo.grid(row=0,column=0,pady=5,padx=5)

    cerox_inn=Entry(totall_rs,textvariable=totalblackp,width=8,font=("arial",12,"bold"))
    cerox_inn.grid(row=0,column=1,pady=4,padx=5)

    cccerox_lbloo=Label(totall_rs,text="TOTAL COLOUR XEROX :-",font=("arial",12,"bold"),fg="green2",bg="RoyalBlue1")
    cccerox_lbloo.grid(row=1,column=0,pady=5,padx=5)

    ccccerox_inn=Entry(totall_rs,textvariable=totalcolourp,width=8,font=("arial",12,"bold"))
    ccccerox_inn.grid(row=1,column=1,pady=4,padx=5)

    Mahabnn_lbloo=Label(totall_rs,text="TOTAL MAHA BANK DOC :-",font=("arial",12,"bold"),fg="green2",bg="RoyalBlue1")
    Mahabnn_lbloo.grid(row=2,column=2,pady=5,padx=5)
    

    Tgbbbb_lbloo=Label(totall_rs,text="TOTAL TGB BANK DOC :-",font=("arial",12,"bold"),fg="green2",bg="RoyalBlue1")
    Tgbbbb_lbloo.grid(row=2,column=0,pady=5,padx=5)

    mahabnnn_inn=Entry(totall_rs,textvariable=totalmahabankp,width=8,font=("arial",12,"bold"))
    mahabnnn_inn.grid(row=2,column=3,pady=4,padx=5)

    Tgbbb_inn=Entry(totall_rs,textvariable=totaltgbp,width=8,font=("arial",12,"bold"))
    Tgbbb_inn.grid(row=2,column=1,pady=4,padx=5)

    grandtot_lbl=Label(totall_rs,text="GRAND \n TOTAL :-",font=("arial",13,"bold"),fg="green2",bg="RoyalBlue1")
    grandtot_lbl.grid(row=3,column=1,pady=5,padx=5)
    

    grand_inn=Entry(totall_rs,textvariable=grandtotal,width=12,font=("arial",13,"bold"))
    grand_inn.grid(row=3,column=2,pady=4,padx=2)



    allbutns_bb=Frame(totall_rs,bd=5,relief=GROOVE)
    allbutns_bb.place(x=700,y=0,width=285,height=170)
    def nandu():
        askk=messagebox.askyesno("Warning","Please save any Data before exiting!")
        if askk>0:
            window.destroy()

        
        
        



    alltotal_btnn=Button(allbutns_bb,command=nandu_toallaall,text="TOTAL",font=("arial",12,"bold"),fg="black",bg="turquoise1",bd=2,width=10,height=2,cursor="hand2").grid(row=0,column=0,pady=10,padx=5)
    genbill_btnn=Button(allbutns_bb,command=all_fun,text="GENERETE \n BILL",font=("arial",12,"bold"),fg="black",bg="turquoise1",bd=2,width=10,height=2,cursor="hand2").grid(row=0,column=1,pady=10,padx=20)
    clear_btnn=Button(allbutns_bb,command=clear_btn_fun,text="CLEAR",font=("arial",12,"bold"),fg="black",bg="turquoise1",bd=2,width=10,height=2,cursor="hand2").grid(row=1,column=0,pady=10,padx=5)
    exit_btnn=Button(allbutns_bb,text="EXIT",font=("arial",12,"bold"),fg="black",bg="turquoise1",bd=2,width=10,height=2,cursor="hand2",command=nandu).grid(row=1,column=1,pady=10,padx=5)

    bill_rescipy()

    


    
    window.mainloop()





    



window = Tk()


window.geometry("1360x720+0+0")


window.resizable(True, True)
window.state('zoomed')


window.wm_iconbitmap("final.ico")
#photo = PhotoImage(file = "final.ico")
#window.iconphoto(False, photo)


window.title("LOGIN TO ACCESS BILLING SOFTWARE")

#**************************frame for login*******************************

logn_frame = LabelFrame(window,font=("time new romen",10,"bold"),fg="gold",bg="RoyalBlue1",relief=GROOVE,bd=5)
logn_frame.place(x=0,y=0,relwidth=1)


#login here
lll_lbl=Label(logn_frame,text="LOGIN HERE",bg="RoyalBlue1",fg="gold",font=("Helvetica","18","bold"))
lll_lbl.grid(row=0,column=1,pady=6,padx=1)

#username label
user_btn = Label(logn_frame, text="Username :-",borderwidth=2, bg="RoyalBlue1", fg="green2", font=("Helvetica","12","bold"))
user_btn.grid(row=0,column=2,pady=6,padx=5)

#username input
username = Entry(logn_frame, width=20, borderwidth=2 , font=("Helvetica","14"))
username.grid(row=0,column=3,pady=6,padx=5)

#password label
password_btn = Label(logn_frame, text="Password :-",borderwidth=2, bg="RoyalBlue1",fg="green2", font=("Helvetica","12","bold"))
password_btn.grid(row=0, column=4, pady=6,padx=5)


#password input
password =Entry(logn_frame,show='*',width=20,borderwidth=2,font=("Helvetica","14"))
password.grid(row=0,column=5,pady=6)



#login algorithm
def login_button():

    if username.get() == "" or password.get() == "":
        messagebox.showerror("empty blocks error","Please fill the username and password blocks")


    if username.get() == "shop" and password.get() == "admin" :


        succ = Label(logn_frame, text="       Logined with admin rights       ", bg="cyan2", fg="black", font=("Helvetica", "12"))
        succ.grid(row=0, column=9, pady=6, padx=5)

        loo()

    else:
        wrong = Label(logn_frame, text="Invaild! Username or password", bg="red", fg="#fff", font=("Helvetica", "12"))
        wrong.grid(row=0, column=9, pady=6, padx=5)

def forgot_passwordff():
    
    messagebox.showinfo("info","Please check owners google drive for all passwords",parent=logn_frame)

    

    

    


#login button
login_btn = Button(logn_frame, text="LOGIN",cursor="hand2", bg="purple1", fg="black", font=("Helvetica",12), command= login_button)
login_btn.grid(row=0, column=6, pady=6, padx=10)

#forgot button
forgot_btn = Button(logn_frame,text="Forgot Password?",bd=0,cursor="hand2",fg="blue",font=("Helvetica",12,),command=forgot_passwordff)
forgot_btn.grid(row=0,column=7,pady=6,padx=5)





window.mainloop()
