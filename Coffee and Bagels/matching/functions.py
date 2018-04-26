import sqlite3 as sql

#defintion of the function that gets and returns the path that leads to the users profile picture
def get_pic_path(email):

    con = sql.connect("../dating.db", timeout=10)
    cursor = con.cursor()

    try:

        cursor.execute("select pp_imagename from profile_pics where pp_email=?", (email,))
        temp = cursor.fetchone()
        return temp[0]

    except Exception as e:

        raise e


#defintion of the function that gets and returns the users questionnaire information
def get_user_question_information(email):

    con = sql.connect("../dating.db", timeout=10)
    cursor = con.cursor()

    try:

        cursor.execute("select * from questionnaire where qemail = ?",(email,))
        temp = cursor.fetchone()
        return temp[2:]

    except Exception as e:

        raise e


#defintion of the user login verification
def validate_user(given_email, given_pass):

    con = sql.connect("../dating.db", timeout=10)
    cursor = con.cursor()

    try:

        cursor.execute("select upass from users where uemail = ?", (given_email,))
        if not cursor.rowcount:
            return 0
        else:
            if not given_pass == cursor.fetchone()[0]:
                return 1
            else:
                return 2

    except Exception as e:

        raise e


#definiton of the registration validation
def validate_registration(user_info):

    temp_user = [user_info[2],user_info[0],user_info[1],user_info[4],user_info[3]]
    temp_quest = [user_info[2],user_info[5]]
    for x in user_info[6:]:
        temp_quest.append(x)

    con = sql.connect("../dating.db", timeout=10)
    cur1 = con.cursor()
    cur1.execute("select * from users where uemail = ?", (temp_quest[0],))

    if not cur1.rowcount:

        cur1.execute("insert into users(uemail,ufname,ulname,ugender,upass) values (?,?,?,?,?)", (x for x in temp_user))
        con.commit()
        
        cur1.execute("insert into questionnaire(qemail,qgenderpreference,q1,q2,q3,q4,q5,q6,q7,q8,q9,q10,q11,q12,q13,q14,q15,q16,q17,q18,q19,q20) values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", (x for x in temp_quest))
        con.commit()

        return 1
    
    else:

        return 0



# if __name__ == "__main__":

#     test = [1,2,3,4,5,6,7,8,9,10]
#     print(validate_registration(test))
