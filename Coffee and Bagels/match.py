""" This is the prototype matching algorithm for the website

V1.3
"""

import sqlite3 as sql

#def of max/min compatability
def min_max(person):
    compat_range = [100.0,0.0]
    try:
        con = sql.connect("dating.db", timeout=10)
        cur1 = con.cursor()
        cur2 = con.cursor()

        cur1.execute("select * from questionnaire where qemail = ?",(person,))
        cur2.execute("select * from questionnaire")
        for row1 in cur1:
            for row2 in cur2:
                if row1[0] == row2[0]:
                    continue
                temp = compatability(compare(row1[2:],row2[2:]))
                if temp < compat_range[0]:
                    compat_range[0] = temp
                elif temp > compat_range[1]:
                    compat_range[1] = temp

        cur1.close()
        cur2.close()
        con.close()

    except Exception as e:
        raise e

    return compat_range

#definition for the comparison function
def compare(p1,p2):
    total_difference = 0
    for x in range(len(p1)):
        total_difference += abs(int(p1[x])-int(p2[x]))

    return total_difference

#definition for the compatability function
def compatability(n):
    if not n:
        return 100
    return ((100-n)/100)*100

#adjusted compatability
def adjusted_compatability(n,com_range):

    try:
        temp = float("{0:.2f}".format((((n-com_range[0])*100) / (com_range[1] - com_range[0]))))
        print(com_range[1])
        print(com_range[0])
        print(com_range[1] - com_range[0])
        return temp

    except ZeroDivisionError as e:
        print(com_range[1])
        print(com_range[0])
        print(com_range[1] - com_range[0])
        raise e


#main return function
def get_matches(person):

    qrange = min_max(person)
    matches = []

    try:
        
        con = sql.connect("dating.db", timeout=10)
        cur1 = con.cursor()
        cur2 = con.cursor()

        p1_deets = cur1.execute("select * from users where uemail=?",(person,)).fetchone()
        p1_ans = cur1.execute("select * from questionnaire where qemail=?",(person,)).fetchone()

        person1 = (p1_deets,p1_ans)

        cur1.execute("select * from users")
        for row1 in cur1:
            if person == row1[0]:
                continue
            else:
                if person1[1][1] == row1[3]:
                    cur2.execute("select * from questionnaire where qemail=?",(row1[0],))
                    for row2 in cur2:
                        if row2[1] == person1[0][3]:
                            if adjusted_compatability(compatability(compare(person1[1][2:],row2[2:])),qrange) < 45.00:
                                continue
                            matches.append([person,adjusted_compatability(compatability(compare(person1[1][2:],row2[2:])),qrange),row1[0]])
                            # print("{0} {1} is %{2:.2f} compatible with {3} {4}".format(person1[0][1],person1[0][2],adjusted_compatability(compatability(compare(person1[1][2:],row2[2:])),qrange),row1[1],row1[2]))

        cur1.close()
        cur2.close()
        con.close()
        matches.sort(key=getkey, reverse=True)
        return matches

    except Exception as e:
        raise e

def getkey(item):
    return item[1]



def get_possible_matches(user_email):

    con = sql.connect("dating.db", timeout=10)
    cur1 = con.cursor()

    try:

        L = get_matches(user_email)
        final = []
        for row in L:
            each_info = cur1.execute("select ufname, ulname, ugender from users where uemail = ?",(row[2],)).fetchone()

            info_dict = {}

            info_dict["First Name: "] = each_info[0]
            info_dict["Last Name: "] = each_info[1]
            info_dict["Gender: "] = each_info[2]
            info_dict["Compatability: "] = "%"+str(row[1])
            info_dict["Email: "] = row[2]

            final.append(info_dict)

        return final

    except Exception as e:

        raise e


if __name__ == "__main__":


    for row in get_possible_matches('r.wells6894@gmail.com'):
        print(row)
#     test_subject = "adebiasi4o@exblog.jp"
#     qrange = min_max(test_subject)

#     try:
        
#         con = sql.connect("../dating.db", timeout=10)
#         cur1 = con.cursor()
#         cur2 = con.cursor()

#         p1_deets = cur1.execute("select * from users where uemail=?",(test_subject,)).fetchone()
#         p1_ans = cur1.execute("select * from questionnaire where qemail=?",(test_subject,)).fetchone()

#         person1 = (p1_deets,p1_ans)

#         cur1.execute("select * from users")
#         for row1 in cur1:
#             if test_subject == row1[0]:
#                 continue
#             else:
#                 if person1[1][1] == row1[3]:
#                     cur2.execute("select * from questionnaire where qemail=?",(row1[0],))
#                     for row2 in cur2:
#                         if row2[1] == person1[0][3]:
#                             print("{0} {1} is %{2:.2f} compatible with {3} {4}".format(person1[0][1],person1[0][2],adjusted_compatability(compatability(compare(person1[1][2:],row2[2:])),qrange),row1[1],row1[2]))

#         cur1.close()
#         cur2.close()
#         con.close()

#     except Exception as e:
#         raise e