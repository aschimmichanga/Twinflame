import sys
import mysql.connector
candidate_email = sys.argv[1]

candidateDB = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
    database="matching")
mycursor = candidateDB.cursor()
mycursor.execute("SELECT * from candidate")
myresult = mycursor.fetchall()

allUserData = {}
for firstName, lastName, email in myresult:

    # query for all question answer
    newCursor = candidateDB.cursor()
    newCursor.execute(f"SELECT answer from question where person='{email}'")
    newResult = newCursor.fetchall()

    # if email already exist, then we have a problem
    if email in allUserData:
        raise BaseException("repeated email, this is bad")
    # create the person inside the dictionary
    allUserData[email] = {"first_name": firstName,
                          "last_name": lastName}
    startNum = 1
    for i in newResult:
        allUserData[email]["q" + str(startNum)] = i[0]
        startNum += 1




