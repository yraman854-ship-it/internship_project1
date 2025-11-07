
import sqlite3 as db
conn=db.connect("dist/quiz.db")
#
# def quizGame():
#     print("Quiz Game")
#     name=input("What is your name?")
#     print(f"Welcome {name} press enter to start quiz")
#     input()
#     limit=int(input("How many questions would you like?"))
#     qry="select * from questions"
#     cur=conn.cursor()
#     cur.execute(qry)
#     qgen=(ques for ques in  cur.fetchall())
#     counter=1
#     score=0
#     while(counter<=limit):
#         q=next(qgen)
#
#         print("""{0:<1}{1:<60}
#         a){2:<10} b){3:<10}
#         c){4:<10} d){5:<10}""".format(*q))
#         correct=q[6]
#         choice=input("enter your choice").title()
#         if(choice==correct):
#             score=score+1
#             print("correct")
#         else:
#             print("incorrect")
#
#         counter+=1
#     print(f"""{name} your score in{score} out of {limit}""")
#
# if __name__ == "__main__":
#     quizGame()

import os

def quizGame(conn):
    os.system("cls")
    print("Quiz Game")
    limit = int(input("No of questions in quiz: "))
    name = input("Please enter your name")
    print(f"Welcome {name} press enter to start quiz")
    input()
    os.system("cls")
    qry="select * from questions"
    cur=conn.cursor()
    cur.execute(qry)
    qgen=(ques for ques in cur.fetchall())
    counter=1
    score=0
    while(counter<=limit):
        os.system("cls")
        q=next(qgen)
        print("""{0:<1}:{1:<60}
a){2:<10} b){3:<10}
c){4:<10} d){5:<10}""".format(*q))
        correct=q[6]
        choice=input("enter your choice :").title()
        if(choice==correct):
            score=score+1
            print("your answer is correct")
        else:
            print("your answer is wrong")
        counter+=1

    print(f"""{name} your score in {score} out of {limit}""")
    input("Press any key to continue")
    savescore=f"insert into leaderboard(name,qlimit,score) values('{name}',{limit},{score})"
    cur.execute(savescore)
    conn.commit()
    cur.close()

if __name__=="__main__":
    quizGame(conn)
