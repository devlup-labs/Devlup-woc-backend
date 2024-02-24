from schema.ProjectSchema import dict_schema
def user_dict(user)->dict:
    return {
        "first_name": str(user["first_name"]),
        "last_name": str(user["last_name"]),
        "email":str(user["email"]),
        "branch": str(user["branch"]),
        "year": str(user["year"]),
        "gender": str(user["gender"]),
        "role": str(user["role"]),
        "phonenumber": int(user["phonenumber"]),
        "githublink" : str(user["githublink"]),
        "id":str(user["id"]),
        "projects": [dict_schema(project) for project in user.get("projects", [])]
          }

def user_list(users)->list:
    return [user_dict(user) for user in users]
