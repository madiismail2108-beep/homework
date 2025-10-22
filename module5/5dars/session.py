from models import USER

class Session:
    _instance=None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance=super(Session, cls).__new__(cls)
        return cls._instance
    
    def __init__(self, user:USER|None=None):
        self.session=user
    
    def add_session(self, user:USER):
        self.session=user

    def check_session(self):
        return self.session
        