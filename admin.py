import quizmgmt
import os
def auth(conn):
    cur=conn.cursor()
    un=input("Enter Username")
    pwd=input("Enter Password")
    qry = f"""select username,role 
    from login where username='{un}' and password='{pwd}' and status='active'"""
    cur.execute(qry)
    rs= cur.fetchone()
    if(rs==None):
        print("Invalid Username or password")
    else:
        print(f"Welcome {un} ")
        manageAdmin(un,conn)
    cur.close()

def manageAdmin(un,conn):
    while (True):
        choice = int(input('''
            Main Menu
            1)Manage Quiz
            2)Create New Admin
            3)Change Own Password
            4)Exit
            Enter your choice:-'''))
        if (choice == 1):
            quizmgmt.QuizMgmt(conn)
        elif (choice == 2):
            createNewAdmin(conn)
        elif (choice == 3):
            changePassword(un,conn)
        elif (choice == 4):
            return
        else:
            print("Invalid Choice")


def createNewAdmin(conn):
    cur=conn.cursor()
    un = input("Enter Username")
    pwd = input("Enter Password")
    cnfpwd = input("Retype Password")
    if(pwd==cnfpwd):
        qry=f"insert into login values('{un}','{pwd}','admin','active')"
        cur.execute(qry)
        cur.close()
        conn.commit()
    else:
        print("password not matched")


def changePassword(un,conn):
    cur=conn.cursor()
    pwd = input("Enter New Password")
    cnfpwd = input("Retype Password")
    if(pwd==cnfpwd):
        qry=f"update login set password='{pwd}' where username='{un}'"
        cur.execute(qry)
        cur.close()
        conn.commit()
    else:
        print("password not matched")