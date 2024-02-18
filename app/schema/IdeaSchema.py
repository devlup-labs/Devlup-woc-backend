def idea_dict(ideas)->dict:
    return {
        "title": str(ideas["title"]),
        "description": str(ideas["description"]),
        "name": str(ideas["name"])
    }

def idea_list(ideas)->list:
    return [idea_dict(idea) for idea in ideas]

