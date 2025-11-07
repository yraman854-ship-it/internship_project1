import sqlite3
import os
def loadQuestions(conn):
    cur=conn.cursor()
    filename = input("Enter file name")
    fp=open(filename,"r")
    qry="""insert into questions(ques,a,b,c,d,correct,hint,explanation) values"""
    c=0
    for i in fp.readlines():
        if c==0:
            pass
        else:
            qry+="""('{0}','{1}','{2}','{3}','{4}','{5}','{6}','{7}'),""".format(*i.split(",")[1:])
        c+=1
    qry=qry.rstrip(",")
    cur.execute(qry)
    conn.commit()
    cur.close()
    print("Questions uploaded...")

def addQuestion(conn):
    cur=conn.cursor()
    tup=("Question","Option1","Option2","Option3","Option4","Correct","Hint","Explanation")
    lst=[]
    for i in tup:
        lst.append(input(f"enter {i}"))

    qry="""insert into questions(ques,a,b,c,d,correct,hint,explanation) 
    values('{0}','{1}','{2}','{3}','{4}','{5}','{6}','{7}')""".format(*lst)
    cur.execute(qry)
    conn.commit()
    cur.close()
    print("Questions uploaded...")


def deleteQuestion(conn):
    cur=conn.cursor()
    choice=int(input("""
    1)Remove all Questions
    2)Remove Selected Question
    Enter your choice:-
    """))
    if choice==1:
        qry="delete from questions"
        cur.execute(qry)
        conn.commit()
        qry = "update sqlite_sequence set seq=0 where name='questions'"
        cur.execute(qry)
        conn.commit()
    elif choice==2:
        qno=int(input("enter qno u want to delete"))
        qry = f"delete from questions  where qno={qno}"
        cur.execute(qry)
        conn.commit()
    cur.close()

def showAllQuestion(conn):
    cur=conn.cursor()
    qry="select * from questions"
    cur.execute(qry)
    rs=cur.fetchall()
    for q in rs:
        print("""
        Q{0:<2}- {1:<60} 
             a){2:<20} b){3:<20} 
             c){4:<20} d){5:<20} 
           Ans){6:<20}""".format(*q))
    cur.close()





def QuizMgmt(conn):
    while (True):
        choice = int(input('''
            Main Menu
            1)Load Questions From CSV
            2)Add Question
            3)Delete Question
            4)Show All Questions
            5)Exit
            Enter your choice:-'''))
        if (choice == 1):
            loadQuestions(conn)
        elif (choice == 2):
            addQuestion(conn)
        elif (choice == 3):
            deleteQuestion(conn)
        elif (choice == 4):
            showAllQuestion(conn)
        elif (choice == 5):
            break
        else:
            print("Invalid Choice")


if __name__=="__main__":
    conn=sqlite3.connect("dist/quiz.db")

    QuizMgmt(conn)
