class Authorizer:
    def __init__(self, isAuthorized):
        self.isAuthorized = isAuthorized

    def authorize(self):
        return self.isAuthorized
