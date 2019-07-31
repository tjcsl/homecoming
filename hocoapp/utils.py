def is_authenticated(req):
    return "uid" in req.session


def is_admin(req):
    username = req.session.get("uid")
    return username and username in ["2019okulkarn", "2019nkothari"]
