def dict_schema(projects)->dict:
    return {
        "id": str(projects["id"]),
        "title": str(projects["title"]),
        "tag": str(projects["tag"]),
        "description": str(projects["description"]),
        "technology": str(projects["technology"]),
        "mentor": str(projects["mentor"])
    }

def list_schema(projects)->list:
    return [dict_schema(project) for project in projects]

