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

QUESTION_AMT = 10

def matches(dict , target_email):
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
                score_dict[email] = score

        #print(score_dict.values())
        return max(score_dict.keys(), key=lambda a: score_dict[a])


    # find top 3 matches
    match_emails = make_matches([target_email])
    return f"{match_emails}, {dict[match_emails]['first_name']}, {dict[match_emails]['last_name']}"
print(matches(allUserData, candidate_email), end="")
sys.stdout.flush()