class TestFoo:
    class MyClass:
         def test_method_myclass(self):
             pass

    def test_method_with_inner_class(self):
        obj = self.MyClass()
        assert isinstance(obj, object)