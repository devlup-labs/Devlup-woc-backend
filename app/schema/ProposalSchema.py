def proposal_dist(proposals)->dict:
    return {
         "title": str(proposals["title"]),
        "name": str(proposals["name"]),
        "drive": str(proposals["drive"]),
        "mentor": str(proposals["mentor"]),
    }

def proposal_list(proposals)->list:
    return [proposal_dist(proposal) for proposal in proposals]