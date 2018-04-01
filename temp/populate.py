# import sqlite3 as sql

# if __name__ == "__main__":

#     con = sql.connect("../dating.db", timeout=10)
#     cur = con.cursor()

#     statement = "insert into users(uemail, ufname, ulname, ugender, upass) values (?,?,?,?,?);"

#     with open("users.csv") as fr:
#         for i,info in enumerate(fr):
#             temp = info
#             temp = temp.split(",")
#             cur.execute(statement,(temp[0],temp[1],temp[2],temp[3],(temp[4].replace("\n", ""))))
#             con.commit()

#     cur.close()
#     con.close()