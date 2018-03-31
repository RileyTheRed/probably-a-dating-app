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
    return ((70-n)/70)*100


if __name__ == "__main__":

    persons = {}
    with open("people.txt") as fpeople:
        for line in fpeople:
            line = line.replace('\n','')
            a = line.split(',')
            s = a[0]
            persons[s] = (a[1:])

    for person in persons:
        for person2 in persons:
            print("{0} is %{1} compatible with {2}".format(person,compatability(compare(persons[person],persons[person2])),person2))