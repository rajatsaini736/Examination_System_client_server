import tkinter as tk 
import pymysql
from PIL import Image, ImageTk
import time


### SOCKETING
import socket
import pickle



#####
# HOST NAME OF SERVER'S PC
def get_hostname():
    return socket.gethostname()

def mysql_connection():
    return pymysql.connect(host="localhost", user="rajat saini", password="RajatsainI736@gmail.com", db="rajat")



def put_data_for_login(frame,current_user,ques_no,count,data1,data2,data3,d1,d2,d3,temp):
    if "@gmail.com" in data2 and all(x.isalpha() or x.isspace() for x in data1) and len(data3)!=0 and len(data1)!=0 and len(data2)!=0:
        tk.Label(frame,text="                                                                           ",bg="#99ccff").place(x=1100,y=245)
        tk.Label(frame,text="                                                                           ",bg="#99ccff").place(x=1100,y=290)
        tk.Label(frame,text="                                                                           ",bg="#99ccff").place(x=1100,y=335)
        total_data = "login"+" "+data1+" "+data2+" "+data3

        s = socket.socket()
        host = get_hostname()
        port = 9077
        s.connect((host, port))

        s.send(total_data.encode())
        info = (s.recv(2048)).decode()

        if info=="failed":
            delete_from_login(d1,d2,d3)
            tk.Label(frame,text="Incorrect details, please REGISTER first",fg="red",bg="#99ccff").place(x=600,y=195)
        else:
            frame.destroy()
            current_user.append(data2)
            current_user.append(temp)
            show(ques_no,current_user,count,temp)
        s.close()
    else:
        delete_from_login(d1,d2,d3)
        tk.Label(frame,text="                                                                                         ",bg="#99ccff").place(x=600,y=195)
        tk.Label(frame,text="                                                                                          ",bg="#99ccff").place(x=1100,y=290)
        tk.Label(frame,text="                                                                                         ",bg="#99ccff").place(x=1100,y=245)   
        tk.Label(frame,text="                                                                                         ",bg="#99ccff").place(x=1100,y=335)
        if "@gmail.com" not in data2 or len(data2)==0:
            tk.Label(frame,text="insert a valid email                      ",fg="red",bg="#99ccff").place(x=1100,y=290)
        if (any(x.isdigit() for x in data1)) or len(data1)==0:
            tk.Label(frame,text="insert a valid name                    ",fg="red",bg="#99ccff").place(x=1100,y=245)
        if len(data3)==0:
            tk.Label(frame,text="insert your password here                           ",fg="red",bg="#99ccff").place(x=1100,y=335)
        
def put_data_for_signin(frame,data1,data2,data3,data4,data5,current_user,ques_no,count,d1,d2,d3,d4,d5,temp):
        if "@gmail.com" in data2 and all(x.isalpha() or x.isspace() for x in data1) and len(data4)!=0 and len(data5)!=0 and len(data3)==10 and len(data2)!=0 and len(data1)!=0 and data4==data5 and (all(x.isdigit() for x in data3)):
            tk.Label(frame,text="                                                                                ",bg="#99ccff").place(x=1100,y=265)
            tk.Label(frame,text="                                                                                ",bg="#99ccff").place(x=1100,y=220)
            tk.Label(frame,text="                                                                                ",bg="#99ccff").place(x=1100,y=310)
            tk.Label(frame,text="                                                                                ",bg="#99ccff").place(x=1100,y=355)
            tk.Label(frame,text="                                                                                ",bg="#99ccff").place(x=1100,y=400)
            tk.Label(frame,text="                                                                                ",bg="#99ccff").place(x=1100,y=355)
            total_data = "signin"+" "+data1+" "+data2+" "+data4
            s = socket.socket()
            host = get_hostname()
            port = 9077
            s.connect((host,port))
            s.send(total_data.encode())
            info = (s.recv(2048)).decode()

            if info=="already_exist":
                delete_from_signin(d1,d2,d3,d4,d5)
                tk.Label(frame,text="your email is already registered, please login to continue",fg="red",bg="#99ccff").place(x=600,y=195)
            elif info=="success":
                current_user.append(data2)
                current_user.append(temp)
                frame.destroy()
                show(ques_no,current_user,count,temp)
            s.close()
        else:
            delete_from_signin(d1,d2,d3,d4,d5)
            tk.Label(frame,text="                                                                                ",bg="#99ccff").place(x=1100,y=265)
            tk.Label(frame,text="                                                                                ",bg="#99ccff").place(x=1100,y=220)
            tk.Label(frame,text="                                                                                ",bg="#99ccff").place(x=1100,y=310)
            tk.Label(frame,text="                                                                                ",bg="#99ccff").place(x=1100,y=355)
            tk.Label(frame,text="                                                                                ",bg="#99ccff").place(x=1100,y=400)
            tk.Label(frame,text="                                                                                ",bg="#99ccff").place(x=1100,y=355)
            if "@gmail.com" not in data2 or len(data2)==0:
                tk.Label(frame,text="insert a valid email                                                   ",fg="red",bg="#99ccff").place(x=1100,y=265)
            if (any(x.isdigit() for x in data1)) or len(data1)==0:
                tk.Label(frame,text="insert a valid name                                                    ",fg="red",bg="#99ccff").place(x=1100,y=220)
            if (any(x.isalpha() for x in data3)) or len(data3)!=10:
                tk.Label(frame,text="insert a valid mobile number                                          ",fg="red",bg="#99ccff").place(x=1100,y=310)
            if len(data4)==0: 
                tk.Label(frame,text="insert your password here                                             ",fg="red",bg="#99ccff").place(x=1100,y=355)
            if len(data5)==0:
                tk.Label(frame,text="re-insert your password here                                          ",fg="red",bg="#99ccff").place(x=1100,y=400)
            if data4!=data5:
                tk.Label(frame,text="re-enter your password                                                ",fg="red",bg="#99ccff").place(x=1100,y=355)

def delete_from_login(d1,d2,d3):
    d1.delete(0,tk.END)
    d2.delete(0,tk.END)
    d3.delete(0,tk.END)

def delete_from_signin(d1,d2,d3,d4,d5):
    d1.delete(0,tk.END)
    d2.delete(0,tk.END)
    d3.delete(0,tk.END)
    d4.delete(0,tk.END)
    d5.delete(0,tk.END)

def skip_page(frame2,current_user,ques_no,count,temp):
    frame2.destroy()
    count+=1
    ques_no+=1
    show(ques_no,current_user,count,temp)

def prev_page(frame3,current_user,ques_no,count,temp):
    frame3.destroy()
    count-=1
    ques_no-=1
    show(ques_no,current_user,count,temp)

def next_page(frame,current_user,temp_ans,ques_no,count,temp):
    if temp_ans==-1:
        tk.Label(frame,text="please select an answer or to skip this question press SKIP QUES button",fg="red",bg="#99ccff").place(x=0,y=250)
    elif ques_no==10:
        tk.Label(frame,text="                                                                                              ").place(x=0,y=250)
        frame.destroy()
        connection1=mysql_connection()
        cursor1=connection1.cursor()
        cursor1.execute("update questions set temp_ans=(%s) where id=(%s)"%(temp_ans+1,count))
        connection1.commit()
        show(ques_no,current_user,count,temp)
    else:
        tk.Label(frame,text="                                                                                              ").place(x=0,y=250)
        frame.destroy()
        connection=mysql_connection()
        cursor=connection.cursor()
        cursor.execute("update questions set temp_ans=(%s) where id=(%s)"%(temp_ans+1,count))   
        connection.commit()
        count+=1
        ques_no+=1
        show(ques_no,current_user,count,temp)

def link_ques(frame,current_user,ques_no,count,temp):
    frame.destroy()
    ques_no=count+1-temp
    show(ques_no,current_user,count,temp)

def calculate_score(current_user,temp):
    frame=tk.Tk()
    temp_ans=[]
    corr_ans=[]
    sum_list=[]
    frame.configure(background="#99ccff")
    frame.attributes('-fullscreen',True)
    connection=mysql_connection()
    connection1=mysql_connection()
    
    cursor=connection.cursor()
    cursor1=connection1.cursor()
    
    for i in range(current_user[1],current_user[1]+10):
        cursor.execute("select answer from questions where id=(%s)"%(i))
        cursor1.execute("select temp_ans from questions where id=(%s)"%(i))
        temp_ans.append(*cursor1.fetchall())
        corr_ans.append(*cursor.fetchall())
    sum_list+=([1 for i in range(len(corr_ans)) if corr_ans[i][0]==temp_ans[i][0]])
    tk.Label(frame,text="Your Final Score is :",bg="#99ccff",font="Times 30 bold").place(x=50,y=50)
    score1=sum(sum_list)
    tk.Label(frame,text=score1,bg="#99ccff",font="Times 30 bold").place(x=400,y=50)

    connection2=mysql_connection()
    cursor2=connection2.cursor()
    cursor2.execute("update questions set temp_ans=0")
    connection2.commit()

    connection3=mysql_connection()
    cursor3=connection3.cursor()
    if temp==41:
        cursor3.execute("update ques_index set ques_index=1")
        connection3.commit()
    else:
        cursor3.execute("update ques_index set ques_index=(%s)"%(temp+10))
        connection3.commit()


    s = socket.socket()
    host = get_hostname()
    port = 9077
    s.connect((host,port))

    total_data = "score"+" "+current_user[0]+" "+str(score1)
    s.send(total_data.encode())

    tk.Button(frame,text="EXIT",width=10,font="Arial 15 bold",bd=5,padx=5,pady=5,bg="darkblue",fg="white",command=frame.destroy).place(x=700,y=300)
    tk.Label(frame,text="* Designed and developed by Rajat Saini",bg="#99ccff",fg="tomato",font="Times 20 bold").place(x=10,y=600)
    tk.Label(frame,text="   C.S.E. 2016-2020, GECJ",bg="#99ccff",fg="tomato",font="Times 20 bold").place(x=10,y=635)
    tk.Label(frame,text="Python3 is used in this system",bg="#99ccff",font="Times 15",fg="OliveDrab").place(x=10,y=670)
    tk.Label(frame,text="Tkinter (G.U.I.) is used in this system",bg="#99ccff",font="Times 15",fg="OliveDrab").place(x=10,y=690)
    tk.Label(frame,text="MySQL database is used in this system",bg="#99ccff",font="Times 15",fg="OliveDrab").place(x=10,y=710)
    tk.Label(frame,text="TCP-SOCKET PROGRAMMING is used in this system to connect server and client files",bg="#99ccff",font="Times 15",fg="OliveDrab").place(x=10,y=730)
    frame.mainloop()

def final_submit(frame,current_user,temp):
    root=tk.Tk()
    root.geometry("500x100+500+300")
    root.configure(background="#ff6600")
    root.overrideredirect(True)
    tk.Label(root,text="Are you sure to exit",bg="#ff6600",font="Times 13 bold",fg="black").pack(anchor=tk.N)
    tk.Button(root,text="Yes",width=10,bd=5,padx=5,pady=5,bg="orange",command=lambda: (root.destroy(),frame.destroy(),calculate_score(current_user,temp))).place(x=130,y=50)
    tk.Button(root,text="No",width=10,bd=5,padx=5,pady=5,command=root.destroy).place(x=270,y=50)
    root.mainloop()
    
def instructions():
    root=tk.Tk()
    root.configure(background="#99ccff")
    root.attributes('-fullscreen',True)
    tk.Label(root,text="INSTRUCTIONS :",bg="#99ccff",font="Times 20 bold").pack(anchor=tk.N)
    tk.Label(root,text="* 10 questions are given for each student.",bg="#99ccff",font="Times 15 bold").place(x=70,y=50)
    tk.Label(root,text="* save & next - this button is used to save your temporary answer and proceed to the next question.",bg="#99ccff",font="Times 15 bold").place(x=70,y=100)
    tk.Label(root,text="* skip ques - this button is used to proceed to the next question without saving it.",bg="#99ccff",font="Times 15 bold").place(x=70,y=150)
    tk.Label(root,text="* prev ques - this button is used to proceed to the previous questionk.",bg="#99ccff",font="Times 15 bold").place(x=70,y=200)
    tk.Label(root,text="*",bg="#99ccff",font="Times 15 bold").place(x=70,y=250)
    tk.Button(root,text="1",width=5,bd=2,padx=2,pady=2).place(x=90,y=250)
    tk.Label(root,text="shows that you have not attempt this question yet.",bg="#99ccff",font="Times 15 bold").place(x=140,y=250)
    tk.Label(root,text="*",bg="#99ccff",font="Times 15 bold").place(x=70,y=300)
    tk.Button(root,text="1",width=5,bd=2,bg="green",padx=2,pady=2).place(x=90,y=300)
    tk.Label(root,text="shows that you have attempt this qusetion.",bg="#99ccff",font="Times 15 bold").place(x=140,y=300)

    tk.Button(root,text="Back",width=10,bg="pink",bd=5,padx=5,pady=5,font="Times 10 bold",command=root.destroy).place(x=1100,y=700)

    root.mainloop()

def search_result(root,mail):
    tk.Label(root,text="                                                                               ",font="Times 20 bold",bg="#99ccff").place(x=100,y=300)
    if(len(mail)!=0):
        total_data = "result"+" "+mail
        s=socket.socket()
        host = get_hostname()
        port = 9077
        s.connect((host,port))

        s.send(total_data.encode())
        info = (s.recv(2048)).decode()
        if info=="failed":
                tk.Label(root,text="enter a valid email",fg="red",bg="#99ccff",font="Times 20 bold").place(x=100,y=300)
        else:
            tk.Label(root,text="Your previous score is :-",bg="#99ccff",font="Times 20 bold").place(x=100,y=300)
            tk.Label(root,text=info,bg="#99ccff",font="Times 20 bold").place(x=400,y=300)
    else:
        tk.Label(root,text="Please enter something in searchbox",fg="red",bg="#99ccff",font="Times 20 bold").place(x=100,y=300)


def result():
    root= tk.Tk()
    root.configure(background="#99ccff")
    root.attributes('-fullscreen',True)
    tk.Label(root,text="SEARCH RESULT HERE - ",bg="#99ccff",font="Arial 25 bold").pack(anchor=tk.N)
    tk.Label(root,text="enter candidate's E-mail here -",bg="#99ccff",font="Times 20 bold").place(x=100,y=150)
    E1 = tk.Entry(root,width=30,font="black 20")
    E1.place(x=500,y=150)
    tk.Button(root,text="Search",width=10,bg="green",bd=2,padx=5,pady=5,font="Times 10 bold",command=lambda: (search_result(root,E1.get()))).place(x=680,y=200)

    tk.Button(root,text="Back",width=10,bg="pink",bd=5,padx=5,pady=5,font="Times 10 bold",command=root.destroy).place(x=1100,y=700)
    root.mainloop()

def show(ques_no,current_user,count,temp):
    root=tk.Tk()
    v=tk.IntVar()
    root.configure(background="#99ccff")
    root.attributes('-fullscreen',True)
    temp_ans=[]


    connection=mysql_connection()
    connection1=mysql_connection()
    connection2=mysql_connection()
    connection3=mysql_connection()
    connection4=mysql_connection()

    cursor=connection.cursor()
    cursor1=connection1.cursor()
    cursor2=connection2.cursor()
    cursor3=connection3.cursor()
    cursor4=connection4.cursor()

    cursor.execute("select question from questions where id=(%s)"%count)
    cursor2.execute("select answer from questions where id=(%s)"%count)
    cursor1.execute("select choice1,choice2,choice3,choice4 from questions where id=(%s)"%count)
    cursor3.execute("select temp_ans from questions where id=(%s)"%count)
    for i in range(temp,temp+10):
        cursor4.execute("select temp_ans from questions where id=(%s)"%i)
        temp_ans.append(*cursor4.fetchall())

    data=cursor.fetchall()
    data1=cursor1.fetchall()
    data2=cursor2.fetchall()
    data3=cursor3.fetchall()

    v.set(data3[0][0]-1)
    tk.Label(root,text="Q.",bg="#99ccff",font="Times 20 bold").pack(anchor=tk.NW)
    tk.Label(root,text=ques_no,bg="#99ccff",font="Times 20 bold").place(x=30,y=0)
    for val,daata in enumerate(data[0]):
        tk.Label(root,text=daata,bg="#99ccff",font="Times 20 bold").place(x=60,y=0)
    
    for val,dt in enumerate(*data1):
        tk.Radiobutton(root,text=dt,bg="#99ccff",variable=v,value=val,font="Times 20 bold").pack(anchor=tk.SW)
    if ques_no>1:
        tk.Button(root,text="Prev Ques",width=12,bd=5,padx=5,font="Tiimes 10 ",pady=5,bg="cyan",command=lambda: prev_page(root,current_user,ques_no,count,temp)).place(x=260,y=300)
    if ques_no<10:
        tk.Button(root,text="Skip Ques",width=12,bd=5,padx=5,font="Tiimes 10 ",pady=5,bg="cyan",command=lambda: skip_page(root,current_user,ques_no,count,temp)).place(x=520,y=300)
    if ques_no<10:
        tk.Button(root,text="Save & Next",width=12,bd=5,padx=5,pady=5,bg="lightgreen",font="Times 10 ",command=lambda: next_page(root,current_user,v.get(),ques_no,count,temp)).place(x=400,y=300)
    if ques_no==10:
        tk.Button(root,text="Save",width=12,bd=5,padx=5,pady=5,bg="lightgreen",font="Times 10 ",command=lambda: next_page(root,current_user,v.get(),ques_no,count,temp)).place(x=400,y=300)
    tk.Button(root,text="SUBMIT & EXIT",width=12,bd=5,padx=5,pady=5,font="Tiimes 10 bold",bg='black',fg='white',command=lambda: final_submit(root,current_user,temp)).place(x=1100,y=700)
    tk.Label(root,text="* Instructions are here! ",fg="red",bg="#99ccff",font="Times 20 bold").place(x=100,y=700)
    tk.Button(root,text="Instructions",width=10,bd=5,padx=5,pady=5,bg="pink",font="Times 10 bold",command=instructions).place(x=430,y=700)
    tk.Label(root,text="* you can go direct on any questions from here",font="Times 15 bold",bg="#99ccff",fg="#ff6600").place(x=900,y=300)
    tk.Button(root,text="1",width=5,bd=2,padx=2,pady=2,command=lambda: link_ques(root,current_user,ques_no,temp,temp)).place(x=900,y=350)
    tk.Button(root,text="2",width=5,bd=2,padx=2,pady=2,command=lambda: link_ques(root,current_user,ques_no,temp+1,temp)).place(x=950,y=350)
    tk.Button(root,text="3",width=5,bd=2,padx=2,pady=2,command=lambda: link_ques(root,current_user,ques_no,temp+2,temp)).place(x=900,y=400)
    tk.Button(root,text="4",width=5,bd=2,padx=2,pady=2,command=lambda: link_ques(root,current_user,ques_no,temp+3,temp)).place(x=950,y=400)
    tk.Button(root,text="5",width=5,bd=2,padx=2,pady=2,command=lambda: link_ques(root,current_user,ques_no,temp+4,temp)).place(x=900,y=450)
    tk.Button(root,text="6",width=5,bd=2,padx=2,pady=2,command=lambda: link_ques(root,current_user,ques_no,temp+5,temp)).place(x=950,y=450)
    tk.Button(root,text="7",width=5,bd=2,padx=2,pady=2,command=lambda: link_ques(root,current_user,ques_no,temp+6,temp)).place(x=900,y=500)
    tk.Button(root,text="8",width=5,bd=2,padx=2,pady=2,command=lambda: link_ques(root,current_user,ques_no,temp+7,temp)).place(x=950,y=500)
    tk.Button(root,text="9",width=5,bd=2,padx=2,pady=2,command=lambda: link_ques(root,current_user,ques_no,temp+8,temp)).place(x=900,y=550)
    tk.Button(root,text="10",width=5,bd=2,padx=2,pady=2,command=lambda: link_ques(root,current_user,ques_no,temp+9,temp)).place(x=950,y=550)
    
    if temp_ans[0][0]!=0:
        tk.Button(root,text="1",width=5,bd=2,bg="green",padx=2,pady=2,command=lambda: link_ques(root,current_user,ques_no,temp,temp)).place(x=900,y=350)
    if temp_ans[1][0]!=0:
        tk.Button(root,text="2",width=5,bd=2,bg="green",padx=2,pady=2,command=lambda: link_ques(root,current_user,ques_no,temp+1,temp)).place(x=950,y=350)
    if temp_ans[2][0]!=0:   
        tk.Button(root,text="3",width=5,bd=2,bg="green",padx=2,pady=2,command=lambda: link_ques(root,current_user,ques_no,temp+2,temp)).place(x=900,y=400)
    if temp_ans[3][0]!=0:   
        tk.Button(root,text="4",width=5,bd=2,bg="green",padx=2,pady=2,command=lambda: link_ques(root,current_user,ques_no,temp+3,temp)).place(x=950,y=400)
    if temp_ans[4][0]!=0:   
        tk.Button(root,text="5",width=5,bd=2,bg="green",padx=2,pady=2,command=lambda: link_ques(root,current_user,ques_no,temp+4,temp)).place(x=900,y=450)
    if temp_ans[5][0]!=0:
        tk.Button(root,text="6",width=5,bd=2,bg="green",padx=2,pady=2,command=lambda: link_ques(root,current_user,ques_no,temp+5,temp)).place(x=950,y=450)
    if temp_ans[6][0]!=0:
        tk.Button(root,text="7",width=5,bd=2,bg="green",padx=2,pady=2,command=lambda: link_ques(root,current_user,ques_no,temp+6,temp)).place(x=900,y=500)
    if temp_ans[7][0]!=0:
        tk.Button(root,text="8",width=5,bd=2,bg="green",padx=2,pady=2,command=lambda: link_ques(root,current_user,ques_no,temp+7,temp)).place(x=950,y=500)
    if temp_ans[8][0]!=0:
        tk.Button(root,text="9",width=5,bd=2,bg="green",padx=2,pady=2,command=lambda: link_ques(root,current_user,ques_no,temp+8,temp)).place(x=900,y=550)
    if temp_ans[9][0]!=0:
        tk.Button(root,text="10",width=5,bd=2,bg="green",padx=2,pady=2,command=lambda: link_ques(root,current_user,ques_no,temp+9,temp)).place(x=950,y=550)
    root.mainloop()

def call_the_login_page(frame1,ques_no,count,current_user,temp):
    frame1.destroy()
    login_page(ques_no,count,current_user,temp)

def call_the_sign_in_page(frame1,ques_no,count  ,current_user,temp):
    frame1.destroy()
    sign_in(ques_no,count,current_user,temp)

def sign_in(ques_no,count,current_user,temp):
    root=tk.Tk()
    root.attributes('-fullscreen',True)
    root.configure(background="#99ccff")
    image=tk.PhotoImage(file="LOGO.gif")
    v=tk.IntVar()

    tk.Label(root,text="Online Examination System",bg="#99ccff",font="black 50 bold").grid(row=0)
    tk.Label(root,image=image,bg="#99ccff",width="200",height="200").place(x=1100,y=0)
    tk.Label(root,text="Name -",bg="#99ccff",font="black 25").place(x=250,y=220)
    tk.Label(root,text="E-mail -",bg="#99ccff",font="black 25").place(x=250,y=265)  
    tk.Label(root,text="Mobile No. -",bg="#99ccff",font="black 25").place(x=250,y=310)
    tk.Label(root,text="Password -",bg="#99ccff",font="black 25").place(x=250,y=355)
    tk.Label(root,text="Re-enter Password -",bg="#99ccff",font="black 25").place(x=250,y=400)
    
    e1=tk.Entry(root,width=30,font="black 20")
    e2=tk.Entry(root,width=30,font="black 20")
    e3=tk.Entry(root,width=30,font="black 20")
    e4=tk.Entry(root,width=30,font="black 20",show="*")
    e5=tk.Entry(root,width=30,font="black 20",show="*")
    
    e1.place(x=600,y=220)
    e2.place(x=600,y=265)
    e3.place(x=600,y=310)
    e4.place(x=600,y=355)
    e5.place(x=600,y=400)

    tk.Button(root,text="Register",width=10,bd=5,bg='cyan',padx=5,pady=5,command=lambda: put_data_for_signin(root,e1.get(),e2.get(),e3.get(),e4.get(),e5.get(),current_user,ques_no,count,e1,e2,e3,e4,e5,temp)).place(x=600,y=452)
    tk.Button(root,text="Login here",width=10,bd=5,padx=5,pady=5,bg="orange",command=lambda: call_the_login_page(root,ques_no,count,current_user,temp)).place(x=775,y=452)
    tk.Button(root,text="Clear",width=10,bd=5,bg="lightgrey",padx=5,pady=5,command=lambda: delete_from_signin(e1,e2,e3,e4,e5)).place(x=950,y=452)
    tk.Button(root,text="Quit",width=10,bd=5,bg="darkblue",fg="white",font="Times 10 bold",padx=5,pady=5,command=root.destroy).place(x=1100,y=700)

    tk.Label(root,text="* Instructions are here! -",bg="#99ccff",font="Times 25 bold",fg="red").place(x=100,y=700)
    tk.Button(root,text="Instructions",width=10,bd=5,padx=5,pady=5,bg="pink",font="Times 12 bold",command=instructions).place(x=470,y=700)
    root.mainloop()

def login_page(ques_no,count,current_user,temp):
    root=tk.Tk()
    root.configure(background="#99ccff")
    root.attributes('-fullscreen',True)
    image=tk.PhotoImage(file="LOGO.gif")

    v=tk.IntVar()

    tk.Label(root,text="Online Examination System",bg="#99ccff",font="black 50 bold").place(x=0,y=0)
    tk.Label(root,image=image,width="200",bg="#99ccff",height="200").place(x=1100,y=0)
    tk.Label(root,text="Name -",bg="#99ccff",font="black 30").place(x=250,y=245)
    tk.Label(root,text="E-mail-",bg="#99ccff",font="black 30").place(x=250,y=290)
    tk.Label(root,text="Password-",bg="#99ccff",font="black 30").place(x=250,y=335)
    
    e1=tk.Entry(root,width=30,font="red 20")
    e2=tk.Entry(root,width=30,font="red 20")
    e3=tk.Entry(root,width=30,show="*",font="black 20")
    
    e1.place(x=600,y=245)
    e2.place(x=600,y=290)
    e3.place(x=600,y=335)
    
    tk.Button(root,text="LOG-IN",width=10,bd=5,bg='cyan',padx=5,pady=5,command=lambda: put_data_for_login(root,current_user,ques_no,count,e1.get(),e2.get(),e3.get(),e1,e2,e3,temp)).place(x=600,y=412)
    tk.Button(root,text="Register here",width=10,bd=5,padx=5,pady=5,bg="orange",command=lambda: call_the_sign_in_page(root,ques_no,count,current_user,temp)).place(x=775,y=412)
    tk.Button(root,text="Clear",width=10,bd=5,padx=5,bg="lightgrey",pady=5,command=lambda: delete_from_login(e1,e2,e3)).place(x=950,y=412)
    tk.Button(root,text="Quit",width=10,bd=5,bg="darkblue",fg="white",font="Times 10 bold",padx=5,pady=5,command=root.destroy).place(x=1100,y=700)

    tk.Label(root,text="* Result is here! -",bg="#99ccff",font="Times 25 bold",fg="red").place(x=100,y=650)
    tk.Button(root,text="Result",width=10,bd=5,padx=5,pady=5,bg="pink",font="Times 12 bold",command=result).place(x=370,y=650)
    tk.Label(root,text="* Instructions are here! -",bg="#99ccff",font="Times 25 bold",fg="red").place(x=100,y=700)
    tk.Button(root,text="Instructions",width=10,bd=5,padx=5,pady=5,bg="pink",font="Times 12 bold",command=instructions).place(x=470,y=700)
    root.mainloop()



###########   MAIN FUNCTION #############

connection=mysql_connection()


cursor=connection.cursor()
cursor.execute("select ques_index from ques_index where id=1")
index=cursor.fetchall()
temp=int(index[0][0])
count=temp
ques_no=1
current_user=[]
login_page(ques_no,count,current_user,temp)
