import sys
import mysql.connector
import json
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

QUESTION_AMT = 10

def matches(dict, target_email):
    target_user = dict.get(target_email)
    score_dict = {}

    def make_matches(emails_to_exclude):
        for email in dict.keys():
            if not email in emails_to_exclude:
                other_user = dict.get(email)
                score = 0
                for i in range(1, QUESTION_AMT + 1):
                    if other_user.get("q" + str(i)) == target_user.get("q" + str(i)):
                        score += 1
                    else:
                        score -= 1
                score_dict[email] = score_dict
        if len(emails_to_exclude) < 4:
            return make_matches(emails_to_exclude.append(score_dict.values().index(max(score_dict.values()))))
        return emails_to_exclude

    # find top 3 matches
    match_emails = make_matches([target_email]).remove(target_user)
    first = {
        "first_name": dict.get(match_emails[0]).get("first_name"),
        "last_name": dict.get(match_emails[0]).get("last_name"),
        "email": match_emails[0]
    }
    second = {
        "first_name": dict.get(match_emails[1]).get("first_name"),
        "last_name": dict.get(match_emails[1]).get("last_name"),
        "email": match_emails[1]
    }
    third = {
        "first_name": dict.get(match_emails[2]).get("first_name"),
        "last_name": dict.get(match_emails[2]).get("last_name"),
        "email": match_emails[2]
    }

    match_emails = {
        "first": first,
        "second": second,
        "third": third
    }

    print(match_emails["first"])

matches("sampleemail1")