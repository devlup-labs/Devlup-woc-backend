def projectpage_dict(project) -> dict:
    return {
        "id": str(project["_id"]),
        "avatarSrc": str(project["avatarSrc"]),
        "name": str(project["name"]),
        "bio": str(project["bio"]),
        "socialIcons": project.get("socialIcons", []),
        "buttons": project.get("buttons", []),
        "isPro": project.get("isPro", False)
    }

def list_projectpage_schema(projects) -> list:
    return [projectpage_dict(project) for project in projects]
