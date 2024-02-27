def contactus_dict(conn) -> dict:
    return {
        "email": str(conn["email"]),
        "name": str(conn["name"]),
        "contactno": str(conn["contactno"]),
        "comments": str(conn["comments"])

    }

def list_contact(con) -> list:
    return [contactus_dict(conn) for conn in con]
