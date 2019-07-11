# content of test_fixture_marks.py
import pytest
@pytest.fixture(params=[0, 1, 3])
def data_set(request):
    return request.param

def test_data(data_set):
    pass  