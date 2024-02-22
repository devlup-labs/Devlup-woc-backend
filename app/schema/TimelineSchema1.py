def timeline1_dict(tl_item) -> dict:
    return {
        "Index": int(tl_item["Index"]),
        "colorClass": str(tl_item["colorClass"]),
        "date": str(tl_item["date"]),
        "title": str(tl_item["title"]),
        "info": str(tl_item["info"]),
        "firstButtonText": str(tl_item["firstButtonText"]),
        "firstButtonLink": str(tl_item["firstButtonLink"]),
        "secondButtonText": str(tl_item["secondButtonText"]),
        "secondButtonLink": str(tl_item["secondButtonLink"])
    }

def list_schema3(tl_items) -> list:
    return [timeline1_dict(item) for item in tl_items]
