def dict_schema(projects)->dict:
    return {
        "id": str(projects["_id"]),
        "title:": str(projects["title"]),
        "description": str(projects["description"]),
        "mentor": str(projects["mentor"])
    }

def list_schema(projects)->list:
    return [dict_schema(project) for project in projects]

