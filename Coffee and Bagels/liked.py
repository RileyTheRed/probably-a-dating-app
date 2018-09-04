#Version 1.0 of the liking algorithm
######

# import 'match.py'
# import importlib
# importlib.import_module('match.py')

import sqlite3 as sql
import functions as f

#definition of the liked function
def liked(liker,liked,compat):
    con = sql.connect("../dating.db", timeout=10)
    cur1 = con.cursor()

    try:
        cur1.execute("select * from likes where likes.liker = ? and likes.liked = ?",(liker,liked))
        if not cur1.rowcount:
            cur1.execute("select * form likes where likes.liker = ? and likes.liked = ?",(liked,liker))
            if not cur1.rowcount:
                cur1.execute("insert into likes(liker,liked,compatability) values (?,?,?)",(liker,liked,compat))
                con.commit()
            else:
                cur1.execute("select * from mutual where (person1 = ? or person1 = ?) and (person2 = ? or person2 = ?)",(liker,liked,liker,liked))
                if not cur1.rowcount:
                    cur1.execute("insert into mutual(person1,person2,compatability) values (?,?,?)",(liker,liked,compat))
                    con.commit()
        
        cur1.close()
        con.close()
    
    except Exception as e:
        raise e


#definition of function that retrieves mutual likes between user and other persons
def get_mutual_likes(person):
    con = sql.connect("dating.db", timeout=10)
    cur1 = con.cursor()

    try:
        temp = cur1.execute("select * from mutual where person1 = ? or person2 = ?",(person,person)).fetchall()
        L = []
        for row in temp:
            if row[0] == person:
                L.append({"Name: ":f.get_user_first_name(row[1]), "Compatability: ":"%"+row[2],"Email: ":row[1]})
            else:
                L.append({"Name: ":f.get_user_first_name(row[0]), "Compatability: ":"%"+row[2],"Email: ":row[0]})

        return L

    except Exception as e:
        raise e


if __name__ == "__main__":

    for row in get_mutual_likes("r.wells6894@gmail.com"):
        print(row)

