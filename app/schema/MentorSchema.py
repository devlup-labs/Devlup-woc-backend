def mentor_dist(mentor)->dict:
    return {
        "id": str(mentor["id"]),
        "name":str(mentor["name"]),
    }
def mentor_list(mentors)->list:
    return [mentor_dist(mentor) for mentor in mentors]

