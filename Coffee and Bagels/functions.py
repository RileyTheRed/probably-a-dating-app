import sqlite3 as sql

#defintion of the function that gets and returns the path that leads to the users profile picture
def get_pic_path(email):

    con = sql.connect("dating.db", timeout=10)
    cursor = con.cursor()

    try:

        cursor.execute("select pp_imagename from profile_pics where pp_email=?", (email,))
        temp = cursor.fetchone()
        return temp[0]

    except Exception as e:

        raise e


#defintion of the function that gets and returns the users questionnaire information
def get_user_question_information(email):

    con = sql.connect("dating.db", timeout=10)
    cursor = con.cursor()

    try:

        cursor.execute("select * from questionnaire where qemail = ?",(email,))
        temp = cursor.fetchone()
        return temp[2:]

    except Exception as e:

        raise e


#defintion of the user login verification
def validate_user(given_email, given_pass):

    con = sql.connect("dating.db", timeout=10)
    cursor = con.cursor()

    try:

        cursor.execute("select upass from users where uemail = ?", (given_email,))
        rows = cursor.fetchone()
        if not rows:
            return 0
        else:
            if not given_pass == rows[0]:
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

    con = sql.connect("dating.db", timeout=10)
    cur1 = con.cursor()

    try:

        if validate_user(temp_user[0],"") == 0:

            cur1.execute("insert into users(uemail,ufname,ulname,ugender,upass) values (?,?,?,?,?)", (temp_user[0],temp_user[1],temp_user[2], temp_user[3],temp_user[4]))
            
            cur1.execute("insert into questionnaire(qemail,qgenderpreference,q1,q2,q3,q4,q5,q6,q7,q8,q9,q10,q11,q12,q13,q14,q15,q16,q17,q18,q19,q20) values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", (temp_quest[0],temp_quest[1],temp_quest[2],temp_quest[3],temp_quest[4],temp_quest[5],temp_quest[6],temp_quest[7],temp_quest[8],temp_quest[9],temp_quest[10],temp_quest[11],temp_quest[12],temp_quest[13],temp_quest[14],temp_quest[15],temp_quest[16],temp_quest[17],temp_quest[18],temp_quest[19],temp_quest[20],temp_quest[21]))
            con.commit()

            return 1
        
        else:

            return 0

    except Exception as e:

        raise e


#definition of get_user_info
def get_user_info(user_email):

    con = sql.connect('dating.db', timeout=10)
    cur1 = con.cursor()

    try:

        L = {}
        cur1.execute("select ufname, ulname, ugender from users where uemail = ?",(user_email,))
        row = cur1.fetchone()
        L["fname"] = row[0]
        L["lname"] = row[1]
        L["gender"] = row[2]

        cur1.execute("select qgenderpreference from questionnaire where qemail = ?",(user_email,))
        row = cur1.fetchone()
        L["preference"] = row[0]

        cur1.close()

        return L

    except Exception as e:

        raise e


#defintion of the get_user_first_name function
def get_user_first_name(user_email):

    con = sql.connect('dating.db', timeout=10)
    cur1 = con.cursor()

    try:

        cur1.execute("select ufname, ulname from users where uemail = ?",(user_email,))

        temp = cur1.fetchone()

        name = temp[0] + " " + temp[1]

        return name
    
    except Exception as e:

        raise e


if __name__ == "__main__":

    print(get_user_info("r.wells6894@gmail.com"))

    # print(validate_user("bstarkey5e@dyndns.org","a5zNfx"))
