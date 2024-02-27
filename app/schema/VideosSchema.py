def videos_dict(vid) -> dict:
    return {
        "id": str(vid["id"])
    }

def videos_list(vids) -> list:
    return [videos_dict(vid) for vid in vids]
