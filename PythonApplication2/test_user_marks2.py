import pytest
import sys
 

@pytest.mark.webtest
def test_send_http():
    pass  # perform some webtest test for your app


def test_something_quick():
    pass   
 
 
def test_another2():
    pass 
 
 
@pytest.mark.skip(reason="no way of currently testing this")
def test_skip():
    self.fail("Not implemented")

@pytest.mark.skipif(sys.version_info < (3,6), reason="requires python3.6 or higher")
def test_skipif():
    self.fail("Not implemented")

class TestClass(object):
    def test_method(self):
        pass

    