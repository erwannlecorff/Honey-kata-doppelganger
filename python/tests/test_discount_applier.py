from discount_applier import DiscountApplier
from tests.notifier import Notifier


def test_apply_v1():
    # TODO: write a test that fails due to the bug in
    # DiscountApplier.apply_v1
    notifier = Notifier()
    discount = DiscountApplier(notifier)
    discount.apply_v1(10, ["user1", "user2"])
    assert len(notifier.users) == 2

def test_apply_v2():
    # TODO: write a test that fails due to the bug in
    # DiscountApplier.apply_v2
    notifier = Notifier()
    discount = DiscountApplier(notifier)
    users = ["user1", "user2"]
    discount.apply_v2(10, users)
    assert notifier.users == users