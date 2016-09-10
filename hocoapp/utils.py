def is_authenticated(req):
    return 'uid' in req.session

def is_admin(req):
    username = req.session.get("uid")
    if username:
        return username in ["2019okulkarn", "2017jhoughto", "2017ewang"]
