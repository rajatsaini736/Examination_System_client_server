import socket
import pickle
import pymysql

s = socket.socket()

host = socket.gethostname()


port = 9077
s.bind((host,port))
s.listen(5)

def mysql_connection():
    return pymysql.connect(host="localhost",user="rajat saini", password="RajatsainI736@gmail.com", db="rajat_server")

while True:
    c, addr = s.accept()
    data = (c.recv(2048)).decode()
    mylist = list(data.split())
    process = mylist[0]
    connection1=mysql_connection()
    cursor1=connection1.cursor()
    if process=="login":
        name,mail,password = mylist[1],mylist[2],mylist[3]
        cursor1.execute("select name,email,password from userinfo where email=('%s')"%mail)
        fetch_data = cursor1.fetchall()
        if len(fetch_data)!=0 and name==fetch_data[0][0] and mail==fetch_data[0][1] and password==fetch_data[0][2]:
            c.send("success".encode())
        else:
            c.send("failed".encode())

    elif process=="signin":
        name,mail,password = mylist[1],mylist[2],mylist[3]
        cursor1.execute("select email from userinfo")
        mails = cursor1.fetchall()
        if mail in [item[0] for item in mails]:
            c.send("already_exist".encode())
        else:
            connection=mysql_connection()
            cursor=connection.cursor()
            cursor.execute("insert into userinfo(name,email,password) values('%s','%s','%s')"%(name,mail,password))
            connection.commit()
            c.send("success".encode())

    elif process=="score":
        mail,score = mylist[1],mylist[2]
        cursor1.execute("update rajat_server.userinfo set score=(%s) where email=('%s')"%(score,mail))
        connection1.commit()
    elif process=="result":
        mail = mylist[1]
        connection = mysql_connection()
        cursor = connection.cursor()
        cursor.execute("select score from userinfo where email=('%s')"%mail)
        user_score= cursor.fetchall()
        if len(user_score)==0:
            c.send("failed".encode())
        else:
            c.send(user_score[0][0].encode())



    c.close()

   

    



    # print((c.recv(2048).decode()))