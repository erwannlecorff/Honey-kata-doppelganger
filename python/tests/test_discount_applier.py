from discount_applier import DiscountApplier

class NotifierMock:
    def __init__(self):
        self.messages = []

    def notify(self, user, message):
        self.messages.append(message)

def test_apply_v1():
    # TODO: write a test that fails due to the bug in
    # DiscountApplier.apply_v1
    notifier = NotifierMock()
    applier = DiscountApplier(notifier)
    list_of_users = ["user1", "user2"]
    applier.apply_v1(20, list_of_users)
    assert len(list_of_users) == len(notifier.messages)
    pass


def test_apply_v2():
    # TODO: write a test that fails due to the bug in
    # DiscountApplier.apply_v2
    pass
