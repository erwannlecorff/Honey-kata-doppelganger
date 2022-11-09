from discount_applier import DiscountApplier
from typing import List, Dict
import pytest

class NotifierMock:
    def __init__(self):
        self.messages = []

    def notify(self, user, message):
        self.messages.append({"user": user, "message": message})

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
    notifier = NotifierMock()
    applier = DiscountApplier(notifier)
    list_of_users = ["user1", "user2"]
    applier.apply_v2(20, list_of_users)
    for i in range(0, len(list_of_users)):
        assert list_of_users[i] in notifier.messages[i]['user'] 
    pass
