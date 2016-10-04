def is_authenticated(req):
    return 'uid' in req.session


def is_admin(req):
    username = req.session.get("uid")
    if username:
        return username in ["2019okulkarn", "2017jhoughto", "2017ewang", "2018kdu", "2017zli", "2018sxie", "2018jprabhal", "2017gvaldeta", "2017ycho"]
    return False
