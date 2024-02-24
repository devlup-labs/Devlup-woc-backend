def blog_dict(blog) -> dict:
    return {
        "id": int(blog["id"]),
        "title": str(blog["title"]),
        "author": str(blog["author"]),
        "date": str(blog["date"]),
        "avatarid": str(blog["avatarid"]),
        "readTime": str(blog["readTime"]),
        "image": str(blog["image"]),
        "link": str(blog["link"])
    }

def list_blogs_schema(blogs) -> list:
    return [blog_dict(blog) for blog in blogs]
