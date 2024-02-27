
def currteam_dict(c_team) -> dict:
    return {
        "name": str(c_team["name"]),
        "role": str(c_team["role"]),
        "avatar": str(c_team["avatar"]),
        "linkedin": str(c_team["linkedin"]),
        "mail": str(c_team["mail"]),
        "github": str(c_team["github"]),
        "AlumniStatus" :int(c_team["AlumniStatus"])
    }


def list_schema1(c_team) -> list:
    return [currteam_dict(i) for i in c_team]
