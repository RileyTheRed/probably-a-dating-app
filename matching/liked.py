#Version 1.0 of the liking algorithm
######

import sqlite3 as sql

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
    con = sql.connect("../dating.db", timeout=10)
    cur1 = con.cursor()

    try:
        cur1.execute("select * from mutual where (person1 = ? or person2 = ?)",(person,))
        if not cur1.rowcount:
            cur1.close()
            con.close()
            return []
        else:
            con.close()
            return [row for row in cur1.fetchall()]

    except Exception as e:
        raise e