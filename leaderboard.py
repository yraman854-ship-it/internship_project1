import os

def printLeaderBoard(conn):
    os.system("cls")
    cur=conn.cursor()
    qry="select * from leaderboard order by score desc limit 5"
    cur.execute(qry)
    rs=cur.fetchall()
    print("-" * 50)
    print("{0:<5} {1:<15} {2:>5} {3:>5}".format(*("Uid","Name","Limit","Score")))
    print("-"*50)
    for rec in rs:
        print("{0:<5} {1:<15} {2:>5} {3:>5}".format(*rec))
    print("-" * 50)

    input("press any key to continue")