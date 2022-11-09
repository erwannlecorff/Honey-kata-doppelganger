class Notifier:
    def __init__(self):
        self.users = []

    def notify(self, user, message):
        self.users.append(user)
