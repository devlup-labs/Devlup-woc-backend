def alumniteam_dict(a_team) -> dict:
    return {
        "name": str(a_team["name"]),
        "role": str(a_team["role"]),
        "avatar": str(a_team["avatar"]),
        "linkedin": str(a_team["linkedin"]),
        "mail": str(a_team["mail"]),
        "github": str(a_team["github"])
    }

def list_schema2(a_team) -> list:
    return [alumniteam_dict(project) for project in a_team]
