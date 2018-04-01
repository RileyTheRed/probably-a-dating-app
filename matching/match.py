""" This is the prototype matching algorithm for the website

V1.0
"""

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
    return ((140-n)/140)*100


if __name__ == "__main__":

    persons = []
    with open("answers.txt") as fpeople:
        for line in fpeople:
            line = line.replace('\n','')
            line = line.split(",")
            persons.append([line[0],line[1],line[2:]])

    for x in persons:
        print(x)

    # for person in persons:
    #     for person2 in persons:
    #         if person is person2:
    #             continue
    #         if compatability(compare(person[2],person2[2])) <= 50.0:
    #             print("{0} is %{1} compatible with {2}".format(person[0],round(compatability(compare(person[2],person2[2])),2),person2[0]))