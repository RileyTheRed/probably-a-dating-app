# import sqlite3 as sql

# if __name__ == "__main__":

#     con = sql.connect("dating.db", timeout=10)
#     cur = con.cursor()

#     statement = '''insert or replace into questionnaire(qemail, qpreference, q1, q2, q3, q4, q5, q6, q7, q8, q9, q10, q11, q12, q13, q14, q15, q16, q17, q18, q19, q20) values (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)'''

#     with open("answers.txt") as fr:
#         for i,ans in enumerate(fr):
#             temp = ans
#             temp = temp.strip()
#             temp = tuple(filter(None,temp.split(",")))
#             cur.execute(statement,(temp[:22]))
#             con.commit()
#     cur.close()
#     con.close()

#     statement = "insert into users(uemail, ufname, ulname, ugender, upass) values (?,?,?,?,?);"

#     with open("users.csv") as fr:
#         for i,info in enumerate(fr):
#             temp = info
#             temp = temp.split(",")
#             cur.execute(statement,(temp[0],temp[1],temp[2],temp[3],(temp[4].replace("\n", ""))))
#             con.commit()

#     cur.close()
#     con.close()

    # gen = ('Male',)
    # user = cur.execute("select * from users where ugender=?;",gen).fetchall()
    # con.close()
    # for x in user:
    #     print(x)