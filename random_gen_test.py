import mysql.connector
from random import choice
import sys

def createCandidate(fname: str, lname: str, email: str) -> str:
    return f"""INSERT INTO candidate (fname, lname, email) VALUES ("{fname}", "{lname}",  "{email}");"""

def createKey(question_num: int, answer: str, email: str) -> str:
    return f"""INSERT INTO question (questionNum, answer, person) VALUES({str(question_num)}, "{answer}", "{email}"); """

def createManyKeys(email: str) -> list:
    return [createKey(i, choice(["A", "B", "C", "D"]), email) for i in range(1, 11)]

def generate_candidates(list_of_email):
    return [(createCandidate("a", "a", i), createManyKeys(i)) for i in list_of_email]

def insert_sql():
    result = generate_candidates(["agiu@gmail.com",
                                  "aehifui@gmail.com",
                                  "eajkabgefi@gmail.com",
                                  "aeFwA@gmail.com"])
    candidateDB = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
    database="matching")
    mycursor = candidateDB.cursor()
    mycursor.execute(" * from candidate")



print(generate_candidates(["agiu@gmail.com",
                     "aehifui@gmail.com",
                     "eajkabgefi@gmail.com",
                     "aeFwA@gmail.com"])[0], file=sys.stout)