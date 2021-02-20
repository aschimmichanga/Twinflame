import json
import pandas as pd

def matches(data, target_user):
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
                    if df.iloc[df.rows.get_loc(target_user), col] == df.iloc[pos, col]:
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

    return match_emails.dump()
