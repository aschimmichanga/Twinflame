import json
# import pandas as pd
# import numpy as np

# nested dict keys:
# first_name, last_name, matched, q1, q2, q3, q4, q5, q6, q7, q8, q9, q10, score
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
        "first_name": dict.get(match_emails[0]).get(first_name),
        "last_name": dict.get(match_emails[0]).get(last_name),
        "email": match_emails[0]
    }
    second = {
        "first_name": dict.get(match_emails[1]).get(first_name),
        "last_name": dict.get(match_emails[1]).get(last_name),
        "email": match_emails[1]
    }
    third = {
        "first_name": dict.get(match_emails[2]).get(first_name),
        "last_name": dict.get(match_emails[2]).get(last_name),
        "email": match_emails[2]
    }

    match_emails = {
        "first" : first,
        "second" : second,
        "third" : third
    }

    print(match_emails)
    return json.dumps(match_emails)

matches("sampleemail1")







'''
#if using pandas 
# if data is csv:
data = pd.read_excel('user_info.xlsx')
# target_user = "user email address of who we wanna match"
QUESTION_AMT = 10
data["match_score"] = 0
# returns array of emails of the top 3 closest matches to the target person,
# excluding emails in the given list
def make_matches(df, target_email, list_to_exclude):
    for pos in range(data.iloc[:,0].size): 
        if not df.iloc[pos, df.columns.get_loc("email")] in list_to_exclude:
            score = 0
            for col in range(df.columns.get_loc("last_name") + 1, df.columns.get_loc("last_name") + QUESTION_AMT + 2):
                user_row = np.argwhere(df.index < target_user).flatten()[-1]
                if df.iloc[user_row, col] == df.iloc[pos, col]:
                    score += 1
                else:
                    score -= 1
            data.iloc[pos, df.columns.get_loc("match_score")] = score
    match_email = data.iloc[data['match_score'].idxmax(), data.columns.get_loc("email")]
    if len(list_to_exclude) < 4:
        return make_matches(df, target_email, list_to_exclude.append(match_email))
    return list_to_exclude
# find top 3 matches
match_emails = make_matches(data, target_user, [target_user]).remove(target_user)
first = {
    "first_name": data.iloc[data.rows.get_loc(match_emails[0]), data.columns.get_loc("first_name")],
    "last_name": data.iloc[data.rows.get_loc(match_emails[0]), data.columns.get_loc("last_name")],
    "email": match_emails[0]
}
second = {
    "first_name": data.iloc[data.rows.get_loc(match_emails[1]), data.columns.get_loc("first_name")],
    "last_name": data.iloc[data.rows.get_loc(match_emails[1]), data.columns.get_loc("last_name")],
    "email": match_emails[1]
}
third = {
    "first_name": data.iloc[data.rows.get_loc(match_emails[2]), data.columns.get_loc("first_name")],
    "last_name": data.iloc[data.rows.get_loc(match_emails[2]), data.columns.get_loc("last_name")],
    "email": match_emails[2]
}
match_emails = {
    "first" : first,
    "second" : second,
    "third" : third
}
print(match_emails)
return json.dumps(match_emails)
matches("sampleemail1")
'''
    