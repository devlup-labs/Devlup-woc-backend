def timeline_dict(timeline)->dict:
    return {
        "id": str(timeline["_id"]),
        "date": str(timeline["date"]),
        "events": timeline["events"],
        "completed": bool(timeline["completed"])
    }

def timeline_list(projects)->list:
    return [timeline_dict(project) for project in projects]
