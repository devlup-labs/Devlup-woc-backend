def program_dist(programs)->dict:
    return {
        "title": str(programs["title"]),
        "codelink": str(programs["codelink"]),
        "description": str(programs["description"]),
        "technology": str(programs["technology"]),
        "mentor": str(programs["mentor"]),
        "mentee": str(programs["mentee"]),
        "year": str(programs["year"])
    }

def program_list(programs)->list:
    return [program_dist(program) for program in programs]

