class Outer:
    behavior_one = True

    def outer_test(self):
        assert self.behavior_one

    class Inner:
        behavior_two = True

        def inner_test(self):
            assert self.behavior_one and self.behavior_two